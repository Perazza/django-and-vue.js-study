<template>
  <div class="hello">
    <h1>Hello World</h1>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    // prop é usado como atributo no template
    // Aqui foi definido o tipo de valor que o prop recebe. No caso, a mensagem é string
    props: {
      msg: String
    }
  }
</script>

<style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
