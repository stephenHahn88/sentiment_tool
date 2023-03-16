<!--BASED ON THE 'vue-music-notation' LIBRARY IMPLEMENTATION-->
<template>
    <div >
      <svg
        :width="width"
        :height="height"
        style="shape-rendering: crispEdges;"
        class="root"
      >
        <path
          :d="path.path"
          :class="{ [path.className]: true, 'anchor-note': path.anchor, active: path.active }"
          :key="path.note"
          v-for="path in keys"
        />
      </svg>
    </div>
  </template>
  
  <script setup lang="ts">
  import {ref, Ref} from 'vue'
  
  interface Props {
    length?: number,
    start?: number,
    notes?: number[]
  }
  
  const props = withDefaults(defineProps<Props>(), {
    length: 36,
    start: 53,
    notes: () => []
  })
  
  let width = ref(0)
  let height = ref(0)
  let keys_list: Ref<{ path: string; className: string; note: number; active: boolean; }[]> = ref([])
  
  const KEYSHAPES = [
    {type: 0, right: 1},          // C
    {type: 1},                    // C#
    {type: 0, right: 1, left: 1}, // D
    {type: 1},                    // D#
    {type: 0, left: 1},           // E
    {type: 0, right: 1},          // F
    {type: 1},                    // F#
    {type: 0, right: 1, left: 1}, // G
    {type: 1},                    // G#
    {type: 0, right: 1, left: 1}, // A
    {type: 1},                    // A#
    {type: 0, left: 1},           // B
  ];
  let NATURAL_WIDTH = 25
  let NATURAL_HEIGHT = NATURAL_WIDTH * 4;
  let SHARP_WIDTH = NATURAL_WIDTH / 2.5;
  let SHARP_HEIGHT = NATURAL_HEIGHT / 2;
  
  let notes = props.notes
  let start = props.start
  let length = props.length
  
  const isActive: { [id: number]: boolean } = {};
  notes.forEach(n => isActive[n] = true);

  let keys = [];
  
  let position = -NATURAL_WIDTH;
  position += 1;
  let wasSharp = false;
  for (let note = start; note < start + length; note++) {
    const shape = {...KEYSHAPES[note % 12]};
    if (note === start) {
      delete shape.left;
    }
    if (note === (start + length) - 1) {
      delete shape.right;
    }
  
    let path = '';
    let className = '';
    if (shape.type === 0) {
      position += wasSharp ? (SHARP_WIDTH / 2) : NATURAL_WIDTH;
      wasSharp = false;
  
      if (shape.right && shape.left) {
        path = `M ${position} ${NATURAL_HEIGHT + 1} v ${-SHARP_HEIGHT} `;
        path += `h ${(SHARP_WIDTH / 2)} v ${-SHARP_HEIGHT} `;
        path += `h ${NATURAL_WIDTH - SHARP_WIDTH} v ${SHARP_HEIGHT} h ${SHARP_WIDTH / 2} `;
        path += `v ${SHARP_HEIGHT} h ${-NATURAL_WIDTH}`;
      } else if (shape.right) {
        path = `M ${position} ${NATURAL_HEIGHT + 1} v ${-NATURAL_HEIGHT} `;
        path += `h ${NATURAL_WIDTH - (SHARP_WIDTH / 2)} v ${SHARP_HEIGHT} `;
        path += `h ${SHARP_WIDTH / 2} v ${SHARP_HEIGHT} h ${-NATURAL_WIDTH}`;
      } else if (shape.left) {
        path = `M ${position} ${NATURAL_HEIGHT + 1} v ${-SHARP_HEIGHT} `;
        path += `h ${SHARP_WIDTH / 2} v ${-SHARP_HEIGHT} `;
        path += `h ${NATURAL_WIDTH - (SHARP_WIDTH / 2)} v ${NATURAL_HEIGHT} h ${-NATURAL_WIDTH}`;
      } else {
        path = `M ${position} ${NATURAL_HEIGHT + 1} v ${-NATURAL_HEIGHT} `;
        path += `h ${NATURAL_WIDTH} v ${NATURAL_HEIGHT} h ${-NATURAL_WIDTH}`;
      }
      className = 'natural';
    } else {
      position += NATURAL_WIDTH - (SHARP_WIDTH / 2);
  
      path = `M ${position} ${SHARP_HEIGHT + 1} v ${-SHARP_HEIGHT} `;
      path += `h ${SHARP_WIDTH} v ${SHARP_HEIGHT} h ${-SHARP_WIDTH}`;
  
      wasSharp = true;
      className = 'sharp';
    }
  
    keys.push({
      path,
      className,
      note,
      active: isActive[note],
      anchor: note === 60
    });
  }
  
  
  keys_list.value = keys
  height.value = NATURAL_HEIGHT + 2
  width.value = position + NATURAL_WIDTH + 2
  </script>
  
  <style scoped>
  .root {
    --white-key: #F7F3E5;
    --black-key: #1C110F;
    --activated: mediumpurple;
    --stroke-width: 2;
    --anchor-note: #D5D1C3;
  }
  
  .natural {
    fill: var(--white-key);
    stroke-width: var(--stroke-width);
    stroke: var(--black-key);
  }
  
  .sharp {
    fill: var(--black-key);
    stroke-width: var(--stroke-width);
    stroke: var(--black-key);
  }
  
  .active {
    fill: var(--activated);
  }
  
  .anchor-note {
    fill: var(--anchor-note)
  }
  </style>