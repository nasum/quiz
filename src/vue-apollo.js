import Vue from "vue";
import VueApollo from "vue-apollo";
import {
  createApolloClient
} from "vue-cli-plugin-apollo/graphql-client";

Vue.use(VueApollo);

const AUTH_TOKEN = "apollo-token";

const httpEndpoint =
  process.env.VUE_APP_GRAPHQL_HTTP || "http://localhost:8000/graphql/";

export const filesRoot =
  process.env.VUE_APP_FILES_ROOT ||
  httpEndpoint.substr(0, httpEndpoint.indexOf("/graphql"));

Vue.prototype.$filesRoot = filesRoot;
console.log(document.querySelector('input[name=csrfmiddlewaretoken]'))
const defaultOptions = {
  httpEndpoint,
  tokenName: AUTH_TOKEN,
  persisting: false,
  ssr: false,
  httpLinkOptions: {
    headers: {
      'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').getAttribute('value'),
    }
  }
};

export function createProvider(options = {}) {
  const { apolloClient } = createApolloClient({
    ...defaultOptions,
    ...options,
  });

  console.log(apolloClient)

  const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
    defaultOptions: {
      $query: {
      }
    },
    errorHandler(error) {
      console.log(
        "%cError",
        "background: red; color: white; padding: 2px 4px; border-radius: 3px; font-weight: bold;",
        error.message
      );
    }
  });

  return apolloProvider;
}
