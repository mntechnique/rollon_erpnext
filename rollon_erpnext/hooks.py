# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from .hooks_property_setter import property_setter 
from .hooks_custom_field import custom_field

app_name = "rollon_erpnext"
app_title = "Rollon ERPNext"
app_publisher = "MN Technique"
app_description = "ERPNext customisation for Rollon Hydraulics"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@mntechnique.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rollon_erpnext/css/rollon_erpnext.css"
# app_include_js = "/assets/rollon_erpnext/js/rollon_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/rollon_erpnext/css/rollon_erpnext.css"
# web_include_js = "/assets/rollon_erpnext/js/rollon_erpnext.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rollon_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rollon_erpnext.install.before_install"
# after_install = "rollon_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rollon_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rollon_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"rollon_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"rollon_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rollon_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rollon_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rollon_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rollon_erpnext.event.get_events"
# }

fixtures = [
	property_setter,
	custom_field
]