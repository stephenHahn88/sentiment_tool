<template>
    <div>
      <canvas id="chart"></canvas>
    </div>
</template>

<script>

import { Chart, registerables } from 'chart.js'
import ChartJSdragDataPlugin from 'chartjs-plugin-dragdata'

let chartOptions = {
            type: "bar",
            data: {
                labels: ["anger", "fear", "sadness", "none", "irony", "love", "joy"],
                datasets: [ { data: [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2] } ]
            },
            options: {
                responsive: true,
                plugins: {dragData: true},
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