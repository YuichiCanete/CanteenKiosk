<script setup>
    import {data} from './data.js'
</script>

<template>
    <Header title="Edit Menu"></Header>

    <div class="m-3">
        <div class="menu-table color-base p-2 m-2 box-shadow round-border">
            <table class="w-100">
                <tr class="text-white text-shadow under-line">
                    <th>Image</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Available Stock</th>
                    <th>Actions</th>
                </tr>
                <tr v-for="food in data.foodList" class="under-line">
                    <td>IMAGE</td>
                    <td>{{ food.name }}</td>
                    <td>{{ food.price }}</td>
                    <td>{{ food.inventory }}</td>
                    <td>
                        <button class="btn-uic m-2">Done</button>
                        <button class="btn-uic m-2">Cancel</button>
                    </td>
                    
                </tr>
                <tr>
                    <td colspan="5" style="text-align: center;">
                        <button class="btn-uic m-2">Add New Item</button>
                    </td>
                </tr>
            </table>

        </div>

    </div>

</template>

<style scoped>


    .menu-table{
        margin: 0 auto;
        width: min(750px,80%);
        height: 60vh;
    }

    .under-line {
        border-bottom: 1px solid white;
    }

</style>