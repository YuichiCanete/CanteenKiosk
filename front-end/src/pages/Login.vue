<script setup>

    import { ref } from 'vue';    
    import { data,apiFunc } from './data.js';
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }

    
    async function getUsers(){
        return await apiFunc.value.get('http://127.0.0.1:8000/api/user/')
    }
    let users = ref(getUsers().data)
    
    function loginUser(){
        let id = parseInt(document.getElementById('inputID').value);
        let pass = document.getElementById('inputPass').value;
        
        var user = users.find(function(user){
            return user.user_id === id && user.password === pass; // Check both ID and password
        });

        if (user){
            alert("Login Success");
            switchTo('/createOrder')
            // switch (user.userType){
            //     case "student":
            //         switchTo('/createOrder');
            //         break;
            //     case "cashier":
            //         switchTo('/viewOrders');
            //         break;
            // }
        }else{
            alert("Login Failed. Please check your ID and password.");
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
