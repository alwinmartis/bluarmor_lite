<template>
  <div class="master w-full h-full flex" >
    <div class="bg-indigo-400">
      <Sidebar />
    </div>

    <div class="w-full h-[calc(100vh-50px)]">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>
import Sidebar from '@/components/Sidebar.vue'
</script>
<style scoped>
/* .master {
  display: flex;
  width:100vh
}
.navbar{
    height:100vh;
    width:15vh;
}
.router{
    height:100vh;
    width:85vh
} */
</style>
