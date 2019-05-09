<template>
<div>
  <h1>Setting</h1>
  <ul>
    <li v-for="term in terms" :key="term">
      {{term.title}}
    </li>
  </ul>
</div>
</template>

<script lang="ts">
import Vue from 'vue'
import gql from 'graphql-tag'

export default Vue.extend({
  apollo: {
    terms: gql`query{
      terms {
        title
      }
    }`
  }    
})
</script>

