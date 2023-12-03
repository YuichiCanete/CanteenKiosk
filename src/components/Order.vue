<script setup>

    import Image from 'primevue/image';
    import Button from 'primevue/button';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import InputNumber from 'primevue/inputnumber';

    import { useRouter } from 'vue-router';  
    const router = useRouter();
    const newScreen = (nscr) => {
        router.push(nscr)
    };


    const val1 = 0;

    const products = [
        {
            food: "Siomai",
            price: 25,
            quantity: 0
        },
        {
            food: "Juice",
            price: 25,
            quantity: 0
        },
        {
            food: "Chicken",
            price: 50,
            quantity: 0
        },
        {
            food: "Cheese Stick",
            price: 10,
            quantity: 0
        },
        {
            food: "Sphagetti",
            price: 50,
            quantity: 0
        },
        {
            food: "Rice",
            price: 10,
            quantity: 0
        },
    ]

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

    <div class="topbar">
        <h1>What Will You Have Today?</h1>
    <Image src="https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/305975246_480030324173600_4611494949818294877_n.png?_nc_cat=100&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeEr57RjIzT2zI2IQkX3pZSnQWGQxV8Is6NBYZDFXwizo44xuY1kIT1yfOrKmbYzqdAxUVOp0EsS-E4HPBgFi1fY&_nc_ohc=VQCL02lBF98AX_pkHbN&_nc_ht=scontent.fcgy2-1.fna&oh=00_AfDSnbS3_4nKI7o5j51OBUpY-IkPSAc2rYhj9HN9EjrO5Q&oe=6570F5EC" alt="Image" width="150"/>
    </div>

    <div class="top">
        <Button label="Breads"></Button>
        <Button label="Meals"></Button>
        <Button label="Drinks"></Button>
        <Button label="Snacks"></Button>
        <Button label="Toppings"></Button>
        <Button label="Extra"></Button>
    </div>

    <div class="container">    
        <div class="left">
            <h3>Items</h3>
            <DataTable :value="products" scrollable scrollHeight="300px">
                <Column field="food" header="Food"></Column>
                <Column field="price" header="Price"></Column>
                <Column field="quantity" header="Quantity">
                    <template #body="rowData">
                        <InputNumber
                        v-model="val1"
                        inputId="horizontal-buttons"
                        showButtons
                        buttonLayout="horizontal"
                        :step="1"
                        decrementButtonClass="p-button-danger"
                        incrementButtonClass="p-button-success"
                        incrementButtonIcon="pi pi-plus"
                        decrementButtonIcon="pi pi-minus"
                        inputStyle="display: inline-block; width: 70px;"
                        />
                    </template>
                </Column>
            </DataTable>
        </div>
    
        <!-- SELECTED -->
        <div class="right">
            <h3>Selected Items</h3>
            <DataTable :value="selected" tableStyle="width: 350px;" scrollable scrollHeight="500px" class="datatable">
                <Column field="food" header="Food"></Column>
                <Column field="price" header="Price"></Column>
                <Column field="quantity" header="Quantity"></Column>
            </DataTable>
            <div style="text-align: center;">
                <h3>Total: P50</h3>
                <Button label="Confirm Order" @click="newScreen('/payment')"></Button>
            </div>
        </div>
        
    </div>

 
</template>

<style scoped>

    .top {
        text-align: center;
        margin: 15px;
    }

    .container {
        
        width: 90%;
        height: 50vh;
        background-color: pink;
        border: 3px solid rgb(255, 107, 132);
        display: flex;
        margin-left: 5%;
        padding: 0 30px;
        border-radius: 15px;
    }

    .left {
        width: 60%;
        margin-right: 5%;
    }

    .right {
        width: 35%
    }


</style>
