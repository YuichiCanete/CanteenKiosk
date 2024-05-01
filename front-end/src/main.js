import { createApp } from 'vue'

import App from './App.vue'

import 'primeicons/primeicons.css'
import './style.css'
import 'primevue/resources/themes/aura-light-pink/theme.css'

import PrimeVue from "primevue/config";
import Menubar from "primevue/menubar";
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import FloatLabel from 'primevue/floatlabel'
import Button from 'primevue/button';
import Message from 'primevue/message';
import Card from 'primevue/card'
import Divider from 'primevue/divider'

import router from "./router";

import Header from "./components/Header.vue"


import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';

import ConfirmDialog from 'primevue/confirmdialog';
import Toast from 'primevue/toast';

createApp(App)
    .use(router)
    .use(ConfirmationService)
    .use(ToastService)
    .use(PrimeVue, { ripple: true })
    .component("ConfirmDialog",ConfirmDialog)
    .component("Toast",Toast)
    .component("Menubar", Menubar)
    .component("InputText", InputText)
    .component("DataTable",DataTable)
    .component("Column",Column)
    .component("FloatLabel",FloatLabel)
    .component("Button",Button)
    .component("Card",Card)
    .component("Diveder",Divider)
    .component("Message",Message)
    .component("Header", Header)
    .mount('#app')

