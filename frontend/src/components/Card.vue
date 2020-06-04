<template>
    <div class="container main-area">
        <div class="game" v-for="game of getOrderedGames" :key="game.uuid">
            <div class="game-title">{{ game.title }}</div>
            <div class="game-price">${{ game.price }}</div>
        </div> 
        <div class="confirm-button">
            <button type="button" class="btn btn-primary btn-lg">Confirm</button>
        </div>
    </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  
  computed: {
    ...mapGetters(['getOrderedGames', 'getAmountGames'])
  },
};
</script>

<style scoped>
.main-area {
  background-color: #2c2c2c;
  padding: 20px 30px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: center;
  color: #ffffff;
  border-radius: 1%;
}

.game {
    flex: 1;
    align-self: center;
    width: 50%;
    display: flex;
    flex-direction: row;
    border: solid 2px #737e88;
    border-radius: 2%;
    padding: 20px;
    margin: 10px;
}

.game-title {
    flex: 1;
    display: flex;
    justify-content: flex-start;
    font-weight: bolder;
}

.game-price {
    flex: 1;
    display: flex;
    justify-content: flex-end;
}

.confirm-button {
    flex: 1;
    display: flex;
    align-self: center;
    width: 20%;
}

</style>