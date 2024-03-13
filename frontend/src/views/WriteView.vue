<template>
    <div>
        <h2>게시물 작성하기</h2>
        <form>
            <table>
                <tr>
                    <label for="board_id">board_id: </label>
                    <input id="board_id" type="number" v-model="board_id" :readonly="true">
                </tr>
                <tr>
                    <label for="title">title: </label>
                    <input id="title" type="text" v-model="title" placeholder="제목을 입력하세요">
                </tr>
                <tr>
                    <label for="writer">writer: </label>
                    <input id="writer" type="text" v-model="writer" placeholder="작성자 이름">
                </tr>
                <tr>
                    <label for="content" style="vertical-align: top;">content: </label>
                    <textarea id="content" v-model="content" placeholder="본문을 입력하세요"></textarea>
                </tr>
            </table>
            <button @click="writeNotice">게시물 작성하기</button>
            <button @click="goHome">홈으로</button>
        </form>
    </div>
</template>

<script>
import apiBoard from "@/api/board";
// import router from "@/router";

export default {
    data() {
        return {
            board_id: null,
            title: null,
            writer: null,
            content: null,
        };
    },

    mounted() {
        apiBoard
            .getNotices()
            .then((response) => {
                this.board_id = response.data.data.length + 1;
            })
            .catch((e) => {
                console.log(e);
            })
    },

    methods: {
        goHome() {
            this.$router.push({path: '/main'});
        },
        writeNotice() {
            if (!this.title) {
                alert("제목을 작성해주세요.");
                return;
            } else if (!this.writer) {
                alert("작성자를 작성해주세요.");
                return;
            } else if (!this.content) {
                alert("본문을 작성해주세요.");
                return;
            }

            apiBoard
                .postNotice(this.board_id, this.title, this.writer, this.content)
                .then((response) => {
                    console.log(response.data.data)
                })
                .catch((e) => {
                    console.log(e);
                    alert("게시물 작성 중 에러가 발생하셨습니다.");
                });
            this.$router.push('/');
        },
    },
};
</script>

<style scoped>
    #content {
        width: 400px;
        height: 100px;
        border-color: #8d8d8d;
        resize: none;
    }

    table {
        box-shadow: 0px 0px 5px 0px;
        padding: 20px;
    }
    tr {
        border: 1px solid black;
    }
</style>
