<script setup>
    import FoodCard from '../components/FoodCard.vue'
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }

    function addOrder(){
        switchTo('/orderSuccess')
    }

</script>

<template>

    <Header title="Create Order"></Header>
    
    <div class="parent">
        <div class="food-list p-2">
            <h2 class="text-white text-shadow">Menu Items</h2>

            <div class="food-grid justify-content-between p-3">
                <div v-for="i in 20">
                    <FoodCard/>
                </div>    
            </div>

        </div>
        <div class="my-order p-2">
            <h2 class="text-shadow text-white">My Order</h2>
            <div class="my-order-list">

            </div>
            <div class="my-payment text-center">
                <h4>Payment</h4>
                <p>Total Payment: 99999</p>
                <input type="button" value="Cash" class="p-2 m-2" @click="addOrder()">
                <input type="button" value="Tally" class="p-2" @click="addOrder()">
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
        overflow-y: scroll;
        gap: 20px;
    }

</style>

