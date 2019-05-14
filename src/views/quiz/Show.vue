<template>
  <div>
    <h1>{{term.title}}</h1>
    <div class="content">
      <h2>{{term.questionsSet[this.index].description}}</h2>
      <ul>
        <li v-for="answer in term.questionsSet[this.index].answersSet" :key="answer.id">
          <input type="radio" name="answer" :value="answer.right" :id="answer.id"><label :for="answer.id">{{answer.description}}</label>
        </li>
      </ul>
      <div class="next" @click="next">
        つぎへ
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
</style>

