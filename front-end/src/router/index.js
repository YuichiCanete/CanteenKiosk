import { createRouter, createWebHistory } from "vue-router";

import Login from "../pages/Login.vue"
import PageB from "../pages/PageB.vue"
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
addRoute("/pageB","Page B",PageB)
addRoute("/pageC","Page C",PageC)

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
