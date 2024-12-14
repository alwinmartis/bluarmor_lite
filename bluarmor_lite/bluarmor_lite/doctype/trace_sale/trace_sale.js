// Copyright (c) 2024, alwin martis and contributors
// For license information, please see license.txt

frappe.ui.form.on("Trace Sale", {
	refresh:function(frm){
        console.log("In")
        if(frm.doc.from_date && frm.doc.to_date && frm.doc.item){
            console.log("inside")
            frappe.call({
                method:"bluarmor_lite.bluarmor_lite.doctype.trace_sale.trace_sale.calculate_qty",
                args:{
                    doc_name:frm.doc.name
                },
                callback:function(r){
                    console.log(r)
                    if(r.message){
                        frm.set_value("completed_quantity",r.message.completed_qty);
                        frm.set_value("pending_quantity",r.message.pending_qty);
                        console.log(r.item)
                    }
                }
            })
        }
    }

})
