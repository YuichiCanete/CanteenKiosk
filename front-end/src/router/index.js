import { createRouter, createWebHistory } from "vue-router";

import Login from "../pages/Login.vue"
import CreateOrder from "../pages/CreateOrder.vue"
import OrderSuccess from "../pages/OrderSuccess.vue"

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
addRoute("/orderSuccess","Order Success",OrderSuccess)

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
