<template>
    <Bar
      id="input-bar"
      :options="chartOptions"
      :data="chartData"
    />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

let chartData = {
            labels: ["anger", "fear", "sadness", "none", "irony", "love", "joy"],
            datasets: [ { data: [1, 0.8, 0.6, 0.4, 0.2, 0.2, 0.2] } ]
        }

export default {
    name: 'BarChart',
    components: { Bar },
    data() {
        return {
        chartData,
        chartOptions: {
            responsive: true
        }
        }
    }
}
</script>