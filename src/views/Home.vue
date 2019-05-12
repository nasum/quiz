<template>
  <div class="home">
    root
    <router-link to="/terms/">
      terms
    </router-link>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "home",
});
</script>
