<script setup>
    import { myOrder } from '../pages/data.js';
    defineProps({ food: Object })
</script>

<template>
    <div class="m-2 d-inline-flex">
        <img src="../assets/food_placeholder.jpg" alt="" style="height: 75px;" class="round-border box-shadow">
        <div class="m-2 mt-0">
            <p style="font-weight: bold;">{{ food.food_name }}</p>
            <p>{{ food.quantity }}x</p>
            <p>P{{ food.price * food.quantity }}</p>
        </div>
        <div>
            <button class="btn-uic plus-minus" @click="myOrder.decFood(food.food_name)">-</button>
            <button class="btn-uic plus-minus" @click="myOrder.incFood(food.food_name)">+</button>
        </div>
        
    </div>
</template>

<style scoped>

    p {
        margin: 0;
    }

    .plus-minus {
        border-radius: 100%;
        width: 45px;
        height: 45px;
        font-weight: bold;
        margin: 3px;
    }

</style>