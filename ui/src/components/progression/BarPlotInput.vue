<template>
    <div>
      <canvas id="chart"></canvas>
    </div>
</template>

<script setup>
    defineEmits(["emotionMixtureUpdate"])
</script>

<script>

import { Chart, registerables } from 'chart.js'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

let inputData = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2]
let chartOptions = {
            type: "bar",
            data: {
                labels: ["anger", "fear", "sadness", "none", "irony", "love", "joy"],
                datasets: [ { data: inputData } ]
            },
            options: {
                responsive: true,
                onHover: function(e) {
                    const point = e.chart.getElementsAtEventForMode(e, 'nearest', { intersect: true }, false)
                    if (point.length) e.native.target.style.cursor = 'grab'
                    else e.native.target.style.cursor = 'default'
                },
                plugins: {dragData: {
                    onDragStart: function(e) {
                        // console.log(e)
                    },
                    onDrag: function(e, datasetIndex, index, value) {              
                        e.target.style.cursor = 'grabbing'
                        // console.log(e, datasetIndex, index, value)
                    },
                    onDragEnd: function(e, datasetIndex, index, value) {
                        e.target.style.cursor = 'default' 
                        console.log(datasetIndex, index, value)
                        inputData[index] = value;
                        console.log(inputData)
                        e => {
                            this.emit('emotionMixtureUpdate', inputData)
                        }
                    },
                }},
                scales: {
                    y: {
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
        this.createChart('chart', this.chartOptions)
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