<template>
    <div class="container game">
        <img :src="`data:image/jpeg;base64,${image}`" width="250" height="300">
        <div class="game-description">
            <div class="game-description-row">
                <div class="game-price">
                    <h5>${{ game.price }}</h5>
                </div>
                <div class="buy-button">
                    <button type="button" class="btn btn-success btn-sm" @click="makeOrder">Buy</button>
                </div>
            </div>
            <div class="game-description-row">
                <div class="game-genre" v-for="genre of game.genres" :key="genre.title" >
                    <h5>{{ genre.title }}</h5>
                </div>
            </div>
            <div class="game-description-row">
                <div class="game-title">
                    <router-link :to="'/game/' + game.uuid">
                        <h5>{{ game.title }}</h5>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data() {
        return {
            image: null
        }
    },
    computed: {
        ...mapGetters(['getToken'])
    },
    props: {
        game: {require: true}
    },
    mounted() {
        this.fetchImage();
    },
    methods: {
        ...mapActions(['orderGame']),
        makeOrder(){
            if (this.getToken) {
                this.orderGame(this.game);
            }
        },
        fetchImage() {
            let url = this.game.game_photo.url;
            fetch(`http://127.0.0.1:5000/api/v1${url}`, {
                method: "GET"
            })
            .then(res => {
                return res.json();
            })
            .then(json_data => {
                this.image = json_data.image;
            });  
        }
    },
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

.game-title a {
    text-decoration: none;
    color: #ffffff;
}

</style>