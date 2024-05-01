<script setup>
    import { onBeforeMount, ref } from 'vue';
    import {apiFunc} from './data.js'
    let foodList = ref([])
    async function updateFood(){
        let requestFood = await apiFunc.value.get('http://127.0.0.1:8000/api/food_details')
        if (requestFood.isSuccess){
            foodList.value = requestFood.data
        }
    }
    onBeforeMount(updateFood)

    async function addFood(){
        const [food_id, food_name, food_price, food_stock] =
            ['food_id', 'food_name', 'food_price', 'food_stock']
            .map(i => document.getElementById(i).value);
        
        await apiFunc.value.add('http://127.0.0.1:8000/api/food_details/',{
            food_detail_id:food_id,
            name: food_name,
            price: food_price,
            available_stock: food_stock
        })

        updateFood()
    }

</script>

<template>
    <Header title="Edit Menu"icon='pi-cart-arrow-down'></Header>

    <div class="m-3">
        <div class="menu-table color-base p-2 m-2 box-shadow round-border">
            <table class="w-100">
                <tr class="text-white text-shadow under-line">
                    <th>Name</th>
                    <th>Price</th>
                    <th>Available Stock</th>
                    <th>Actions</th>
                </tr>
                <tr v-for="(food, index) in foodList" class="under-line" :key="index">
                    <td><input type="text" :value=food.name class="w-75"></td>
                    <td><input type="number" :value=food.price class="w-50"></td>
                    <td><input type="number" :value=food.available_stock class="w-50"></td>
                    <td>
                        <button class="btn-uic m-2">Edit</button>
                    </td>
                </tr>
            </table>

        </div>

    </div>

    <h2 class="text-white text-shadow">Add Food</h2>
    <div class="d-flex flex-column w-25">
        <input type="text" placeholder="Food ID" class="inp-uic" id="food_id">
        <input type="text" placeholder="Food Name" class="inp-uic" id="food_name">
        <input type="text" placeholder="Food Price" class="inp-uic" id="food_price">
        <input type="text" placeholder="Food Stocks" class="inp-uic" id="food_stock">
        <button class="btn-uic" @click="addFood()">Submit</button>
    </div>

</template>

<style scoped>


    .menu-table{
        margin: 0 auto;
        width: min(750px,80%);
        height: 60vh;
        overflow: auto;
    }

    .under-line {
        border-bottom: 1px solid white;
    }

    .inp-uic, .btn-uic {
        margin: 5px;
    }

</style>