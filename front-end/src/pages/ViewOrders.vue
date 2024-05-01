<script setup>
    import { onBeforeMount, ref } from 'vue';
    import {apiFunc} from './data.js'
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }  

    let isLoaded = ref(false);
    let orderList = ref([]);

    async function getOrders() {
        let orderRequest = await apiFunc.value.get('http://127.0.0.1:8000/api/view_order');
        let userOrderRequest = await apiFunc.value.get('http://127.0.0.1:8000/api/user_order')

        if (orderRequest.isSuccess && userOrderRequest.isSuccess) {
            let orderDetail = userOrderRequest.data
            let orders = orderRequest.data;
            let groupOrder = {};
            orders.forEach(o => {
                if (!groupOrder[o.order_id]) {
                    let od = orderDetail.find((e) => e.user_order_id === o.order_id)
                    groupOrder[o.order_id] = {
                        orderNum: o.order_id,
                        foodList: [],
                        total: 0,
                        paytype: od.payment_type,
                        date: od.order_date
                    };
                    orderList.value.push(groupOrder[o.order_id]);
                }
                groupOrder[o.order_id].foodList.push({name: o.food_name, quantity:o.quantity});
                groupOrder[o.order_id].total += o.unit_price * o.quantity;
            });
            console.log(orderList.value);
            isLoaded.value = true;
        }
    }

    onBeforeMount(getOrders);



    



    

</script>

<template>
    <Header title="View Orders" icon="pi-eye"></Header>

    <div class="m-3">
        <div class="order-table color-base p-2 m-2 box-shadow round-border">
            <table class="w-100" v-if="isLoaded">
                <tr class="text-white text-shadow under-line">
                    <th>ID</th>
                    <th>Order</th>
                    <th>Payment Type</th>
                    <th>Total</th>
                    <th>Date</th>
                </tr>
                <tr v-for="order in orderList" class="under-line">
                    <td>{{ order.orderNum }}</td>
                    <td>
                        <p v-for="food in order.foodList">
                            
                            {{ food.name }} x{{ food.quantity }}
                            
                        </p>
                    </td>
                    <td>{{ order.paytype }}</td>
                    <td>{{ order.total }}</td>
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