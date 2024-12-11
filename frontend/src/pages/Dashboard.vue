<template>
    <div>
        Welcome to Bluarmor App!
    </div>
  </template>

  <script setup>
  import { createListResource } from "frappe-ui";
//   import {sessionUser} from "../data/session";

  const salestarger = createListResource({
    doctype: "Trace Sale",
    fields:["target_quantity","from_date","to_date"],
    auto:true,
    onSuccess(d){
       console.log(d);
  }
  })
</script>