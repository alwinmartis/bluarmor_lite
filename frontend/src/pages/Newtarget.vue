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
            <!-- <Card title="items">
                <ListView :columns="[
                    {label: 'ItemCode',
                        key:'item_code',
                        width:4,
                    },{
                        lable:'ItemName',
                        key:'item_name'
                    }
                ]"
                :options="{
                    selecttable: false,
                    showTooltip: false,
                    resizeColumn:false,
                    emptyState:{
                        title:'No Item yet'
                    },
                }"
                :rows="itemsautocompleteoptions"
                :rowKey="item_code"
                :v-model="targetDetails.item">
            </ListView> -->
    <!-- </Card> -->
            <select v-model="targetDetails.item">
                <option v-for="item in itemsautocompleteoptions" :rows="itemsautocompleteoptions" :key="item.item_code" :value="item.item_code">
                    {{ item.item_code }}
                </option>
            </select>
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


const items = createListResource({
        doctype:'Item',
        fields:['item_code','item_name'],
        filters:[
            ["item_code","Like","FG-%"],
        ],
        auto:true,
        orderby: 'creation desc',
        limit: false
        });
console.log(items.list)

const itemsautocompleteoptions = computed(()=>{
    if (items.list.data){
        return items.list.data.map((item)=>{
            return {
                ...items,
                item_code:item.item_code
            }
        })
    }
    return []
})


// const Items = ref([]);
// // const mappedItems = ref([]);
// const selectedItem = ref('');

// const fetchItems = ()=>{
//     const itemResource = createListResource({
//         doctype:'Item',
//         fields:['item_code','item_name'],
//         auto:true,
//         orderBy:'creation Desc'
//     })
//     const datas = itemResource
//     console.log(datas)
//     console.log("data collected")
//     if (datas){
//         console.log(datas.data)
//         console.log(datas.list)
//         console.log(datas.list.data)
//         Items.value = datas.list.map(item)({
//             label:item.item_name,
//             value:item.item_code
//         })}
//     else{
//         console.log("error in fetching")
//         item.value = []
//     }
// }
// onMounted(()=>{
//     fetchItems();
//     console.log("Items fetching successful")
// })

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
    background-color:aqua;
}
.head{
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin:25px 10px;
    background-color: aqua;
}
.body-data{
display:flex;
justify-content:space-evenly;
background-color:aqua;
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