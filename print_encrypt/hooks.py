app_name = "print_encrypt"
app_title = "Print Encrypt"
app_publisher = "Ganu Reddy"
app_description = "Print Encrypt"
app_email = "ganureddy54@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/print_encrypt/css/print_encrypt.css"
# app_include_js = "/assets/print_encrypt/js/print_encrypt.js"

# include js, css files in header of web template
# web_include_css = "/assets/print_encrypt/css/print_encrypt.css"
# web_include_js = "/assets/print_encrypt/js/print_encrypt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "print_encrypt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "print_encrypt/public/icons.svg"

# Home Pages
# ----------

fixtures = [
    {
        "dt":
            "Custom Field",
            "filters":[[
                "name",
                "in",
                {
                    "Notification-custom_column_break_orxgw",
                    "Notification-custom_encrypt_print",
                    "Notification-custom_password_policy"        
                },
                
            ]]
    }
]

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "print_encrypt.utils.jinja_methods",
# 	"filters": "print_encrypt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "print_encrypt.install.before_install"
# after_install = "print_encrypt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "print_encrypt.uninstall.before_uninstall"
# after_uninstall = "print_encrypt.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "print_encrypt.utils.before_app_install"
# after_app_install = "print_encrypt.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "print_encrypt.utils.before_app_uninstall"
# after_app_uninstall = "print_encrypt.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "print_encrypt.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "Notification": "print_encrypt.print_encrypt.print_encrypt.Notification"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"print_encrypt.tasks.all"
# 	],
# 	"daily": [
# 		"print_encrypt.tasks.daily"
# 	],
# 	"hourly": [
# 		"print_encrypt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"print_encrypt.tasks.weekly"
# 	],
# 	"monthly": [
# 		"print_encrypt.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "print_encrypt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.email.doctype.notification.get_attachment" : "print_encrypt.print_encrypt.get_attachment_encrypt_print"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "print_encrypt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["print_encrypt.utils.before_request"]
# after_request = ["print_encrypt.utils.after_request"]

# Job Events
# ----------
# before_job = ["print_encrypt.utils.before_job"]
# after_job = ["print_encrypt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"print_encrypt.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

