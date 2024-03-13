<template>
    <div>
        <table>
            <tr v-for="(items, i) in notices" :key="i" @click="rowClicked(items.board_id)">
                <td>{{items.board_id}}</td>
                <td>{{items.title}}</td>
                <td>{{items.writer}}</td>
            </tr>
        </table>
        <a href="/board/write" class="write_btn">
            <img src="/images/pen_icon.png" />
        </a>
    </div>
</template>

<script>
import apiBoard from "@/api/board";

export default {
    data() {
        return {
            notices: null,
        };
    },
    mounted() {
        apiBoard
            .getNotices(0)
            .then((response) => {
                console.log("getNotices", response.data.data[0].title);
                this.notices = response.data.data;
            })
            .catch((e) => {
                console.log(e);
            });
    },
    methods: {
        rowClicked(row) {
            console.log(row);
            this.$router.push({
                path: `/board/detail/${row}`,
            });
        },
    },
};
</script>

<style scoped>
.write_btn {
    position: fixed;
    bottom: 40px;
    right: 40px;
    width: 48px;
    height: 48px;
    border-radius: 50px;
    background: #fc1f49;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
    z-index: 10;
    display: inline-block;
}
.write_btn img {
    position: relative;
    top: 50%;
    left: 25%;
    transform: translate(-50%, -55%);
}
table {
    border-collapse: collapse;
}
tr {
    border-bottom: 1px solid #a6a6a6;
}
td {
    padding-top: 10px;
}
tr:hover {
    cursor: pointer;
    border: solid 1px black;
    box-sizing: border-box;
}
</style>
