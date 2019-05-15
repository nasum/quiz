<template>
  <div>
    <ul>
      <li v-for="term in terms" :key="term.id">
        <router-link :to="`${term.id}`">
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

<style lang="scss" scoped>
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