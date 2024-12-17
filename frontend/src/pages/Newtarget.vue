<template>
    <div class="head">
        <p class="head-name">Create Your Targets</p>
    </div>
    <div class="body-data">
        <div class="body-data-in">
            <p class="name">From Date</p>
            <FormControl placeholder="From Date" type="date"></FormControl>
        </div>
        <div class="body-data-in">
            <p class="name">To Date</p>
            <FormControl placeholder="To Date" type="date"></FormControl>
        </div> 
    </div>
    <div class="body-data">
        <div class="body-data-in">
            <p class="name">Item name</p>
            <FormControl placeholder="Item" type="taxt"></FormControl>
        </div>
        <div class="body-data-in">
            <p class="name">Target Quantity</p>
            <FormControl placeholder="Quantity" type="text"></FormControl>
        </div> 
    </div>
    <div class="body-data">
    <div class="save">
        <Button class="button">Save </Button>
    </div>
</div>
    
</template>
<script setup>
import { FormControl, Button } from 'frappe-ui';
</script>

<style scoped>
.body{
    background-color: antiquewhite;
}
.head{
    display:flex;
    justify-content: center;
    margin:25px 10px;
    background-color:azure;
}
.body-data{
display:flex;
justify-content:space-evenly;
background-color:azure;
}
.body-data-in{
display:flex;
flex-direction: column;
justify-content: center;
align-items:center;
margin-bottom:40px
}
.name{
    padding-bottom: 10px;
}
.save{
    display: flex;
    align-items: center;
    justify-content: center;
}
.button{
    background-color: blue;
    color: white;
    width: 90px;
    margin-bottom: 10px
}
.button:hover{
    background-color:orange;
    color: black;
}
.head-name{
    font-weight:500;
    font-size:30px;
}
</style>