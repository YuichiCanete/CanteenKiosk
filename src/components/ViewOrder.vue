<script setup>

    import Button from 'primevue/button';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import { ref } from 'vue';

    var order = [
        { order_id: 'OR111', user_id: 22000347, payment_id: 'PI111', date: '12-1-2023' },
        { order_id: 'OR112', user_id: 22000348, payment_id: 'PI112', date: '12-2-2023' },
        { order_id: 'OR113', user_id: 22000349, payment_id: 'PI113', date: '12-3-2023' },
        { order_id: 'OR114', user_id: 22000350, payment_id: 'PI114', date: '12-4-2023' },
        { order_id: 'OR115', user_id: 22000351, payment_id: 'PI115', date: '12-5-2023' },
        { order_id: 'OR116', user_id: 22000352, payment_id: 'PI116', date: '12-6-2023' },
        { order_id: 'OR117', user_id: 22000353, payment_id: 'PI117', date: '12-7-2023' },
        { order_id: 'OR118', user_id: 22000354, payment_id: 'PI118', date: '12-8-2023' },
        { order_id: 'OR119', user_id: 22000355, payment_id: 'PI119', date: '12-9-2023' },
        { order_id: 'OR120', user_id: 22000356, payment_id: 'PI120', date: '12-10-2023' }
    ];

    var menu = [
        {description: "rice, siomai", total:50},
        {description: "juice", total:25},
        {description: "chicken, spaghetti", total:100},
    ];

    const showOrder = ref(false);
    function showToggle() {
        showOrder.value = !showOrder.value;
    }

</script>

<template>

    <DataTable :value="order" tableStyle="width: 100%" scrollable scrollHeight="500px">
        <Column field="user_id" header="User ID"></Column>
        <Column field="order_id" header="Order ID"></Column>
        <Column field="payment_id" header="Payment ID"></Column>
        <Column field="date" header="Date"></Column>
        <Column field="action" header="Action">
            <template #body="rowData">
                <Button label="View Orders" icon="pi pi-eye" severity="success" @click="showToggle()"></Button>
                <Button label="Process" icon="pi pi-check" severity="info"></Button>
                <Button label="Cancel" icon="pi pi-times" severity="danger"></Button>
            </template>
        </Column>
    </DataTable>

    <div v-if="showOrder">
        <DataTable :value="menu" tableStyle="width: 100%" scrollable scrollHeight="500px">
            <Column field="description" header="Description"></Column>
            <Column field="total" header="Total"></Column>
        </DataTable>
    </div>
    

    <br><br><br>
    <Button label="Edit Menu"></Button>

</template>

<style scoped>

</style>
