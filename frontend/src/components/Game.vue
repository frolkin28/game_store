<template>
    <div class="container game">
        <img src="static/images/witcher.jpeg" width="250" height="300">
        <div class="game-description">
            <div class="game-description-row">
                <div class="game-price">
                    <h5>${{ game.price }}</h5>
                </div>
                <div class="buy-button">
                    <button type="button" class="btn btn-success btn-sm">Buy</button>
                </div>
            </div>
            <div class="game-description-row">
                <div class="game-genre" v-for="genre of game.genres" :key="genre.title" >
                    <h5>{{ genre.title }}</h5>
                </div>
            </div>
            <div class="game-description-row">
                <div class="game-title">
                    <h5>{{ game.title }}</h5>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        game: {require: true}
    }
}
</script>

<style scoped>
.game {
    flex: 1;
    display: flex;
    width: 300px;
    flex-direction: column;
    align-items: center;
    margin: 10px 10px;
    padding-top: 20px;
    border: solid 1px #737e88;
    border-radius: 2%;
}

.game-description {
    display: flex;
    width: 100%;
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
    color: #ffffff;
}

.game-description-row:nth-of-type(1) {
    flex: 1;
    width: 100%;
    display: flex;
    padding-top: 10px;
}

.game-description-row:nth-of-type(2) {
    padding-top: 5px;
    flex: 1;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.game-description-row:nth-of-type(3) {
    flex: 1;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.game-price {
    display: flex;
    justify-content: center;
    flex: 1;
}

.buy-button {
    display: flex;
    justify-content: flex-end;
    flex: 2;
    padding-right: 20px;
}

.game-genre {
    flex: 1;
    display: flex;
    flex-direction: row;
}

.game-genre h5 {
    font-size: 14px;
    flex: 1;
    display: flex;
    justify-content: center;
}

.game-title {
    flex: 2;
    font-weight: bolder;
    align-self: center;
}

</style>