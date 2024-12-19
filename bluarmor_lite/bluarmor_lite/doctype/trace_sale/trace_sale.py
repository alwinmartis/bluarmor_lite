# Copyright (c) 2024, alwin martis and contributors
# For license information, please see license.txt

import frappe # type: ignore
from frappe.model.document import Document # type: ignore
from frappe.utils import flt # type: ignore

class TraceSale(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		completed_quantity: DF.Int
		from_date: DF.Date
		item: DF.Link
		pending_quantity: DF.Int
		target_quantity: DF.Int
		to_date: DF.Date
	# end: auto-generated types

	# def onload(self):
	# 	self.pending_quantity = self.target_quantity - self.completed_quantity
	# 	print(self.pending_quantity)

	def calculate_qty(self):
		print("server")
		if not self.from_date or not self.to_date or not self.item:
			frappe.throw("Please validate the data!")

		completed_qty = frappe.db.sql("""
				SELECT sum(`dni`.qty) AS `qty`
					FROM `tabDelivery Note Item` As `dni`
					Inner Join `tabDelivery Note` As `dn`
						On `dni`.parent = `dn`.name
					WHERE `dni`.item_code = %s
					AND `dn`.posting_date Between %s AND %s
			""",(self.item, self.from_date, self.to_date))[0][0] or 0
		
		self.completed_quantity=completed_qty
		self.pending_quantity = self.target_quantity - completed_qty

		self.save()
		return{
			"completed_qty":self.completed_quantity,
			"pending_qty":self.pending_quantity,
			"item":self.item
		}
@frappe.whitelist()
def calculate_qty(doc_name):
	print("Hello")
	doc = frappe.get_doc("Trace Sale",doc_name)
	return doc.calculate_qty()

