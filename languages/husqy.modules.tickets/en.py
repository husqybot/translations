# MODULE TICKETS
# Enable
module_tickets_support_type_general = "🛠️ General Support"
module_tickets_support_type_account = "📩 Account support"
module_tickets_support_type_sales = "💵 Sales/billing support"
module_tickets_support_type_hardware = "💻 Hardware support"
module_tickets_support_type_product = "📦 Product Availability support"
module_tickets_support_type_bug = "🐛 Bug support"
module_tickets_support_type_fr = "💡 Feature request"
module_tickets_support_type_fi = "💡 Feature improvement"
module_tickets_default_types = {
    "general_support": module_tickets_support_type_general,
    "account_support": module_tickets_support_type_account,
    "sales_billing_support": module_tickets_support_type_sales,
    "hardware_support": module_tickets_support_type_hardware,
    "product_availability_support": module_tickets_support_type_product,
    "bug_support": module_tickets_support_type_bug,
    "feature_request": module_tickets_support_type_fr,
    "feature_improvement": module_tickets_support_type_fi,
}
module_tickets_role_used_for_ticket_module = "This role will be used for the `tickets` module, please DO NOT remove this role from the server without reconfiguring the `tickets` module!"
module_tickets_channel_used_for_ticket_module = "This channel will be used for the `tickets` module, please DO NOT remove this channel from the server without reconfiguring the `tickets` module!"
module_tickets_default_ticket_category = "{bot_name} Tickets"
module_tickets_create_a_ticket = "create-a-ticket"
module_tickets_view_tickets = "view-tickets"
module_tickets_default_modal = """{'custom_id': '260666db-aa41-422d-b7ae-4b906cd35054', 'title': 'New ticket', 'components': ["{'type': 1, 'components': [{'type': 4, 'style': 1, 'custom_id': 'bf835028-1c56-4537-b4d2-bfa667135d19', 'label': 'Ticket title', 'placeholder': 'Please insert the title of your ticket'}]}", "{'type': 1, 'components': [{'type': 4, 'style': 2, 'custom_id': '78f400da-f670-411e-9658-9b109a46cbbc', 'label': 'Ticket description', 'placeholder': 'Please describe why you are submitting this ticket'}]}"]}"""
module_tickets_default_ticket_creation_message = """{"title": "Create a ticket", "description": "If you are experiencing problems or are in need of help, feel free to create a ticket!", "footer": {"text": "Tickets made possible by: Husqy"}}"""
module_tickets_please_select_default_type_to_create = "Please select a default type to create a ticket"
module_tickets_please_select_custom_type_to_create = "Please select a custom type to create a ticket"
response_ticket_created = "your ticket has been created!"
response_ticket_created_support = "would you mind looking at this?"
module_tickets_new_ticket_embed_title = "New Ticket!"
module_tickets_new_ticket_embed_description = "{user} created a new ticket!\n Ticket type: {ticket_type}"
module_tickets_new_ticket_embed_footer = "Ticket ID: {ticket_id} | Tickets provided by: {bot_name}"
