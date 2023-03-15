<template>
    <div>
      <canvas id="lineChart"></canvas>
    </div>
</template>

<script setup>
    defineEmits(["emotionMixtureUpdate"])
</script>

<script>
import { Chart, registerables } from 'chart.js'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

// Each row is the progression of one emotion through 10 time steps
let emotionProgressionMatrix = [[1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2, 0.4, 0.2, 0.2, 0.2],
                                [0.8, 0.7, 0.8, 0.2, 0.3, 0.2, 0.2, 0.5, 0.2, 0.2, 0.2],
                                [0.6, 0.6, 0.7, 0.4, 0.4, 0.2, 0.2, 0.6, 0.2, 0.2, 0.2],
                                [0.4, 0.5, 0.6, 0.3, 0.5, 0.2, 0.2, 0.9, 0.2, 0.2, 0.2],
                                [0.3, 0.4, 0.5, 0.4, 0.6, 0.2, 0.2, 0.5, 0.2, 0.2, 0.2],
                                [0.2, 0.3, 0.4, 0.1, 0.7, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2],
                                [0.1, 0.2, 0.3, 0.1, 0.8, 0.2, 0.2, 0.9, 0.2, 0.2, 0.2]]
let timePerChord = 1

function generateLabels() {
    return Array.from(new Array(10), (val,index) => timePerChord*index );
}

function normalize(input) {
    let sum = 0;
    for (let i=0; i<input.length; i++) {
        sum += input[i];
    }
    if (sum == 0) {
        sum = 1;
    }
    for (let i=0; i<input.length; i++) {
        input[i] = input[i] / sum;
    }
    return input;
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

function normData() {

    // Transpose matrix
    emotionProgressionMatrix = emotionProgressionMatrix[0].map((_, colIndex) => emotionProgressionMatrix.map(row => row[colIndex]));

    // Normalize each row (former columns)
    for (let i=0; i<emotionProgressionMatrix.length; i++) {
        emotionProgressionMatrix[i] = normalize(emotionProgressionMatrix[i]);
        // emotionProgressionMatrix[i] = cumulativeSum(emotionProgressionMatrix[i]);
    }
    
    // Tranpose matrix back
    emotionProgressionMatrix = emotionProgressionMatrix[0].map((_, colIndex) => emotionProgressionMatrix.map(row => row[colIndex]));

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
                    }
                },
                scales: {
                    y: {
                        stacked: true,
                        max: 1.0,
                        min: 0.01
                    }
                }
            }
        }

export default {
    data() {
        return {
            chartOptions
        }
    },
    mounted() {
        Chart.register(...registerables)
        this.createChart('lineChart', this.chartOptions)
    },
    methods: {
        createChart(chartId, chartData) {
            const ctx = document.getElementById(chartId)
            const myChart = new Chart(ctx, {
                type: chartData.type,
                data: chartData.data,
                options: chartData.options,
            })
        }
    }
}

</script>

<style>
</style>