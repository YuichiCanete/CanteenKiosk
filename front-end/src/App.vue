<script setup>
  
  import {apiFunc} from './pages/data.js'
  

  async function tryPost() {
    return await apiFunc.value.add('http://127.0.0.1:8000/api/users/',{
      user_id:70,
      password:"420pass",
      user_type:"helloworld"
    });
  }

  async function tryDel() {
    return await apiFunc.value.remove('http://127.0.0.1:8000/api/users/70');
  }

  async function tryUpdate() {
    return await apiFunc.value.update('http://127.0.0.1:8000/api/users/70',{
      password:"pass320",
      user_type:"helloworld"
    });
  }

  // tryDel()
  // tryPost()
  // tryUpdate()

</script>

<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<style scoped>

  .logout-btn {
    position: fixed;
    top: 95%;
    left: 90%;
    transform: translate(-50%,-50%);
  }

</style>
