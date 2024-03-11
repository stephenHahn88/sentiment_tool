<template>
    <b-container class="mt-5">
      <!-- File Upload Section -->
      <b-container v-if="!musicRendered" class="mb-5">
        <h1 class="mb-5">Provide a melody to harmonize</h1>
        <b-container>
          <p>The melody must be:</p>
          <ul>
            <li>A .musicxml file</li>
            <li>In a soprano's register in Treble clef</li>
            <li>Up to 8 measures long</li>
            <li>In the key of C</li>
          </ul>
        </b-container>
      </b-container>
      <b-container
          v-if="!musicRendered"
          class="container d-flex align-items-center justify-content-center"
      >
        <b-row>
          <b-col>
            <b-form-file
                v-model="uploadedFile"
                accept=".xml, .musicxml"
            ></b-form-file>
<!--              @change="handleFileUpload"-->
          </b-col>
          <b-col>
            <b-button
                pill
                @click="renderMusicSheet(-1)"
                :disabled="!uploadedFile"
                variant="info"
            >
              Upload MusicXML
            </b-button>
          </b-col>
        </b-row>
      </b-container>
      <b-container v-if="!musicRendered" class="mt-3 mb-5">
        <h1 class="mb-5">Or select a preset melody:</h1>
        <b-row>
          <b-col>
            <b-button @click="renderMusicSheet(1)" class="m-1">Melody 1</b-button>
            <b-button @click="renderMusicSheet(2)" class="m-1">Melody 2</b-button>
            <b-button @click="renderMusicSheet(3)" class="m-1">Melody 3</b-button>
          </b-col>
        </b-row>
      </b-container>
      <b-container v-if="musicRendered">
        <h1>Provide your desired sentiment mixture</h1>
        <p>Click or drag the bars to change their values</p>
      </b-container>
      <b-container
          v-if="musicRendered"
          style="width: 60%"
          class="container align-items-center justify-content-center"
      >
        <!-- Put bar plot input controls here -->
        <BarPlotInput
            :priorDist="currentEmotionMixture"
            @emotionMixtureUpdate="handleEmotionMixtureUpdate"
        >
        </BarPlotInput>
      </b-container>
      <b-container v-if="musicRendered">
        <h1>Provide your preferred harmonic rhythm</h1>
        <p>Using the note buttons below, fill the measures with the rhythm that defines where you want harmonies to change</p>
      </b-container>
      <b-container v-if="musicParsed">
        <b-row>
          <b-row class="mb-2 mx-1 pb-3 px-3 letter-group" style="width:100%">
            <b-button variant="warning" @click="backspace()" class="m-2">
              &#8592
            </b-button>
            <div id="boo" style="overflow: auto;"></div>
            <div class="mt-3">
              <b-button
                  v-for="rhythm in possibleRhythms"
                  v-on:click="placeNotes(rhythm)"
                  class="mb-3 ml-3 pl-5"
                  variant="primary"
              >
                <img
                    class="p-0 m-0"
                    v-for="r in rhythm.split(' ')"
                    :src="`.//static/floatingNotes/${rhythmToSVGName[r]}.svg`" :alt="rhythm"
                    style="width: 25px; filter: invert(100%)"
                >
              </b-button>
            </div>
          </b-row>
        </b-row>
      </b-container>
      <b-row class="my-5">
        <!-- Music Sheet Display Section -->
        <b-container
            id="osmd-container"
        ></b-container>
      </b-row>
      <b-overlay :show="waiting" rounded="lg" class="py-3">
        <b-row class="container d-flex align-items-center justify-content-center">
          <b-button
              pill
              v-if="musicRendered"
              id="harmonize"
              @click="sendNotesToServer"
              variant="primary"
              :disabled="waiting"
          >
            Send Notes and Sentiment to Server
          </b-button>
        </b-row>
      </b-overlay>
    </b-container>
</template>

<script setup>

import Vue from 'vue'
import { ref, watch } from 'vue';
import { OpenSheetMusicDisplay, PointF2D } from 'opensheetmusicdisplay';
import Vex from 'vexflow'

import { piano, casio, playVoices } from "@/harmonize-playback";
import BarPlotInput from "@/components/progression/BarPlotInput.vue";

const { Renderer, Stave, Formatter, StaveNote, Dot } = Vex.Flow;

let currentEmotionMixture = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2];
const emotionLabels = ["anger", "fear", "sadness", "none", "irony", "love", "joy"];

let possibleRhythms = ['1', '1/2 1/2']//, '1/2 1/4 1/4', '1/4 1/4 1/4 1/4'] //['𝅝', '𝅗𝅥 𝅗𝅥', '𝅗𝅥. ♩', '𝅗𝅥 ♩ ♩', '♩ ♩ ♩ ♩']

let rhythmToSVGName = {
  '1/8': 'eighth',
  '1/4': 'quarter',
  '1/4.': 'dquarter',
  '1/2': 'half',
  '1/2.': 'dhalf',
  '1': 'whole',
  '1.': 'dwhole'
}

let rhythmToQL = {
  '1/8': 0.25,
  '1/4': 1,
  '1/4.': 1.5,
  '1/2': 2,
  '1/2.': 3,
  '1': 4
}

function handleEmotionMixtureUpdate (mixtures) {
  currentEmotionMixture = mixtures;
}

let emojis = {
  piano: '&#127929;',
  casio: '&#127899;',
  game: '&#127928;'
}

let uploadedFile = ref(null);
let musicRendered = ref(false);
let musicParsed = ref(false);

let score = null;
let notes = [];
let notesParsed = [];
let rests = [];
let meter = ref("4/4");

let numMeasures = 0;
let measurePositions = [];
let notePositions = [];
let selectedNotesIndeces = [];

let div = ref(null);
let renderers;
let contexts;
let measures = []

watch(musicParsed, (val) => {
  if (val) {
    Vue.nextTick(() => {
      div.value = document.getElementById("boo");
      console.log(div.value)
      drawStaves();
    });
  }
})

let defaultWidth;
let totalMeasures;
let currMeasures = 0
let noteGroups = []
let storedMeasures = []

let buttons = [];

let waiting = ref(false);

function handleFileUpload (event) {
  uploadedFile.value = event.target.files[0];
}

function pitchToMidi (pitch) {
  let frequency = pitch.frequency;
  return 69 + 12 * Math.log2(frequency / 440);
}

function getOSMDCoordinates(osmd, container, x, y) {
  const sheetX = (x - container.offsetLeft) / 10 / osmd.Zoom;
  const sheetY = (y - container.offsetTop) / 10 / osmd.Zoom - 28;
  return new PointF2D(sheetX, sheetY);
}

function setupClickHandler(osmd) {
  const osmdContainer = document.getElementById('osmd-container'); // Replace with your actual container ID

  osmdContainer.addEventListener('click', function(event) {
      // Get click coordinates relative to the OSMD container
      const x = event.pageX;
      const y = event.pageY;
      const musicSheetPosition = getOSMDCoordinates(osmd, osmdContainer, x, y);

      let closestNote = null;
      let closestPosition = 0;
      let closestDistance = Infinity;

      for (let i=0; i<notePositions.length; i++) {
        let note = notePositions[i].noteBoundingBox;
        const centerX = note.absolutePosition.x;
        const centerY = note.absolutePosition.y;
        // Calculate distance from the click to the center of the note
        const distance = Math.sqrt(Math.pow(centerX - musicSheetPosition.x, 2) + Math.pow(centerY - musicSheetPosition.y, 2));

        if (distance < closestDistance) {
            closestNote = notePositions[i];
            closestPosition = i;
            closestDistance = distance;
        }
      }

      if (closestNote) {
          if (selectedNotesIndeces.includes(closestPosition)) {
            // Remove from selectedNotes
            closestNote.graphicalNote.noteheadColor = "#000000";
            selectedNotesIndeces = selectedNotesIndeces.filter(x => x !== closestPosition);
          } else {
            closestNote.graphicalNote.noteheadColor = "#0000FF";
            selectedNotesIndeces.push(closestPosition);
          }
          osmd.render();
      }

  });
}

async function renderMusicSheet (preset) {
  if (!uploadedFile.value && preset == -1) return;
  if (!uploadedFile.value) {
    const requestOptions = {
      method: "GET"
    }

    // POST request to /api/harmonize
    await fetch(`/api/load_preset?value=${preset}`, requestOptions)
    .then(response => {
      console.log(response);
      return response.blob();
    })
    .then(blob => {
      console.log(blob);
      const reader = new FileReader();
      let file = new File([blob], "Example.xml", {type: blob.type});
      uploadedFile.value = file;
    }).catch(error => {
          console.error('Error:', error);
    });

  }

  const reader = new FileReader();
  reader.onload = (event) => {
    console.log(event.target)
    // Load the uploaded musicXML file with OSMD
    const osmd = new OpenSheetMusicDisplay('osmd-container', {
      autoResize: false,
      backend: "svg",
      drawTitle: false,
      drawMetronomeMarks: false,
      drawPartNames: false,
      drawMeasureNumbers: false,
      drawComposer: false,
      drawSubtitle: false,
      drawUpToMeasureNumber: 8,
      pageBackgroundColor: "white",
      renderSingleHorizontalStaffline: true
    });

    osmd.load(event.target.result).then(() => {

      // Access the internal OSMD parsed music structure
      score = osmd.Sheet;

      // Only render the first melodic voice
      // osmd.sheet.instruments[0].voices[0].visible = true
      if (osmd.sheet.instruments.length > 1) {
        for (let instrument=1; instrument<osmd.sheet.instruments.length; instrument++) {
          for (let voice=0; voice< osmd.sheet.instruments[instrument].voices.length; voice++) {
            osmd.sheet.instruments[instrument].voices[voice].visible = false;
          }
        }
      } else {
        for (let voice=1; voice< osmd.sheet.instruments[0].voices.length; voice++) {
          osmd.sheet.instruments[0].voices[voice].visible = false;
        }
      }

      // Get the number of measures
      numMeasures = osmd.graphic.measureList.length;
      musicParsed.value = true;

      osmd.render();
      musicRendered.value = true;

      // Get the number of measures
      numMeasures = osmd.graphic.measureList.length;
      let totalNotes = 0;
      let total = 0;

      // Get the position of the measures and notes
      for (let measure=0; measure<numMeasures; measure++) {
        // Get measure endpoint bounding box, or position of the last note
        measurePositions.push(osmd.graphic.measureList[measure][0].staffEntries[0].boundingBox);
        // Get note positions
        for (let note=0; note<osmd.graphic.measureList[measure][0].staffEntries.length; note++) {
          // Get note bounding box:  osmd.graphic.measureList[measure][0].staffEntries[note].boundingBox
          let noteBoundingBox = osmd.graphic.measureList[measure][0].staffEntries[note].boundingBox;
          let graphicalNote = osmd.graphic.measureList[measure][0].staffEntries[note].graphicalVoiceEntries[0].notes[0].sourceNote;

          if (!graphicalNote.isRestFlag) {
            // Get note pitch
            let notePitch = graphicalNote.Pitch;
            // Convert from Pitch to midi
            let midi = pitchToMidi(notePitch);

            // Get note duration
            let noteDuration = graphicalNote.Length;
            // Get note quarterLength
            let quarterLength = noteDuration.realValue * 4;

            notes.push({graphicalNote, midi, quarterLength});
            notesParsed.push({midi, quarterLength});
            totalNotes++;
          } else {
            // Rest, modify the previous note's duration
            // Get rest duration
            let noteDuration = graphicalNote.Length;
            // Get note quarterLength
            let quarterLength = noteDuration.realValue * 4;

            let prevNote = notesParsed[totalNotes-1];
            console.log(totalNotes-1, prevNote)
            let prevMidi = prevNote.midi;
            let prevDuration = prevNote.quarterLength;
            let currDuration = prevDuration + quarterLength;
            notesParsed[totalNotes-1] = {"midi": prevMidi, "quarterLength": currDuration};
            notes.push({note, "midi": -1, quarterLength});
            rests.push({total, quarterLength})
          }

          notePositions.push({noteBoundingBox, graphicalNote});
          total++;

        }
      }

      // osmd.graphic.measureList[0][0].staffEntries[0].graphicalVoiceEntries[0].notes[0].sourceNote.noteheadColor = "#FF0000";
      // console.log(notes);
      console.log(notesParsed);
      //console.log(notePositions);
      //console.log(rests);

    });

    // After initializing and rendering OSMD
    setupClickHandler(osmd);

  };

  // Render the music without title, instrument, or tempo markers
  reader.readAsText(uploadedFile.value);
}

function harmonicRhythm(notes, selectedIndeces) {
  let harmonicRhythm = []
  let currQL = 0
  for (let i=0; i < notes.length; i++) {
    if (selectedIndeces.includes(i) && i !== 0) {
      harmonicRhythm.push(currQL)
      currQL = 0
    }
    currQL += notes[i]['quarterLength']
  }
  harmonicRhythm.push(currQL)
  return harmonicRhythm
}

async function sendNotesToServer() {
  console.log("Sent to server");
  waiting.value = true

  // Read parsed notes from OSMD container
  // Note that we pass back the note pitches/rhythm of the melody line (as well as note durations)
  // We need to read in the user input breakpoints to determine harmonic rhythm
  let hRhythm = [];
  if (storedMeasures.length === numMeasures) {
    for (let i=0; i<storedMeasures.length; i++) {
      let measure = storedMeasures[i];
      console.log(measure)
      const fractions = measure.split(" ");
      console.log(fractions)
      fractions.forEach(fraction => {
        hRhythm.push(rhythmToQL[fraction]);
      });
    }
    // hRhythm.pop();
  } else {
    let hRhythm = harmonicRhythm(notesParsed, selectedNotesIndeces);
  }
  
  console.log(hRhythm);

  const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ "notes": notesParsed, "sentiment": currentEmotionMixture, "harmonicRhythm": hRhythm})
  }
  console.log(requestOptions)

  // POST request to /api/harmonize
  let harmonized = await (await fetch("/api/harmonize", requestOptions)).json();
  console.log(harmonized);

  waiting.value = false;

  let pitches = [];
  let durations = [];

  // Parse melody
  pitches.push([]);
  durations.push([]);
  for (let i=0; i<notes.length; i++) {
    let midi = notes[i].midi;
    let duration = notes[i].quarterLength;
    pitches[0].push(midi);
    durations[0].push(duration);
  }

  pitches.push(harmonized["alto_notes"]);
  pitches.push(harmonized["tenor_notes"]);
  pitches.push(harmonized["bass_notes"]);

  durations.push(harmonized["alto_rhythm"]);
  durations.push(harmonized["tenor_rhythm"]);
  durations.push(harmonized["bass_rhythm"]);

  playVoices(notes, pitches, durations, harmonized["tempo"]);
}

function drawStaves() {
    defaultWidth = 440
    let rendererSize = defaultWidth * 6
    let xPart = defaultWidth / 4
    let height = 0

    totalMeasures = numMeasures

    renderers = new Renderer(div.value, Renderer.Backends.SVG)

    renderers.resize(rendererSize, 150)
    contexts = renderers.getContext()
    contexts.scale(1.4, 1.4)
    contexts.setFont('Arial', 18)

    // Create number of measures based on uploaded file
    let measures_l = []
    for (let i = 0; i < totalMeasures; i++) {
      if (i===0) {
        measures_l[i] = new Stave(xPart * i, height, xPart + 50)
        measures_l[i].addClef('percussion').addTimeSignature(meter.value)
      } else {
        measures_l[i] = new Stave(50 + xPart * i, height, xPart)
        measures_l[i].measure = i + 1
      }
      measures_l[i].setContext(contexts).draw()
    }
    measures = measures_l
}

// Removes last measure of rhythms
function backspace() {
  if (currMeasures === 0) return
  contexts.svg.removeChild(noteGroups.pop())
  storedMeasures.pop()
  console.log(storedMeasures)
  currMeasures--;
}

// Places rhythms in the context for the given letter
function placeNotes(rhythms) {
  if (storedMeasures.length === numMeasures){
    return
  }
  let notes = _parseRhythms(rhythms)

  noteGroups.push(contexts.openGroup())
  Formatter.FormatAndDraw(contexts, measures[currMeasures], notes)
  currMeasures++
  storedMeasures.push(rhythms)
  contexts.closeGroup()
}

function checkValidInput() {
  for (let letter in storedMeasures) {
    if (hypermeter.value[letter] <= 0 || hypermeter.value[letter] === "# measures") continue
    if (storedMeasures[letter].length !== hypermeter.value[letter]) return {status: "invalid"}
  }
  return {status: "valid"}
}

function _parseRhythms(rhythms) {
    let glyphs = rhythms.split(" ")
    let finalRhythms = []
    glyphs.forEach((glyph) => {
        switch (glyph) {
            case '1/8':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '8'}));
              break;
            case '1/8.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '8'})));
              break;
            case '1/4':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '4'}));
              break;
            case '1/4.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '4'})));
              break;
            case '1/2':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '2'}));
              break;
            case '1/2.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '2'})));
              break;
            case '1':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '1'}));
              break;
            case '1.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '1'})));
              break;
            case '2':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '1/2'}));
              break;
            case '2.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '1/2'})));
              break;
            case '4':
              finalRhythms.push(new StaveNote({ keys: ["b/4"], duration: '1/4'}));
              break;
            case '4.':
              finalRhythms.push(_dotted(new StaveNote({ keys: ["b/4"], duration: '1/4'})));
              break;
        }
    })
    return finalRhythms
}

// Attaches a rhythmic dot to a StaveNote
function _dotted(staveNote, noteIndex = -1) {
    if (noteIndex < 0) {
        Dot.buildAndAttach([staveNote], {
            all: true,
        });
    } else {
        Dot.buildAndAttach([staveNote], {
            index: noteIndex,
        });
    }
    return staveNote;
}

</script>

<style>

#osmd-container {
  height: 200px;
  width: 90%;
  overflow-x: auto;
}

p {
  font-size: 24px;
}

</style>
