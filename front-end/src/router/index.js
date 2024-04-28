import { createRouter, createWebHistory } from "vue-router";

import Admin from "../pages/Admin.vue"
import Login from "../pages/Login.vue"
import CreateOrder from "../pages/CreateOrder.vue"
import OrderSuccess from "../pages/OrderSuccess.vue"
import Counter from "../pages/Counter.vue"
import EditMenu from "../pages/EditMenu.vue"
import ViewOrders from "../pages/ViewOrders.vue"


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
addRoute("/counter","Counter",Counter) //Low priority
addRoute("/editMenu","Edit Menu",EditMenu) 
addRoute("/viewOrders","View Orders",ViewOrders)
addRoute("/admin","Admin",Admin)

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
