<script setup>

import { ref } from 'vue';
import { apiFunc } from './data.js';
import { useRouter } from 'vue-router';

const router = useRouter();
let errorMessage = ref('')

function switchTo(path) {
    router.push(path);
}

async function getUsers(useID) {
    return await apiFunc.value.get('http://127.0.0.1:8000/api/users/' + useID);
}

async function loginUser() {
    let id = parseInt(document.getElementById('inputID').value);
    let pass = document.getElementById('inputPass').value;

    let user = await getUsers(id);
    
    console.log(user);

    if (user.isSuccess && user.data.length > 0) {
        user = user.data[0];
        if (id === user.user_id && pass === user.password) {
            alert('Login Success');
            switch (user.user_type){
                case "personnel":
                    switchTo('/createOrder');
                    break;
                case "cashier":
                    switchTo('/viewOrders');
                    break;
                case "admin":
                    break;
                case "counter":
                    break;
            }
        } else {
            errorMessage.value = 'Incorrect Credentials'
        }
    } else {
        errorMessage.value = 'Incorrect Credentials'
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
            <p class="text-red">{{ errorMessage }}</p>
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
