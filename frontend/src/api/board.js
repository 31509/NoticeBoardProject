import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/";

export default {
    getNotice: function(id) {
        return axios.get(BASE_URL + `notice/${id}`);
    },

    getNotices: function (page) {
        console.log(page);
        return axios.get(BASE_URL + "notices")
    },

    postNotice: function (board_id, title, writer, content) {
        return axios.post(BASE_URL + "notice", {
            board_id: board_id,
            title: title,
            writer: writer,
            content: content,
        });
    },

    updateNotice: function (board_id, title, writer, content) {
        return axios.put(BASE_URL + 'notice', {
            board_id: board_id,
            title: title,
            writer: writer,
            content: content,
        });
    },

    deleteNotice: function (id) {
        return axios.delete(BASE_URL + `notice/${id}`);
    },
}