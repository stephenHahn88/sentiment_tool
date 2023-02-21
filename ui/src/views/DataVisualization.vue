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
        <b-container id="debug-container">
            <p id="debug"></p>
        </b-container>
        <MultiRangeSlider
          :min="0"
          :max="300"
          :minValue="minVal"
          :maxValue="maxVal"
          :labels="sliderLabels"
          min-caption="hi"
          max-caption="yo"
          :step="1"
          @input="UpdateValues"
        />
    </b-container>
    <div id="chart-container">
      <Doughnut
        :data="data"
        :options="options"
      ></Doughnut>
    </div>
  </b-container>
</template>

<script setup lang="ts">
import {computed, ref, Ref, reactive, watch} from "vue";
import MultiRangeSlider from "multi-range-slider-vue"
import {Analysis} from "@/types"
import {Doughnut} from "vue-chartjs";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend)

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

let minVal = ref(0)
let maxVal = ref(120)
function UpdateValues(e: any) {
  minVal.value = e.minValue
  maxVal.value = e.maxValue
}
let sliderLabels: Ref<string[]> = ref([])

let currData: Ref<Analysis[]> = ref([])
watch([minVal, maxVal], () => {
  data.datasets = [
      {
        backgroundColor: [
                '#c23a22',
                '#7d54ae',
                '#3e65bf',
                '#000000',
                '#bbbbbb',
                '#ffa0c5',
                '#f9d476'
            ],
        data: getEmotionPercentages(),
        hoverOffset: 10
      }
    ]
})

let data = reactive({
  labels: ['Anger', 'Fear', 'Sadness', 'None', 'Irony', 'Love', 'Joy'],
    datasets: [
      {
        backgroundColor: [
                '#c23a22',
                '#7d54ae',
                '#3e65bf',
                '#000000',
                '#bbbbbb',
                '#ffa0c5',
                '#f9d476'
            ],
        data: [1,1,1,1,1,1,1],
        hoverOffset: 10
      }
    ]
})

const options = {
  animation: {duration: 0},
  responsive: true,
  maintainAspectRatio: false
}

async function updateCurrChoice(choice: string) {
  currChoice.value = choice
  let choiceURI = choice.slice(0, 2).replace(".", "")
  let response = await (await fetch(`/api/song-analyses/${choiceURI}`)).json()
  currData.value = response.analyses
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
  console.log(answer)
  return answer
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