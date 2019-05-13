<template>
  <div>
    <input type="text" v-model="name">
    <div>次へ</div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      name: ""
    }
  }
})
</script>

