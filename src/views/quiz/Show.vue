<template>
  <div>
    <h1>{{term.title}}</h1>
    <div>
      <h2>{{term.questionsSet[this.index].description}}</h2>
      <ul>
        <li v-for="answer in term.questionsSet[this.index].answersSet" :key="answer.id">
          <label><input type="radio" name="answer" value="answer.right">{{answer.description}}</label>
        </li>
      </ul>
    </div>
    <div @click="next">
      next
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import gql from 'graphql-tag'

export default Vue.extend({
  name: "QuizShow",
  data() {
    return {
      index: 0,
      term: null
    }
  },
  methods: {
    next(){
      this.index += 1
    }
  },
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
      }
    }
  } 
})
</script>

