export default {
    actions: {
        fetchGames(ctx) {
            fetch("http://127.0.0.1:5000/api/v1/games", {
                method: "GET"
            })
            .then(res => {
                return res.json();
            })
            .then(json_data => {
                ctx.commit('updateGames', json_data);
            });  
        }
    },
    mutations: {
        updateGames(state, games) {
            state.games = games;
        }
    },
    state: {
        games: []
    },
    getters: {
        getGames(state) {
            return state.games
        },
        getGameByUuid(state, uuid) {
            return state.games.filter(game => game.uuid === uuid)
        }
    }
}