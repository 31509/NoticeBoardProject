<template>
<!--    <header>-->
<!--        <div id="logo" @click="gohome"></div>-->
<!--        <button class="userbtn" @click="login">로그인</button>-->
<!--        <button class="userbtn" @click="signup">회원가입</button>-->
<!--    </header>-->
    <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
</template>

<script>
export default {
    name: 'App',
    methods: {
        gohome() {
            this.$router.push({path: '/'});
        },
        login() {
            this.$router.push({path: '/login'});
        },
        signup() {
            this.$router.push({path: '/signup'});
        }
    },
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    max-width: 1280px;
    margin: 20px auto;
}

header #logo {
    position: fixed;
    padding: 0 20px;
    height: 40px;
    width: 110px;
    left: 5%;
    background-image: url("../public/images/logo.png");
    background-size: 50px;
}
header #logo:hover {
    cursor: pointer;
}

header .userbtn {
    position: fixed;
    right: 6%;
}

header .userbtn:last-child {
    right: 1%;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

table {
    margin: 0 auto;
    width: 100%;
    text-align: left;
}

h2 {
    padding-bottom: 30px;
}

button {
    cursor: pointer;
}
</style>
