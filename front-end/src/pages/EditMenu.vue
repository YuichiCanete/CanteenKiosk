<script setup>

</script>

<template>
    <Header title="Edit Menu"></Header>

    <div class="m-3">
        <div class="menu-table color-base p-2 m-2">
            <table class="w-100">
                <tr>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Actions</th>
                </tr>
                <tr v-for="i in 5">
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                    <td>Hello</td>
                </tr>
            </table>

        </div>

    </div>

</template>

<style scoped>

    .menu-table{
        width: 90%;
        height: 60vh;
    }

</style>