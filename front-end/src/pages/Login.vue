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
    
    <div class="p-3">
        <h3>Login Page</h3>
        <input type="text" placeholder="User ID">
        <input type="password" placeholder="Password">
        <input type="button" value="Login" @click="loginUser()">
    </div>
    
        
</template>

<style scoped>

    .custom-input {
        outline: none;
        border: none;
        background-color: rgb(0,0,0,0);
        border-bottom: 1px solid white;
        color: white;
    }

    ::placeholder {
        color: rgb(200,200,200);
        opacity: 1;
    }

</style>
