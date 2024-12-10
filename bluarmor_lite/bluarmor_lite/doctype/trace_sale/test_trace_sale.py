# Copyright (c) 2024, alwin martis and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestTraceSale(FrappeTestCase):
	def test_trace_sales(self):
		test_sales = frappe.get_doc({
			"doctype":"Trace Sale",
			"from_date":"2024/12/01",
			"to_date":"2024/12/07",
			"target_quantity":500
		}).insert()
