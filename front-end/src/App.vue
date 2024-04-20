<script setup>

  
  import {data} from './pages/data.js'
  import {useRouter} from 'vue-router'
  const router = useRouter()
  function switchTo(path){
    router.push(path)
  }

  function logout(){
    switchTo('/')
  }

  

  



  data.value.addFood('Egg', 64, 10);
  data.value.addFood('Hotdog', 30, 15);
  data.value.addFood('Siomai',50,5)
  data.value.addFood('Rice',100,10)
  data.value.addFood('Spaghetti',25,60)
  data.value.addFood('Cheese Stick',50,5)
  data.value.addFood('Lumpia',75,5)
  data.value.addFood('Pizza',32,25)
  data.value.addFood('Mentos',45,5)
  data.value.addFood('Pillows',0,10)

  data.value.addUser('220000743','password1','student')
  data.value.addUser('220000744','password2','student')
  data.value.addUser('220000745','password3','cashier')
  data.value.addUser('220000746','password4','cashier')
  data.value.addUser('220000747','password5','cashier')
  data.value.addUser('220000748','password6','student')
  data.value.addUser('220000749','password7','student')
  data.value.addUser('220000750','password8','student')
  data.value.addUser('220000751','password9','cashier')
  data.value.addUser('220000752','password10','cashier')
  


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
