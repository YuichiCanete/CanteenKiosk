<script setup>
    defineProps({
        title: String,
    })
</script>

<template>
    <div class="bg-pink p-3 container-fluid box-shadow">
        <div class="row">
            <div class="col-4 col-md-2 col-lg-1">
                <img 
                src="../assets/Canteen Kiosk.png"
                alt="Canteen Kiosk Logo"
                style="border-radius: 100%; width: 125px;">           
            </div>
            <div class="col-6 col-md-9 col-lg-10">
                <h1>Canteen Kiosk</h1>
                <h2>{{title}}</h2>
            </div>
        </div>
    </div>
</template>