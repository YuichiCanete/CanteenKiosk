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
        <div class="login-container color-base p-5">
            <h1>Login Page</h1> <br>
            <input type="text" placeholder="User ID" class="p-2 m-2"> <br>
            <input type="password" placeholder="Password" class="p-2 m-2"> <br>
            <input type="button" value="Login" @click="loginUser()" class="p-2 m-2">
        </div>
    </div>
    
        
</template>

<style scoped>


    .login-container {
        width: 50%;
        height: 75%;
    }
    

</style>
