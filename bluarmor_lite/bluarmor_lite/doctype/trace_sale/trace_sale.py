# Copyright (c) 2024, alwin martis and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TraceSale(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		completed_quantity: DF.Int
		from_date: DF.Date | None
		target_quantity: DF.Int
		to_date: DF.Date | None
	# end: auto-generated types

	def validate(self):
		pass
