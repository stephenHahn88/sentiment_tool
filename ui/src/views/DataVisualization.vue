<template>
  <b-container>
    <b-container class="">
        <b-container id="audio-selection-container">
            <label for="audio-options" style="font-size: 28px;">
              Choose a piece:
            </label>
            <b-dropdown
                name="audio-options"
                id="audio-options"
                style="width: 200px"
                variant="light"
                :text="currChoice"
                class="m-3"
            >
                <b-dropdown-item
                  v-for="item in dropDownItems"
                  @click="updateCurrChoice(item)"
                >
                  {{item}}
                </b-dropdown-item>
            </b-dropdown>
        </b-container>
        <audio
            controls
            id="audio"
            :src="currAudioSrc"
            class="m-4"

        ></audio>
        <b-form-group>
          <label for="time-span">Time Span:</label>
          <b-form-input
              id="time-span"
              style="width: 80px;"
            type="number"
            v-model="timeSpan"
          ></b-form-input>
        </b-form-group>
        <b-container id="debug-container">
            <p id="debug"></p>
        </b-container>
        <MultiRangeSlider
          :min="0"
          :max="maxTime"
          :minValue="minVal"
          :maxValue="maxVal"
          :labels="sliderLabels"
          :min-caption="minCaption"
          :max-caption="maxCaption"
          :step="0.01"
          @input="UpdateValues"
        />
    </b-container>
    <div id="chart-container" style="width: 500px; height: 500px">
      <canvas id="chart" style="width: 500px; height: 500px"></canvas>
    </div>
  </b-container>
</template>

<script setup lang="ts">
import {computed, ref, Ref, reactive, watch, onMounted} from "vue";
import MultiRangeSlider from "multi-range-slider-vue"
import {Analysis} from "@/types"
import { Chart, registerables } from 'chart.js'
import {round} from "lodash"
import {createLabels, timeString} from "@/utility";

Chart.register(...registerables)

let audioElement: HTMLAudioElement;
onMounted(() => {
  audioElement = document.getElementById("audio") as HTMLAudioElement
  audioElement.addEventListener('timeupdate', () => {
    currAudioTime.value = audioElement.currentTime
  }, false);
})

let dropDownItems = computed(() => {
  return Object.keys(choiceToPath)
})
let choiceToPath = {
  "1. Gute Nacht (1933)": "src/media/Schubert_D911-01_HU33.wav",
  "2. Die Wetterfahne (1933)": "src/media/Schubert_D911-02_HU33.wav",
  "3. Gefror'ne Tranen (1933)": "src/media/Schubert_D911-03_HU33.wav",
  "4. Erstarrung (1933)": "src/media/Schubert_D911-04_HU33.wav",
  "5. Der Lindenbaum (1933)": "src/media/Schubert_D911-05_HU33.wav",
  "6. Wasserflut (1933)": "src/media/Schubert_D911-06_HU33.wav",
  "7. Auf dem Flusse (1933)": "src/media/Schubert_D911-07_HU33.wav",
  "8. Ruckblick (1933)": "src/media/Schubert_D911-08_HU33.wav",
  "9. Irrlicht (1933)": "src/media/Schubert_D911-09_HU33.wav",
  "10. Rast (1933)": "src/media/Schubert_D911-10_HU33.wav",
  "11. Fruhlingstraum (1933)": "src/media/Schubert_D911-11_HU33.wav",
  "12. Einsamkeit (1933)": "src/media/Schubert_D911-12_HU33.wav",
  "13. Die Post (1933)": "src/media/Schubert_D911-13_HU33.wav",
  "14. Der greise Kopf (1933)": "src/media/Schubert_D911-14_HU33.wav",
  "15. Die Krahe (1933)": "src/media/Schubert_D911-15_HU33.wav",
  "16. Letzte Hoffnung (1933)": "src/media/Schubert_D911-16_HU33.wav",
  "17. Im Dorfe (1933)": "src/media/Schubert_D911-17_HU33.wav",
  "18. Der sturmische Morgen (1933)": "src/media/Schubert_D911-18_HU33.wav",
  "19. Tauschung (1933)": "src/media/Schubert_D911-19_HU33.wav",
  "20. Der Wegweiser (1933)": "src/media/Schubert_D911-20_HU33.wav",
  "21. Das Wirtshaus (1933)": "src/media/Schubert_D911-21_HU33.wav",
  "22. Mut! (1933)": "src/media/Schubert_D911-22_HU33.wav",
  "23. Die Nebensonnen (1933)": "src/media/Schubert_D911-23_HU33.wav",
  "24. Der Leiermann (1933)": "src/media/Schubert_D911-24_HU33.wav",
  "1. Gute Nacht (2006)": "src/media/Schubert_D911-01_SC06.wav",
  "2. Die Wetterfahne (2006)": "src/media/Schubert_D911-02_SC06.wav",
  "3. Gefror'ne Tranen (2006)": "src/media/Schubert_D911-03_SC06.wav",
  "4. Erstarrung (2006)": "src/media/Schubert_D911-04_SC06.wav",
  "5. Der Lindenbaum (2006)": "src/media/Schubert_D911-05_SC06.wav",
  "6. Wasserflut (2006)": "src/media/Schubert_D911-06_SC06.wav",
  "7. Auf dem Flusse (2006)": "src/media/Schubert_D911-07_SC06.wav",
  "8. Ruckblick (2006)": "src/media/Schubert_D911-08_SC06.wav",
  "9. Irrlicht (2006)": "src/media/Schubert_D911-09_SC06.wav",
  "10. Rast (2006)": "src/media/Schubert_D911-10_SC06.wav",
  "11. Fruhlingstraum (2006)": "src/media/Schubert_D911-11_SC06.wav",
  "12. Einsamkeit (2006)": "src/media/Schubert_D911-12_SC06.wav",
  "13. Die Post (2006)": "src/media/Schubert_D911-13_SC06.wav",
  "14. Der greise Kopf (2006)": "src/media/Schubert_D911-14_SC06.wav",
  "15. Die Krahe (2006)": "src/media/Schubert_D911-15_SC06.wav",
  "16. Letzte Hoffnung (2006)": "src/media/Schubert_D911-16_SC06.wav",
  "17. Im Dorfe (2006)": "src/media/Schubert_D911-17_SC06.wav",
  "18. Der sturmische Morgen (2006)": "src/media/Schubert_D911-18_SC06.wav",
  "19. Tauschung (2006)": "src/media/Schubert_D911-19_SC06.wav",
  "20. Der Wegweiser (2006)": "src/media/Schubert_D911-20_SC06.wav",
  "21. Das Wirtshaus (2006)": "src/media/Schubert_D911-21_SC06.wav",
  "22. Mut! (2006)": "src/media/Schubert_D911-22_SC06.wav",
  "23. Die Nebensonnen (2006)": "src/media/Schubert_D911-23_SC06.wav",
  "24. Der Leiermann (2006)": "src/media/Schubert_D911-24_SC06.wav"
}
let currChoice = ref(Object.keys(choiceToPath)[0])
let currAudioSrc: Ref<string> = computed(() => {
  return choiceToPath[currChoice.value]
})
let currAudioTime: Ref<number> = ref(0)
let timeSpan = ref(10)
watch(currAudioTime, async () => {
  maxVal.value = await currAudioTime.value + 0.1
  minVal.value = await Math.max(currAudioTime.value - timeSpan.value, 0)
})

let minVal = ref(0)
let maxVal = ref(120)
function UpdateValues(e: any) {
  minVal.value = e.minValue
  maxVal.value = e.maxValue
}
watch([minVal, maxVal], () => {
  graph(getEmotionPercentages())
})
let maxTime = ref(50)
let minCaption = computed(() => timeString(minVal.value))
let maxCaption = computed(() => timeString(maxVal.value))
let sliderLabels: Ref<string[]> = ref([])

let currData: Ref<Analysis[]> = ref([])

async function updateCurrChoice(choice: string) {
  currChoice.value = choice

  let choiceURI = choice.slice(0, 2).replace(".", "")
  let response = await (await fetch(`/api/song-analyses/${choiceURI}`)).json()
  currData.value = response.analyses
  maxTime.value = round(audioElement.duration)
  sliderLabels.value = createLabels(maxTime.value, 10)
  minVal.value = 0
  maxVal.value = audioElement.duration - 0.1
  graph(getEmotionPercentages())
}

function getEmotionPercentages() {
  let counts = {
      "anger": 0,
      "fear": 0,
      "sadness": 0,
      "none": 0,
      "irony": 0,
      "love": 0,
      "joy": 0
  }
  let total = 0
  for (let analysis of currData.value) {
    for (let key of Object.keys(analysis.analysis)) {
      let k = parseFloat(key)
      if (k > minVal.value && k < maxVal.value) {
        counts[analysis.analysis[key]]++;
        total++;
      }
    }
  }
  let answer = []
  for (let [emotion, count] of Object.entries(counts)) {
    answer.push(count)
  }
  return answer
}

let calls = 0
let myChart: Chart;
function graph(emotion_data: number[]) {
  let chart = document.getElementById('chart') as HTMLCanvasElement
  if (calls > 0) {
    myChart.destroy()
  }
  const labels = ['Anger', 'Fear', 'Sadness', 'None', 'Irony', 'Love', 'Joy']
  const data = {
      labels: labels,
      datasets: [{
          label: 'test',
          backgroundColor: [
              '#c23a22',
              '#7d54ae',
              '#3e65bf',
              '#000000',
              '#bbbbbb',
              '#ffa0c5',
              '#f9d476'
          ],
          data: emotion_data,
          hoverOffset: 10,
      }]
  };
  const config = {
      type: 'doughnut',
      data: data,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          duration: 0
        }
      }
  }
  myChart = new Chart(
      chart,
      config as any
  )

  calls++;
}
</script>

<style scoped>
#audio-options {
    font-size: 24px;
    height: 50px;
}

#audio-selection-container {
    padding: 10px;
}
</style>