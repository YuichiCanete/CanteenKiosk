<script setup>
    import FoodCard from '../components/FoodCard.vue'
</script>

<template>


    <Header title="Create Order"></Header>
    
    <table style="width: 100%;">
        <tr>
            <!-- Left -->
            <td class="bg-danger food-list">
                <div v-for="i in 10">
                    <FoodCard/>
                </div>
            </td>
            <!-- Right -->
            <td class="bg-success order-list">

            </td>
        </tr>
    </table>
    
</template>

<style scoped>

    .food-list {
        width: min(500px,1000px);
        height: 75vh;
        flex-direction: row;
    }

    .order_list {
        width: 50%;
        height: 75vh;
    }

</style>

