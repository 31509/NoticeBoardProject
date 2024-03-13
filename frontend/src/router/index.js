import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Detail from '../views/DetailView.vue'
import Write from '../views/WriteView.vue'
import Update from '../views/UpdateView.vue'
import LoginView from "../views/auth/LoginView.vue";
import SignUpView from "../views/auth/SignUpView.vue";

const routes = [
  {
    path: '/main',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/board/detail/:id',
    name: 'Detail',
    component: Detail
  },
  {
    path: "/board/write/:id?",
    name: "Write",
    component: Write
  },
  {
    path: "/board/update/:id?",
    name: "Update",
    component: Update
  },
  {
      path: '/',
      name: 'Login',
      component: LoginView
  },
  {
      path: '/signup',
      name: 'Signup',
      component: SignUpView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router