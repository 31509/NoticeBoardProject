<template>
    <div>
        <table>
            <tr>
                <td>{{ title }}</td>
            </tr>
            <tr>
                <td>{{ writer }}</td>
            </tr>
            <tr>
                <td id="content">{{ content }}</td>
            </tr>
        </table>
        <button @click="goBack">Back</button>
        <button @click="editNotice">수정</button>
        <button @click="delNotice">삭제</button>

<!--        <el-row>-->
<!--            <el-col :span="2"></el-col>-->
<!--            <el-col :span="20">-->
<!--                <el-container>-->
<!--                    <el-header>{{ notice.title }}</el-header>-->
<!--                    <el-main>{{ notice.body }}</el-main>-->
<!--                </el-container>-->
<!--            </el-col>-->
<!--            <el-col :span="2"></el-col>-->
<!--        </el-row>-->

<!--        <br />-->
<!--        <el-button type="success" @click="goBack">Back</el-button>-->
<!--        <el-button type="success" @click="editNotice">수정</el-button>-->
    </div>
</template>

<script>
import apiBoard from "@/api/board";
// import axios from 'axios';
// import router from "@/router";

export default {
    data() {
        return {
            title: null,
            content: null,
            writer: null,
        };
    },

    mounted() {
        apiBoard
            .getNotice(this.$route.params.id)
            .then((response) => {
                console.log(response.data.data[0].board_id)
                this.title = response.data.data[0].title;
                this.content = response.data.data[0].content;
                this.writer = response.data.data[0].writer;
            })
            .catch((e) => {
                console.log(e);
            });
    },

    methods: {
        goBack() {
            this.$router.push("/main");
        },
        editNotice() {
            this.$router.push({ path: `/board/update/${this.$route.params.id}` });
        },
        delNotice() {
            apiBoard
                .deleteNotice(this.$route.params.id)
                .then(() => {
                    this.$router.push({path: "/"});
                })
                .catch((e) => {
                    console.log(e)
                });
        }
    },

    created() {

    },
};
</script>

<style scoped>
.el-header {
    background-color: #b3c0d1;
    color: #333;
    text-align: left;
    line-height: 60px;
}
#content {
    background-color: #e9eef3;
    color: #333;
    text-align: left;
    width: 100%;
    height: 100%;
    word-break: break-all;
}
</style>
