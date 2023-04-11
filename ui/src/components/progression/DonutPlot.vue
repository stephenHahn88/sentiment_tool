<template>
    <div>
      <canvas id="donutChart" @dragEnd="handleDragEnd" @mouseup="handleClick(null);"></canvas>
    </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import _ from 'lodash'
import Chart from 'chart.js/auto'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

const props = defineProps(["currEmotionDist"])

let donutInput;
let donutChart;
let inputData = props.currEmotionDist;
let chartOptions = {
            type: "doughnut",
            data: {
                labels: ["anger", "fear", "sadness", "none", "irony", "love", "joy"],
                datasets: [ {
                    data: inputData,
                    borderWidth: 3,
                    borderColor: ['#c23a22', '#7d54ae', '#3e65bf', '#000000', '#bbbbbb', '#ffa0c5', '#f9d476'],
                    backgroundColor: ['rgb(194,58,34, 0.7)', 'rgb(125, 84, 174, 0.7)', 'rgb(62, 101, 191, 0.7)', 'rgb(0, 0, 0, 0.7)', 'rgb(187, 187, 187, 0.7)', 'rgb(255, 160, 197, 0.7)', 'rgb(249, 212, 118, 0.7)']
                } ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        }

function createChart(chartId, chartData) {
    const ctx = document.getElementById(chartId)
    donutChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
    })
}

function normalize(input) {
    let sum = _.sum(input)
    return input.map((e) => e/sum)
}

function updateEmotionMixture (newEmotionMixture) {
    donutInput = normalize(JSON.parse(JSON.stringify(newEmotionMixture)));
    donutChart.data.datasets.data = donutInput;
    donutChart.update();
}

onMounted(() => {
    createChart('donutChart', chartOptions)
})

defineExpose({ updateEmotionMixture });

</script>

<style>
</style>