<script setup>

    import Button from 'primevue/button';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';

    const payment = [
        { payment_id: 'PY111', order_id: 'OR111', pay_type: 'cash', total: 100, cash: 100, change: 0 },
        { payment_id: 'PY112', order_id: 'OR112', pay_type: 'tally', total: 200, cash: 500, change: 300 },
        { payment_id: 'PY113', order_id: 'OR113', pay_type: 'tallly', total: 150, cash: 200, change: 50 },
        { payment_id: 'PY114', order_id: 'OR114', pay_type: 'cash', total: 75, cash: 100, change: 25 },
        { payment_id: 'PY115', order_id: 'OR115', pay_type: 'cash', total: 200, cash: 200, change: 0 },
        { payment_id: 'PY116', order_id: 'OR116', pay_type: 'cash', total: 30, cash: 50, change: 20 },
        { payment_id: 'PY117', order_id: 'OR117', pay_type: 'cash', total: 15, cash: 20, change: 5 },
        { payment_id: 'PY118', order_id: 'OR118', pay_type: 'cash', total: 75, cash: 75, change: 0 },
        { payment_id: 'PY119', order_id: 'OR119', pay_type: 'cash', total: 100, cash: 100, change: 0 },
        { payment_id: 'PY120', order_id: 'OR120', pay_type: 'cash', total: 25, cash: 50, change: 25 }
    ];

</script>

<template>
    
    <DataTable :value="payment" tableStye="width: 100%" scrollable scrollHeight="500px">
        <Column field="payment_id" header="Payment ID"></Column>
        <Column field="order_id" header="Order ID"></Column>
        <Column field="pay_type" header="Payment Type"></Column>
        <Column field="total" header="Total"></Column>
        <Column field="cash" header="Cash"></Column>
        <Column field="change" header="Change"></Column>
        <Column header="Action">
            <template #body="rowData">
                <Button icon="pi pi-check" label="Okay" severity="info"></Button>
            </template>
        </Column>
    </DataTable>

</template>

<style scoped>
</style>