<script setup>
    import { data,myOrder } from '../pages/data.js';
    defineProps({
        name: String,
        price: Number,
        available_stock: Number
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
                    <p style="float: left;" class="m-2">{{ name }}</p>
                    <p style="float: right;" class="m-2">P{{ price }}</p>
                </td>
            </tr>
            <tr>
                <button class="btn-uic" style="float: right;" @click="myOrder.addFood(name,price,available_stock)">Add</button>
            </tr>
        </table>
    </div>
</template>

<style scoped>

</style>

