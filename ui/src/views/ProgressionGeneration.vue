<template>
  <b-container>
    <div>
      <b-sidebar id="sidebar-1" title="Generation Controls" width="360px" shadow visible no-header-close>
        <div class="px-3 py-2">
          <h5> Time per Chord (in seconds) </h5>
          <b-form-group>
            <b-form-input
                id="time-span"
                style="width: 80px;"
                type="number"
                v-model="timePerChord"
            ></b-form-input>
          </b-form-group>
          <h5> Input Emotion Mixture </h5>
          <!-- Put bar plot input controls here -->
          <BarPlotInput id = "emotionMixtureInput"
            :priorDist="currentEmotionMixture"
            @emotionMixtureUpdate="handleEmotionMixtureUpdate">
          </BarPlotInput>
          <h5 class="mt-3"> Playback Controls </h5>
          <b-row class="justify-content-md-center mt-3">
              <b-button variant="success" class="pause-button" @click="handlePause">
                <div v-if="paused">Play</div>
                <div v-else>Pause</div>
              </b-button>
          </b-row>
        </div>
      </b-sidebar>
    </div>
    <div class="body">
      <b-row>
        <b-col>
          <h5> Emotional Content over Time </h5>
          <AreaPlot id = "lineChartOutput"
            ref = "areaPlot"
            :time="timePerChord"
            :currEmotionDist="currentEmotionMixture"
            @timedEmit="handleTimedEmit"
            @timedGraphUpdate="handleTimedGraphEmit"
            style="width: 500px;">
          </AreaPlot>
        </b-col>
        <b-col>
          <DonutPlot id = "donutChartOutput"
            ref = "donutPlot"
            class = "mt-5"
            :currEmotionDist="currentEmotionMixture"
            style="width: 250px;">
          </DonutPlot>
        </b-col>
      </b-row>
      <b-row class="mt-3">
        <b-col>
          <h5> Chord Progression </h5>
          <PianoKeyboard class="mt-3" style="width:500px;height:150px;"
            ref="keyboard">
          </PianoKeyboard>
          <li 
            id = "chord-progression"
            class = "mt-3 chords"
            v-for="RN in RNList"
            :key="componentKey">
            {{ RN }}
          </li>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script setup lang="ts">

import { onMounted, ref, Ref, watch, getCurrentInstance } from "vue"
import { playChord } from "@/play-music";
import { weightedRandom } from "@/utility"
import model from "/static/data/transition_matrices.json"

import BarPlotInput from "@/components/progression/BarPlotInput.vue";
import AreaPlot from "@/components/progression/AreaPlot.vue"
import DonutPlot from "@/components/progression/DonutPlot.vue"
import PianoKeyboard from "@/components/PianoKeyboard.vue"

// import "nes.css/css/nes.min.css";

let timePerChord: Ref<number> = ref(5)
let currentEmotionMixture: number[] = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2]
let areaPlot = ref()
let donutPlot = ref()
let keyboard = ref()

watch(timePerChord, (newTime) => {
  areaPlot.value.updateTime(newTime)
})

// Transition matrices from chords to chords given an emotion
let transitionMatrices = model[0]
// RNs mapped to number
let encodeChords = model[1]
// Number mapped to RN (reverse of encodeChords)
let decodeChords = model[2]
// Start RN token
let lastRN = "iii";

const maxListLength = 5
const RNList: string[] = [lastRN];
const componentKey = ref(0);

let paused = ref(true)
const emotionLabels: string[] = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
const chordRNs: string[] = buildChordRNs()

const forceRerender = () => {
  componentKey.value += 1;
};

function buildChordRNs () {
  let RNs = [];
  for (let key in encodeChords) {
    RNs.push(key);
  }
  return RNs;
}

function normalize(input: number[]) {
    let sum = 0;
    for (let i=0; i<input.length; i++) {
        sum += input[i];
    }
    if (sum == 0) {
        sum = 1;
    }
    for (let i=0; i<input.length; i++) {
        input[i] = input[i] / sum;
    }
    return input;
}

function sampleVector (input: Map<string, number>) {
  let keys: string[] = Array.from(input.keys());
  let weights: number[] = Array.from(input.values())
  return weightedRandom(keys, weights);
}

function getNextChord () {

  // To be returned
  let transitions = new Map();

  // For each RN, find the probability of getting that RN given the previous RN and the emotional mixture
  chordRNs.forEach(function (RN) {

    let totalProb = 0;
    let index = 0;
    // Deep copy emotion mixture to avoid mutating the barplot
    let currentMixture = JSON.parse(JSON.stringify(currentEmotionMixture));
    currentMixture = normalize(currentMixture);

    emotionLabels.forEach(function (emotion) {

      let transitionMatrix = transitionMatrices[emotion];
      let weight = currentMixture[index];

      // Turn RN from string to matching index; note that lastRN inits as START
      let i = encodeChords[lastRN];
      let j = encodeChords[RN];

      totalProb += weight * (transitionMatrix[i][j]);
      index++;

    });

    // Check to see if value is NaN; if it is, replace with 0 prob
    if (isNaN(totalProb)) {
       totalProb = 0;
    }
    // Set key (RN) and value (probability) in transitions map
    transitions.set(RN, totalProb);

  });

  return sampleVector(transitions);

}

function handleEmotionMixtureUpdate (mixtures: Array<number>) {
  currentEmotionMixture = mixtures;
}

function handleTimedEmit () {

  // Get next chord's roman numeral and make a deep copy to lastRN if not currently paused
  if (!paused.value) {
    let nextRN = getNextChord();
    lastRN = JSON.parse(JSON.stringify(nextRN));

    // Truncate RNList if it exceeds max display length
    if (RNList.length >= maxListLength) {
      RNList.shift();
    }

    // Add new chord to RNList once space has been freed; force rerender element to display
    RNList.push(JSON.parse(JSON.stringify(lastRN)));
    playChord(lastRN);
    forceRerender();

  }

}

function handleTimedGraphEmit () {
  areaPlot.value.updateEmotionMixture(currentEmotionMixture);
  donutPlot.value.updateEmotionMixture(currentEmotionMixture);
}

function handlePause () {
  console.log("handle pause");
  paused.value = !paused.value;
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Press+Start+2P');

.body {
  margin-left: 320px;
  margin-top: 60px;
}

.chords {
  display: inline-block;
  margin-left: 60px;
  font-size: 40px;
  font-weight: 600;
}

.pause-button {
  width: 200px;
  height: 50px;
  font-size: 20px;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* html, body, pre, code, kbd, samp, span, p, h5 {
  font-family: 'Press Start 2P';
} */

</style>