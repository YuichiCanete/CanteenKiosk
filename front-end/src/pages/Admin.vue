<script setup>
    import { onBeforeMount, ref } from 'vue';
    import { apiFunc } from './data.js';

    let ids = ref([{
        title: 'Add User',
        user_id: 'add_user_id',
        password: 'add_password',
        option: 'add_option',
        submit: 'add_submit',
        whenClicked: async function(){
            let id = parseInt(document.getElementById('add_user_id').value, 10);
            let pass = document.getElementById('add_password').value
            let utype = document.getElementById('add_option').value
            await apiFunc.value.add('http://127.0.0.1:8000/api/users/',{
                user_id: id,
                password: pass,
                user_type: utype
            })
            updateUsers()
        }
    },{
        title: 'Edit User',
        user_id: 'edit_user_id',
        password: 'edit_password',
        option: 'edit_option',
        submit: 'edit_submit',
        whenClicked: async function(){
            const [id, pass, utype] = ['edit_user_id', 'edit_password', 'edit_option'].map(id => document.getElementById(id).value);
            await apiFunc.value.update('http://127.0.0.1:8000/api/users/'.concat(id),{
                password: pass,
                user_type: utype
            })
            document.getElementById('edit_user_id').value = ''
            document.getElementById('edit_password').value = ''
            document.getElementById('edit_option').value = 'admin'
            updateUsers()
        }
    },{
        title: 'Delete User',
        user_id: 'delete_user_id',
        submit: 'delete_submit',
        whenClicked: async function(){
            let id = document.getElementById('delete_user_id').value
            await apiFunc.value.remove('http://127.0.0.1:8000/api/users/'.concat(id));
            updateUsers()
        }
    }])

    let users = ref([]);
    async function updateUsers(){
        let requestUsers = await apiFunc.value.get('http://127.0.0.1:8000/api/users')
        if (requestUsers.isSuccess){
            users.value = requestUsers.data
        }
        console.log(users)
    }
    onBeforeMount(updateUsers)
    

</script>

<template>

    <Header title="Admin Page"></Header>
    <div v-for="id in ids">
        <h2 class="text-white text-shadow">{{ id.title }}</h2>
        <input type="number" placeholder="User ID" class="p-2 m-2 inp-uic" :id=id.user_id v-if="id.user_id">
        <input type="password" placeholder="Password ID" class="p-2 m-2 inp-uic" :id=id.password v-if="id.password">
        <select name="User Type" class="inp-uic" :id=id.option v-if="id.option">
            <option value="admin">Admin</option>
            <option value="personnel">Personnel</option>
            <option value="cashier">Cashier</option>
        </select>
        <button class="btn-uic" :id=id.submit v-if="id.submit" @click="id.whenClicked()">Submit</button>
    </div>

    <table class="w-100">
        <tr class="text-white text-shadow">
            <th>ID</th>
            <th>Password</th>
            <th>User Type</th>
        </tr>
        <tr v-for="user in users">
            <td>{{ user.user_id }}</td>                    
            <td>{{ user.password }}</td>
            <td>{{ user.user_type }}</td>
        </tr>
    </table>

</template>

<style scoped>

</style>