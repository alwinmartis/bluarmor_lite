<template>
    <div>
        Welcome to Bluarmor App!
        <div class="flex items-center justify-between" v-for ="target in salestarget.data" :key="target">
          {{ target.name }}{{ target.target_quantity }}{{ target.from_date }} {{ target.to_date }}<br>
        </div>

        <button variant="solid"theme="blue">Add</button>
    </div>
  </template>

  <script setup>
  import { computed } from "vue";
  import { createListResource } from "frappe-ui";
  import {sessionUser} from "../data/session";

  let salestarget = createListResource({
    doctype: 'Trace Sale',
    fields:['name','target_quantity','from_date','to_date'],
    orderBy:'creation Desc',
    onSuccess(s){
      console.log(s)
    }
  })
  salestarget.fetch()

</script>