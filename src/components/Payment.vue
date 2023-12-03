<script setup>

    import Button from 'primevue/button';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';

    import { useRouter } from 'vue-router';  
    const router = useRouter();
    const newScreen = (nscr) => {
        router.push(nscr)
    };

    const selected = [
        {
            food: 'Rice',
            price: 20,
            quantity: 2,
        },
        {
            food: 'Siomai',
            price: 25,
            quantity: 1,
        },
    ]

</script>

<template>

    <div class="pop">
        <h1>Selected Items</h1>
        <DataTable :value="selected" tableStyle="width: 400px" scrollable scrollHeight="500px">            <Column field="food" header="Food"></Column>
            <Column field="price" header="Price"></Column>
            <Column field="quantity" header="Quantity"></Column>
        </DataTable>
        <h3>Total: P45</h3>

        <h3>Payment Type</h3>
        <Button label="Cash" @click="newScreen('/getorder')"></Button>
        <Button label="Tally" @click="newScreen('/getorder')"></Button>
    </div>
    

    
</template>

<style scoped>
    .pop {
        
        text-align: center;

        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);

        background-color: pink;
        padding: 15px;
        border-radius: 15px;
        border: 3px solid rgb(255, 107, 132);

    }

</style>
