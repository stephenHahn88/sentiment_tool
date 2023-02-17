<template>
  <b-container>
    <b-row>
      <b-col>
        <b-button
          id="start-button"
          @click="startAnnotate"
        >
          Start Annotation
        </b-button>
      </b-col>
      <b-col>
        <b-button
          id="stop-button"
          @click="stopAnnotate"
        >
          Stop Annotation
        </b-button>
      </b-col>
      <b-col>
        <b-button
          id="restart-button"
          @click="restartAnnotate"
        >
          Clear and Restart
        </b-button>
      </b-col>
    </b-row>
    <b-row class="mt-2 overflow-auto">
      <pre
          id="output-result"
          class="pl-3"
      >
        {{resultString}}
      </pre>
    </b-row>
    <b-row>
      <b-textarea
          placeholder="If you would like to comment or clarify your analysis, please write here"
          v-model="comments"
          @focusin="disableAudioListener"
          @focusout="enableAudioListener"
      >
      </b-textarea>
    </b-row>
    <b-row class="mt-2">
      <b-col>
        <input
            id="id-field"
            type="text"
            placeholder="Custom ID goes here"
            v-model="customID"
            @focusin="disableAudioListener"
            @focusout="enableAudioListener"
        >
      </b-col>
      <b-col>
        <b-button
            id="finish-annotate"
            @click="saveAnnotation"
        >Complete and Send to Server</b-button>
      </b-col>
      <b-col></b-col>
    </b-row>
  </b-container>
</template>

<script setup lang="ts">
import {reactive, computed, ref, Ref, onMounted} from "vue"
import {round} from 'lodash'

interface Props {
  currentEmotion: string
  currentFile: string
}

let props = withDefaults(defineProps<Props>(), {
  currentEmotion: "none",
  currentFile: "not chosen"
})

let audio: HTMLAudioElement;
let audioListener: Function;
let valenceInterval: number;
let sampleRate = 100
let outputResult: HTMLElement;

let result = reactive({})
let resultString = ref("")

let customID = ref("")
let comments = ref("")

onMounted(() => {
  outputResult = document.getElementById("output-result") as HTMLElement

  audio = document.getElementById("audio") as HTMLAudioElement
  audioListener = (e: KeyboardEvent) => {
    if (e.key === " " && !audio.paused) {
      audio.pause()
    } else {
      audio.play()
    }
  }
  enableAudioListener()
})

function enableAudioListener() {
  document.addEventListener("keyup", audioListener, true)
}

function disableAudioListener() {
  document.removeEventListener("keyup", audioListener, true)
}

function startAnnotate() {
  // annotates current valence value every 100 ms
  valenceInterval = setInterval(annotate, sampleRate);
}

function stopAnnotate() {
  // stops the annotation process
  clearInterval(valenceInterval)
}

function annotate() {
  // appends the current time, valence pair to a p tag
  if (!audio.paused) {
    result[audio.currentTime] = props.currentEmotion
    resultString.value += `\n${round(audio.currentTime, 4)}\t: ${props.currentEmotion}`
    outputResult.scrollTop = outputResult.scrollHeight
  }
}

function restartAnnotate() {
  // resets the time, valence pairs and stops annotation
  stopAnnotate();
  audio.currentTime = 0
  audio.pause()
  result = {}
  resultString.value = ""
}

async function saveAnnotation() {
  let options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      piece: props.currentFile,
      analysis: result,
      comments: comments.value,
      custom_id: customID.value
    })
  }
  let response = await (await fetch('/api/analyses', options)).json()
  console.log(response)
}


</script>

<style scoped>
.btn {
  width: 100%;
  height: 100%;
  color: black;
}

#output-result {
  background-color: rgba(255, 255, 255, 0.6);
  width: 100%;
  height: 200px;
}

#start-button, #stop-button, #finish-annotate {
    background-color: rgba(255, 255, 255, 0.4);
    border: none;
}

#start-button:hover, #stop-button:hover, #finish-annotate:hover {
    background-color: rgba(200, 200, 200, 0.4);
    border: none;
}

#restart-button {
    background-color: rgba(233, 102, 94, 0.4);
    border: none;
}

#restart-button:hover {
    background-color: rgba(183, 52, 44, 0.4);
    border: none;
}

#custom-textarea {
    background-color: rgba(255, 255, 255, 0.4);
    border: none;
}
</style>