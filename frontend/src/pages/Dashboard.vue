<template>
  <div class="header">
    <div class="head">Welcome to Bluarmor App !</div>
    <Button class="edit" route="/add-target">Insert</Button>
  </div>
  
  <div>
    <div
      class="flex items-center justify-between content"
      v-for="target in salestarget.data"
      :key="target"
    >
      <div class="circle">
        <CircularProgressBar
          :step="1"
          :totalsteps="20"
          :showPercentage="true"
        ></CircularProgressBar>
      </div>
      {{ target.name }}<span>  </span> {{target.item}} <span>  </span>{{ target.target_quantity }} <span>  </span> {{ target.completed_quantity }}<span></span>{{ target.pending_quantity }}
      <div>
        <Button class = 'edit' @click="console.log('Clicked')" route="/new-target">Edit</Button>
      </div>
      <br />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { createListResource, Button, CircularProgressBar } from 'frappe-ui'
import { sessionUser } from '../data/session'

let salestarget = createListResource({
  doctype: 'Trace Sale',
  fields: ['name', 'target_quantity', 'from_date', 'to_date', 'completed_quantity', 'item', 'pending_quantity'],
  orderBy: 'creation Desc',
  onSuccess(s) {
    console.log(s)
  },
})
salestarget.fetch()
</script>

<style scoped>
.head{
  padding:10px 2px;
  font-size:25px;
  font-weight: 500;
  margin-left: 10px;
}

.content{
  padding:10px 2px;
  display:flex;
  justify-content: space-between;
  margin-left:10px;
  background-color: beige;
  margin-bottom: 2px;
}

.circle{
  margin-left: 10px;
}

.edit{
  background-color: orange;
  color:aliceblue;
  width:60px;
}

.edit:hover{
  background-color: chartreuse;
  color: white;
}

.header{
  display:flex;
  justify-content:space-between;
  align-items: center;
}

</style>
