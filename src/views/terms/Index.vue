<template>
  <div>
    <h2>イベントの作成</h2>
    <div>
      <label>イベント名</label>:<input type="text" v-model="title"><br>
      <ul>
        <li v-for="(question, q_index) in questions" :key="q_index">
          <div class="question">
            <div><button @click="deleteQuestion(q_index)">×</button> Question {{q_index}}</div>
            <div>
              <label>問題 </label>:<textarea v-model="question.description"></textarea>
            </div>
            <ul>
              <li v-for="(answer, index) in question.answers" :key="index">
                <div class="answer">
                  <div>
                    答え {{index}}
                  </div>
                  <div>
                    <label>答え文字</label>:<input type="text" v-model="answer.description">
                  </div>
                  <div>
                    <label>画像URL</label><input type="text" v-model="answer.imgUrl"><br>
                    <img v-if="answer.imgUrl !== ''" :src="answer.imgUrl" width="100">
                  </div>
                  <div>
                    <label>正解</label>
                    <select v-model="answer.right">
                      <option value="true">正解</option>
                      <option value="false">不正解</option>
                    </select>
                  </div>
                </div>
              </li>
            </ul>
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

const QUESTION = {
  description: "question 1",
  answers: [
    {
      description: "answer 1",
      imgUrl: "",
      right: false
    },{
      description: "answer 2",
      imgUrl: "",
      right: false
    },{
      description: "answer 3",
      imgUrl: "",
      right: false
    },{
      description: "answer 4",
      imgUrl: "",
      right: false
    },
  ]
}

export default Vue.extend({
  name: 'Index',
  data: () => ({
    title: "term1",
    questions: [JSON.parse(JSON.stringify(QUESTION))]
  }),
  methods: {
    addQuestion() {
      this.questions.push(JSON.parse(JSON.stringify(QUESTION)))
    },
    deleteQuestion(index: number) {
      this.questions.splice(index, 1)
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
                  imgUrl
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

<style lang="scss" scoped>
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
