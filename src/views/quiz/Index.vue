<template>
  <div>
    <ul>
      <li v-for="term in terms" :key="term.id">
        <router-link :to="`quiz/${term.id}`">
          {{term.title}}
        </router-link>
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
        id,
        title
      }
    }`
  }
})
</script>