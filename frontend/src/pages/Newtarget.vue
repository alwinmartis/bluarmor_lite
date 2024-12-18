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

              <!-- ``<ListView :columns="[
                {label: 'ItemCode',
                    key:'item_code'
                }
              ]"
              :options="{
                selecttable: false,
                showTooltip: false,
                emptyState:{
                    title:'No Item yet'
                },
              }"
              :rows="itemsautocompleteoptions"
              :rowKey="item_code"
              v-model="targetDetails.item"></ListView> -->
            <select v-model="selectedItem">
                <option v-for="item in mappedItems" :key="item.value" :value="item.value">
                    {{ item.label }}
                </option>
            </select>
              <p>{{ selectedItem || 'None'}}</p>
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
import { FormControl,ListView, Button, Dropdown, Autocomplete, createListResource, createResource, ErrorMessage } from 'frappe-ui';
import {reactive, ref, computed, inject, watch, onMounted} from "vue";
import { useRouter } from 'vue-router';
const router = useRouter();

// const selectedItem = ref('');
// const items = ref([])
// const fetchItems = async()=>{
//     try{
//         const itemresource = createListResource({
//         doctype:'Item',
//         fields:['item_code','item_name'],
//         auto:true
//         });

//         itemresource.subscribe((data)=>{
//             items.value = data;
//         })
//     } catch(error){
//         console.error("Error in fetching items")
//     }
//     return {
//         items,
//         selectedItem
//     }
// }
// fetchItems();


//feature added

// let fetch_items = items.fetch()
// console.log(items)
// const value = ref('')
// const itemsautocompleteoptions = computed(()=>{
//     const options = items.data.map((f)=>{
//         return {
//             ...items,
//             label:f.item_name,
//             value:f.item_code
//         }
// })
//     return options
// })

const rawItems = ref([]);
const mappedItems = ref([]);
const selectedItem = ref('');

const fetchAndMapItems = async() =>{
    try{
        const response =await frappe.call({
        method:'frappe.cleint.get_list',
        args:{
            doctype:'Item',
            fields:['item_code','item_name']
            },
        });
        if (response && response.message && Array.isArray(response.message)){
            rawItems.value = response.message;
            mappedItems.value = rawItems.value.map((item)=>({
            label:item.item_name,
            value:item.item_code,
        }))
        }
        else{
            console.log("error in fetching")
        }
    } catch(error){
        console.error("error in fetching item", error)
    } 
}

onMounted(()=>{
    fetchAndMapItems();
    console.log("Items fetching successful")
})

const targetDetails = reactive({
    fdate: null,
    tdate: null,
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
item:selectedItem,
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