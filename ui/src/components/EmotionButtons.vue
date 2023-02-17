<template>
  <b-container>
    <b-row>
      <b-col
        v-for="(emotion, i) in primaryEmotions"
        class="m-0"
      >
        <button
          :id="emotion"
          class="p-3 m-0 primary-emotion"
          @click="handleClick(emotion)"
        >
          {{emotion.charAt(0).toUpperCase() + emotion.slice(1)}}
          <br/>
          ({{i >= 4 ? i+3 : i+1}})
        </button>
      </b-col>
    </b-row>
    <b-row>
      <b-col
        v-for="(secondary, primary, i) in secondaryEmotions"
      >
        <button
          v-for="emotion in secondary"
          :class="primary"
          class="m-0 text-center secondary-emotion"
        >
          {{emotion}}
        </button>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <img class="squiggle reflect" src="../images/squiggle.svg" alt="squiggles">
      </b-col>
      <b-col>
        <button
            id="current-category"
            :class="currSelected"
            class="p-3 mt-2 text-center"
        >
          Current category: <br/>{{currSelected.at(0).toUpperCase() + currSelected.slice(1)}}
        </button>
      </b-col>
      <b-col>
        <img class="squiggle reflect" src="../images/squiggle.svg" alt="squiggles">
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup lang="ts">
import {onMounted, reactive, ref, Ref, watch} from "vue"

const emit = defineEmits<{
  (e: 'emotionUpdate', emotion: string): void
}>()

let angerButton: HTMLElement;
let fearButton: HTMLElement;
let sadnessButton: HTMLElement;
let noneButton: HTMLElement;
let ironyButton: HTMLElement;
let loveButton: HTMLElement;
let joyButton: HTMLElement;
onMounted(() => {
  angerButton = document.getElementById("anger") as HTMLElement
  fearButton = document.getElementById("fear") as HTMLElement
  sadnessButton = document.getElementById("sadness") as HTMLElement
  noneButton = document.getElementById("none") as HTMLElement
  ironyButton = document.getElementById("irony") as HTMLElement
  loveButton = document.getElementById("love") as HTMLElement
  joyButton = document.getElementById("joy") as HTMLElement

  document.addEventListener("keydown", (e) => {
    switch (e.key) {
      case "1": angerButton.focus(); angerButton.click(); break;
      case "2": fearButton.focus(); fearButton.click(); break;
      case "3": sadnessButton.focus(); sadnessButton.click(); break;
      case "4": noneButton.focus(); noneButton.click(); break;
      case "7": ironyButton.focus(); ironyButton.click(); break;
      case "8": loveButton.focus(); loveButton.click(); break;
      case "9": joyButton.focus(); joyButton.click(); break;
    }
  })
})

let primaryEmotions = ref([
    "anger",
    "fear",
    "sadness",
    "none",
    "irony",
    "love",
    "joy"
])
let currSelected = ref("none")

let secondaryEmotions = reactive({
  anger: ["Disgust", "Envy", "Exasperation", "Irritability", "Rage", "Torment"],
  fear: ["Nervousness", "Horror", "Anxiety", "Suspense", "Panic", "Worry"],
  sadness: ["Disappointment", "Loneliness", "Rejection", "Shame", "Embarrassment", "Suffering", "Sympathy"],
  none: [],
  irony: ["Sarcastic", "Satirical", "Cynical"],
  love: ["Caring", "Sentimental", "Tender", "Longing", "Lustful"],
  joy: ["Cheerful", "Content", "Enthrallment", "Optimism", "Pride", "Relief", "Zest"]
})

function handleClick(emotion: string) {
  currSelected.value = emotion
  emit('emotionUpdate', emotion)
}
</script>

<style scoped>
* {
  font-family: 'Arial', serif;
  border-radius: 10px;
}

.secondary-emotion {
    flex: auto;
    margin: 0;
    font-size: 12px;
    width: auto;
    height: 20px;
    border-style: none;
}

.primary-emotion {
    height: 100%;
    width: 100%;
    transition-duration: 0.2s;
    font-size: 24px;
    border-width: 10px;
    border-style: solid;
}

.emotion-container {
    height: 200px;
}

#anger, .anger {
    background-color: #c23a22;
    border-color: #c23a22;
    color: lightgray;
}

#anger:hover {
    background-color: white;
    color: black;
}

#anger:focus {
    background-color: white;
    color: black;
}

#fear, .fear {
    background-color: #7d54ae;
    border-color: #7d54ae;
    color: lightgray;
}

#fear:hover {
    background-color: white;
    color: black;
}

#fear:focus {
    background-color: white;
    color: black;
}

#joy, .joy {
    background-color: #f9d476;
    border-color: #f9d476;
}

#joy:hover {
    background-color: white;
}

#joy:focus {
    background-color: white;
}

#love, .love {
    background-color: #ffa0c5;
    border-color: #ffa0c5;
}

#love:hover {
    background-color: white;
}

#love:focus {
    background-color: white;
}

#sadness, .sadness {
    background-color: #3e65bf;
    border-color: #3e65bf;
    color: lightgray;
}

#sadness:hover {
    background-color: white;
    color: black;
}

#sadness:focus {
    background-color: white;
    color: black;
}

#irony, .irony {
    background-color: #bbbbbb;
    border-color: #bbbbbb;
}

#irony:hover {
    background-color: white;
}

#irony:focus {
    background-color: white;
}

#none, .none {
    background-color: black;
    border-color: black;
    color: lightgray;
}

#none:hover {
    background-color: white;
    color: black;
}

#none:focus {
    background-color: white;
    color: black;
}

.squiggle {
    height: 100px;
    width: 300px;
    padding-top: 30px;
}

.reflect {
    transform: scaleX(-1);
    float: right;
}

#current-category {
  font-size: 24px;
  width: 100%;
  height: 100%;
}
</style>