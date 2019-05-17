<template>
  <div>
    <h1 v-if="!showTotalResult">{{term.questionsSet[this.index].description}}</h1>
    <h1 v-else>最終結果</h1>
    <div class="content">
      <div v-if="!showTotalResult">
        <ul class="answers">
          <li v-for="answer in term.questionsSet[this.index].answersSet" :key="answer.id">
            <label :for="answer.id" :class="answer.right && right ? 'show_right' : ''">
              <div>
                {{answer.description}}
                <img :src="answer.imgUrl" v-if="answer.imgUrl !== ''" class="answer_img">
              </div>
            </label>
          </li>
        </ul>
        <div>
          <button @click="toggleRight">正解を表示</button>
          <button @click="toggleResult">回答結果</button>
        </div>
        <div v-if="result">
          <ul class="result">
            <li v-for="(answer, index) in term.questionsSet[this.index].answersSet" :key="index">
              回答 {{index + 1}} :<div :style="{ width: answer.useranswerSet.length + '0px' }" :class="`answer_` + index">{{ answer.useranswerSet.length }}</div>
            </li>
          </ul>
        </div>
        <div class="next" @click="next">
          つぎへ
        </div>
      </div>
      <div v-else>
        <ul class="totalResult">
          <li v-for="(result, index) in sortedResult()" :key="index">
            <span>
              {{index + 1}}位
            </span>
            <span>
              {{result[1]}}問正解
            </span>
            <span>
              {{result[0]}}
            </span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import gql from 'graphql-tag'

export default Vue.extend({
  name: "Show",
  data () {
    return {
      index: 0,
      result: false,
      right: false,
      showTotalResult: false,
      totalResult: {}
    }
  },
  methods: {
    next() {
      if ((this.term.questionsSet.length - 1) == this.index) {
        this.showTotalResult = true
        this.createTotalResult()
      } else {
        this.index += 1
        this.result = false
        this.right = false
      }
    },
    toggleResult(){
      this.result = !this.result
    },
    toggleRight() {
      this.right = !this.right
    },
    createTotalResult(){
      this.term.questionsSet.forEach((question: any) => {
        const answer = question.answersSet.filter((answer: any) => answer.right === true)[0]
        answer.useranswerSet.forEach((userAnswer: any) => {
          const userId = userAnswer.userId
          if(this.totalResult.hasOwnProperty(userId)) {
            this.totalResult[userId] += 1
          } else {
            this.totalResult[userId] = 1
          }
        })
      })
    },
    sortedResult() {
      let sortable = [];
      for (let result in this.totalResult) {
        sortable.push([result, this.totalResult[result]]);
      }

      sortable.sort(function(a, b) {
        return b[1] - a[1];
      });
      return sortable
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
              right
              imgUrl
              useranswerSet {
                userId
                answersId
              }
            }
          }
        }
      }`,
      variables() {
        return {
          id: this.$route.params.id
        }
      },
      fetchPolicy: "no-cache"
    },
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

ul.answers {
  padding: 0;
  li {
    display: inline-block;
    list-style: none;
    width: 50%;
  }
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

ul.result {
  padding: 0;
  li {
    list-style: none;
  }
}

.answer_ {
  &0{
    background: #dc143c;
    color: #fff;
    display: inline-block;
  }
  &1{
    background: #006400;
    color: #fff;
    display: inline-block;
  }
  &2{
    background: #4169e1;
    color: #fff;
    display: inline-block;
  }
  &3 {
    background: #8a2be2;
    color: #fff;
    display: inline-block;
  }
}

.show_right {
  border: 10px solid #dc143c;
}

ul.totalResult {
  li {
    list-style: none;
    margin-left: 10px;
  }
  li:nth-child(1) span {
    font-size: 60px;
  }
  li:nth-child(2) span {
    font-size: 50px;
  }
  li:nth-child(3) span {
    font-size: 40px;
  }
  li:nth-child(4) span {
    font-size: 30px;
  }
}

  .answer_img {
    width: 100%;
    max-width: 500px;
  }
</style>
