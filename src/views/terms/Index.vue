<template>
<ul>
  <li v-for="term in terms" :key="term.id">
    <router-link :to="`/terms/${term.id}`">
      {{term.title}}
    </router-link>
  </li>
</ul>
</template>

<script lang="ts">
import Vue from 'vue'
import gql from 'graphql-tag'

export default Vue.extend({
  name: 'Index',
  apollo: {
    terms: gql`query{
      terms {
        id,
        title
      }
    }`
  }    
})
</script>

