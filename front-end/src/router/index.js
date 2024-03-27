import { createRouter, createWebHistory } from "vue-router";

import Login from "../pages/Login.vue"
import CreateOrder from "../pages/CreateOrder.vue"
import PageC from "../pages/PageC.vue"

const routes = []

function addRoute(path,name,component){
    routes.push({
        path:path,
        name:name,
        component:component
    })
}

addRoute("/","Login",Login)
addRoute("/createOrder","Create Order",CreateOrder)
addRoute("/pageC","Page C",PageC)

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
