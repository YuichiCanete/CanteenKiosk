<script setup>

  import {useRouter} from 'vue-router'
  const router = useRouter()
  function switchTo(path){
    router.push(path)
  }
  switchTo('/')

  const items = [];

</script>

<script>
  import {useRouter} from 'vue-router'
  const router = useRouter()
  function switchTo(path){
    router.push(path)
  }
</script>

<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<style scoped>

</style>
