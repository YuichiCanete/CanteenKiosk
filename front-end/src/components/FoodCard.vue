<script setup>
    import { data } from '../pages/data.js';
    defineProps({
        food: Object
    })
</script>

<template>
    <div class="color-base p-3 text-center text-light box-shadow round-border" style="width: 225px;">
        <table>
            <tr>
                <td><img src="../assets/food_placeholder.jpg" style="width: 90%;" class="round-border"></td>
            </tr>
            <tr>
                <td>
                    <p style="float: left;" class="m-2">{{ food.name }}</p>
                    <p style="float: right;" class="m-2">P{{ food.price }}</p>
                </td>
            </tr>
            <tr>
                <button class="btn-uic" style="float: right;" @click="data.addFoodToOrder(food.name)">Add</button>
            </tr>
        </table>
    </div>
</template>

<style scoped>

</style>

