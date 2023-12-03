<script setup>
    import { useRouter } from 'vue-router';  
    const router = useRouter();
    const newScreen = (nscr) => {
        router.push(nscr)
    };

    import Button from 'primevue/button';
</script>

<template>

    <div class="pop">
        <h1>Order Successful</h1>
        <h3>Your waiting number is</h3>
        <h3>12</h3>

        <Button label="Create Another Order" @click="newScreen('/login')"></Button>
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