<template>
    <div>
        <h2>게시물 수정하기</h2>
        <form>
            <table>
                <tr>
                    <label for="board_id">board_id: </label>
                    <input id="board_id" type="text" v-model="board_id" :readonly="true">
                </tr>
                <tr>
                    <label for="title">title: </label>
                    <input id="title" type="text" v-model="title" placeholder="글 제목">
                </tr>
                <tr>
                    <label for="writer">writer: </label>
                    <input id="writer" type="text" v-model="writer" placeholder="작성자 이름">
                </tr>
                <tr>
                    <label for="content" style="vertical-align: top;">content: </label>
                    <textarea id="content" style="width: 400px; height: 100px;" v-model="content" placeholder="글 내용"></textarea>
                </tr>
            </table>
            <button @click="updateNotice()">게시물 수정하기</button>
            <button @click="goBack">Back</button>
        </form>
    </div>
</template>

<script>
import apiBoard from "@/api/board";

export default {
    data() {
        return {
            board_id: null,
            title: null,
            writer: null,
            content: null,
        };
    },

    computed: {

    },

    mounted() {
        if (this.$route.params.id) {
            apiBoard
                .getNotice(this.$route.params.id)
                .then((response) => {
                    this.board_id = response.data.data[0].board_id;
                    this.title = response.data.data[0].title;
                    this.writer = response.data.data[0].writer;
                    this.content = response.data.data[0].content;
                })
                .catch((e) => {
                    console.log(e);
                })
        }
    },

    methods: {
        goBack() {
            this.$router.push({path: `/board/detail/${this.$route.params.id}`})
        },
        updateNotice() {
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

            if (this.$route.params.id) {
                apiBoard
                    .updateNotice(this.$route.params.id, this.title, this.writer, this.content)
                    .then(() => {

                    })
                    .catch((e) => {
                        console.log(e);
                    });
                this.$router.push({path: `/board/detail/${this.$route.params.id}`});
            }
        },
    },
};
</script>

<style scoped>

</style>
