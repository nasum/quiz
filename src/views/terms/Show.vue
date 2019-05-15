<template>
  <div>
    イベント名：{{term.title}}
    <ul>
      <li v-for="question in term.questionsSet" :key="question.id">
        {{question.description}}
        <ul>
          <li v-for="answer in question.answersSet" :key="answer.id">
            <div>
              {{answer.description}}
            </div>
            <div>
              <img :src="answer.imgUrl" v-if="answer.imgUrl !== ''">
            </div>
            <div>
              <span v-if="answer.right">○</span>
              <span v-else>×</span>
            </div>
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
              right
              imgUrl
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

<style lang="scss" scoped>
  ul {
    padding: 0;
  }
  li {
    list-style-type: none;
  }
</style>
