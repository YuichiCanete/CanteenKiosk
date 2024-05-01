<script setup>
    import FoodCard from '../components/FoodCard.vue'
    import FoodInList from '../components/FoodInList.vue';
    import {apiFunc,myOrder} from './data.js'
    import {useRouter} from 'vue-router'
    import { onBeforeMount, ref } from 'vue';
    
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }

    function addOrder(){
        data.value.addOrder()
        switchTo('/orderSuccess')
    }

    let isloaded = ref(false)
    let foodList = ref([])
    async function getFood() {
        let getF = await apiFunc.value.get('http://127.0.0.1:8000/api/food_details')
        foodList.value = getF.data
        if (getF.isSuccess){
            isloaded.value = true
        }
    }
    onBeforeMount(getFood)

    let myOrdaer = ref()

    

    


</script>

<template>

    <Header title="Create Order" icon="pi-shopping-cart"></Header>
    <div class="parent">
        <div class="food-list p-2">
            <h2 class="text-white text-shadow">Menu Items</h2>
            <div class="food-grid" v-if="isloaded">
                <div v-for="food in foodList">
                    <FoodCard :name="food.name" :price="food.price" :available_stock="food.available_stock" v-if="food.available_stock > 0"/>
                </div>    
            </div>
        </div>
        <div class="my-order p-2">
            <h2 class="text-shadow text-white">My Order</h2>
            <div class="my-order-list" style="overflow-y: auto; overflow-x: hidden;">
                <!-- <div v-for="food in myOrder.foodList">
                    <FoodInList :food="food" v-if="food.quantity"/>
                </div> -->
            </div>
            <div class="my-payment text-center">
                <!-- <h4>Payment</h4>
                <p>Total Payment: {{ data.getTotal(data.foodList) }}</p>
                <input type="button" value="Cash" class="m-2 btn-uic" @click="addOrder()">
                <input type="button" value="Tally" class="btn-uic" @click="addOrder()"> -->
            </div>
        </div>
    </div>
    
</template>

<style scoped>

    .my-order-list {
        height: 40vh;
    }

    .my-payment {
        height: 25vh;
    }

    .parent {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        grid-template-rows: repeat(5, 1fr);
        grid-column-gap: 0px;
        grid-row-gap: 0px;
    }

    .food-list { grid-area: 1 / 1 / 6 / 4; }
    .my-order { grid-area: 1 / 4 / 6 / 6; }

    .food-grid {
        display: flex;
        flex-wrap: wrap; 
        height: 67.3vh;
        overflow-y: auto;
        gap: 20px;
    }

</style>

