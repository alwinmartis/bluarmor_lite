<template>
    <div class="w-screen h-screen mx-0 my-0 px-0 py-0 flex items-center">
        <!-- navbar -->
        <div class="w-[300px] h-full bg-sky-500">
            <div class="h-[50px] font-bold text-3xl font-sans navbar w-full text-white flex items-center justify-center">
                BluArmor
            </div>
            <div class="h-[calc(100vh-50px)] navbar-right py-[20px] font-sans flex flex-col justify-between align-between">
                <div class="px-[20px] flex flex-col space-y-[10px]">
                    <router-link to="/home" class="rounded-md hover:bg-white text-xl font-semibold inline-flex relative items-center justify-center py-[20px] w-full">
                        Home
                    </router-link> 
                    <router-link to="/sales" class="rounded-md hover:bg-white text-xl font-semibold inline-flex relative items-center justify-center py-[20px] w-full">
                        Targets
                    </router-link>
                    <router-link to="/dashboard" class="rounded-md hover:bg-white text-xl font-semibold inline-flex relative items-center justify-center py-[20px] w-full">
                        Dashboards
                    </router-link>
                </div>
                <div class="px-[20px] flex flex-col space-y-[10px]">
                    <router-link to="/dashboard" class="rounded-md hover:bg-white text-xl font-semibold inline-flex relative items-center justify-center py-[20px] w-full">
                        Setting
                    </router-link>

                </div>
            </div>
            
        </div>

        <!-- main page -->
        <div class="w-full h-full bg-white">
            <div class="h-[50px] navbar">

            </div>
            <div class="h-[calc(100vh-75px)] w[calc(100vh-340px)] rounded-md px-5 py-5  main">
                <div >
                    <RouterView></RouterView>
                </div>
                
            </div>
        </div>

    </div>
</template>


<script setup>
</script>


<style>
.navbar{
    background-color: #383838;
}
.navbar-right{
    background-color: #f4f4f4;
}
.main{
    background-color: #f4f4f4;
    margin-top: 20px;
    margin-left:20px;
    margin-right:20px
}
</style>
