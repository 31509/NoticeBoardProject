<template>
    <div>
        <h2>로그인</h2>

            <table>
                <tr><td><input id="user_id" type="text" v-model="user_id" placeholder="아이디"></td></tr>
                <tr><td><input id="password" type="password" v-model="password" placeholder="비밀번호"></td></tr>
                <tr><button id="loginBtn" @click="Login">로그인</button></tr>
                <tr><button id="signupBtn" @click="Signup">회원가입</button></tr>
            </table>

    </div>
</template>

<script>
import apiBoard from "@/api/user";
// import router from "@/router";

export default {
    data() {
        return {
            user_id: null,
            password: null,
        };
    },

    mounted() {

    },

    methods: {
        Signup() {
            this.$router.push("/signup");
        },
        Login() {
            if (!this.user_id) {
                alert("아이디를 작성해주세요.");
                return;
            } else if (!this.password) {
                alert("비밀번호를 작성해주세요.");
                return;
            }

            apiBoard
                .Login(this.user_id, this.password)
                .then((response) => {
                    console.log(response)
                })
                .catch((e) => {
                    console.log(e);
                    alert("로그인 오류 발생");
                });
                // this.$router.push({path: '/main'});
        },
    },
};
</script>

<style scoped>
table {
    width: 0;
    text-align: center;
    border: 1px solid #989898;
    padding: 80px;
}
input {
    width: 500px;
    height: 40px;
    font-size: 15px;
    margin: 5px;
}
button {
    margin: 10px;
}
#loginBtn {
    width: 500px;
    height: 50px;
    font-size: 17px;
    background: #5cd0ff;
    border: none;
    color: white;
}
#signupBtn {
    border: none;
    background: none;
    color: deepskyblue;
    font-size: 13px;
    left: 0;
}
tr:last-child {
    text-align: left;
}
</style>
