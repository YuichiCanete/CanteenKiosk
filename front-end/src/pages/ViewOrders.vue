<script setup>
    import {data} from './data.js'
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }  
</script>

<template>
    <Header title="View Orders"></Header>

    <div class="m-3">
        <div class="order-table color-base p-2 m-2 box-shadow round-border">
            <table class="w-100">
                <tr class="text-white text-shadow under-line">
                    <th>ID</th>
                    <th>Order</th>
                    <th>Payment Type</th>
                    <th>Total</th>
                    <th>Date</th>
                </tr>
                <tr v-for="order in data.orderList" class="under-line">
                    <td>{{ order.orderNum }}</td>
                    <td><p v-for="food in order.foodList">{{ food.name }} x{{ food.quantity }}</p></td>
                    <td>{{ order.payType }}</td>
                    <td>{{ data.getTotal(order.foodList) }}</td>
                    <td>{{ order.date }}</td>
                </tr>
            </table>
        </div>

        <input type="button" value="Edit Menu" class="btn-uic m-2" @click="switchTo('/editMenu')">
        <input type="button" value="Print" class="btn-uic m-2">

    </div>

    
    

</template>

<style scoped>

    .order-table{
        width: 90%;
        height: 60vh;
        overflow: auto;
    }

    td ,tr {
        vertical-align: baseline;
    }

    .under-line {
        border-bottom: 1px solid white;
    }

</style>