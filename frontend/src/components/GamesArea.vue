<template>
  <div class="container main-area">
    <div class="container main-area">
      <Game />
    </div>
  </div>
</template>

<script>
import Game from "@/components/Game";

export default {
  data() {
    return {};
  },
  mounted() {
    this.get_games();
  },
  methods: {
    get_games() {
      fetch('http://127.0.0.1:5000/api/v1/games', {
        method: "GET"
      })
        .then(function(res) {
          return res.json();
        })
        .then(function(data) {
            console.log(data);
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
}
</style>