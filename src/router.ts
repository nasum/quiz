import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Terms from "./views/Terms.vue"
import TermsIndex from "./views/terms/Index.vue"
import TermsShow from "./views/terms/Show.vue"
import Quiz from "./views/Quiz.vue"
import QuizIndex from "./views/quiz/Index.vue"
import QuizShow from "./views/quiz/Show.vue"

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/terms",
      name: "terms",
      component: Terms,
      children: [
        {
          path: "",
          name: "index",
          component: TermsIndex
        },
        {
          path: ":id",
          name: 'show',
          component: TermsShow
        }
      ]
    },
    {
      path: "/quiz",
      name: "quiz",
      component: Quiz,
      children: [
        {
          path: "/",
          name: "QuizIndex",
          component: QuizIndex
        },
        {
          path: ":id",
          name: "QuizShow",
          component: QuizShow
        }
      ]
    }
  ]
});
