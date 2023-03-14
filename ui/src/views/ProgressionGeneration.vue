<template>
    <b-container>
      <Instructions></Instructions>
      <b-row>
        <b-col>
          <PieceSelection
            @choiceUpdated="handleChoiceUpdated"
          ></PieceSelection>
        </b-col>
        <b-col>
          <audio
              controls
              id="audio"
              :src="currAudioSrc"
              class="m-4"
          >
          </audio>
        </b-col>
      </b-row>
      <b-row>
        <EmotionButtons
          @emotionUpdate="handleEmotionUpdate"
        ></EmotionButtons>
      </b-row>
      <b-row class="my-5">
        <OutputPanel
          :current-emotion="currEmotion"
          :current-file="currAudioSrc"
        ></OutputPanel>
      </b-row>
    </b-container>
  </template>
  
  <script setup lang="ts">
  import {onMounted, ref, Ref, watch} from "vue"
  import Instructions from "@/components/Instructions.vue";
  import PieceSelection from "@/components/PieceSelection.vue";
  import EmotionButtons from "@/components/EmotionButtons.vue";
  import OutputPanel from "@/components/OutputPanel.vue";
  
  let audioElement: HTMLAudioElement;
  
  onMounted(() => {
    audioElement = document.getElementById("audio") as HTMLAudioElement
  })
  
  let currEmotion: Ref<string> = ref("none")
  
  let currAudioSrc = ref("src/media/op18_no1_mov4.mp3")
  
  function handleEmotionUpdate(emotion: string) {
    currEmotion.value = emotion
  }
  
  function handleChoiceUpdated(path: string) {
    currAudioSrc.value = path
  }
  
  
  </script>
  
  <style scoped>
  
  </style>