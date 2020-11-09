<template>
  <div id="">

    <table class="table">
      <thead>
        <th>Titulo</th>
        <th>Plataformas</th>
      </thead>
      <tbody>
        <tr v-for="game in lista" :key = "game">
          <td>{{ game.titulo }}</td>
          <td>{{ game.plataformas }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
export default {

  data() {
    return {
      lista: []
    }
  },
  mounted() {
    this.$http.get("/homepage/api/games").then( (req) => this.lista = req.data )
  },
}
</script>

<style>

</style>
