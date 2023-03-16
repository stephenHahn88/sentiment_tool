<template>
    <div>
        <h1 id = "chord-progression"> {{ props.currChord }}
        </h1>
    </div>
</template>

<script setup>

import { ref, watch, onMounted } from 'vue'
const props = defineProps(['currChord'])

function addChord () {
    
}

defineExpose({addChord})

</script>

<style>
</style>