<template>
    <div>
      <canvas id="barChart" @dragEnd="handleDragEnd"></canvas>
    </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

const props = defineProps(["priorDist"])
const emit = defineEmits(["emotionMixtureUpdate"])

let barInput
let inputData = props.priorDist
let chartOptions = {
            type: "bar",
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
                onHover: function(e) {
                    const point = e.chart.getElementsAtEventForMode(e, 'nearest', { intersect: true }, false)
                    if (point.length) e.native.target.style.cursor = 'grab'
                    else e.native.target.style.cursor = 'default'
                },
                plugins: {
                    dragData: {
                        onDragStart: function(e) {
                            // console.log(e)
                        },
                        onDrag: function(e, datasetIndex, index, value) {              
                            e.target.style.cursor = 'grabbing'
                            // console.log(e, datasetIndex, index, value)
                        },
                        onDragEnd: function(e, datasetIndex, index, value) {
                            e.target.style.cursor = 'default' 
                            inputData[index] = value;
                            const dragEndEvent = new Event("dragEnd")
                            e.target.dispatchEvent(dragEndEvent)
                        },
                    },
                    legend: {
                        display: false
                    },
                },
                scales: {
                    y: {
                        max: 1.0,
                        min: 0.01
                    }
                }
            }
        }

function createChart(chartId, chartData) {
    const ctx = document.getElementById(chartId)
    const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
    })
}

onMounted(() => {
    // Chart.register(...registerables)
    createChart('barChart', chartOptions)
})

function handleDragEnd (e) {
    console.log("drag end detected")
    emit("emotionMixtureUpdate", inputData)
}

</script>

<style>
</style>