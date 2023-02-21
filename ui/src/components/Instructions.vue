<template>
  <b-container>
    <b-button
        v-b-toggle.collapse
        class="m-1"
        variant="light"
    >Toggle Instructions</b-button>
    <b-collapse visible id="collapse">
      <b-container id="description-large-container" class="largest-div">
      <div id="description-header-container">
        <h1 id="description-header">Instructions for use:</h1>
      </div>
      <div id="description-container">
        <ol>
          <li>Choose a recording from the drop down menu next to "Choose a piece."</li>
          <li>Listen as much as you like to the recording to prepare for annotation.</li>
          <li>When ready to annotate, press the "start annotation" button.</li>
          <ul>
            <li>The chosen piece will be locked until the page is reloaded or "clear and restart" is pressed</li>
            <li>Annotations will only be recorded while the recording is playing.</li>
            <li>Annotation can be halted at any time with the "stop annotation" button.</li>
            <li>If you wish to restart your annotation, use the "clear and restart" button (annotation must be off).</li>
          </ul>
          <li class="important-instruction">
            Choose from the large colored emotion buttons to annotate the recording with the appropriate emotion. Smaller colored bubbles show words that belong to the larger, primary emotions - you can look to these words if you have trouble associating a primary emotion with the music.
            <ul>
                <li>Choose the emotion that best fits each passage in your opinion. There are <strong>no wrong answers</strong>.</li>
                <li>
                    Buttons can be pressed with the mouse, or changed with the numbers in parentheses.
                    For example, you can switch to "Fear" by pressing 2 on your keyboard or "Joy" by pressing 9.
                </li>
            </ul>
          </li>
          <li>If there are any concerns with your analysis, the recording, or bugs, please write your comment(s) in the text area below your analysis.</li>
          <li>Once annotation is complete, submit your annotation with the "Complete and send to server" button below.</li>
          <li>Check out previous analyses <a id="data-anchor" @click="pushRouter('/data')">here</a> (under construction)</li>
        </ol>
      </div>
    </b-container>
    </b-collapse>
  </b-container>

</template>

<script setup lang="ts">
import {pushRouter} from "@/utility";


</script>

<style scoped>
#annotation-tool, #description-large-container  {
    background-color: rgba(255, 255, 255, 0);
    margin: 5px;
}

#data-anchor {
  color: blue;
}

#data-anchor:hover {
  color: blueviolet;
  cursor: pointer;
}

</style>