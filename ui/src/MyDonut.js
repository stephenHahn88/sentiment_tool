import {Doughnut} from "vue-chartjs";

export class MyDonut extends Doughnut {
  name: 'DoughnutChart',
  props: ['data', 'options'],
  mounted () {
    this.renderChart(this.data, this.options)
  },
  watch: {
    data: function () {
      this._data._chart.destroy()
      this.renderChart(this.data, this.options)
    }
  }
})