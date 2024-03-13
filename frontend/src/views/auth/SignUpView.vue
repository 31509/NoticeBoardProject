<template>
    <div>
        <h2>회원가입</h2>
        <form>
            <table>
                <tr>
                    <th><label for="id">id: </label></th>
                    <td><input id="id" type="text" v-model="id" placeholder="아이디"></td>
                </tr>
                <tr>
                    <th><label for="password">password: </label></th>
                    <td><input id="password" type="password" v-model="password" placeholder="비밀번호"></td>
                </tr>
                <tr>
                    <th><label for="username">name: </label></th>
                    <td><input id="username" type="text" v-model="username" placeholder="이름"></td>
                </tr>
                <tr><td colspan="2"><button @click="goBack">회원가입</button></td></tr>
                <tr><td colspan="2"><button @click="Login">로그인</button></td></tr>
            </table>
        </form>
    </div>
</template>

<script>
import apiBoard from "@/api/board";
// import router from "@/router";

export default {
    data() {
        return {
            id: null,
            password: null,
            username: null,
        };
    },

    mounted() {
        apiBoard
            .getNotices()
            .then((response) => {
                this.id = response.data.data.length + 1;
            })
            .catch((e) => {
                console.log(e);
            })
    },

    methods: {
        Login() {
            this.$router.push("/");
        },
        writeNotice() {
            if (!this.id) {
                alert("아이디를 작성해주세요.");
                return;
            } else if (!this.password) {
                alert("비밀번호를 작성해주세요.");
                return;
            }

            apiBoard
                .postNotice(this.id, this.title, this.writer)
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
div {
    margin: 0 auto;
    width: 700px;
}
table, tr, th, td {
    border-collapse: collapse;
    border: 1px solid black;
    padding: 10px;
}
table {
    width: 0;
    text-align: center;
}
th {
    width: 300px;
    text-align: right;
}
td {
    width: 500px;
}
input {
    margin: 2px;
    width: 500px;
    height: 30px;
}
button {
    width: 100%;
    height: 40px;
    font-size: 17px;
}
</style>
