<script setup>

    import { data } from './data.js';
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }  

    function loginUser(){
        let id = document.getElementById('inputID').value
        let pass = document.getElementById('inputPass').value
        
        var user = data.value.userList.find(function(user){
            return user.userID === id
        })

        if (user){
            alert("Login Success")
            switch (user.userType){
                case "student":
                    switchTo('/createOrder')
                break;
                case "cashier":
                    switchTo('/viewOrders')
                break;
            }
        }else{
            alert("Login Failed")
        }
    }

    
</script>

<template>

    <Header title="Login Page"></Header>
    <div class="container-fluid d-flex align-items-center justify-content-center text-center" style="height: 75vh;">
        <div class="login-container color-base p-5 box-shadow round-border">
            <h1 class="text-white text-shadow">Login</h1> <br>
            <input type="text" placeholder="User ID" class="p-2 m-2 inp-uic" id="inputID"> <br>
            <input type="password" placeholder="Password" class="p-2 m-2 inp-uic" id="inputPass"> <br>
            <input type="button" value="Login" @click="loginUser()" class="p-2 m-2 btn-uic">
        </div>
    </div>
    
        
</template>

<style scoped>


    .login-container {
        width: min(500px,50%);
        height: 75%;
    }

    .inp-uic {
        width: min(250px,90%);
    }
    

</style>
