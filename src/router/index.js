import { createRouter, createWebHistory } from "vue-router";


import Login from '../components/Login.vue'
import Order from '../components/Order.vue'
import Payment from '../components/Payment.vue'
import GetOrder from '../components/GetOrder.vue'
import ViewOrder from '../components/ViewOrder.vue'
import Finance from '../components/Finance.vue'

const routes = [
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/order",
      name: "Order",
      component: Order,
    },
    {
      path: "/payment",
      name: "Payment",
      component: Payment,
    },
    {
      path: "/getorder",
      name: "GetOrder",
      component: GetOrder,
    },
    {
      path: "/vieworder",
      name: "ViewOrder",
      component: ViewOrder,
    },
    {
      path: "/finance",
      name: "Finance",
      component: Finance,
    },
  ];

  const router = createRouter({
    history: createWebHistory(),
    routes,
  });

  export default router;