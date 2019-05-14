<template>
  <div>
    <h2>New Term</h2>
    <div>
      <label>Term title</label>:<input type="text" v-model="title"><br>
      <ul>
        <li v-for="(question, index) in questions" :key="index">
          <div class="question">
            <div>Question {{index}}</div>
            <div>
              <label>Question Description</label>:<textarea v-model="question.description"></textarea>
            </div>
            <ul>
              <li v-for="(answer, index) in question.answers" :key="index">
                <div class="answer">
                  <div>
                    Answer {{index}}
                  </div>
                  <div>
                    <label>Answer Description</label>:<input type="text" v-model="answer.description">
                  </div>
                  <div>
                    <label>right</label><input type="radio" v-model="answer.right">
                  </div>
                </div>
              </li>
            </ul>
            <button class="button" @click="addAnswer(question)">new Answer</button>
          </div>
        </li>
      </ul>
      <button class="button" @click="addQuestion">new Question</button>
    </div>
    <div>
      <button @click="register">登録</button>
    </div>
    <ul>
      <li v-for="term in terms" :key="term.id">
        <router-link :to="`/terms/${term.id}`">
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
  name: 'Index',
  data: () => ({
    title: "term1",
    questions: [{
      description: "question 1",
      answers: [
        {
          description: "answer 1",
          right: false
        }
      ]
    }]
  }),
  methods: {
    addQuestion() {
      this.questions.push({
        description: "question 1",
        answers: [
          {
            description: "answer 1",
            right: false
          }
        ]
      })
    },
    addAnswer(question: any) {
      question.answers.push(
        {
          description: "answer 1",
          right: false
        }
      )
    },
    async register() {
      const result = await this.$apollo.mutate({
        // Query
        mutation: gql`mutation ($title: String!, $questions: [QuestionsInputType]){
          createTerm(title: $title, questions: $questions) {
            term {
              title
              questionsSet {
                description
                answersSet {
                  description
                  right
                }
              }
            }
          }
        }`,
        // Parameters
        variables: {
          title: this.title,
          questions: this.questions
        },
      })
      this.title = ""
      this.questions = [{
      description: "",
      answers: [
        {
          description: "",
          right: false
        }
      ]
    }]
    }
  },
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

<style lang="scss">
ul {
  padding: 0
}
li {
  list-style-type: none;
}

.question {
  margin: 5px;
  border: 1px solid black;
}

.answer {
  margin: 5px;
  border: 1px solid black;
}
</style>
