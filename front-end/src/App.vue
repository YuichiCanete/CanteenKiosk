<script setup>

  import {data} from './pages/data.js'
  import {useRouter} from 'vue-router'
  const router = useRouter()
  function switchTo(path){
    router.push(path)
  }
  switchTo('/')

  function logout(){
    switchTo('/')
  }

  data.value.addFood('Egg', 20, 20);
  data.value.addFood('Hotdog', 10, 10);

  data.value.addUser('220000742','userpass','student')
  data.value.addUser('220000743','userpass','student')
  data.value.addUser('220000744','userpass','cashier')

  data.value.foodList[0].quantity = 69
  data.value.foodList[1].quantity = 420
  data.value.addOrder()
  data.value.addOrder()

</script>

<template>
  <div>
    <router-view></router-view>
    <input type="button" value="Logout" class="logout-btn btn-uic" @click="logout()">
  </div>
</template>

<style scoped>

  .logout-btn {
    position: absolute;
    top: 95%;
    left: 90%;
    transform: translate(-50%,-50%);
  }

</style>
