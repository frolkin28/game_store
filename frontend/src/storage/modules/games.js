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
        },
        fetchGame(ctx, uuid) {
            fetch(`http://127.0.0.1:5000/api/v1/game/${uuid}`, {
                method: "GET"
            })
                .then(res => {
                    return res.json();
                })
                .then(json_data => {
                    ctx.commit('updateGame', json_data);
                });
        },

    },
    mutations: {
        updateGames(state, games) {
            state.games = games;
        },
        updateGame(state, game) {
            state.game = game;
        }
    },
    state: {
        games: [],
        game: null
    },
    getters: {
        getGames(state) {
            return state.games
        },
        getGame(state) {
            return state.game
        }
    }
}