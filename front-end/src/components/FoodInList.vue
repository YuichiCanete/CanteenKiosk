<script setup>
    import { data } from '../pages/data.js';
    defineProps({ food: Object })
</script>

<template>
    <div class="m-2 d-inline-flex">
        <img src="../assets/food_placeholder.jpg" alt="" style="height: 75px;" class="round-border box-shadow">
        <div class="m-2 mt-0">
            <p style="font-weight: bold;">{{ food.name }}</p>
            <p>{{ food.quantity }}</p>
            <p>P{{ food.price * food.quantity }}</p>
        </div>
    </div>
</template>

<style scoped>

    p {
        margin: 0;
    }

</style>