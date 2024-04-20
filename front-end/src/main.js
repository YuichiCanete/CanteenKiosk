import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import PrimeVue from "primevue/config";
import Menubar from "primevue/menubar";
import router from "./router";

import Header from "./components/Header.vue"

import Button from "primevue/button"


createApp(App)
    .use(router)
    .use(PrimeVue, { ripple: true })
    .component("Menubar", Menubar)
    .component("Header", Header)
    .mount('#app')

