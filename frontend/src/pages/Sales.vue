<template>
  <div class="h-full">
    <div class="flex justify-around date mb-2">  
      <div class="flex space-x-7">
        <p >From Date</p>
        <FormControl
          placeholder="From Date"
          type="date"
          lable="fdate"
          v-model="fromdate"
        ></FormControl>
      </div>
      <div class="flex space-x-7">
        <p >To Date</p>
        <FormControl
          placeholder="To Date"
          type="date"
          lable="tdate"
          v-model="todate"
        ></FormControl>
      </div>
      </div>
      <div class="flex justify-center item-center pb-30">
        <Button theme="blue" :variant="outline" @click="addcard">Add</Button>
        <Button theme="blue" :variant="outline"> Remove</Button>
      </div>
      <div>
        <div v-for="(card, index) in cards" :key="index" class="mb-4">
            <div class="p-4 bg-white rounded flex justify-between">
                <input v-model="card.item_code" type="text" placeholder="Item Code">
                <Button @click="removecard(index)">Remove</Button>
            </div> 
        </div>
      </div>
  </div>
</template>

<script setup>
import Chart from 'chart.js/auto'
import { ref, watch, onMounted } from 'vue'
import {FormControl, Button} from "frappe-ui"

const fromdate = ref(null)
const todate = ref(null)

const cards = ref([])
const addcard = ()=>{
    cards.value.push({
        item_code: "",
    });
};

const removecard = (index)=>{
    cards.value.splice(index,1)
}

</script>

<style>
.date{
    border-bottom:2px solid white;
    padding-bottom: 10px;
}
</style>
