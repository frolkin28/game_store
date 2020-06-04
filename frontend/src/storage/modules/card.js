export default {
    actions: {
        orderGame(ctx, game) {
            let games = ctx.state.ordered_games;
            for (let item of games) {
                if (game.uuid === item.uuid){
                    return
                }
            }
            ctx.commit('updateOrderedGames', game);
        },

    },
    mutations: {
        updateOrderedGames(state, game) {
            state.ordered_games.push(game)
        }
    },
    state: {
        ordered_games: [],
    },
    getters: {
        getAmountGames(state) {
            return state.ordered_games.length
        },
        getOrderedGames(state) {
            return state.ordered_games
        }
    }
}