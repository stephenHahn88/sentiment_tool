<template>
    <div>
      <canvas id="lineChart"></canvas>
    </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
const props = defineProps(['time', 'currEmotionDist'])
const emit = defineEmits(['timedEmit', 'timedGraphUpdate'])

import Chart from 'chart.js/auto'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

let areaChart;

const displayDuration = 10
let timePerChord = props.time

function buildInitMatrix (currEmotionDist) {
    let matrix = [[],[],[],[],[],[],[]]
    for (let i=0; i<7; i++) {
        for (let j=0; j<displayDuration; j++) {
            matrix[i].push(currEmotionDist[i])
        }
    }
    return matrix
}

// Each row is the progression of one emotion through 10 time steps
let emotionProgressionMatrix = buildInitMatrix(props.currEmotionDist)

function updateTime (newTime) {
    if (newTime === '') {
        return;
    }
    timePerChord = newTime;
    //let newLabels = generateLabels();
    //areaChart.data.labels = newLabels;
    //areaChart.update();
}

function updateEmotionMixture (newEmotionMixture) {
    newEmotionMixture = normalize(JSON.parse(JSON.stringify(newEmotionMixture)));
    // Update emotionProgressionMatrix
    for (let r=0; r<emotionProgressionMatrix.length; r++) {
        emotionProgressionMatrix[r].shift();
        emotionProgressionMatrix[r].push(newEmotionMixture[r]);
    }
    // Update chart - remove earliest data
    areaChart.data.labels.shift();
    areaChart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });

    // Update chart - push new data
    areaChart.data.labels.push(parseInt(areaChart.data.labels[areaChart.data.labels.length - 1]) + parseInt(timePerChord));
    // areaChart.data.datasets = generateDataset();
    let index = 0;
    areaChart.data.datasets.forEach((dataset) => {
        dataset.data.push(newEmotionMixture[index]);
        index++;
    });
    areaChart.update();
}

function generateLabels() {
    return Array.from(new Array(displayDuration), (val,index) => timePerChord*index );
}

function normalize(input) {
    let sum = _.sum(input)
    return input.map((e) => e/sum)
}

function cumulativeSum(input) {
    let sum = input[0];
    let newInput = [input[0]];
    for (let i=1; i<input.length; i++) {
        newInput.push(input[i] + sum);
        sum += input[i];
    }
    return newInput;
}

function transposeMatrix(input) {
    return input[0].map((_, colIndex) => input.map(row => row[colIndex]));
}

function normData() {
    // Transpose matrix
    emotionProgressionMatrix = transposeMatrix(emotionProgressionMatrix);
    // Normalize each row (former columns)
    for (let i=0; i<emotionProgressionMatrix.length; i++) {
        emotionProgressionMatrix[i] = normalize(emotionProgressionMatrix[i]);
        // emotionProgressionMatrix[i] = cumulativeSum(emotionProgressionMatrix[i]);
    }
    // Tranpose matrix back
    emotionProgressionMatrix = transposeMatrix(emotionProgressionMatrix);
}

const emotionLabels = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
const fillTo = ["origin", "+1", "+2", "+3", "+4", "+5", "+6"]
const borderColors = ['#c23a22', '#7d54ae', '#3e65bf', '#000000', '#bbbbbb', '#ffa0c5', '#f9d476']
const backgroundColors = ['rgb(194,58,34, 0.7)', 'rgb(125, 84, 174, 0.7)', 'rgb(62, 101, 191, 0.7)', 'rgb(0, 0, 0, 0.7)', 'rgb(187, 187, 187, 0.7)', 'rgb(255, 160, 197, 0.7)', 'rgb(249, 212, 118, 0.7)']

function generateDataset() {
    // Normalize matrix
    normData();
    let chartDataset = [];
    let chartDataTemplate = {
        label: "anger",
        data: emotionProgressionMatrix[0],
        fill: "stack",
        borderColor: '#c23a22',
        backgroundColor: 'rgb(194,58,34, 0.7)'
    };
    for (let i=0; i<7; i++) {
        let currData = JSON.parse(JSON.stringify(chartDataTemplate));
        currData.label = emotionLabels[i];
        currData.data = emotionProgressionMatrix[i];
        currData.borderColor = borderColors[i];
        currData.backgroundColor = backgroundColors[i];
        chartDataset.push(currData);
    }
    return chartDataset;
}

let chartOptions = {
            type: "line",
            data: {
                labels: generateLabels(),
                datasets: generateDataset()
            },
            options: {
                responsive: true,
                plugins: {
                    filler: {
                        propagate: true
                    },
                    // legend: {
                    //     labels: {   
                    //         font: {
                    //             family: 'consolas'
                    //         }
                    //     }
                    // }
                },
                scales: {
                    x: {
                        display: false
                    },
                    y: {
                        stacked: true,
                        max: 1.0,
                        min: 0.01
                    }
                }
            }
        }

function createChart(chartId, chartData) {
    const ctx = document.getElementById(chartId)
    areaChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
    })
    areaChart.options.animations = false;
}

onMounted(() => {
    createChart('lineChart', chartOptions)
})

setInterval(() => {
    emit("timedGraphUpdate")
}, 1000);


setInterval(() => {
    emit("timedEmit")
}, timePerChord * 1000);

defineExpose({ updateTime, updateEmotionMixture });

</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Press+Start+2P');
</style>