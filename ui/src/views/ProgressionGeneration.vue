<template>
  <b-container>
    <div>
      <b-sidebar id="sidebar-1" title="Generation Controls" width="360px" shadow visible no-header-close>
        <div class="px-3 py-2">
          <h5> Time per Chord </h5>
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
          <BarPlotInput id = "emotionMixtureInput" :priorDist="currentEmotionMixture" @emotionMixtureUpdate="handleEmotionMixtureUpdate"></BarPlotInput>
          <h5> Playback Controls </h5>
        </div>
      </b-sidebar>
    </div>
    <div class="body">
      <AreaPlot id = "lineChartOutput"
          ref = "areaPlot"
          :time="timePerChord"
          :currEmotionDist="currentEmotionMixture">
      </AreaPlot>
    </div>
  </b-container>
</template>

<script setup lang="ts">

import { onMounted, ref, Ref, watch } from "vue"
import BarPlotInput from "@/components/progression/BarPlotInput.vue";
import AreaPlot from "@/components/progression/AreaPlot.vue"

import model from "/static/data/transition_matrices.json"

let timePerChord: Ref<number> = ref(1)
let currentEmotionMixture: number[] = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2]
let areaPlot = ref()

watch(timePerChord, (newTime) => {
  console.log("time change")
  areaPlot.value.updateTime(newTime)
})

// watch(currentEmotionMixture, (newEmotionMixture) => {
//   console.log("emotion change")
//   areaPlot.value.updateEmotionMixture(newEmotionMixture)
// })

let transition_matrices = model[0]
let encode_chords = model[1]
let decode_chords = model[2]

function handleEmotionMixtureUpdate (mixtures: Array<number>) {
  console.log(mixtures)
  currentEmotionMixture = mixtures;
}

</script>

<style scoped>

.body {
  margin-left: 320px;
  margin-top: 50px;
}

</style>