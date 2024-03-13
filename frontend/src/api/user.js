import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/";

export default {
    getUser: function(user_id) {
        return axios.get(BASE_URL + `notice/${user_id}`);
    },

    getUsers: function (page) {
        console.log(page);
        return axios.get(BASE_URL + "notice")
    },

    postUser: function (user_id, password, username) {
        return axios.post(BASE_URL + "insert", {
            user_id: user_id,
            password: password,
            username: username,
        });
    },

    updateUser: function (user_id, password, username) {
        return axios.put(BASE_URL + 'update', {
            user_id: user_id,
            password: password,
            username: username,
        });
    },

    deleteUser: function (user_id) {
        return axios.delete(BASE_URL + `delete/${user_id}`);
    },

    Login: function (user_id, password) {
        return axios.post(BASE_URL + "login", {
            user_id: user_id,
            password: password,
        });
    },
}