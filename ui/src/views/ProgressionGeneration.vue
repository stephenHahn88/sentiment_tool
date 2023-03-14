<template>
    <b-container>
      <div>
        <b-sidebar id="sidebar-1" title="Sidebar" shadow visible no-header-close>
          <div class="px-3 py-2">
            <p>
              Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
              in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
            </p>
            <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>
          </div>
        </b-sidebar>
      </div>
    </b-container>
  </template>
  
  <script setup lang="ts">
  import {onMounted, ref, Ref, watch} from "vue"
  import Instructions from "@/components/Instructions.vue";
  
  </script>
  
  <style scoped>
  
  </style>