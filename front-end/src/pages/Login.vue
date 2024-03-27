<script setup>
    import {useRouter} from 'vue-router'
    const router = useRouter()
    function switchTo(path){
        router.push(path)
    }  



</script>

<template>

    <Header title="Login Page"></Header>
    <div class="container-fluid d-flex justify-content-center p-5">
        <div class="bg-pink row col-3 p-3 text-center box-shadow">
            <h3 class="text-white mb-3">Login</h3>
            <input type="text" placeholder="User ID" class="custom-input mb-3" id="inputId">
            <input type="password" placeholder="Password" class="custom-input mb-3" id="inputPassword">
            <input type="button" value="Login" class="btn btn-light" id="buttonLogin" @click="switchTo('/pageB')">
        </div>
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
