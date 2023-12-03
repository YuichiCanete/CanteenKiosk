<script setup>

  import { onBeforeMount } from 'vue';
  //function for changing screen
  import { useRouter } from 'vue-router';  
  const router = useRouter();
  const newScreen = (nscr) => {
    router.push(nscr)
  };

  //Open Login on load
  onBeforeMount(() => {
    router.push('/login');
  });

</script>

<template>

  <!-- Display Current Screen -->
  <div>
    <router-view></router-view>
  </div>

</template>

<style scoped>

</style>
