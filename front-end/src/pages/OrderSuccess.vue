<script setup>
    // import {data} from './data.js'
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }

</script>

<template>
    <Header title="Create Order" icon="pi-check-circle"></Header>
    <div class="container-fluid d-flex align-items-center justify-content-center text-center" style="height: 75vh;">
        <div class="order-container color-base p-3 round-border box-shadow text-white text-shadow">
            <h1>Order Successful</h1>
            <p>Your Order Number is...</p>
            <p style="font-size: 100px; font-weight: bold;">{{ data.orderNum }}</p>
            <input type="button" value="New Order" class="btn-uic m-2" @click="switchTo('/createOrder')">
            <input type="button" value="Logout" class="btn-uic m-2" @click="switchTo('/')">
        </div>
    </div>
</template>

<style scoped>

    .order-container {
        width: 50%;
        height: 75%;
    }

</style>
