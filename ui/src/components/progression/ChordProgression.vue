<template>
    <div>
        <h1 class = "chordRN">
            {{ RN }}
        </h1>
    </div>
</template>

<script setup lang="ts">
defineProps(['RN'])
</script>

<style>
.chordRN {
    margin-left: 50px;
    display: inline-block;
}
</style>