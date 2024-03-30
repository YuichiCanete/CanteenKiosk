<script setup>

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
                <tr>
                    <th>ID</th>
                    <th>Order</th>
                    <th>Payment Type</th>
                    <th>Total</th>
                    <th>Date</th>
                    <th>Actions</th>
                </tr>
                <tr v-for="i in 5">
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
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
    }

</style>