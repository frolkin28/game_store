<template>
  <div class="container main-area">
    <div class="container main-area">
      <Game 
        v-for="game of games" :key="game.uuid" 
        v-bind:game="game"/>
    </div>
  </div>
</template>

<script>
import Game from "@/components/Game";

export default {
  data() {
    return {
      user: localStorage.getItem("user"),
      token: localStorage.getItem("token"),
      games: []
    };
  },
  mounted() {
    this.get_games();
  },
  methods: {
    get_games() {
      fetch("http://127.0.0.1:5000/api/v1/games", {
        method: "GET"
      })
        .then(res => res.json())
        .then(json_data => {
          this.games = json_data;
        });
    }
  },
  components: {
    Game
  }
};
</script>

<style scoped>
.main-area {
  background-color: #2c2c2c;
  padding: 20px 30px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  border-radius: 1%;
}
</style>