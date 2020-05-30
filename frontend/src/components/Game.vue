<template>
    <div class="container game">
        <img src="static/images/witcher.jpeg" width="250" height="300">
        <div class="game-description">
            <div class="game-description-row">
                <div class="game-price">
                    <h5>$250.00</h5>
                </div>
                <button type="button" class="btn btn-success btn-sm buy-button">Buy</button>
            </div>
            <div class="game-description-row">
                <div class="game-genre">
                    <h5>RPG</h5>
                </div>
                <div class="game-title">
                    <h5>The Witcher3: Wild Hunt</h5>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {


}
</script>

<style scoped>
.game {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 10px 0px;
}

.game-description {
    display: flex;
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
    flex: 1;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.game-price {
    align-self: flex-start;
    flex: 2;
}

.buy-button {
    align-self: flex-end;
    flex: 1;
}

.game-genre {
    flex: 1;
}

.game-genre h5 {
    font-size: 14px;
}

.game-title {
    flex: 2;
    font-weight: bolder;
}

</style>