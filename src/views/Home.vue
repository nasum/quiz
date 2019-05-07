<template>
  <div class="home">
    root
    <router-link to="/setting">
      setting
    </router-link>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "home",
});
</script>
