<script setup>
    defineProps({
        name: String,
        price: Number,
        available_stock: Number
    })
</script>

<template>
    <Card style="width: 300px; overflow: hidden;" class="box-shadow">
        <template #header>
            <img src="../assets/food_placeholder.jpg" style="width: 100%;">
        </template>
        <template #title>{{ name }}</template>
        <template #subtitle> P{{ price }}</template>
        <template #footer >
            <div style="float: right;">
                <Button icon="pi pi-cart-plus" label="Add" class="m-1"></Button>
                <Button icon="pi pi-cart-minus" label="Remove" class="m-1"></Button>
            </div>
        </template>
    </Card>
</template>


