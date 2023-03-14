<template>
    <b-container>
        <Bar></Bar>
    </b-container>
</template>

<script setup lang="ts">

import {watch, reactive, computed, ref, Ref, onMounted} from "vue"
import {Bar} from "vue-chartjs";
import {Chart, registerables} from 'chart.js'

Chart.register(...registerables)


</script>

<style scoped>

</style>