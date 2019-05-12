<template>
  <div>
    {{term.title}}
    <ul>
      <li v-for="question in term.questionsSet" :key="question.id">
        {{question.description}}
        <ul>
          <li v-for="answer in question.answersSet" :key="answer.id">
            {{answer.description}}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import gql from 'graphql-tag'

export default Vue.extend({
  name: "Show",
  apollo: {
    term: {
      query: gql`query ($id: ID!){
        term(id: $id) {
          title,
          questionsSet {
            id
            description
            answersSet {
              id
              description
            }
          }
        }
      }`,
      variables() {
        return {
          id: this.$route.params.id
        }
      },
    }
  }
})
</script>

