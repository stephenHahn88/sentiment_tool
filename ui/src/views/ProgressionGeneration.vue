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
                v-model="timerPerChordSpan"
            ></b-form-input>
          </b-form-group>
          <h5> Input Emotion Mixture </h5>
          <!-- Put bar plot input controls here -->
          <BarPlotInput id = "emotionMixtureInput" @emotionMixtureUpdate="handleEmotionMixtureUpdate"></BarPlotInput>
          <h5> Playback Controls </h5>
        </div>
      </b-sidebar>
    </div>
    <div class="body">
      
    </div>
  </b-container>
</template>

<script setup lang="ts">

import {onMounted, ref, Ref, watch} from "vue"
import BarPlotInput from "@/components/progression/BarPlotInput.vue";
import { Vue3Instance } from "vue/types/v3-component-public-instance";

let timerPerChord: Ref<number> = ref(0)
let timerPerChordSpan = ref(10)

function handleEmotionMixtureUpdate (mixtures: Array<number>) {
  console.log("update received");
}

onMounted (()=> {
  let barInput = document.getElementById("emotionMixtureInput") as Vue3Instance
  console.log(barInput)
})

</script>

<style scoped>

.body {
  margin-left: 320px;
}

</style>