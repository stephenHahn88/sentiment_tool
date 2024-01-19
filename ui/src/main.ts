import Vue from 'vue'
import VueRouter from 'vue-router'

import App from '@/App.vue'
import AnnotationTool from '@/views/AnnotationTool.vue'
import DataVisualization from '@/views/DataVisualization.vue'
import ProgressionGeneration from '@/views/ProgressionGeneration.vue'
import SentimentHarmonization from '@/views/SentimentHarmonization.vue'
import UploadMXML from '@/views/UploadMXML.vue'

import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue"

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueRouter)

export const router = new VueRouter({
  mode: "history",
  routes: [
    {
      meta: {title: "Annotation Tool"},
      path: "/",
      component: AnnotationTool
    },
    {
      meta: {title: "Data Charts"},
      path: "/data",
      component: DataVisualization
    },
    {
      meta: {title: "Progressions"},
      path: "/gen",
      component: ProgressionGeneration
    },
    {
      meta: {title: "Harmonization"},
      path: "/harmonize",
      component: SentimentHarmonization
    }
  ],
})

Vue.config.productionTip = false
Vue.config.devtools = true
Vue.config.warnHandler = (msg, instance, trace) =>
    ![
      'Avoid using Array as root value for reactive()'
    ].some((warning) => msg.includes(warning)) &&
    console.warn('[Vue warn]: '.concat(msg).concat(trace))

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  render: h => h(App),
})
