<template>
    <div>
      <canvas id="barChart" @dragEnd="handleDragEnd" @mouseup="handleClick(null);"></canvas>
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
let textColor = "#888888"
let sentimentColors = ['rgb(194,58,34, 0.7)', 'rgb(125, 84, 174, 0.7)', 'rgb(62, 101, 191, 0.7)', 'rgb(0, 0, 0, 0.7)', 'rgb(187, 187, 187, 0.7)', 'rgb(255, 160, 197, 0.7)', 'rgb(249, 212, 118, 0.7)']
let sentimentBorderColors = ['#c23a22', '#7d54ae', '#3e65bf', '#000000', '#bbbbbb', '#ffa0c5', '#ecaa77']
let chartOptions = {
            type: "bar",
            data: {
                labels: ["anger", "fear", "sadness", "none", "irony", "love", "joy"],
                datasets: [ {
                    data: inputData,
                    borderWidth: 3,
                    borderColor: sentimentBorderColors,
                    backgroundColor: sentimentColors
                } ]
            },
            options: {
                responsive: true,
                onHover: function(e) {
                    const point = e.chart.getElementsAtEventForMode(e, 'nearest', { intersect: true }, false)
                    if (point.length) e.native.target.style.cursor = 'grab'
                    else e.native.target.style.cursor = 'default'
                },
                onClick: function(e) {
                    const points = e.chart.getElementsAtEventForMode(e, 'x', { intersect: false }, true);
                    if (points.length) {

                        const firstPoint = points[0];
                        const label = e.chart.data.labels[firstPoint.index];
                        const value = e.chart.data.datasets[firstPoint.datasetIndex].data[firstPoint.index];
                        
                        console.log(e.chart.data.datasets);

                        const height = e.chart.height;
                        e.chart.data.datasets[firstPoint.datasetIndex].data[firstPoint.index] = (height - e.y)/height;
                        e.chart.update();

                        // Send a mouseup event to so that it triggers after the code in this onClick function triggers
                        const clickEvent = new Event("mouseup")
                        e.native.target.dispatchEvent(clickEvent)
                    }
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
                    x: {
                      ticks: {
                        font: {
                          size: 18
                        },
                        color: sentimentBorderColors
                      },
                      title: {
                        display: true,
                        text: 'Sentiments',
                        font: {
                          size: 24
                        },
                        padding: 20,
                        color: textColor
                      }
                    },
                    y: {
                        max: 1.0,
                        min: 0.01,
                        includeBounds: false,
                        ticks: {
                          font: {
                            size: 18
                          },
                          stepSize: 0.25,
                          autoSkip: false,
                            // Include a dollar sign in the ticks
                          callback: function(value, index, ticks) {
                              if (value <= 0.01) {
                                  return "none"
                              } else if (value <= 0.25) {
                                  return "mild"
                              } else if (value <= 0.5) {
                                  return "moderate"
                              } else if (value <= 0.75) {
                                  return "intense"
                              } else if (value <= 1) {
                                  return "extreme"
                              }
                          },
                          color: textColor
                        },
                        title: {
                          display: true,
                          text: 'Intensity',
                          font: {
                            size: 24
                          },
                          padding: 20,
                          color: textColor
                        }
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

function handleClick (e) {
    console.log("click updated")
    emit("emotionMixtureUpdate", inputData)
}

</script>

<style>
</style>
