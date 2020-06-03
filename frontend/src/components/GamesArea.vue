<template>
  <div class="container main-area">
    <div class="container main-area">
        <Game 
          v-for="game of getGames" :key="game.uuid" 
          v-bind:game="game"/>
    </div>
  </div>
</template>

<script>
import Game from "@/components/Game";
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(['getGames'])
  },
  mounted() {
    this.fetchGames();
  },
  methods: {
    ...mapActions(['fetchGames'])
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