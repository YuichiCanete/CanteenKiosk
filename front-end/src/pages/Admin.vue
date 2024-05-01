<script setup>
    import { onBeforeMount, ref } from 'vue';
    import { apiFunc } from './data.js';
    import Dropdown from 'primevue/dropdown';
    import TabMenu from 'primevue/tabmenu';
    import { useConfirm } from "primevue/useconfirm";
    import { useToast } from "primevue/usetoast";

    const confirm = useConfirm();
    const toast = useToast();

    let users = ref([]);
    async function updateUsers(){
        let requestUsers = await apiFunc.value.get('http://127.0.0.1:8000/api/users')
        if (requestUsers.isSuccess){
            users.value = requestUsers.data
            console.log(users.value)
        }
        resetForm()
    }
    onBeforeMount(updateUsers)

    function resetForm(){
        userInp.value = ''
        passInp.value = ''
        selectedType.value = {}
    }
    
    const userTypes = ref([
        {name: 'Admin', code:'admin',},
        {name: 'Personnel', code:'personnel'},
        {name: 'Cashier', code:'cashier'},
        {name: 'Counter', code:'counter'}
    ])

    const tabOptions = ref([
        { label: 'Add User', icon: 'pi pi-user-plus', availForm:[1,1,1,1],},
        { label: 'Edit User', icon: 'pi pi-user-edit', availForm:[1,1,1,1],},
        { label: 'Delete User', icon: 'pi pi-trash', availForm:[1,0,0,1],}, 
    ]);


    async function onSubmit() {
        const actions = [
            async () => {
                await apiFunc.value.add('http://127.0.0.1:8000/api/users/', {
                    user_id: parseInt(userInp.value),
                    password: passInp.value,
                    user_type: selectedType.value.code
                });
            },
            async () => {
                await apiFunc.value.update(`http://127.0.0.1:8000/api/users/${userInp.value}`, {
                    password: passInp.value,
                    user_type: selectedType.value.code
                });
            },
            async () => {
                await apiFunc.value.remove(`http://127.0.0.1:8000/api/users/${userInp.value}`);
            }
        ];
        await actions[selectedTab.value]();
        updateUsers();
        loginError()

    }

    const selectedTab = ref(0)
    const userInp = ref()
    const passInp = ref()
    const selectedType = ref()    

    function loginError(){
        toast.add({
            severity: 'error', 
            summary: 'Login Error',
            detail: 'Incorrect Credentials',
            life: 2000 });
    }

</script>

<template>

    <Header title="Admin Page" icon="pi-user"></Header>

    <Toast />
    <ConfirmDialog></ConfirmDialog>

    <TabMenu :model="tabOptions" v-model:activeIndex="selectedTab"/>
                
    <h2 class="text-pink m-2">{{ tabOptions[selectedTab].label }}</h2>
    <InputText placeholder="User Id" class="m-2" id="inputID" v-if="tabOptions[selectedTab].availForm[0]" v-model="userInp"></InputText>
    <InputText placeholder="Password" class="m-2" id="inputPass" v-if="tabOptions[selectedTab].availForm[1]" v-model="passInp"></InputText>
    <Dropdown v-model="selectedType" :options="userTypes" optionLabel="name" placeholder="User Type" checkmark :highlightOnSelect="false" class="m-2" id="inputSelect" v-if="tabOptions[selectedTab].availForm[2]"/>
    <Button label="Submit" @click="onSubmit()" :icon="tabOptions[selectedTab].icon" class="m-2" id="inputSubmit" v-if="tabOptions[selectedTab].availForm[3]"></Button>

    <h2 class="text-pink m-2">Users</h2>
    <div style="width: 500px;" class="m-2">
        <DataTable :value="users" tableStyle="width: 100%" scrollable scrollHeight="400px">
            <Column field="user_id" header="ID"></Column>
            <Column field="password" header="Password"></Column>
            <Column field="user_type" header="User type"></Column>
        </DataTable>
    </div>
        
</template>

<style scoped>

    :deep(.p-menuitem-text), :deep(.p-menuitem-icon){
        color: #D94496;
    }

    :deep(.p-menuitem-link){
        text-decoration: none;
    }

</style>