<template>
    <div>
      <canvas id="barChart" @dragEnd="handleDragEnd"></canvas>
    </div>
</template>

<script setup>
    defineEmits(["emotionMixtureUpdate"])
</script>

<script>
import { Chart, registerables } from 'chart.js'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

let barInput;
let inputData = [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2]
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

export default {
    data() {
        return {
            chartOptions
        }
    },
    mounted() {
        Chart.register(...registerables)
        this.createChart('barChart', this.chartOptions)
    },
    methods: {
        createChart(chartId, chartData) {
            const ctx = document.getElementById(chartId)
            const myChart = new Chart(ctx, {
                type: chartData.type,
                data: chartData.data,
                options: chartData.options,
            })
        },
        handleDragEnd: function (e) {
            console.log("drag end detected")
            this.$emit("emotionMixtureUpdate", inputData)
        }
    }
}

</script>

<style>
</style>