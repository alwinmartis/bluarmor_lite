<template>
    <div class="head">
        <p>New Target</p>
        <Button>Save</Button>  
    </div>
    <div>
        <FormControl placeholeder="From Date" type="Date"></FormControl>
        <FormControl placeholeder="To Date" type="Date"></FormControl>
    </div>
</template>
<script setup>
import {Button, FormControl} from "frappe-ui"
</script>

<style scoped>
.head{
    display: flex;
    flex-direction: row;
    justify-content: space-between
}
</style>