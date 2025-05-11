# MODULE TICKETS
removed_user = "(removed_user)"
default_create_ticket_message_content = '{"title": "Create a ticket", "description": "If you are experiencing problems or are in need of help, feel free to create a ticket!", "color": 661809, "footer": {"text": "Tickets provided by: Husqy"}}'
default_form_content = """{"title": "New ticket", "rows": [{"paragraph": true, "title": "Reason", "description": "What is the reason for your ticket?", "required": true}]}"""
default_ticket_opened_message = '{"title": "Ticket ID: <ticket_id>", "description": "Thank you for opening a ticket. Our support staff will be with you as soon as possible!", "color": 661809, "footer": {"text": "Tickets provided by: Husqy"}}'
default_ticket_support_engineer_role_name = "Support engineer"
default_ticket_create_category_name = "SUPPORT TICKETS"
default_ticket_create_channel_name = "create-a-ticket"
create_ticket_button_label = "Create a ticket"
form_answers = "Form answers:"
claim_ticket = "Claim ticket (support engineer)"
transfer_ticket = "Transfer ticket (support engineer)"
close_ticket = "Close"
delete_ticket = "Delete"
reopen_ticket = "Re-open"
# Responses
response_ticket_creation_check_failed_no_language = (
    "I could not check for the creation of the ticket because the servers language is not found!"
)
response_ticket_creation_check_failed_no_auto_delete = (
    "I could not check for the creation of the ticket because the servers auto delete is not found!"
)
response_ticket_creation_check_failed_no_timezone = (
    "I could not check for the creation of the ticket because the servers timezone is not found!"
)
response_ticket_creation_check_failed_unable_to_create_thread = (
    "I could not create the ticket because something went wrong with creating the thread!"
)
response_ticket_creation_check_failed_no_open_ticket_categories_configured = (
    "I could not create the ticket because the server has not configured any category channels for new tickets!"
)
response_ticket_creation_check_failed_open_ticket_categories_full = (
    "I could not create the ticket because the configured ticket categories for new tickets are full!"
)
response_ticket_creation_check_failed_sending_message = (
    "I could not create the ticket because something went wrong with sending the start message to the tickets channel!"
)
response_ticket_creation_check_failed = "Something went wrong while creating the ticket!"
response_ticket_creation_check_success = "The ticket has been created!"
response_ticket_creation_check_form_failed_no_form_configuration_found = (
    "I could not show the form because there is not form configuration found!"
)
response_ticket_creation_check_form_failed_invalid_form_config = (
    "I could not show the form because the form configuration is not valid!"
)
response_ticket_creation_check_failed_limit_reached = (
    "The limit of active tickets has been reached! Please wait until a ticket is closed!"
)
response_ticket_creation_check_failed_invalid_member = "The target member for the ticket is not valid!"
response_ticket_creation_check_failed_prevent_data_collection = (
    "I could not create the ticket because you have prevent data collection enabled!"
)
response_ticket_delete_failed_no_language = "I could not delete the ticket because the servers language is not found!"
response_ticket_delete_failed_no_auto_delete = (
    "I could not delete the ticket because the servers auto delete is not found!"
)
response_ticket_delete_failed_no_timezone = "I could not delete the ticket because the servers timezone is not found!"
response_ticket_delete_failed_not_administrator = (
    "I could not delete the ticket because you are not a server adminstrator!"
)
response_ticket_delete_failed = "Something went wrong while deleting the ticket!"
response_ticket_delete_failed_ticket_not_found = "I could not delete the ticket because I could not find the ticket!"
response_ticket_deleted = "I have deleted the ticket!"
response_ticket_claim_failed_no_language = (
    "I could not make you claim  the ticket because the servers language is not found!"
)
response_ticket_claim_failed_no_auto_delete = (
    "I could not make you claim  the ticket because the servers auto delete is not found!"
)
response_ticket_claim_failed_no_timezone = (
    "I could not make you claim  the ticket because the servers timezone is not found!"
)
response_ticket_claim_failed_ticket_not_found = "I could not make you claim the ticket because the ticket is not found!"
response_ticket_claim_failed_panel_not_found = (
    "I could not make you claim the ticket because the ticket panel used to create the ticket is not found!"
)
response_ticket_claim_failed_unknown_claimer = "I could not make you claim the ticket because something went wrong!"
response_ticket_claim_failed_not_support_engineer = (
    "I could not make you claim the ticket because you are not a support engineer!"
)
response_ticket_claim_failed_invalid_member = "The claimer of the ticket can not be {bot_name} or an API Key!"
response_ticket_claim_failed_prevent_data_collection = (
    "I could not make you claim the ticket because you have prevent data collection enabled!"
)
response_ticket_claim_failed = "Something went wrong while claiming the ticket!"
response_ticket_claimed = "You have claimed the ticket and are now the linked support engineer for this ticket!"
response_ticket_claimed_notification = "{member} has claimed the ticket and will be with you shortly!"
response_ticket_transfer_failed_no_language = (
    "I could not transfer the ticket because the servers language is not found!"
)
response_ticket_transfer_failed_no_auto_delete = (
    "I could not transfer the ticket because the servers auto delete is not found!"
)
response_ticket_transfer_failed_no_timezone = (
    "I could not transfer the ticket because the servers timezone is not found!"
)
response_ticket_transfer_failed_ticket_not_found = (
    "I could not transfer the ticket because I could not find the ticket!"
)
response_ticket_transfer_failed_panel_not_found = (
    "I could not transfer the ticket because I could not find the ticket panel used to create the ticket!"
)
response_ticket_transfer_failed_not_current_support_engineer = (
    "I could not transfer the ticket because you are not the current support engineer!"
)
response_ticket_transfer_failed_prevent_data_collection = (
    "I could not transfer the ticket because the new engineer has prevent data collection enabled!"
)
response_ticket_transfer_failed_not_support_engineer = (
    "I could not transfer the ticket because the target member is not a support engineer!"
)
response_ticket_transfer_failed = "Something went wrong while transferring the ticket!"
response_ticket_transferred_notification = "The ticket has been transferred to {member}!"
response_ticket_transferred = "The ticket has been transferred!"
response_ticket_close_failed_no_language = "I could not close the ticket because the servers language is not found!"
response_ticket_close_failed_no_auto_delete = (
    "I could not close the ticket because the servers auto delete is not found!"
)
response_ticket_close_failed_no_timezone = "I could not close the ticket because the servers timezone is not found!"
response_ticket_close_failed_ticket_not_found = "I could not close the ticket because I could not find the ticket!"
response_ticket_close_failed_panel_not_found = (
    "I could not close the ticket because I could not find the ticket panel used to create the ticket!"
)
response_ticket_close_failed_not_current_support_engineer = (
    "I could not close the ticket because you are not the current support engineer!"
)
response_ticket_close_failed = "Something went wrong while closing the ticket!"
response_ticket_closed_notification = "The ticket has been closed by {member}! If you wish to interact with this ticket, please use the provided `/tickets` commands."
response_ticket_close_failed_no_closed_ticket_categories = (
    "The ticket has been closed but could not be moved because there are no categories available for closed tickets!"
)
response_ticket_closed = "The ticket has been closed!"
response_ticket_reopen_failed_no_language = "I could not reopen the ticket because the servers language is not found!"
response_ticket_reopen_failed_no_auto_delete = (
    "I could not reopen the ticket because the servers timezone is not found!"
)
response_ticket_reopen_failed_no_timezone = "I could not reopen the ticket because the servers timezone is not found!"
response_ticket_reopen_failed_ticket_not_found = "I could not reopen the ticket because the ticket is not found!"
response_ticket_reopen_failed_panel_not_found = (
    "I could not reopen the ticket because the panel used to create the ticket is not found!"
)
response_ticket_reopen_failed_not_current_support_engineer = (
    "I could not reopen the ticket because you are not the current support engineer for the ticket!"
)
response_ticket_reopen_failed = "Something went wrong while reopening the ticket!"
response_ticket_reopen_notification = "The ticket has been reopened by {member}!"
response_ticket_reopen_failed_no_open_ticket_categories = (
    "The ticket has been reopened but could not be moved because there are no categories available for open tickets!"
)
response_ticket_reopened = "The ticket has been reopened!"
response_ticket_transcribed = "The ticket has been transcribed and it has been sent to your DM."
response_ticket_transcribe_failed = "Something went wrong while transcribing the ticket!"
response_ticket_transcribe_failed_not_allowed = "The ticket can not be transcribed. Only the ticket creator or the current support engineer can transcribe the ticket."
