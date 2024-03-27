<script setup>
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }

</script>

<template>
    <Header title="Create Order"></Header>
    <div class="container-fluid d-flex align-items-center justify-content-center text-center" style="height: 75vh;">
        <div class="order-container color-base p-3">
            <h1>Order Successful</h1>
            <p>Your Order Number is...</p>
            <p style="font-size: 100px; font-weight: bold;">##</p>
            <input type="button" value="New Order" class="p-2" @click="switchTo('/createOrder')">
            <input type="button" value="Logout" class="p-2" @click="switchTo('/')">
        </div>
    </div>
</template>

<style scoped>

    .order-container {
        width: 50%;
        height: 75%;
    }

</style>
