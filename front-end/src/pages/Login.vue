<script setup>
    import { ref } from 'vue';
    import { apiFunc } from './data.js';
    import { useRouter } from 'vue-router';
    import { useConfirm } from "primevue/useconfirm";
    import { useToast } from "primevue/usetoast";

    const confirm = useConfirm();
    const toast = useToast();
    const router = useRouter();

    let errorMessage = ref('')
    let userInp = ref('')
    let passInp = ref('')
    let isLogging = ref(false)

    async function getUsers(useID) {
        return await apiFunc.value.get('http://127.0.0.1:8000/api/users/' + useID);
    }

    async function loginUser() {
        let user = await getUsers(userInp.value);
        if (user.isSuccess && user.data.length > 0) {
            user = user.data[0];
            if (parseInt(userInp.value) === user.user_id && passInp.value === user.password) {
                isLogging.value = true
                loginSuccess()
                setTimeout(()=>{
                    switch (user.user_type){
                        case "personnel":
                            router.push('/createOrder')
                            break;
                        case "cashier":
                            router.push('/viewOrders')
                            break;
                        case "admin":
                            router.push('/admin')
                            break;
                        case "counter":
                            break;
                    }
                },1000)
            } else {
                errorMessage.value = 'Incorrect Credentials'
                loginError()
            }
        } else {
            errorMessage.value = 'Incorrect Credentials'
            loginError()
        }
    }

    function loginError(){
        toast.add({
            severity: 'error', 
            summary: 'Login Error',
            detail: 'Incorrect Credentials',
            life: 2000 });
    }

    function loginSuccess(){
        toast.add({
            severity: 'success', 
            summary: 'Login Successful',
            detail: 'successfully logged in your account',
            life: 1000 });
    }
</script>

<template>

    <img src="..\assets\background.jpg" class="uicBg">
    <Header title="Login Page" icon="pi-user"></Header>
    <Toast />
    <ConfirmDialog></ConfirmDialog>
    <div class="container-fluid d-flex align-items-center justify-content-center text-center" style="height: 75vh;">
        <div class="login-container p-5">
            <h1 class="text-white text-shadow">Login</h1> <br>
            <InputText placeholder="User ID" class="m-2 w-75" id="inputID" v-model="userInp"/>
            <InputText type='password' placeholder="Password" class="m-2 w-75" id="inputPass" v-model="passInp"/> <br>
            <Button label="Login" class="m-2" @click="loginUser()" :disabled="isLogging" icon="pi pi-user"></Button>
            <p style="color: red; font-weight: bold; font-size: 20px;" class="text-shadow" id="errorMessage">{{ errorMessage }}</p>
        </div>
    </div>    
        
</template>

<style scoped>

    .login-container {
        width: min(500px,50%);
        height: 75%;
        border-radius: 15px;
        border: 3px solid white;
        background-color: rgba(255, 255, 255, .25);
        backdrop-filter: blur(3px);
    }

    .inp-uic {
        width: min(250px,90%);
    }

    .uicBg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background-size: cover;
    }
    

</style>
