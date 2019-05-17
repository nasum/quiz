<template>
  <div>
    <h1>{{term.title}}</h1>
    <div class="content">
      <div v-if="step === 0">
        IDを入力してください
        <input class="user_name_input" type="text" v-model="userId">
        <div class="next" @click="goQuiz">
          つぎへ
        </div>
      </div>
      <div v-else-if="step === 1">
        <h2>{{term.questionsSet[this.index].description}}</h2>
        <ul>
          <li v-for="answer in term.questionsSet[this.index].answersSet" :key="answer.id">
            <input type="radio" name="answer" :value="answer.right" :id="answer.id" @click="setAnswer(answer.id)">
            <label :for="answer.id">
              <div>
                {{answer.description}}
                <img :src="answer.imgUrl" v-if="answer.imgUrl !== ''" class="answer_img">
              </div>
            </label>
          </li>
        </ul>
        <div class="next" @click="next">
          つぎへ
        </div>
      </div>
      <div v-else>
        <h2>クイズの結果</h2>
        <table>
          <tr v-for="(answer, index) in answerHistory" :key="index">
            <td>第{{index + 1}}問目</td>
            <td>
              <span v-if="answer">○</span>
              <span v-else>×</span>
            </td>
          </tr>
        </table>
      </div>
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
      term: null,
      userId: '',
      answerId: null,
      step: 0,
      answerHistory: [],
    }
  },
  methods: {
    goQuiz(){
      if(this.userId !== '') {
        this.step = 1
      }
    },
    setAnswer(id: number){
      this.answerId = id
    },
    async next(){
      if(!confirm('次の問題に進みますか？')){
        return
      }
      await this.$apollo.mutate({
        // Query
        mutation: gql`
        mutation($answersId: Int!, $userId: String!){
          createUserAnswer(answersId: $answersId, userId: $userId){
           userAnswer{
              answersId
           }
          }
        }
        `,
        // Parameters
        variables: {
          answersId: this.answerId,
          userId: this.userId
        }
      })

      const answer = this.term.questionsSet[this.index].answersSet.find((answer: any) => answer.id == this.answerId)

      if(answer.right) {
        this.answerHistory.push(true)
      } else {
        this.answerHistory.push(false)
      }

      if ((this.term.questionsSet.length - 1) == this.index) {
        alert('終了')
        this.step = 2
      } else {
        this.index += 1
        this.answerId = null
      }
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
              imgUrl
              right
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

<style lang="scss" scoped>
h1 {
  background: #002F89;
  color: #fff;
  margin: 0;
  padding: 5px;
}

.content {
  padding: 5px;
}

ul {
  padding: 0;
}

li {
  display: inline-block;
  list-style: none;
  width: 50%;
}

input[type=radio] {
  display: none;
}

input[type="radio"]:checked + label {
  background: #31A9EE;
  color: #ffffff;
}

label {
  box-sizing: border-box;
  padding: 5px;
  display: block;
  border: 1px solid #006DD9;
  width: 100%;
  cursor: pointer;
  text-align: center;
}

.next {
  text-align: center;
  border: 1px solid #006DD9;
  box-sizing: border-box;
  padding: 5px;
  cursor: pointer;
}

.user_name_input {
  width: 100%;
  border:0;
  padding:10px;
  font-size:1.3em;
  font-family:Arial, sans-serif;
  color:#aaa;
  border:solid 1px #ccc;
  margin-bottom: 20px;
}

.answer_img {
  width: 100%;
  max-width: 500px;
}
</style>

