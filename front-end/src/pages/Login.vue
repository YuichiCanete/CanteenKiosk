<script setup>

    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }  

    function loginUser(){
        switchTo('/createOrder')
    }
    
</script>

<template>

    <Header title="Login Page"></Header>

    <div class="container-fluid d-flex align-items-center justify-content-center text-center" style="height: 75vh;">
        <div class="login-container color-base p-5 box-shadow round-border">
            <h1 class="text-white text-shadow">Login</h1> <br>
            <input type="text" placeholder="User ID" class="p-2 m-2 inp-uic"> <br>
            <input type="password" placeholder="Password" class="p-2 m-2 inp-uic"> <br>
            <input type="button" value="Login" @click="loginUser()" class="p-2 m-2 btn-uic">
        </div>
    </div>
    
        
</template>

<style scoped>


    .login-container {
        width: 50%;
        height: 75%;
    }
    

</style>
