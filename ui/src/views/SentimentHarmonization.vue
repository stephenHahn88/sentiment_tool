<template>
    <b-container class="mt-5">
      <!-- File Upload Section -->
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
                @click="renderMusicSheet"
                :disabled="!uploadedFile"
                variant="info"
            >
              Upload MusicXML
            </b-button>
          </b-col>
        </b-row>
      </b-container>
      <b-container
          v-if="musicRendered"
          style="width: 60%"
          class="container d-flex align-items-center justify-content-center"
      >
        <!-- Put bar plot input controls here -->
        <BarPlotInput
            :priorDist="currentEmotionMixture"
            @emotionMixtureUpdate="handleEmotionMixtureUpdate"
        >
        </BarPlotInput>
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

import { ref } from 'vue';
import { OpenSheetMusicDisplay, PointF2D } from 'opensheetmusicdisplay';

import BarPlotInput from "@/components/progression/BarPlotInput.vue";

let currentEmotionMixture = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2];
const emotionLabels = ["anger", "fear", "sadness", "none", "irony", "love", "joy"];

function handleEmotionMixtureUpdate (mixtures) {
  currentEmotionMixture = mixtures;
}

let uploadedFile = ref(null);
let musicRendered = ref(false);

let score = null;
let notes = [];
let notesParsed = [];

let numMeasures = 0;
let measurePositions = [];
let notePositions = [];
let selectedNotesIndeces = [];

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

function renderMusicSheet () {
  if (!uploadedFile.value) return;

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

        osmd.render();
        musicRendered.value = true;

        // Assuming a single melody line and single voice
        score.Instruments.forEach(instrument => {
          instrument.Staves.forEach(staff => {
            let voice = staff.Voices[0];
            voice.VoiceEntries.forEach(voiceEntry => {
              voiceEntry.Notes.forEach(note => {

                // Get note pitch
                let notePitch = note.Pitch;
                // Convert from Pitch to midi
                let midi = pitchToMidi(notePitch);

                // Get note duration
                let noteDuration = note.Length;
                // Get note quarterLength
                let quarterLength = noteDuration.realValue * 4;

                notes.push({note, midi, quarterLength});
                notesParsed.push({midi, quarterLength});

              });
            });
            });
        });

        // Get the number of measures
        numMeasures = osmd.graphic.measureList.length;

        // Get the position of the measures and notes
        for (let measure=0; measure<numMeasures; measure++) {
          // Get measure endpoint bounding box, or position of the last note
          measurePositions.push(osmd.graphic.measureList[measure][0].staffEntries[0].boundingBox);
          // Get note positions
          for (let note=0; note<osmd.graphic.measureList[measure][0].staffEntries.length; note++) {
            // Get note bounding box:  osmd.graphic.measureList[measure][0].staffEntries[note].boundingBox
            let noteBoundingBox = osmd.graphic.measureList[measure][0].staffEntries[note].boundingBox;
            let graphicalNote = osmd.graphic.measureList[measure][0].staffEntries[note].graphicalVoiceEntries[0].notes[0].sourceNote;
            notePositions.push({noteBoundingBox, graphicalNote});
          }
        }

        // osmd.graphic.measureList[0][0].staffEntries[0].graphicalVoiceEntries[0].notes[0].sourceNote.noteheadColor = "#FF0000";
        console.log(notes);
        console.log(notesParsed);
        console.log(notePositions);

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
  const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ "notes": notesParsed, "sentiment": currentEmotionMixture, "harmonicRhythm": harmonicRhythm(notesParsed, selectedNotesIndeces)})
  }
  console.log(requestOptions)

  // POST request to /api/harmonize
  let harmonized = await (await fetch("/api/harmonize", requestOptions)).json();
  console.log(harmonized);
  waiting.value = false;
}

async function saveMelodySurveyResponse(rating) {
    // Hide the survey popup UI
    closed.value = true
    // Retrieve current melody from server
    let melody = await (await fetch("/api/composer/"+encodeURIComponent(composerId.value)+"/melody/"+encodeURIComponent(melodyId.value)+"/notes-harmonies-tempo")).json()
    const requestOptions = {
        method: "PUT",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "rating": rating, "notes": melody.notes, "harmonies": melody.harmonies })
    }
    let response = await fetch("/api/surveys", requestOptions)

    response = await response.json()
    console.log(response)
    // Close the survey component
    closed = true
  }

</script>

<style>

#osmd-container {
  height: 200px;
  width: 90%;
  overflow-x: auto;
}

/*.centered {*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  align-items: center;*/
/*  justify-content: center;*/
/*}*/

</style>
