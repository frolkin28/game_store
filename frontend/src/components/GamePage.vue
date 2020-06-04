<template>
    <div class="main-area container">
        <div class="image">
        </div>
        <div class="title-section">
            <div class="title-price">
                <h4>{{ getGame.title }}</h4>
                <h5>${{ getGame.price }}</h5>
            </div>
            <div class="buy-button" @click="makeOrder">
                <button type="button" class="btn btn-success">Buy</button>
            </div>
        </div>
        <div class="line">
            <hr>
        </div>
        
        <div class="genres-section">
            <div class="genre" v-for="genre of getGame.genres" :key="genre.title">
                <h5>{{ genre.title }}</h5>
            </div>
        </div>
        <div class="discription-section">
            <h5>Description</h5>
            <p>{{ getGame.details }}</p>
        </div>
        <div class="comments-section"></div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
    mounted() {
        let uuid = this.$route.params.uuid;
        this.fetchGame(uuid);
    },
    computed: {
        ...mapGetters(['getGame', 'getToken'])
    },
    methods: {
        ...mapActions(['fetchGame']),
        ...mapActions(['orderGame']),
        makeOrder(){
            if (this.getToken) {
                this.orderGame(this.getGame);
            }
        },
    }
}
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
.image {
    width: 100%;
    margin-bottom: 30px;
}
.title-section {
    flex: 1;
    display: flex;
    flex-direction: row;
}
.title-price {
    flex: 1;
}
.buy-button {
    flex: 1;
    display: flex;
    justify-content: flex-end;
}
.buy-button button {
    height: 50%;
    width: 30%;
}
.title-price h4{
    font-weight: bolder;
}
 hr {
    border: none; /* Убираем границу для браузера Firefox */
    color: #ffffff; /* Цвет линии для остальных браузеров */
    background-color:#ffffff; /* Цвет линии для браузера Firefox и Opera */
    height: 1px
}
.genres-section {
    flex: 1;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
}
.genre {
    flex: 1;
    justify-content: flex-start;
}
.genre h5{
    font-style: italic;
    font-size: 14px;
}
.discription-section {
    padding-top: 50px;
    flex: 1;
}
</style>