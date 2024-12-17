<template>
    <div class="head">
        <p class="head-name">Create Your Targets</p>
        <ErrorMessage :message="salesListResource.insert.error" />
    </div>
    <div class="body-data">
        
        <div class="body-data-in">
            <p class="name" >From Date</p>
            <FormControl v-model="targetDetails.fdate" placeholder="From Date" type="date" lable="fdate"></FormControl>
        </div>
        <div class="body-data-in">
            <p class="name">To Date</p>
            <FormControl v-model="targetDetails.tdate" placeholder="To Date" type="date" lable="tdate"></FormControl>
        </div> 
    </div>
    <div class="body-data">
        <div class="body-data-in">
            <p class="name">Item name</p>
            <!-- <FormControl v-model="targetDetails.item" placeholder="Item" type="taxt" lable="item"></FormControl> -->
             <Autocomplete v-model="targetDetails.item" :options="itemsautocompleteoptions" :multiple="true"></Autocomplete>
        </div>
        <div class="body-data-in">
            <p class="name">Target Quantity</p>
            <FormControl v-model="targetDetails.tqty" placeholder="Quantity" type="text" lable="tqty"></FormControl>
        </div> 
    </div>
    <div class="body-data">
    <div class="save">
        <Button :loading="salesListResource.insert.loading" class="button" @click="savetarget">Save </Button>
    </div>
</div>
    
</template>


<script setup>
import { FormControl, Button, Dropdown, Autocomplete, createListResource, createResource, ErrorMessage } from 'frappe-ui';
import {reactive, ref, computed, inject, watch} from "vue";
import { useRouter } from 'vue-router';
const router = useRouter();

let items = createListResource({
    doctype:'Item',
    fields:['item_code','item_name'],
    onSuccess(s){
        console.log(s)
    }
})
//feature added

let fetch_items = items.fetch()
console.log(fetch_items)
const itemsautocompleteoptions = computed(()=>{
    const options = fetch_items.map((f)=>({
        lable: f.item_name,
        value:f.item_code
    }))
    return options
})

const targetDetails = reactive({
    fdate: null,
    tdate: null,
    item: '',
    tqty: 0.0,
})

const salesListResource = createListResource({
    doctype:"Trace Sale",
})


function savetarget(){
    salesListResource.insert.submit({
        ...targetDetails,
    from_date:targetDetails.fdate,
to_date:targetDetails.tdate,
item:targetDetails.item,
target_quantity:targetDetails.tqty
})
,{
    onSuccess(){
        router.replace({name:"Dashboard"})
    }
}
}
</script>


<style scoped>
.body{
    background-color: antiquewhite;
}
.head{
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
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