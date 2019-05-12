<template>
  <div class="home">
    <ul>
      <li>
        <router-link to="/terms/">
          terms
        </router-link>
      </li>
      <li>
        <router-link to="/quiz">
          quiz
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "home",
});
</script>
