<script setup>
    import { useRouter } from 'vue-router';
    const router = new useRouter()
    defineProps({
        icon: String,
        title: String,
    })
</script>

<template>

<div class="color-base p-2" style="display: flex; justify-content: space-between; align-items: center;">
    <div style="display: flex; align-items: center;">
        <img src="../assets/Canteen Kiosk.png" alt="" style="border-radius: 100%; width: 100px;" class="box-shadow m-2">
        <div class="text-light">
            <h1 class="text-shadow">Canteen Kiosk</h1>    
            <h2 class="text-shadow" style="font-size: 30px;"><i :class="icon" class="pi text-shadow m-2 mt-0 mb-0" style="font-size: 25px;"></i >{{ title }}</h2>
        </div>
    </div>
    <Button icon="pi pi-power-off" label="Logout" class="logoutButton text-shadow" @click="router.push('/')" v-if="title !== 'Login Page'"></Button>
</div>


    
</template>

<style scoped>

    .logoutButton {
        background: none;
        outline: none;
        border: none;
        box-shadow: none;
        font-size: 20px;
    }

</style>