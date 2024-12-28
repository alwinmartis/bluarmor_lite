<template>
    <div class="w-screen h-screen mx-0 my-0 px-0 py-0 flex items-center">
        <!-- navbar -->
        <div class="w-[300px] h-full bg-gray-200">
            <div class="h-[50px] bg-blue-600 w-full text-white flex items-center justify-center">
                Bluarmor
            </div>
            <div class="h-[calc(100vh-50px)] bg-violet-400 py-[20px] flex flex-col justify-between align-between">
                <div class="px-[20px] flex flex-col space-y-[10px]">
                    <router-link to="/Dashboard" class="inline-flex relative items-center justify-center py-[20px] w-full">
                        Home
                    </router-link> 
                    <router-link to="/dashboard" class="inline-flex relative items-center justify-center py-[20px] w-full">
                        About
                    </router-link>
                    <router-link to="/dashboard" class="inline-flex relative items-center justify-center py-[20px] w-full">
                        Dashboards
                    </router-link>
                </div>
                <div>
                    <router-link to="/dashboard" class="inline-flex relative items-center justify-center py-[20px] w-full">
                        Setting
                    </router-link>

                </div>
            </div>
            
        </div>

        <!-- main page -->
        <div class="w-full h-full bg-gray-400">
            <div class="h-[50px] bg-blue-600">

            </div>
            <div class="h-[calc(100vh-50px)] bg-violet-300">
                <RouterView></RouterView>

            </div>
        </div>

    </div>
</template>
<script setup>
</script>