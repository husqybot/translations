# ------------------------------------------------------------------------- #
# GLOBAL VARIABLES #
# ------------------------------------------------------------------------- #
# Footer
embed_footer = "Info requested by: {member}! This embed will show for {auto_delete} seconds!"
# Other
add = "Add"
remove = "Remove"
unknown = "Unknown"
no_nickname = "No nickname"
no_timeout_for_user = "Not timed-out"
deafend = "Deafend"
not_deafend = "Not deafend"
muted = "Muted"
not_muted = "Not muted"
pending = "Pending"
not_pending = "Not pending"
yes = "Yes"
no = "No"
enabled = "Enabled"
disabled = "Disabled"
continue_message = "Continue"
cancel_message = "Cancel"
not_in_use = "Not in use!"
no_reason_specified = "*No reason specified!*"
no_url = "No URL available"
no_author = "No author available"
back = "Back"
website = "Website"
documentation = "Documentation"
support_server = "Support Server"
dashboard = "Dashboard"

# ------------------------------------------------------------------------- #
# GENERAL #
# ------------------------------------------------------------------------- #
response_db_user_not_found = "Something went wrong while getting your user information! Please try again later."

# ------------------------------------------------------------------------- #
# UTILS QR GENERATE #
# ------------------------------------------------------------------------- #
qr_generate_response_component_title_info = "### Your QR-code"
response_time_converted_success = (
    "{days} days, {hours} hours, {minutes} minutes and {seconds} seconds totals to `{total_seconds}` seconds!"
)

# ------------------------------------------------------------------------- #
# UTILS CUSTOM EMBED SEND #
# ------------------------------------------------------------------------- #
response_custom_embed_send_success = "The embed has been send to {channel}!"
response_custom_embed_send_failed = "Something went wrong while sending the embed to {channel}!"

# ------------------------------------------------------------------------- #
# UTILS CUSTOM MODAL CREATE/PREVIEW #
# ------------------------------------------------------------------------- #
custom_modal_change_title = "Change modal title"
custom_modal_edit_text_field = "Edit modal text field"
custom_modal_add_text_field = "Add modal text field"
custom_modal_remove_text_field_1 = "First text field"
custom_modal_remove_text_field_2 = "Second text field"
custom_modal_remove_text_field_3 = "Third text field"
custom_modal_remove_text_field_4 = "Fourth text field"
custom_modal_remove_text_field_5 = "Fifth text field"
custom_modal_remove_text_field = "Remove text field"
custom_modal_reset = "Reset modal"
custom_modal_finish = "Finish modal"
custom_modal_preview = "Preview modal"
custom_modal_create_this_can_be_safely_removed = (
    "<NOTE: Everything inside the (double) quotation marks can be safely removed! The trailing , too>"
)
custom_modal_change_title_new_title = "title"
custom_modal_add_text_field_text_field_title = "Field title"
custom_modal_add_text_field_text_field_description = "Field description"
custom_modal_add_text_field_text_field_type = "Field type (Long/Short)"
custom_modal_add_text_field_text_field_required = "Required (True/False)"
custom_modal_add_text_field_title = "Text field"
# Responses
response_custom_modal_finished = (
    "The custom modal creation is finished, the JSON of your modal is: \n```{modal_json}```"
)
response_custom_modal_preview = "By pressing Continue I will show the preview of the custom modal! This modal can be interacted with but no data will be saved!"
response_custom_modal_preview_failed = "The custom modal preview reached a timeout!"
response_custom_modal_preview_failed_canceled = "The custom modal preview was canceled!"
response_custom_modal_preview_success = "Custom modal has been previewed!"
# Embeds
custom_modal_default_embed_title = "Custom modal creation"
custom_modal_embed_description = "Welcome to the custom modal creation. Using the buttons below, you can configure the modal and preview it. When finished, select Finish to retrieve the JSON.\n **When previewing the modal, press cancel or fill in the form and press submit to continue modal creation!**"

# ------------------------------------------------------------------------- #
# INFO #
# ------------------------------------------------------------------------- #
info_response_channel_not_found = "The channel with that ID is not found!"
info_response_channel_unknown = "Unknown channel!"
info_response_component_title_info = "Info"
info_response_component_title_general_channel_info = "General info"
info_response_component_title_general_channel_id = "ID"
info_response_component_title_general_channel_name = "Name"
info_response_component_title_general_channel_created_at = "Created at"
info_response_component_title_general_channel_type = "Type"
info_response_component_title_specific_channel_info = "Specific info"
info_response_component_title_specific_channel_nsfw = "NSFW"
info_response_component_title_specific_channel_last_message = "Last message"
info_response_component_title_specific_channel_parent_id = "Parent"
info_response_component_description_no_parent = "No parent"
info_response_component_title_specific_channel_last_thread_id = "Last thread"
info_response_component_description_specific_channel_no_last_thread_id = "No last thread"
info_response_component_title_specific_channel_last_pin_timestamp = "Last pin timestamp"
info_response_component_title_specific_channel_position = "Position"
info_response_component_title_specific_channel_topic = "Topic"
info_response_component_title_specific_channel_default_auto_archive_duration = "Default auto archive duration"
info_response_component_title_specific_channel_rate_limit_per_user = "Rate limit (per user)"
info_response_component_title_specific_channel_available_tags = "Available tags"
info_response_component_title_specific_channel_default_layout = "Default layout"
info_response_component_description_specific_channel_default_layouts = {
    "NOT_SET": "Not set",
    "LIST_VIEW": "List view",
    "GALLERY_VIEW": "Gallery view",
}
info_response_component_title_specific_channel_default_reaction_emoji = "Default reaction emoji (or emoji ID)"
info_response_component_description_specific_channel_no_default_reaction_emoji = "No default reaction emoji"
info_response_component_title_specific_channel_default_sort_order = "Default sort order"
info_response_component_description_specific_channel_default_sort_orders = {
    "LATEST_ACTIVITY": "Latest activity",
    "CREATION_DATE": "Creation date",
}
info_response_component_title_specific_channel_default_thread_rate_limit_per_user = "Threat rate limit (per user)"
info_response_component_title_specific_channel_bitrate = "Bitrate"
info_response_component_title_specific_channel_region = "Region"
info_response_component_description_specific_channel_region_auto = "Region automatically determined"
info_response_component_title_specific_channel_user_limit = "User limit"
info_response_component_description_specific_channel_no_user_limit = "No limit set"
info_response_component_title_specific_channel_video_quality_mode = "Video quality mode"
info_response_component_description_specific_channel_video_quality_modes = {"AUTO": "Auto", "FULL": "720p"}
info_response_component_title_specific_channel_approximate_member_count = "Member count (aprox.)"
info_response_component_title_specific_channel_approximate_message_count = "Message count (aprox.)"
info_response_component_title_specific_channel_archive_timestamp = "Archive timestamp"
info_response_component_title_specific_channel_auto_archive_duration = "Auto archive duration"
info_response_component_title_specific_channel_is_archived = "Archived"
info_response_component_title_specific_channel_is_locked = "Locked"
info_response_component_title_specific_channel_owner_id = "Owner"
info_response_component_title_specific_channel_thread_created_at = "Thread created at"
info_response_component_description_specific_channel_thread_created_at_unknown = "Unknown"
info_response_role_not_found = "The role with that ID is not found!"
info_response_component_title_general_role_info = "General info"
info_response_component_title_general_role_id = "ID"
info_response_component_title_general_role_name = "Name"
info_response_component_title_general_role_created_at = "Created at"
info_response_component_title_general_role_color = "Color"
info_response_component_title_general_role_position = "Position"
info_response_component_title_general_role_unicode_emoji = "Emoji"
info_response_component_title_general_role_is_guild_linked_role = "Linked role"
info_response_component_title_general_role_is_hoisted = "Hoisted"
info_response_component_title_management_role_info = "Management info"
info_response_component_title_general_role_is_managed = "Managed by integration or application"
info_response_component_title_general_role_bot_id = "Bot"
info_response_component_description_general_role_no_bot_id = "Not managed by an integration or application"
info_response_component_title_general_role_integration_id = "Integration ID"
info_response_component_title_general_role_is_mentionable = "Mentionable"
info_response_component_title_general_role_is_premium_subscriber_role = "Premium subscriber role"
info_response_component_title_monetization_role_info = "Monetization info"
info_response_component_title_general_role_is_available_for_purchase = "Available for purchase"
info_response_component_title_general_role_subscription_listing_id = "Subscription SKU ID"
info_response_component_description_general_role_no_subscription_listing_id = "Not available for purchase"
info_response_guild_not_found = "The server is not found!"
info_response_component_title_general_guild_info = "General info"
info_response_component_title_general_guild_id = "ID"
info_response_component_title_general_guild_name = "Name"
info_response_component_title_general_guild_created_at = "Created at"
info_response_component_title_general_guild_owner_id = "Onwer"
info_response_component_title_general_guild_description = "Description"
info_response_component_description_general_guild_no_description = "No description"
info_response_component_title_general_guild_preferred_locale = "Preferred locale"
info_response_component_title_general_guild_vanity_url = "Vanity URL code"
info_response_component_description_general_guild_no_vanity_url = "No vanity URL code"
info_response_component_title_general_guild_max_video_channel_users = "Max video channel users"
info_response_component_title_general_guild_nsfw_level = "NSFW Level"
info_response_component_description_general_guild_nsfw_levels = {
    "DEFAULT": "Default",
    "EXPLICIT": "Explicit",
    "SAFE": "Safe",
    "AGE_RESTRICTED": "Age restricted",
}
info_response_component_title_general_guild_afk_timeout = "AFK timeout"
info_response_component_title_general_guild_afk_channel = "AFK channel"
info_response_component_description_general_guild_no_afk_channel = "No AFK channel"
info_response_component_title_general_invites_disabled = "Invites disabled"
info_response_component_title_general_default_message_notifications = "Default message notifications"
info_response_component_description_general_default_message_notifications = {
    "ALL_MESSAGES": "All messages",
    "ONLY_MENTIONS": "Notify only users when mentioned",
}
info_response_component_title_general_explicit_content_filter = "Explicit content filter"
info_response_component_description_general_explicit_content_filters = {
    "DISABLED": "No explicit content filter",
    "MEMBERS_WITHOUT_ROLES": "Filter all content from members without a role",
    "ALL_MEMBERS": "Filter all content",
}
info_response_component_title_security_guild_info = "Security info"
info_response_component_title_security_guild_mfa_level = "MFA level"
info_response_component_description_security_guild_mfa_levels = {"NONE": "No MFA required", "ELEVATED": "MFA required"}
info_response_component_title_security_guild_verification_level = "Verification level"
info_response_component_description_security_guild_verification_levels = {
    "NONE": "Unrestricted",
    "LOW": "Verifier email required",
    "MEDIUM": "Must be registered on Discord for more than 5 minutes",
    "HIGH": "Must be registered on Discord for more than 10 minutes",
    "VERY_HIGH": "Verifier phone number required",
}
info_response_component_title_system_channel_guild_info = "System channel info"
info_response_component_title_general_guild_public_updates_channel_id = "Public updates channel"
info_response_component_title_description_guild_no_public_updates_channel_id = "No public updates channel"
info_response_component_title_general_guild_rules_channel_id = "Rules channel"
info_response_component_title_description_guild_no_rules_channel_id = "No rules channel"
info_response_component_title_general_guild_system_channel_id = "System channel"
info_response_component_title_description_guild_no_system_channel_id = "No system channel"
info_response_component_title_general_guild_is_widget_enabled = "Widget enabled"
info_response_component_title_general_guild_widget_channel_id = "Widget channel"
info_response_component_title_description_guild_no_widget_channel_id = "No system channel"
info_response_component_title_premium_guild_info = "Premium info"
info_response_component_title_premium_guild_subscription_count = "Boosts"
info_response_component_title_premium_guild_premium_tier = "Premium tier"
info_response_component_description_premium_guild_premium_tiers = {
    "NONE": "No premium tier",
    "TIER_2": "Tier 2 nitro",
    "TIER_1": "Tier 1 nitro",
    "TIER_3": "Tier 3 nitro",
}
info_response_component_title_features_guild_info = "Features"
info_response_component_title_features_guild_features = {
    "ANIMATED_ICON": "Able to set an animated guild icon",
    "BANNER": "Able to set a server banner image",
    "COMMERCE": "Able to use commerce features",
    "COMMUNITY": "Community features enabled",
    "DISCOVERABLE": "Disoverable in directory",
    "FEATURABLE": "Able to be featured in directory",
    "INVITE_SPLASH": "Able to set an invite splash background",
    "MORE_EMOJI": "Can host more custom emojis than normal",
    "NEWS": "Able to create news channels",
    "PARTNERED": "Partnered",
    "RELAY_ENABLED": "Using relays",
    "VANITY_URL": "Able to set a vanity URL",
    "VERIFIED": "Verified",
    "VIP_REGIONS": "VIP regions (384kbps bitrate)",
    "WELCOME_SCREEN_ENABLED": "Welcome screens enabled",
    "MEMBER_VERIFICATION_GATE_ENABLED": "Memberschip screening enabled",
    "PREVIEW_ENABLED": "Server can be viewed before screening is completed",
    "TICKETED_EVENTS_ENABLED": "Ticketed events enabled",
    "MONETIZATION_ENABLED": "Monetization enabled",
    "MORE_STICKERS": "Can have more custom stickers",
    "CREATOR_MONETIZABLE": "Monetization enabled",
    "CREATOR_STORE_PAGE": "Store page enabled",
    "ROLE_SUBSCRIPTIONS_ENABLED": "Role subscriptions enabled",
    "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE": "Role subscriptions available for purchase",
    "INVITES_DISABLED": "Invites paused, no users can join",
    "RAID_ALERTS_DISABLED": "Raid alerts disabled",
    "BYPASS_SLOWMODE_PERMISSION_MIGRATION_COMPLETE": "Bypass slowmode permissions migration completed",
    "PIN_PERMISSION_MIGRATION_COMPLETE": "Pin permissions migration completed",
    "NONE": "Unknown",
}
info_response_component_title_icon_guild_info = "Server icon"
info_response_user_not_found = "The user with that ID is not found!"
info_response_component_title_general_user_info = "General info"
info_response_component_title_general_user_id = "ID"
info_response_component_title_general_user_global_name = "Global name"
info_response_component_title_general_user_name = "Username"
info_response_component_title_general_user_created_at = "Created at"
info_response_component_title_general_user_accent_color = "Accent color"
info_response_component_title_general_user_flags = "Flags"
info_response_component_title_general_user_is_bot = "Bot"
info_response_component_title_general_user_is_system = "System"
info_response_component_title_general_user_primary_guild = "Primary server ID"
info_response_component_description_general_user_no_primary_guild = "No primary server"
info_response_component_title_member_user_info = "Member info"
info_response_component_title_member_user_joined_at = "Joined at"
info_response_component_description_member_user_no_joined_at = "Unknown join date"
info_response_component_title_member_user_premium_since = "Boosted server since"
info_response_component_description_member_user_no_premium_since = "Has not boosted server"
info_response_component_title_member_user_nickname = "Nickname"
info_response_component_description_member_user_no_nickname = "No nickname"
info_response_component_title_member_user_is_deaf = "Deafend"
info_response_component_title_member_user_is_mute = "Muted"
info_response_component_title_member_user_is_pending = "Pending"
info_response_component_title_member_user_communication_disabled_until = "Communication disabled until"
info_response_component_description_member_user_no_communication_disabled_until = "Communication not disabled"
info_response_component_title_member_user_roles = "Roles"
info_response_component_title_avatar_user_info = "User avatar"
info_response_ping = "Pong! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
info_response_component_title_general_bot_info = "General info"
info_response_component_title_bot_language = "Language"
info_response_component_title_bot_timezone = "Timezone"
info_response_component_title_bot_unit_system = "Unit system"
info_response_component_title_bot_auto_delete = "Auto delete"
info_response_component_description_bot_auto_delete_seconds = "seconds"
info_response_component_title_enabled_modules_bot_info = "Enabled modules"
info_response_component_description_no_enabled_modules_bot_info = "No modules enabled"
info_response_component_title_disabled_modules_bot_info = "Disabled modules"
info_response_component_description_no_disabled_modules_bot_info = "No modules disabled"
module_logging = "Logging module"
module_welcoming = "Welcoming module"
module_tempchannels = "Tempchannels module"
module_socials = "Socials module"
module_reactionroles = "Reactionroles module"
module_autoresponder = "Autoresponder module"
module_tickets = "Tickets module"
module_ticket_view_types = "View ticket types"
module_ticket_view_generals_settings = "View settings"
module_serverstats = "Serverstats module"
module_tags = "Tags module"
module_verifier = "Verifier module"
module_rules = "Rules module"
module_invite_tracker = "Invite tracker module"
module_polls = "Polls module"
module_reminders = "Reminders module"
module_giveaways = "Giveaways module"

# ------------------------------------------------------------------------- #
# HELP #
# ------------------------------------------------------------------------- #
help_response_title_documentation = "Documentation"
help_response_description_documentation = "The Husqy documentation is the best place to start. It explains all features and possibilities of Husqy. There is also a FAQ page which maybe can answer the questions you have."
help_response_button_title_documentation = "Documentation"
help_response_button_title_faq = "FAQ"
help_response_title_dashboard = "Dashboard"
help_response_description_dashboard = "The dashboard is the quick all in one tool to configure Husqy for the server, click the link below to go to the dashboard."
help_response_button_title_dashboard = "Dashboard"
help_response_title_still_need_help = "Still need help?"
help_response_description_still_need_help = "If you are still in need of support, please follow one of the links below and contact us! We would like to help you!"
help_response_button_title_still_need_help = "Official Husqy Support Server"

# ------------------------------------------------------------------------- #
# MEME #
# ------------------------------------------------------------------------- #
response_meme_getting_meme = "I am getting your meme, please wait!"
response_meme_request_failed = (
    "Something went wrong while sending the request to the socials service! Please try again later."
)

# ------------------------------------------------------------------------- #
# GAMES #
# ------------------------------------------------------------------------- #
response_games_heads_or_tails_heads = "It's `heads`!"
response_games_heads_or_tails_tails = "It's `tails`!"
higher_lower_higher = "Higher"
higher_lower_equal = "Equal"
higher_lower_lower = "Lower"
rps_rock = "Rock"
rps_paper = "Paper"
rps_scissors = "Scissors"
higher_lower_response_component_text = "### Higher/lower\nHello {member}! I have picked a number between 0 and 100! Do you think this number is higher, lower or equal to `{hint_number}`?"
higher_lower_response_component_won_text = "### Higher/lower\nCongratulations {member}! You are **correct**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
higher_lower_response_component_loss_text = "### Higher/lower\nToo bad {member}! You are **wrong**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
rps_response_component_text = "### Rock, Paper, Scissors game\n\n{user_one} is choosing...\n{user_two} is waiting..."
rps_response_component_winner_text = "Congratulations {user}! You won the Rock, Paper, Scissors game!"

# ------------------------------------------------------------------------- #
# TICKETS #
# ------------------------------------------------------------------------- #
response_module_tickets_request_failed = (
    "Something went wrong while sending the request to the tickets service! Please try again later."
)
response_module_tickets_transfer_select_new_support_engineer = "Please select the support engineer for this ticket!"

# ------------------------------------------------------------------------- #
# RULES #
# ------------------------------------------------------------------------- #
response_module_rules_request_failed = (
    "Something went wrong while sending the request to the rules service! Please try again later."
)
response_module_rules_no_rules_found = "There are no rules based on your selection."
response_module_rules_invalid_rule_id = "There is no valid rule ID given."
info_module_rules_button_settings = "Settings"
info_module_rules_button_rules = "Rules"
info_module_rules_response_component_title_settings = "Rules module info"
info_module_rules_response_component_description_settings_rules_channel = "Rules channel"
info_module_rules_response_component_description_settings_no_rules_channel = "No rules channels configured"
info_module_rules_response_component_description_settings_rules_message = "Rules message"
info_module_rules_response_component_description_settings_rules_actions_enabled = "Actions enabled"
info_module_rules_response_component_description_settings_rules_denied_action = "Denied action"
info_module_rules_response_component_description_settings_rules_accepted_role_ids = "Accepted roles"
info_module_rules_response_component_description_settings_rules_denied_role_ids = "Denied roles"
info_module_rules_response_component_description_settings_rules_no_accepted_role_ids = "No accepted role IDs configured"
info_module_rules_response_component_description_settings_rules_no_denied_role_ids = "No denied role IDs configured"
info_module_rules_response_component_title_rules = "Rule"
info_module_rules_response_component_description_rules_rule_text = "Text"
info_module_rules_response_component_description_no_rules = "No rules configured"

# ------------------------------------------------------------------------- #
# REMINDERS #
# ------------------------------------------------------------------------- #
response_module_reminders_request_failed = (
    "Something went wrong while sending the request to the reminders service! Please try again later."
)
response_module_reminders_no_reminders_found = "There are no reminders based on your selection."
response_module_reminders_one_destination_type_allowed = "You cannot have destination channel and member. You must choose between a DM (destination member) or a channel (destination channel)."
response_module_reminders_new_duration = (
    "Please provide the duration for the reminder. Please use format: {delay}{d/h/m/s} - f.e. 1h or 20m)"
)
list_module_reminders_response_component_description_reminder_id = "Reminder ID"
list_module_reminders_response_component_description_title = "Title"
list_module_reminders_response_component_description_description = "Description"
list_module_reminders_response_component_description_no_description = "No description set"
list_module_reminders_response_component_description_url = "URL"
list_module_reminders_response_component_description_no_url = "No url set"
list_module_reminders_response_component_description_destination = "Destination"
list_module_reminders_response_component_description_content_is_embed = "Content is embed"
list_module_reminders_response_component_description_content = "Content"
list_module_reminders_response_component_title_info_quick = "Quick reminders"
list_module_reminders_response_component_description_no_quick_reminders = "No quick reminders in this server"
list_module_reminders_response_component_title_info_repeated = "Repeated reminders"
list_module_reminders_response_component_description_no_repeated_reminders = "No repeated reminders in this server"
list_module_reminders_response_component_title_info_scheduled = "Scheduled reminders"
list_module_reminders_response_component_description_no_scheduled_reminders = "No scheduled reminders in this server"

# ------------------------------------------------------------------------- #
# POLLS #
# ------------------------------------------------------------------------- #
response_module_polls_request_failed = (
    "Something went wrong while sending the request to the polls service! Please try again later."
)
response_module_polls_determine_action_timeout = (
    "The poll vote determine action has reached a timeout. No vote will be placed or removed!"
)
response_module_polls_response_choose_poll_action = "What action do you want to perform on the answer? Add = Add vote & Remove = Remove all of your votes for that answer."
response_module_polls_provide_details_failed = (
    "Timeout while waiting for details of the poll answer! Cancelling poll create....."
)
response_module_polls_add_answer = "Do you want to add an extra answer to the list? Please keep in mind the answer limits of the server, these will only be checked when finishing this command."
response_module_polls_provide_answer_text = (
    "Please provide the text of the answer by sending it in the chat. Please only insert the answer text in one line."
)
response_module_polls_provide_answer_emoji = (
    "Please provide the emoji of the answer by sending it in the chat. Please only send the emoji."
)
response_module_polls_provide_answer_label = (
    "Please provide the label of the answer by sending it in the chat. Please only send the emoji."
)
response_module_polls_provide_answer_description = (
    "Please provide the description of the answer by sending it in the chat. Please only send the emoji."
)
response_module_polls_add_label_to_answer = (
    "Do you want to add a label to the button? If no, an emoji is required. If yes, an emoji is optional."
)
response_module_polls_add_description_to_answer = (
    "Do you want to add a description to the button (not visible in discord)?"
)
response_module_polls_add_emoji_to_answer = "Do you want to add a emoji to the button?"
info_module_polls_response_component_title_settings = "Polls module settings"
info_module_polls_response_component_description_settings_polls_save_duration = "Save duration"
info_module_polls_response_component_description_settings_polls_save_duration_seconds = "seconds"
info_module_polls_response_component_description_settings_polls_delete_ended_discord_polls = (
    "Delete ended Discord polls"
)
info_module_polls_response_component_description_settings_polls_delete_ended_husqy_polls = "Delete ended Husqy polls"
# Embeds
details_module_polls_response_component_title_info = "Polls details"
details_module_polls_response_component_description_info_poll_id = "Poll ID"
details_module_polls_response_component_description_info_question = "Question"
details_module_polls_response_component_description_info_description = "Description"
details_module_polls_response_component_description_info_no_description = "No description set"
details_module_polls_response_component_description_info_active_for = "Poll is active for: {countdown}"
details_module_polls_response_component_title_info_poll_results = "Poll results"
details_module_polls_response_component_description_votes = "Votes"
details_module_polls_response_component_title_info_poll_votes = "Voters"

# ------------------------------------------------------------------------- #
# VERIFIER #
# ------------------------------------------------------------------------- #
response_module_verifier_request_failed = (
    "Something went wrong while sending the request to the verifier service! Please try again later."
)
info_module_verifier_response_component_title_settings = "Verifier info"
info_module_verifier_response_component_description_settings_verifier_type = "Verifier type"
info_module_verifier_response_component_description_settings_verifier_channel = "Channel"
info_module_verifier_response_component_description_settings_no_verifier_channel = "No verifier channel configured"
info_module_verifier_response_component_description_settings_verifier_message_is_embed = "Verification message is embed"
info_module_verifier_response_component_description_settings_verifier_message_content = "Verification message content"
info_module_verifier_response_component_description_settings_verifier_message_completed_is_embed = (
    "Verification completed message is embed"
)
info_module_verifier_response_component_description_settings_verifier_message_content_success = (
    "Verification completed message content"
)
info_module_verifier_response_component_description_settings_verifier_verified_role_ids = "Verified role IDs"
info_module_verifier_response_component_description_settings_verifier_no_verified_role_ids = (
    "No verifier role IDs configured"
)

# ------------------------------------------------------------------------- #
# TEMPCHANNELS #
# ------------------------------------------------------------------------- #
response_module_tempchannels_request_failed = (
    "Something went wrong while sending the request to the tempchannels service! Please try again later."
)
response_module_tempchannels_request_failed_invalid_selection = (
    "Something went wrong while sending the request to the tempchannels service! Please enter a valid selection."
)
response_module_tempchannels_no_channels_found = "There are no channels based on your selection."
list_module_tempchannels_response_component_title_info_creation_channels = "Creation channels"
list_module_tempchannels_response_component_description_creation_channel = "Creation channel"
list_module_tempchannels_response_component_description_creation_category = "Creation category"
list_module_tempchannels_response_component_description_no_creation_category = "No creation category specified"
list_module_tempchannels_response_component_description_create_voice = "Create voice channel"
list_module_tempchannels_response_component_description_voice_name = "Voice channel name"
list_module_tempchannels_response_component_description_no_voice_name = "No voice channel created"
list_module_tempchannels_response_component_description_voice_category = "Voice category"
list_module_tempchannels_response_component_description_no_voice_category = "No voice category specified"
list_module_tempchannels_response_component_description_create_text = "Create text channel"
list_module_tempchannels_response_component_description_text_name = "Text channel name"
list_module_tempchannels_response_component_description_no_text_name = "No text channel created"
list_module_tempchannels_response_component_description_text_category = "Text category"
list_module_tempchannels_response_component_description_no_text_category = "No text category specified"
list_module_tempchannels_response_component_description_no_creation_channels = "No creation channels"
list_module_tempchannels_response_component_title_info_tempchannels = "Tempchannels"
list_module_tempchannels_response_component_description_tempchannel_id = "Tempchannel ID"
list_module_tempchannels_response_component_description_owner = "Owner"
list_module_tempchannels_response_component_description_no_owner = "No owner"
list_module_tempchannels_response_component_description_voice_channel = "Voice channel"
list_module_tempchannels_response_component_description_no_voice_channel = "No voice channel created"
list_module_tempchannels_response_component_description_text_channel = "Text channel"
list_module_tempchannels_response_component_description_no_text_channel = "No text channel created"
list_module_tempchannels_response_component_description_last_text_activity = "Last text activity"
list_module_tempchannels_response_component_description_no_last_text_activity = "No activity"
list_module_tempchannels_response_component_description_used_creation_channel = "Creation channel"
list_module_tempchannels_response_component_description_no_tempchannels = "No tempchannels in use"

# ------------------------------------------------------------------------- #
# TAGS #
# ------------------------------------------------------------------------- #
response_module_tags_request_failed = (
    "Something went wrong while sending the request to the tags service! Please try again later."
)
response_module_tags_no_tags_found = "There are no tags based on your selection."
response_module_tags_no_content = "There is no content given."
response_module_tags_invalid_tag_id = "There is no valid tag ID given."
response_module_tags_edit_provide_content = "Please provide the content of the tag by sending the content in the chat."
response_module_tags_create_provide_content = (
    "Please provide the tags content of the tag by sending the content in the chat."
)
list_module_tags_response_component_title_info = "Tags"
list_module_tags_response_component_description_tag_id = "Tag ID"
list_module_tag_response_component_description_owner = "Owner"
list_module_tag_response_component_description_visibility = "Visibility"
list_module_tag_response_component_description_names = "Names"
list_module_tags_response_component_description_no_tags = "No tags configured"

# ------------------------------------------------------------------------- #
# INVITE_TRACKER #
# ------------------------------------------------------------------------- #
response_module_invite_tracker_request_failed = (
    "Something went wrong while sending the request to the invite tracker service! Please try again later."
)
response_module_invite_tracker_no_shared_invite_link = "This server has not set a shared invite link!"
response_module_invite_tracker_no_invite_links = "There are not known invite links in this server!"
info_module_invite_tracker_button_settings = "Settings"
info_module_invite_tracker_response_component_description_settings_prevent_own_invite_code = (
    "Prevent own invite code from couting towards stats"
)
info_module_invite_tracker_response_component_description_settings_server_shared_invite_link = (
    "Server shared invite link"
)
info_module_invite_tracker_response_component_description_settings_server_no_shared_invite_link = (
    "No invite link configured"
)
info_module_invite_tracker_response_component_title_settings_join_messages = "Join messages"
info_module_invite_tracker_response_component_description_join_messages_enabled = "Join messages enabled"
info_module_invite_tracker_response_component_description_join_messages_channel = "Channel"
info_module_invite_tracker_response_component_description_no_join_messages_channel = "No channel configured"
info_module_invite_tracker_response_component_description_join_messages_is_embed = "Join message is embed"
info_module_invite_tracker_response_component_description_join_messages_content = "Join message content"
info_module_invite_tracker_response_component_title_settings_leave_messages = "Leave messages"
info_module_invite_tracker_response_component_description_leave_messages_enabled = "Leave messages enabled"
info_module_invite_tracker_response_component_description_leave_messages_channel = "Channel"
info_module_invite_tracker_response_component_description_no_leave_messages_channel = "No channel configured"
info_module_invite_tracker_response_component_description_leave_messages_is_embed = "Leave message is embed"
info_module_invite_tracker_response_component_description_leave_messages_content = "Leave message content"
info_module_invite_tracker_button_invites = "Invites"
info_module_invite_tracker_response_component_title_settings = "Invite tracker module info"
info_module_invite_tracker_response_component_title_invites = "Invites"
info_module_invite_tracker_response_component_description_invite_code = "Invite code"
info_module_invite_tracker_response_component_description_invite_url = "URL"
info_module_invite_tracker_response_component_description_no_invites = "No invites configured"
# Embeds
stats_module_invite_tracker_response_component_text = "### Invite tracker stats\n{member} has a total of `{total_invites}` invites over the pas 31 days!\n\n✅ Joins: `{joins}`\n❌ Leaves: `{leaves}`"
invite_link_module_invite_tracker_response_component_text = (
    "### Server invite link\nDo you want to invite other friends? Please use the following invite link:\n{link}"
)

# ------------------------------------------------------------------------- #
# GIVEAWAYS #
# ------------------------------------------------------------------------- #
response_module_giveaways_request_failed = (
    "Something went wrong while sending the request to the giveaways service! Please try again later."
)
response_module_giveaways_no_giveaways_found = "There are no giveaways based on your selection."
info_module_giveaways_button_settings = "Settings"
info_module_giveaways_button_giveaways = "Giveaways"
info_module_giveaways_response_component_title_settings = "Giveaways module info"
info_module_giveaways_response_component_description_settings_giveaways_save_duration = "Save duration"
info_module_giveaways_response_component_description_settings_giveaways_save_duration_seconds = "seconds"
info_module_giveaways_response_component_description_settings_giveaways_delete_ended_giveaways = (
    "Delete ended giveaways"
)
info_module_giveaways_response_component_title_giveaways = "Giveaways"
info_module_giveaways_response_component_description_giveaway_id = "Giveaway ID"
info_module_giveaways_response_component_description_giveaway_channel = "Channel"
info_module_giveaways_response_component_description_giveaway_owner = "Owner"
info_module_giveaways_response_component_description_giveaway_message_id = "Message"
info_module_giveaways_response_component_description_giveaway_winner_count = "Winner count"
info_module_giveaways_response_component_description_giveaway_prize = "Prize"
info_module_giveaways_response_component_description_giveaway_description = "Description"
info_module_giveaways_response_component_description_giveaway_no_description = "No description configured"
info_module_giveaways_response_component_description_no_giveaways = "No giveaways active"

# ------------------------------------------------------------------------- #
# LOGGING #
# ------------------------------------------------------------------------- #
response_module_logging_request_failed = (
    "Something went wrong while sending the request to the logging service! Please try again later."
)
LOGGABLE_TRANSLATIONS = {
    "log_errors": "Errors",
    "log_info": "Info requests",
    "log_settings_changed": "Setting changes",
    "log_channel_create": "Channel creations",
    "log_channel_delete": "Channel deletions",
    "log_channel_update": "Channel updates",
    "log_clear_messages": "Clear messages",
    "log_slowmode": "Slowmode changes",
    "log_channel_lock": "Channel locked",
    "log_channel_unlock": "Channel unlocked",
    "log_channel_join": "Joined voice channel",
    "log_channel_leave": "Left voice channel",
    "log_channel_move": "Moved voice channel",
    "log_role_create": "Role creations",
    "log_role_delete": "Role deletions",
    "log_role_update": "Role updates",
    "log_user_warn_create": "Warn create",
    "log_user_warn_delete": "Warn delete",
    "log_kick_event": "Kicked users",
    "log_vckick": "User kicked from VC",
    "log_move": "User moved to different VC by command",
    "log_ban_create": "Bans",
    "log_ban_delete": "Unbans",
    "log_tempmute": "Tempmute command",
    "log_temptimeout": "Temptimeout command",
    "log_games": "Games played",
    "log_help": "Help commands",
    "log_modules": "Module changes",
    "log_customembed_send": "Custom Embeds Sent",
    "log_customembed_create": "Custom Embeds Creations",
    "log_custommodal_create": "Custom Modal Creations",
    "log_custommodal_preview": "Cuustom Modal Previewed",
    "log_reminder_add": "Reminders added",
    "log_reminder_delete": "Reminders deleted",
    "log_user_server_muted": "User got server muted",
    "log_user_server_unmuted": "User got server unmuted",
    "log_user_server_deafend": "User got server deafend",
    "log_user_server_undeafend": "User got server undeafend",
    "log_user_deafend": "User self deafend",
    "log_user_undeafend": "User self undeafend",
    "log_user_muted": "User self muted",
    "log_user_unmuted": "User self unmuted",
    "log_user_stream_started": "User started streaming",
    "log_user_stream_stopped": "User stopped streaming",
    "log_user_camera_stream_started": "User turned on camera",
    "log_user_camera_stream_stopped": "User turned off camera",
    "log_color_viewed": "Color viewed",
    "log_giveaway_create": "Giveaway create",
    "log_giveaway_delete": "Giveaway delete",
    "log_giveaway_reroll": "Giveaway reroll",
    "log_domain_validated": "Domain validated",
    "log_qr_generated": "QR-code generated",
    "log_time_converted": "Time converted to seconds",
    "log_meme": "Meme requests",
    "log_kick_events": "Users being kicked",
    "log_reactionroles_panel_create": "Reactionrole panel created",
    "log_reactionroles_panel_delete": "Reactionrole panel deleted",
    "log_reactionroles_panel_edit": "Reactionrole panel edited",
    "log_reactionroles_panel_entry_create": "Reactionrole entry added to panel",
    "log_reactionroles_panel_entry_delete": "Reactionrole entry deleted from panel",
    "log_reactionroles_panel_entry_edit": "Reactionrole entry edited",
    "log_tag_create": "Tag created",
    "log_tag_delete": "Tag deleted",
    "log_tag_edit": "Tag edited",
    "log_tag_send": "Tag send",
    "log_tag_preview": "Tag previewed",
    "log_autoresponder_trigger_created": "Autoresponder trigger created",
    "log_autoresponder_trigger_deleted": "Autoresponder trigger deleted",
    "log_autoresponder_trigger_edited": "Autoresponder trigger edited",
    "log_autoresponder_trigger_hit": "Autoresponder trigger hit",
    "log_autoresponder_response_created": "Autoresponder response created",
    "log_autoresponder_response_deleted": "Autoresponder response deleted",
    "log_welcoming_response_create": "Welcoming response created",
    "log_welcoming_response_delete": "Welcoming response delete",
    "log_welcoming_timedrole_create": "Welcoming timedrole created",
    "log_welcoming_timedrole_delete": "Welcoming timedrole delete",
    "log_welcoming_check_welcome_dm": "Welcome messages in DM checked",
    "log_welcoming_check_welcome_channel": "Welcome messages in channel checked",
    "log_welcoming_check_leave_channel": "Leave messages in channel checked",
    "log_welcoming_check_role_on_join": "Autorole checked",
    "log_welcoming_check_role_timed": "Timedrole checked",
    "log_socials_reddit_remove": "Subreddit removed",
    "log_socials_reddit_add": "Subreddit added",
    "log_socials_rss_remove": "RSS feed removed",
    "log_socials_rss_add": "RSS feed added",
    "log_socials_twitch_remove": "Twitch account removed",
    "log_socials_twitch_add": "Twitch account added",
    "log_socials_youtube_remove": "YouTube channel removed",
    "log_socials_youtube_add": "YouTube channel added",
    "log_creation_channel_create": "Tempchannels creation channels created",
    "log_creation_channel_delete": "Tempchannels creation channels deleted",
    "log_creation_channel_edit": "Tempchannels creation channels edited",
    "log_tempchannel_check_create": "Checked for tempchannel creation",
    "log_tempchannel_check_delete": "Checked for tempchannel deletion",
    "log_tempchannel_name_edited": "Tempchannel name edited",
    "log_tempchannel_user_limit_edited": "Tempchannel user limit edited",
    "log_tempchannel_slowmode_edited": "Tempchannel slowmode edited",
    "log_tempchannel_bitrate_edited": "Tempchannel bitrate edited",
    "log_tempchannel_age_restriction_edited": "Tempchannel age restriction setting edited",
    "log_tempchannel_region_edited": "Tempchannel region edited",
    "log_tempchannel_claimed": "Tempchannel claimed",
    "log_tempchannel_transferred": "Tempchannel transferred",
    "log_tempchannel_deleted": "Tempchannel set deleted",
    "log_tempchannel_block_rule_added": "Tempchannel block rule added",
    "log_tempchannel_block_rule_removed": "Tempchannel block rule removed",
    "log_tempchannel_trust_rule_added": "Tempchannel trust rule added",
    "log_tempchannel_trust_rule_removed": "Tempchannel trust rule removed",
    "log_verifier_verification_create": "Verifier verification created",
    "log_verifier_verification_handle": "Verifier verification handled",
    "log_rules_rule_add": "Rule added",
    "log_rules_rule_remove": "Rule removed",
    "log_rules_send_check": "Checked rule send",
    "log_rules_interaction_check": "Checked rule interaction",
    "log_ticket_panel_create": "Ticket panel created",
    "log_ticket_panel_edit": "Ticket panel edited",
    "log_ticket_panel_delete": "Ticket panel deleted",
    "log_ticket_type_add": "Ticket type added to panel",
    "log_ticket_type_delete": "Ticket type removed from panel",
    "log_ticket_create": "Ticket created",
    "log_ticket_form_showed": "Ticket form showed",
    "log_ticket_delete": "Ticket deleted",
    "log_ticket_transfer": "Ticket transferred",
    "log_ticket_reopen": "Ticket reopened",
    "log_ticket_close": "Ticket closed",
    "log_ticket_claim": "Ticket claimed",
    "log_ticket_transcribe": "Ticket transcribed",
    "log_invite_created": "Invite link created",
    "log_invite_deleted": "Invite link deleted",
    "log_invite_based_join": "Log join with invite",
    "log_invite_based_leave": "Log leave linked to invite",
    "log_serverstats_counter_created": "Log counters created",
    "log_serverstats_counter_deleted": "Log counters deleted",
    "log_serverstats_starboard_check": "Log starboard checked",
    "log_serverstats_counters_updated": "Log counters updated",
    "log_polls_created": "Log polls created",
    "log_polls_edited": "Log polls edited",
    "log_polls_deleted": "Log polls deleted",
    "log_polls_closed": "Log polls closed",
    "log_polls_closed_manually": "Log polls closed manually",
    "log_polls_vote_added": "Log polls vote added",
    "log_polls_vote_removed": "Log polls vote removed",
    "log_reminders_created": "Log reminders created",
    "log_reminders_deleted": "Log reminders deleted",
    "log_reminders_send": "Log reminders send",
    "log_reminders_completed": "Log reminders completed",
    "log_reminders_reminded_later": "Log reminders reminded later",
    "log_giveaways_created": "Log giveaways created",
    "log_giveaways_deleted": "Log giveaways deleted",
    "log_giveaways_edited": "Log giveaways edited",
    "log_giveaways_rerolled": "Log giveaways rerolled",
    "log_giveaways_entered": "Log giveaways entered",
    "log_giveaways_leaves": "Log giveaway leaved",
    "log_giveaways_finished": "Log giveaways finished",
}
info_module_logging_response_component_title_info = "Logging module info"
info_module_logging_response_component_title_logs_channel = "Logs channel"
info_module_logging_response_component_description_no_logs_channel = "No logs channel"
info_module_logging_response_component_title_events = "Events"

# ------------------------------------------------------------------------- #
# WELCOMING #
# ------------------------------------------------------------------------- #
response_module_welcoming_request_failed = (
    "Something went wrong while sending the request to the welcoming service! Please try again later."
)
info_module_welcoming_button_settings = "Settings"
info_module_welcoming_button_responses = "Responses"
info_module_welcoming_button_timedroles = "Timedroles"
info_module_welcoming_response_component_title_info = "Welcoming module info"
info_module_welcoming_response_component_description_settings_response_randomized = "Responses randomized"
info_module_welcoming_response_component_description_settings_response = "Response"
info_module_welcoming_response_component_description_settings_responses_are_randomized = "Responses are randomized"
info_module_welcoming_response_component_title_settings_dm_welcome = "DM welcoming settings"
info_module_welcoming_response_component_description_settings_dm_welcome_enabled = "Enabled"
info_module_welcoming_response_component_title_settings_channel_welcome = "Channel welcoming settings"
info_module_welcoming_response_component_description_settings_channel_welcome_channel = "Channel"
info_module_welcoming_response_component_description_settings_no_channel_welcome_channel = "Not configured"
info_module_welcoming_response_component_description_settings_channel_welcome_enabled = "Enabled"
info_module_welcoming_response_component_title_settings_channel_leave = "Channel leave settings"
info_module_welcoming_response_component_description_settings_channel_leave_channel = "Channel"
info_module_welcoming_response_component_description_settings_no_channel_leave_channel = "Not configured"
info_module_welcoming_response_component_description_settings_channel_leave_enabled = "Enabled"
info_module_welcoming_response_component_title_settings_autoroles = "Autoroles settings"
info_module_welcoming_response_component_description_settings_autoroles_enabled = "Enabled"
info_module_welcoming_response_component_description_settings_autoroles_not_configured = "No autoroles configured!"
info_module_welcoming_response_component_description_response_id = "Response ID"
info_module_welcoming_response_component_description_response_type = "Response type"
info_module_welcoming_response_component_description_response_content = "Response content"
info_module_welcoming_response_component_description_no_responses = (
    "This server does not have any responses configured!"
)
info_module_welcoming_response_component_description_timedrole_id = "Timedrole ID"
info_module_welcoming_response_component_description_timedrole_role = "Role"
info_module_welcoming_response_component_description_timedrole_add_after = "Added after"
info_module_welcoming_response_component_description_timedrole_add_after_seconds = "seconds"
info_module_welcoming_response_component_description_no_timedroles = (
    "This server does not have any timedroles configured!"
)
# ------------------------------------------------------------------------- #
# Mod_User #
# ------------------------------------------------------------------------- #
# Embeds
user_events_ban_create_component = (
    "### You have been banned!\nYou have been banned from `{guild}`!\n\n[Reason] -- {reason}"
)
user_events_ban_delete_component = (
    "### You have been unbanned!\nYou have been unbanned from `{guild}`!\n\n[Reason] -- {reason}"
)
user_events_kick_component = "### You have been kicked!\nYou have been kicked from `{guild}`!\n\n[Reason] -- *{reason}*"

# ------------------------------------------------------------------------- #
# SOCIALS #
# ------------------------------------------------------------------------- #
response_module_socials_request_failed = (
    "Something went wrong while sending the request to the socials service! Please try again later."
)
info_module_socials_button_reddit = "Reddit"
info_module_socials_button_twitch = "Twitch"
info_module_socials_button_rss = "RSS"
info_module_socials_button_youtube = "YouTube"
info_module_socials_response_component_title_info = "Socials module info"
info_module_socials_response_component_description_reddit_enabled = "Reddit monitor enabled"
info_module_socials_response_component_description_rss_enabled = "RSS monitor enabled"
info_module_socials_response_component_description_twitch_enabled = "Twitch monitor enabled"
info_module_socials_response_component_description_youtube_enabled = "YouTube monitor enabled"
info_module_socials_response_component_description_reddit_subreddit = "Subreddit"
info_module_socials_response_component_description_reddit_mention_everyone = "Mention everyone"
info_module_socials_response_component_description_reddit_channel = "Channel"
info_module_socials_response_component_description_no_reddits = "No monitored subreddits"
info_module_socials_response_component_description_rss_feed = "RSS Feed"
info_module_socials_response_component_description_rss_mention_everyone = "Mention everyone"
info_module_socials_response_component_description_rss_channel = "Channel"
info_module_socials_response_component_description_no_rss_feeds = "No monitored RSS feeds"
info_module_socials_response_component_description_twitch_account = "Twitch account"
info_module_socials_response_component_description_twitch_mention_everyone = "Mention everyone"
info_module_socials_response_component_description_twitch_channel = "Channel"
info_module_socials_response_component_description_no_twitch_accounts = "No monitored Twitch accounts"
info_module_socials_response_component_description_youtube_handle = "YouTube channel"
info_module_socials_response_component_description_youtube_mention_everyone = "Mention everyone"
info_module_socials_response_component_description_youtube_channel = "Channel"
info_module_socials_response_component_description_no_youtube_channels = "No monitored YouTube channels"

# ------------------------------------------------------------------------- #
# SERVERSTATS #
# ------------------------------------------------------------------------- #
response_module_serverstats_request_failed = (
    "Something went wrong while sending the request to the serverstats service! Please try again later."
)
info_module_serverstats_button_settings = "Settings"
info_module_serverstats_button_counters = "Counters"
info_module_serverstats_response_component_title_info = "Serverstats module info"
info_module_serverstats_response_component_title_settings_counters = "Counters"
info_module_serverstats_response_component_description_settings_counters_enabled = "Counters enabled"
info_module_serverstats_response_component_description_settings_counters_category = "Counters category"
info_module_serverstats_response_component_description_settings_no_counters_category = "No category configured"
info_module_serverstats_response_component_title_settings_starboard = "Starboard"
info_module_serverstats_response_component_description_settings_starboard_enabled = "Starboard enabled"
info_module_serverstats_response_component_description_settings_starboard_channel_id = "Channel"
info_module_serverstats_response_component_description_settings_starboard_count = "Stars required"
info_module_serverstats_response_component_description_settings_no_starboard_channel_id = "No starboard configured"
info_module_serverstats_response_component_title_settings_stats_enabled = "Enabled stats"
info_module_serverstats_response_component_title_settings_no_stats_enabled = "No stats enabled"
info_module_serverstats_response_component_title_settings_stats_disabled = "Disabled stats"
info_module_serverstats_response_component_title_settings_no_stats_disabled = "No stats disabled"
info_module_serverstats_response_component_description_no_counters = "No counters configured"
info_module_serverstats_response_component_description_counter_id = "Counter ID"
info_module_serverstats_response_component_description_counter_channel = "Channel"
info_module_serverstats_response_component_description_counter_type = "Type"
info_module_serverstats_response_component_description_counter_format = "Format"
info_module_serverstats_response_component_description_counter_goal_count = "Goal count"
info_module_serverstats_response_component_description_counter_no_goal_count = "No goal count configured"
info_module_serverstats_response_component_description_counter_role_id = "Role ID"
info_module_serverstats_response_component_description_no_counter_role_id = "No role ID configured"
stats_messages_enabled = "Message stats"
stats_members_enabled = "Member stats"
stats_commands_enabled = "Command stats"
stats_activities_enabled = "Activities stats"
stats_voice_enabled = "Voice stats"
stats_modules_autoresponder_enabled = "Module autoresponder stats"
stats_modules_tags_enabled = "Module tags stats"
stats_modules_verifier_enabled = "Module verifier stats"
stats_modules_socials_enabled = "Module socials stats"
stats_modules_rules_enabled = "Module rules stats"
stats_modules_invite_tracker_enabled = "Module invite tracker stats"
stats_modules_reactionroles_enabled = "Module reactionroles stats"
stats_modules_welcoming_enabled = "Module welcoming stats"
stats_modules_tempchannels_enabled = "Module tempchannels stats"
stats_modules_tickets_enabled = "Module tickets stats"
stats_modules_polls_enabled = "Module polls stats"
stats_modules_reminders_enabled = "Module reminders stats"
stats_modules_giveaways_enabled = "Module giveaways stats"

# ------------------------------------------------------------------------- #
# PRIVACY #
# ------------------------------------------------------------------------- #
allowed = "Allowed"
not_allowed = "Not allowed"
privacy_info_response_component_title = "Privacy configuration"
privacy_info_response_component_description = """
Welcome to the Husqy privacy configurator.
Currently, Husqy is `{status}` to collect data from you in this server!c
### About this configurator
This privacy configurator is the place to configure your privacy related settings in Husqy.
You are free to retrieve your data and delete this data and instruct Husqy to not collect your data to deliver its services.
BEWARE: Deleting your data or restricting Husqy in collecting your data will result in loss of functionality for you and may result in loss of functionality or configuration changes to Husqy for other server members!
### Changing privacy configuration
Please use the other privacy commands (prefixed with `/privacy`) to get or delete privacy related information! Use the buttons below to update the data collection status for you for this server.
"""
privacy_info_response_component_questions = """
### Questions
If you have any further questions, please visit: [our website](https://www.husqy.xyz/) or contact our support!
Note: Husqy does not store all data, some data (like sent messages, f.e. mentions in the logging channel) will still exist in Discord, please contact the server administrator if you want to remove these entries.
Not all data can be deleted, some data is required (f.e. for settings the data collection preference or warnings).
"""
enable_data_collection = "Enable data collection"
disable_data_collection = "Disable data collection"
privacy_info_response_component_disclaimer = """
DISCLAIMER: This configurator works on a per server basis! Want to get or delete information in other servers, use this privacy configurator in the other servers!
"""
privacy_info_response_data_collection_changed = "The data collection information has been changed to: `{status}`"
privacy_shared_servers_response_component_title = "Shared servers"
privacy_get_data_response_component_title = "Privacy data"
privacy_get_data_response_component_description = """
These are the amount of times we have found your details:\n
- ID: {id_counts}
- Username: {username_counts}
- Display name: {display_name_counts}
- Global name: {global_name_counts}
- Nickname: {nickname_counts}

To remove this data please use the `/privacy delete_data` command.
"""
privacy_delete_data_response = "Your data is deleted for as far as possible. Not all data can be deleted, some data is required (f.e. for settings the data collection preference)"
