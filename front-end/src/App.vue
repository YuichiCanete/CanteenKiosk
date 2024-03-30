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

  data.addFood('Egg', 20, 20);
  data.addFood('Hotdog', 10, 10);

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
