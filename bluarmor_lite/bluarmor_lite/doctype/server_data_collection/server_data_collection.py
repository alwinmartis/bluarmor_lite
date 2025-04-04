# Copyright (c) 2024, alwin martis and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServerDataCollection(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Datetime | None
		device_id: DF.Data | None
		employee: DF.Link | None
		status: DF.Data | None
	# end: auto-generated types
	
	def push_api_data(device_id, employee, date, status):
		# try:
		# 	if not all([device_id, employee, date, status]):
		# 		frappe.throw("missing required fields")
		pass