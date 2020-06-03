export default {
    actions: {
        fetchLogin(ctx) {
            var email = ctx.getters.getEmail;
            var password = ctx.getters.getPassword;
            let data;
            if (email.length > 0 && password.length > 0) {
                let xhr = new XMLHttpRequest();
                xhr.open("GET", "http://127.0.0.1:5000/login", false);
                xhr.setRequestHeader("Authorization", "Basic " + btoa(`${email}:${password}`));
                xhr.send()
                if (xhr.status < 299) {  
                    ctx.commit('updateRetry', false);
                    data = JSON.parse(xhr.response);
                    ctx.commit('updateEmail', '');
                    ctx.commit('updatePassword', '');
                    let user = JSON.stringify(data.user);
                    localStorage.setItem("user", user);
                    localStorage.setItem("token", data.token);
                    ctx.commit('updateUser', user);
                    ctx.commit('updateToken', data.token);
                }
                else {
                    ctx.commit('updateRetry', true);
                    data = null;
                }
            }
        }
    },
    mutations: {
        updateUser(state, user) {
            state.user = user;
        },
        updateToken(state, token) {
            state.token = token;
        },
        updateRetry(state, value) {
            state.retry = value;
        },
        updateEmail(state, email) {
            state.email = email;
        },
        updatePassword(state, password) {
            state.password = password;
        }
    },
    state: {
        email: "",
        password: "",
        user: localStorage.getItem('user'),
        token: localStorage.getItem('token'),
        retry: false
    },
    getters: {
        getUser(state) {
            return JSON.parse(state.user);
        },
        getToken(state) {
            return state.token;
        },
        getRetry(state) {
            return state.retry;
        },
        getEmail(state) {
            return state.email;
        },
        getPassword(state) {
            return state.password;
        }
    }
}