<template>
    <div>
        <h1 id = "chord-progression" v-for="RN in RNList"> {{ RN }}
        </h1>
    </div>
</template>

<script setup>

import { ref, watch, onMounted } from 'vue'
const props = defineProps(['currChord'])

const maxListLength = 5
let RNList = [props.currChord]

function addChord (lastRN) {
    RNList.push(lastRN);
    console.log(RNList)
    if (RNList.length > maxListLength) {
        RNList.shift();
    }
}

defineExpose({addChord})

</script>

<style>
</style>