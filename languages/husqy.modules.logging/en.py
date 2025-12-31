# MODULE LOGGING CONFIGURATION
unknown_user = "an unknown user"
default_logging_channel_name = "{bot_name} logging"
response_module_logging_enabled = "{datetime} -- **{member}** has enabled the `logging` module! I will now log all supported events to the new logging channel!"
response_module_logging_disabled = (
    "{datetime} -- **{member}** has disabled the `logging` module! All related settings are removed!"
)
response_module_logging_disable_failed = "{datetime} -- **{member}** tried to disable the `logging` module but something went wrong! Some of the configuration might be changed!!"
response_module_logging_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `logging` module but something went wrong! Some of the configuration might be changed!!"
response_module_logging_settings_change_success = (
    "{datetime} -- **{member}** changed the settings of the `logging` module!"
)
response_module_logging_settings_change_success_old_channel = "{datetime} -- **{member}** changed the logs channel of the `logging` module! This is now the old logs channel. The new channel is: {new_channel}!"
response_module_logging_settings_change_success_new_channel = "{datetime} -- **{member}** changed the logs channel of the `logging` module! This is now the new logs channel. The old channel is: {old_channel}!"

# LOGGED EVENTS
## Giveaways
### Create
response_giveaway_created = "{datetime} -- **{member}** has created a giveaway!"
response_giveaway_create_failed_not_a_valid_time = (
    "{datetime} -- **{member}** tried to create a giveaway but they gave me an invalid time duration!"
)
response_giveaway_create_failed = "{datetime} -- **{member}** tried to create a giveaway but something went wrong!"
### Delete
response_giveaway_delete = "{datetime} -- **{member}** has deleted a giveaway!"
response_giveaway_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a giveaway but they are not the owner!"
)
response_giveaway_delete_failed_no_giveaway_found = (
    "{datetime} -- **{member}** tried to delete a giveaway but I don't know of a giveaway with the given ID!"
)
response_giveaway_delete_failed = "{datetime} -- **{member}** tried to delete a giveaway but something went wrong!"
### List
response_giveaway_list_requested = "{datetime} -- **{member}** has requested their giveaways in this server!"
response_giveaway_list_no_giveaways = (
    "{datetime} -- **{member}** tried to list their giveaways in this server but they don't have any!"
)
### Reroll
response_giveaway_reroll = "{datetime} -- **{member}** has rerolled a winner for a giveaway!"
response_giveaway_reroll_failed_no_winner_yet = (
    "{datetime} -- **{member}** tried to reroll a winner for a giveaway but there is no winner yet!"
)
response_giveaway_reroll_failed_not_owner = (
    "{datetime} -- **{member}** tried to reroll a winner for a giveaway but they are not the owner!"
)
response_giveaway_reroll_failed_no_giveaway_found = (
    "{datetime} -- **{member}** tried to reroll a winner for a giveaway but there is no giveaway with the given ID!"
)
response_giveaway_reroll_failed = (
    "{datetime} -- **{member}** tried to reroll a winner for a giveaway but something went wrong!"
)

## General
### Settings
response_failed_no_event_manager = "{datetime} -- **{member}** tried to run the command: `/{command}` but something went wrong! If this issue persist, please contact my support!"
response_settings_changed = "{datetime} -- **{member}** has changed my settings!"
response_settings_changed_not_all_success = (
    "{datetime} -- **{member}** has changed my settings, but not all settings may have been changed successfully!"
)
### Info
response_info_failed = "{datetime} -- **{member}** requested information but something went wrong!"
response_info_bot_requested = "{datetime} -- **{member}** requested my information!"
response_info_user_requested = "{datetime} -- **{member}** requested information about {user}!"
response_info_role_requested = "{datetime} -- **{member}** requested information about the role {role}!"
response_info_channel_requested = "{datetime} -- **{member}** requested information about the channel `{channel}`!"
response_info_channel_requested_failed_channel_not_recognised = (
    "{datetime} -- **{member}** requested information about a channel I don't know!"
)
response_info_server_requested = "{datetime} -- **{member}** requested information about the server!"
response_module_socials_twitch_list = "{datetime} -- **{member}** requested the Twitch account list!"
response_module_socials_rss_list = "{datetime} -- **{member}** requested the RSS Feed list!"
response_module_socials_reddit_list = "{datetime} -- **{member}** requested the Subreddit list!"
### Ping
response_ping_requested = "{datetime} -- **{member}** used `/info ping`! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
### Invite link
response_invite_link_requested = "{datetime} -- **{member}** requested the configured invite link!"
response_invite_link_not_set = "{datetime} -- **{member}** requested the configured invite link but none was set!"
### Help
response_help = "{datetime} -- **{member}** has used the `/help` command!"

## Misc
### Games
response_games_played_heads_or_tails = "{datetime} -- **{member}** played `Heads or Tails`!"
response_games_played_rps = (
    "{datetime} -- **{member}** played `Rock/Paper/Scissors` against {opponent}! The winner is {winner}!"
)
response_games_played_higher_lower_played_won = "{datetime} -- **{member}** played `Higher/Lower` and won!"
response_games_played_higher_lower_played_loss = "{datetime} -- **{member}** played `Higher/Lower` and lost!"
response_games_played_higher_lower_played_failed = (
    "{datetime} -- **{member}** tried to play `Higher/Lower` but something went wrong while starting!"
)
### Meme
response_meme_success = "{datetime} -- **{member}** requested a meme!"
response_meme_failed = "{datetime} -- **{member}** requested a meme but something went wrong while sending!"
### Transcribe audio message
response_transcribe_failed = "{datetime} -- **{member}** tried to transcribe a voice message but something went wrong!"
response_transcribe_success = "{datetime} -- **{member}** transcribed a voice message!"

## Utils
### Custom embed
response_custom_embed_send_success = "{datetime} -- **{member}** sent a custom embed to {channel}!"
response_custom_embed_send_failed = (
    "{datetime} -- **{member}** tried sending a custom embed but something went wrong!"
)
### Custom modal
response_custom_modal_create = "{datetime} -- **{member}** started creating their own modal!"
response_custom_modal_finished = "{datetime} -- **{member}** created a custom modal!"
response_custom_modal_finished_timeout = "{datetime} -- **{member}** created a custom modal but a timeout was reached!"
response_custom_modal_preview_success = "{datetime} -- **{member}** previewed a custom modal!"
response_custom_modal_preview_failed_canceled = (
    "{datetime} -- **{member}** tried to preview a custom modal but canceled it!"
)
response_custom_modal_preview_failed = (
    "{datetime} -- **{member}** tried to preview a custom modal but a timeout was reached!"
)
### QR
response_qr_generate_success = "{datetime} -- **{member}** has generated a QR-code!"
### Convert
response_time_converted_success = "{datetime} -- **{member}** converted: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds to seconds: `{total_seconds}`!"

## Module Autoresponder
### Disable
response_module_autoresponder_disabled = (
    "{datetime} -- **{member}** has disabled the `autoresponder` module! All related settings are removed!"
)
response_module_autoresponder_disable_failed = "{datetime} -- **{member}** tried to disable the `autoresponder` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_autoresponder_enabled = "{datetime} -- **{member}** has enabled the `autoresponder` module!"
response_module_autoresponder_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `autoresponder` module but something went wrong!"
)
### Trigger Create
response_module_autoresponder_create_trigger_success = (
    "{datetime} -- **{member}** has created a new trigger for the `autoresponder` module!"
)
response_module_autoresponder_create_trigger_failed = (
    "{datetime} -- **{member}** tried to create a new trigger for the `autoresponder` module but something went wrong!"
)
response_module_autoresponder_create_trigger_failed_trigger_limit_reached = "{datetime} -- **{member}** tried to create a new trigger for the `autoresponder` module but the limit has already been reached!"
response_module_autoresponder_create_trigger_failed_invalid_trigger_type = "{datetime} -- **{member}** tried to create a new trigger for the `autoresponder` module but they didn't provide a correct trigger type!"
### Trigger Edit
response_module_autoresponder_edit_trigger_success = (
    "{datetime} -- **{member}** has edited a trigger from the `autoresponder` module!"
)
response_module_autoresponder_edit_trigger_failed = (
    "{datetime} -- **{member}** tried to edit a trigger from the `autoresponder` module but something went wrong!"
)
### Trigger Delete
response_module_autoresponder_delete_trigger_success = (
    "{datetime} -- **{member}** has deleted a trigger from the `autoresponder` module!"
)
response_module_autoresponder_delete_trigger_failed = (
    "{datetime} -- **{member}** tried to delete a trigger from the `autoresponder` module but something went wrong!"
)
### Trigger Hit
response_module_autoresponder_trigger_hit = (
    "{datetime} -- **{member}** hit an autoresponder trigger. If configured, the response(s) should be send!"
)
### Response Create
response_module_autoresponder_create_response_success = (
    "{datetime} -- **{member}** has created a new response for the `autoresponder` module!"
)
response_module_autoresponder_create_response_failed = (
    "{datetime} -- **{member}** tried to create a new response for the `autoresponder` module but something went wrong!"
)
response_module_autoresponder_create_response_failed_response_limit_reached = "{datetime} -- **{member}** tried to create a new response for the `autoresponder` module but the limit has already been reached!"
response_module_autoresponder_create_response_failed_invalid_response_type = "{datetime} -- **{member}** tried to create a new response for the `autoresponder` module but they didn't provide a correct response type!"
### Response Delete
response_module_autoresponder_delete_response_success = (
    "{datetime} -- **{member}** has deleted a response from the `autoresponder` module!"
)
response_module_autoresponder_delete_response_failed = (
    "{datetime} -- **{member}** tried to delete a response from the `autoresponder` module but something went wrong!"
)

## Module Tempchannel
### Disable
response_module_tempchannels_disabled = "{datetime} -- **{member}** has disabled the `tempchannels` module! All related settings are removed! Any leftover channels will not be automatically deleted and can safely be deleted manually!"
response_module_tempchannels_disable_failed = "{datetime} -- **{member}** tried to disable the `tempchannels` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_tempchannels_enabled = "{datetime} -- **{member}** has enabled the `tempchannels` module!"
response_module_tempchannels_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `tempchannels` module but something went wrong!"
)
### Creation channels
response_module_tempchannels_creation_channel_created = (
    "{datetime} -- **{member}** has created a new tempchannels creation channel: <#{channel_id}>!"
)
response_module_tempchannels_creation_channel_create_failed = (
    "{datetime} -- **{member}** tried to create a new tempchannels creation channel but something went wrong!"
)
response_module_tempchannels_creation_channel_create_failed_limit_reached = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but the limit has already been reached!"
response_module_tempchannels_creation_channel_create_failed_invalid_text_category_type = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but the given text category value is not valid!"
response_module_tempchannels_creation_channel_create_failed_invalid_voice_category_type = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but the given voice category value is not valid!"
response_module_tempchannels_creation_channel_create_failed_no_text_name_given = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but they did not provide a name for the text channels!"
response_module_tempchannels_creation_channel_create_failed_no_voice_name_given = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but they did not provide a name for the voice channels!"
response_module_tempchannels_creation_channel_create_failed_invalid_creation_category_type = "{datetime} -- **{member}** tried to create a new tempchannels creation channel but the given creation category value is not valid!"
response_module_tempchannels_creation_channel_deleted = "{datetime} -- **{member}** has deleted a tempchannels creation channel! Any leftover categories or channels with child channels are not deleted and can safely be deleted manually!"
response_module_tempchannels_creation_channel_delete_failed = (
    "{datetime} -- **{member}** tried to delete a tempchannels creation channel but something went wrong!"
)
response_module_tempchannels_creation_channel_edited = (
    "{datetime} -- **{member}** has edited a tempchannels creation channel!"
)
response_module_tempchannels_creation_channel_edit_failed = (
    "{datetime} -- **{member}** tried to edit a tempchannels creation channel but something went wrong!"
)
response_module_tempchannels_creation_channel_edit_failed_invalid_text_category_type = "{datetime} -- **{member}** tried to edit a new tempchannels creation channel but the given text category value is not valid!"
response_module_tempchannels_creation_channel_edit_failed_invalid_voice_category_type = "{datetime} -- **{member}** tried to edit a new tempchannels creation channel but the given voice category value is not valid!"
response_module_tempchannels_creation_channel_edit_failed_no_text_name_given = "{datetime} -- **{member}** tried to edit a new tempchannels creation channel but they did not provide a name for the text channels!"
response_module_tempchannels_creation_channel_edit_failed_no_voice_name_given = "{datetime} -- **{member}** tried to edit a new tempchannels creation channel but they did not provide a name for the voice channels!"
response_module_tempchannels_manual_delete_success = (
    "{datetime} -- **{member}** has manually deleted a tempchannels creation channel!"
)
response_module_tempchannels_manual_delete_failed = "{datetime} -- **{member}** tried to manually delete a tempchannels creation channel but something went wrong while removing it from the database!"
# Check create
response_module_tempchannels_check_create_success = (
    "{datetime} -- Checked channel join for tempchannel creation. Triggered by: {member}"
)
response_module_tempchannels_check_create_failed = (
    "{datetime} -- Checking channel join for tempchannel creation failed. Triggered by: {member}"
)
response_module_tempchannels_check_create_failed_limit_reached = "{datetime} -- Checking channel join for tempchannel creation failed because the maximum number of tempchannels has been reached. Triggered by: {member}"
response_module_tempchannels_check_create_failed_prevent_data_collection_enabled = "{datetime} -- Checking channel join for tempchannel creation failed because prevent data collection is enabled for the member. Triggered by: {member}"
# Check delete
response_module_tempchannels_check_delete_success = "{datetime} -- Checked channel leave for tempchannel deletion. Triggered by: {member}. Note: linked text channels with activity will be deleted after 6 hours since the last activity."
response_module_tempchannels_check_manual_delete_success = (
    "{datetime} -- **{member}** has manually deleted a tempchannel!"
)
response_module_tempchannels_check_manual_delete_failed = "{datetime} -- **{member}** tried to manually delete a tempchannels but something went wrong while removing it from the database!"
# Edits
## Name
response_module_tempchannels_edit_name_success = "{datetime} -- **{member}** has changed the name of a tempchannel!"
response_module_tempchannels_edit_name_failed = (
    "{datetime} -- **{member}** tried to change the name of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_name_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the name of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_name_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to change the name of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_edit_name_failed_module_disabled = (
    "{datetime} -- **{member}** tried to change the name of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_edit_name_failed_module_unknown = "{datetime} -- **{member}** tried to change the name of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_name_failed_settings_not_found = "{datetime} -- **{member}** tried to change the name of a tempchannel but something went wrong while getting the settings for the server!"
## Region
response_module_tempchannels_edit_region_success = "{datetime} -- **{member}** has changed the region of a tempchannel!"
response_module_tempchannels_edit_region_failed = (
    "{datetime} -- **{member}** tried to change the region of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_region_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the region of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_region_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to change the region of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_edit_region_failed_module_disabled = (
    "{datetime} -- **{member}** tried to change the region of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_edit_region_failed_module_unknown = "{datetime} -- **{member}** tried to change the region of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_region_failed_settings_not_found = "{datetime} -- **{member}** tried to change the region of a tempchannel but something went wrong while getting the settings for the server!"
## Slowmode
response_module_tempchannels_edit_slowmode_success = (
    "{datetime} -- **{member}** has changed the slowmode timeout of a tempchannel!"
)
response_module_tempchannels_edit_slowmode_failed = (
    "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_slowmode_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_slowmode_failed_no_tempchannel_found = "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but the given tempchannel is not found!"
response_module_tempchannels_edit_slowmode_failed_module_disabled = "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but `tempchannels` module is disabled!"
response_module_tempchannels_edit_slowmode_failed_module_unknown = "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_slowmode_failed_settings_not_found = "{datetime} -- **{member}** tried to change the slowmode timeout of a tempchannel but something went wrong while getting the settings for the server!"
## Bitrate
response_module_tempchannels_edit_bitrate_success = (
    "{datetime} -- **{member}** has changed the bitrate of a tempchannel!"
)
response_module_tempchannels_edit_bitrate_failed = (
    "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_bitrate_failed_not_in_range = "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but they did not provide a value between 8 and 96!"
response_module_tempchannels_edit_bitrate_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_bitrate_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_edit_bitrate_failed_module_disabled = (
    "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_edit_bitrate_failed_module_unknown = "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_bitrate_failed_settings_not_found = "{datetime} -- **{member}** tried to change the bitrate of a tempchannel but something went wrong while getting the settings for the server!"
## User limit
response_module_tempchannels_edit_user_limit_success = (
    "{datetime} -- **{member}** has changed the user limit of a tempchannel!"
)
response_module_tempchannels_edit_user_limit_failed = (
    "{datetime} -- **{member}** tried to change the user limit of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_user_limit_failed_not_in_range = "{datetime} -- **{member}** tried to change the user limit of a tempchannel but they did not provide a value between 0 and 99!"
response_module_tempchannels_edit_user_limit_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the user limit of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_user_limit_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to change the user limit of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_edit_user_limit_failed_module_disabled = (
    "{datetime} -- **{member}** tried to change the user limit of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_edit_user_limit_failed_module_unknown = "{datetime} -- **{member}** tried to change the user limit of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_user_limit_failed_settings_not_found = "{datetime} -- **{member}** tried to change the user limit of a tempchannel but something went wrong while getting the settings for the server!"
## Age restriction
response_module_tempchannels_edit_age_restriction_success = (
    "{datetime} -- **{member}** has changed the age restiction setting of a tempchannel!"
)
response_module_tempchannels_edit_age_restriction_failed = (
    "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but something went wrong!"
)
response_module_tempchannels_edit_age_restriction_failed_not_owner = (
    "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but they are not the owner!"
)
response_module_tempchannels_edit_age_restriction_failed_no_tempchannel_found = "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but the given tempchannel is not found!"
response_module_tempchannels_edit_age_restriction_failed_module_disabled = "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but `tempchannels` module is disabled!"
response_module_tempchannels_edit_age_restriction_failed_module_unknown = "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_edit_age_restriction_failed_settings_not_found = "{datetime} -- **{member}** tried to change the age restiction setting of a tempchannel but something went wrong while getting the settings for the server!"
## Transfer
response_module_tempchannels_transfer_success = "{datetime} -- **{member}** has transferred ownership of a tempchannel!"
response_module_tempchannels_transfer_failed = (
    "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but something went wrong!"
)
response_module_tempchannels_transfer_failed_data_collection_enabled = "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but the new owner has data collection disabled!"
response_module_tempchannels_transfer_failed_member_is_bot = "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but the new owner has data collection disabled!"
response_module_tempchannels_transfer_failed_not_owner = (
    "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but they are not the owner!"
)
response_module_tempchannels_transfer_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_transfer_failed_module_disabled = (
    "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_transfer_failed_module_unknown = "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_transfer_failed_settings_not_found = "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but something went wrong while getting the settings for the server!"
## Claim
response_module_tempchannels_claim_success = "{datetime} -- **{member}** has claimed ownership of a tempchannel!"
response_module_tempchannels_claim_failed = (
    "{datetime} -- **{member}** tried to claim ownership of a tempchannel but something went wrong!"
)
response_module_tempchannels_claim_failed_data_collection_enabled = (
    "{datetime} -- **{member}** tried to claim ownership of a tempchannel but they have data collection disabled!"
)
response_module_tempchannels_claim_failed_owner_linked = (
    "{datetime} -- **{member}** tried to claim ownership of a tempchannel but there is still an owner linked!"
)
response_module_tempchannels_claim_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to claim ownership of a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_claim_failed_module_disabled = (
    "{datetime} -- **{member}** tried to claim ownership of a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_claim_failed_module_unknown = "{datetime} -- **{member}** tried to claim ownership of a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_claim_failed_settings_not_found = "{datetime} -- **{member}** tried to claim ownership of a tempchannel but something went wrong while getting the settings for the server!"
## Delete
response_module_tempchannels_delete_success = "{datetime} -- **{member}** has deleted a tempchannel set!"
response_module_tempchannels_delete_failed = (
    "{datetime} -- **{member}** tried to delete a tempchannel set but something went wrong!"
)
response_module_tempchannels_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a tempchannel set but they are not the owner!"
)
response_module_tempchannels_delete_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to delete a tempchannel set but the given tempchannel is not found!"
)
response_module_tempchannels_delete_failed_module_disabled = (
    "{datetime} -- **{member}** tried to delete a tempchannel set but `tempchannels` module is disabled!"
)
response_module_tempchannels_delete_failed_module_unknown = "{datetime} -- **{member}** tried to delete a tempchannel set but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_delete_failed_settings_not_found = "{datetime} -- **{member}** tried to delete a tempchannel set but something went wrong while getting the settings for the server!"
## Trust rules
response_module_tempchannels_trust_rule_add_success = (
    "{datetime} -- **{member}** has added a trust rule to a tempchannel!"
)
response_module_tempchannels_trust_rule_add_failed = (
    "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but something went wrong!"
)
response_module_tempchannels_trust_rule_add_failed_not_owner = (
    "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but they are not the owner!"
)
response_module_tempchannels_trust_rule_add_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_trust_rule_add_failed_module_disabled = (
    "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_trust_rule_add_failed_module_unknown = "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_trust_rule_add_failed_settings_not_found = "{datetime} -- **{member}** tried to add a trust rule to a tempchannel but something went wrong while getting the settings for the server!"
response_module_tempchannels_trust_rule_delete_success = (
    "{datetime} -- **{member}** has deleted a trust rule from a tempchannel!"
)
response_module_tempchannels_trust_rule_delete_failed = (
    "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but something went wrong!"
)
response_module_tempchannels_trust_rule_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but they are not the owner!"
)
response_module_tempchannels_trust_rule_delete_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_trust_rule_delete_failed_module_disabled = (
    "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_trust_rule_delete_failed_module_unknown = "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_trust_rule_delete_failed_settings_not_found = "{datetime} -- **{member}** tried to delete a trust rule from a tempchannel but something went wrong while getting the settings for the server!"
## Block rules
response_module_tempchannels_block_rule_add_success = (
    "{datetime} -- **{member}** has added a block rule to a tempchannel!"
)
response_module_tempchannels_block_rule_add_failed = (
    "{datetime} -- **{member}** tried to add a block rule to a tempchannel but something went wrong!"
)
response_module_tempchannels_block_rule_add_failed_not_owner = (
    "{datetime} -- **{member}** tried to add a block rule to a tempchannel but they are not the owner!"
)
response_module_tempchannels_block_rule_add_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to add a block rule to a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_block_rule_add_failed_module_disabled = (
    "{datetime} -- **{member}** tried to add a block rule to a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_block_rule_add_failed_module_unknown = "{datetime} -- **{member}** tried to add a block rule to a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_block_rule_add_failed_settings_not_found = "{datetime} -- **{member}** tried to add a block rule to a tempchannel but something went wrong while getting the settings for the server!"
response_module_tempchannels_block_rule_delete_success = (
    "{datetime} -- **{member}** has deleted a block rule from a tempchannel!"
)
response_module_tempchannels_block_rule_delete_failed = (
    "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but something went wrong!"
)
response_module_tempchannels_block_rule_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but they are not the owner!"
)
response_module_tempchannels_block_rule_delete_failed_no_tempchannel_found = (
    "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but the given tempchannel is not found!"
)
response_module_tempchannels_block_rule_delete_failed_module_disabled = (
    "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but `tempchannels` module is disabled!"
)
response_module_tempchannels_block_rule_delete_failed_module_unknown = "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but the status of the `tempchannels` module is unknown!"
response_module_tempchannels_block_rule_delete_failed_settings_not_found = "{datetime} -- **{member}** tried to delete a block rule from a tempchannel but something went wrong while getting the settings for the server!"

## Module Welcoming
### Disable
response_module_welcoming_disabled = (
    "{datetime} -- **{member}** has disabled the `welcoming` module! All related settings are removed!"
)
response_module_welcoming_disable_failed = "{datetime} -- **{member}** tried to disable the `welcoming` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_welcoming_enabled = "{datetime} -- **{member}** has enabled the `welcoming` module!"
response_module_welcoming_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `welcoming` module but something went wrong!"
)
### Settings
response_module_welcoming_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `welcoming` module!"
)
response_module_welcoming_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `welcoming` module but something has gone wrong! Not all settings may have been changed!"
### Responses
response_module_welcoming_response_created = (
    "{datetime} -- **{member}** has created a new response for the `welcoming` module!"
)
response_module_welcoming_response_create_failed = (
    "{datetime} -- **{member}** tried to create a new response for the `welcoming` module but something has gone wrong!"
)
response_module_welcoming_response_create_failed_response_type_limit_reached = "{datetime} -- **{member}** tried to create a new response for the `welcoming` module but the limit for the given response type has been reached!"
response_module_welcoming_response_create_failed_invalid_response_type = "{datetime} -- **{member}** tried to create a new response for the `welcoming` module but the given response type is invalid!"
response_module_welcoming_response_deleted = (
    "{datetime} -- **{member}** has deleted a response for the `welcoming` module!"
)
response_module_welcoming_response_delete_failed = (
    "{datetime} -- **{member}** tried to delete a response for the `welcoming` module but something has gone wrong!"
)
### Timedroles
response_module_welcoming_timedrole_created = (
    "{datetime} -- **{member}** has created a new timedrole for the `welcoming` module!"
)
response_module_welcoming_timedrole_create_failed = "{datetime} -- **{member}** tried to create a new timedrole for the `welcoming` module but something has gone wrong!"
response_module_welcoming_timedrole_create_failed_limit_reached = "{datetime} -- **{member}** tried to create a new timedrole for the `welcoming` module but the limit has been reached!"
response_module_welcoming_timedrole_deleted = (
    "{datetime} -- **{member}** has deleted a timedrole for the `welcoming` module!"
)
response_module_welcoming_timedrole_delete_failed = (
    "{datetime} -- **{member}** tried to delete a timedrole for the `welcoming` module but something has gone wrong!"
)
### Check
response_module_welcoming_check_dm = "{datetime} -- Checked welcoming message in DM for new member: **{member}**!"
response_module_welcoming_check_channel = (
    "{datetime} -- Checked welcoming message in channel for new member: **{member}**!"
)
response_module_leaving_check_channel = "{datetime} -- Checked leaving message in channel for member: **{member}**!"
response_module_welcoming_check_role_on_join = "{datetime} -- Checked autorole for new member: **{member}**!"
response_module_welcoming_check_role_timed = "{datetime} -- Added timedrole to member: **{member}**!"

## Module Reactionroles
### Disable
response_module_reactionroles_disabled = "{datetime} -- **{member}** has disabled the `reactionroles` module! All related settings are removed any left over reactionrole panels can safely be removed!"
response_module_reactionroles_disable_failed = "{datetime} -- **{member}** tried to disable the `reactionroles` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_reactionroles_enabled = "{datetime} -- **{member}** has enabled the `reactionroles` module!"
response_module_reactionroles_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `reactionroles` module but something went wrong!"
)
### Settings
response_module_reactionroles_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `reactionroles` module!"
)
response_module_reactionroles_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `reactionroles` module but something has gone wrong! Not all settings may have been changed!"
### Create
response_module_reactionroles_reactionrole_panel_created = "{datetime} -- **{member}** created a reactionrole panel!"
response_module_reactionroles_reactionrole_panel_create_failed = (
    "{datetime} -- **{member}** tried to create a reactionrole panel but someting went wrong!"
)
response_module_reactionroles_reactionrole_panel_create_failed_panel_limit_reached = (
    "{datetime} -- **{member}** tried to create a reactionrole panel but the panel limit has been reached!"
)
response_module_reactionroles_reactionrole_panel_create_failed_incorrect_panel_type = (
    "{datetime} -- **{member}** tried to create a reactionrole panel but they didn't provide a correct panel type!"
)
### Delete
response_module_reactionroles_reactionrole_panel_deleted = (
    "{datetime} -- **{member}** deleted a reactionrole panel! Any leftovers can safely be removed!"
)
response_module_reactionroles_reactionrole_panel_delete_failed = (
    "{datetime} -- **{member}** tried to delete a reactionrole panel but someting went wrong!"
)
### Edit
response_module_reactionroles_reactionrole_panel_edited = "{datetime} -- **{member}** edited a reactionrole panel!"
response_module_reactionroles_reactionrole_panel_edit_failed = (
    "{datetime} -- **{member}** tried to edit a reactionrole panel but someting went wrong!"
)
response_module_reactionroles_reactionrole_panel_edit_failed_invalid_panel_type = (
    "{datetime} -- **{member}** tried to edit a reactionrole panel but they didn't provide a correct panel type!"
)
### Entry added
response_module_reactionroles_reactionrole_entry_added = (
    "{datetime} -- **{member}** added a reactionrole entry to a panel!"
)
response_module_reactionroles_reactionrole_entry_add_failed = "{datetime} -- **{member}** tried to add a reactionrole entry to a panel but something went wrong! If changes related to this action have persisted, they can safely be removed!"
response_module_reactionroles_reactionrole_entry_add_failed_emoji_limit_reached = "{datetime} -- **{member}** tried to add a reactionrole entry to a panel but the limit for emoji entries has been reached!"
response_module_reactionroles_reactionrole_entry_add_failed_button_limit_reached = "{datetime} -- **{member}** tried to add a reactionrole entry to a panel but the limit for buttons has been reached!"
response_module_reactionroles_reactionrole_entry_add_failed_dropdown_limit_reached = "{datetime} -- **{member}** tried to add a reactionrole entry to a panel but the limit for dropdown items has been reached!"
### Entry deleted
response_module_reactionroles_reactionrole_entry_deleted = (
    "{datetime} -- **{member}** deleted a reactionrole entry from a panel!"
)
response_module_reactionroles_reactionrole_entry_delete_failed = "{datetime} -- **{member}** tried to delete a reactionrole entry from a panel but something went wrong! Any leftovers can safely be removed!"
### Entry edited
response_module_reactionroles_reactionrole_entry_edited = (
    "{datetime} -- **{member}** edited a reactionrole entry for a panel!"
)
response_module_reactionroles_reactionrole_entry_edit_failed = (
    "{datetime} -- **{member}** tried to edit a reactionrole entry for a panel but something went wrong!"
)

## Module Tickets
### Disable
response_module_tickets_disabled = "{datetime} -- **{member}** has disabled the `tickets` module! All related settings are removed! Any leftovers can safely be removed!"
response_module_tickets_disable_failed = "{datetime} -- **{member}** tried to disable the `tickets` module but something went wrong! Some of the configuration might be changed!"
### Enable
response_module_tickets_enabled = "{datetime} -- **{member}** has enabled the `tickets` module!"
response_module_tickets_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `tickets` module but something went wrong!"
)
### Panels
response_module_tickets_panel_created = "{datetime} -- **{member}** has created a new ticket panel!"
response_module_tickets_panel_create_failed = (
    "{datetime} -- **{member}** tried to create a new ticket panel but something went wrong!"
)
response_module_tickets_panel_create_failed_no_open_ticket_categories = (
    "{datetime} -- **{member}** tried to create a new ticket panel but they did not provide open ticket categories!"
)
response_module_tickets_panel_create_failed_invalid_category_or_channel = "{datetime} -- **{member}** tried to create a new ticket panel but they provided a wrong combination of category and channel!"
response_module_tickets_panel_create_failed_incorrect_panel_type = (
    "{datetime} -- **{member}** tried to create a new ticket panel but they provided a wrong ticket panel type!"
)
response_module_tickets_panel_create_failed_panel_limit_reached = "{datetime} -- **{member}** tried to create a new ticket panel but the limit of ticket panels has already been reached!"
response_module_tickets_panel_edited = "{datetime} -- **{member}** has edited a ticket panel!"
response_module_tickets_panel_edit_failed = (
    "{datetime} -- **{member}** tried to edit a ticket panel but something went wrong!"
)
response_module_tickets_panel_edit_failed_invalid_panel_type = (
    "{datetime} -- **{member}** tried to edit a ticket panel but they provided a wrong ticket panel type!"
)
response_module_tickets_panel_deleted = "{datetime} -- **{member}** has deleted a ticket panel!"
response_module_tickets_panel_delete_failed = (
    "{datetime} -- **{member}** has tried to delete a ticket panel but something went wrong!"
)
### Ticket types
response_module_tickets_type_added = "{datetime} -- **{member}** has added a ticket type to a panel!"
response_module_tickets_type_add_failed = (
    "{datetime} -- **{member}** tried to add a ticket type to a panel but something went wrong!"
)
response_module_tickets_type_add_failed_limit_reached = (
    "{datetime} -- **{member}** tried to add a ticket type to a panel but the limit has been reached!"
)
response_module_tickets_type_removed = "{datetime} -- **{member}** has removed a ticket type from a panel!"
response_module_tickets_type_remove_failed = "{datetime} -- **{member}** has removed a ticket type from a panel!"
### Create
response_module_ticket_created = "{datetime} -- **{member}** created a new ticket!"
response_module_ticket_create_failed = "{datetime} -- **{member}** tried to create a ticket but something went wrong!"
response_module_ticket_create_failed_open_message = "{datetime} -- **{member}** tried to create a ticket but something went wrong while sending the open message. The channel may have been created but can safely be removed!"
response_module_ticket_create_failed_open_ticket_categories_full = "{datetime} -- **{member}** tried to create a ticket but the open tickets category is full. The ticket has not been created!"
response_module_ticket_create_failed_no_open_ticket_categories = "{datetime} -- **{member}** tried to create a ticket but there are no open tickets category configured. The ticket has not been created!"
response_module_ticket_create_failed_thread_create = "{datetime} -- **{member}** tried to create a ticket but something went wrong while creating/configuring the thread channel. If the thread is created, it can safely be removed!"
response_module_ticket_create_failed_invalid_member = (
    "{datetime} -- **{member}** tried to create a ticket but the member is not valid!"
)
response_module_ticket_create_failed_max_active_ticket_reached = (
    "{datetime} -- **{member}** tried to create a ticket but the maximum number of active tickets has been reached!"
)
response_module_ticket_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a ticket but the servers settings could not be found!"
)
response_module_ticket_create_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to create a ticket but they have prevent data collection enabled!"
)
### Form show
response_module_ticket_form_showed = "{datetime} -- The ticket form has been showed to **{member}**!"
response_module_ticket_form_show_failed_invalid_form_config = (
    "{datetime} -- Tried to show the ticket form to **{member}** but the configured form is invalid!"
)
response_module_ticket_form_show_failed_no_form_config = "{datetime} -- Tried to show the ticket form to **{member}** but there is no form configured even though it is enabled!"
### Delete
response_module_ticket_deleted = "{datetime} -- **{member}** deleted a ticket!"
response_module_ticket_delete_failed = "{datetime} -- **{member}** tried to delete a ticket but something went wrong!"
response_module_ticket_delete_failed_not_an_administrator = (
    "{datetime} -- **{member}** tried to delete a ticket but they are not an administrator!"
)
response_module_ticket_delete_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to delete a ticket but the ticket is not found!"
)
response_module_ticket_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete a ticket but the server settings were not found!"
)
### Transfer
response_module_ticket_transferred = "{datetime} -- **{member}** has transferred a ticket to another support engineer!"
response_module_ticket_transfer_failed = (
    "{datetime} -- **{member}** tried to transfer a ticket to another support engineer but something wen wrong!"
)
response_module_ticket_transfer_failed_not_support_engineer = (
    "{datetime} -- **{member}** tried to transfer a ticket but the target was not a support engineer!"
)
response_module_ticket_transfer_failed_not_current_support_engineer = "{datetime} -- **{member}** tried to transfer a ticket but they are not the current support engineer for the ticket!"
response_module_ticket_transfer_failed_panel_not_found = "{datetime} -- **{member}** tried to transfer a ticket to another support engineer but the panel used to create the ticket is not found!"
response_module_ticket_transfer_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to transfer a ticket to another support engineer but the ticket is not found!"
)
response_module_ticket_transfer_failed_settings_not_found = "{datetime} -- **{member}** tried to transfer a ticket to another support engineer but the servers settings are not found!"
response_module_ticket_transfer_failed_prevent_data_collection = "{datetime} -- **{member}** tried to transfer a ticket to another support engineer but the other engineer has prevent data collection enabled!"
### Reopen
response_module_ticket_reopened = "{datetime} -- **{member}** reopened a ticket!"
response_module_ticket_reopen_failed = "{datetime} -- **{member}** tried to reopen a ticket but something went wrong!"
response_module_ticket_reopen_move_failed_full = "{datetime} -- **{member}** reopened a ticket but moving the ticket to a open ticket category failed because the configured categories are full!"
response_module_ticket_reopen_move_failed_empty = "{datetime} -- **{member}** reopened a ticket but moving the ticket to a open ticket category failed because there are no open ticket categories configured!"
response_module_ticket_reopen_failed_not_current_support_engineer = (
    "{datetime} -- **{member}** tried to reopen a ticket but they are not the current support engineer for that ticket!"
)
response_module_ticket_reopen_failed_panel_not_found = (
    "{datetime} -- **{member}** tried to reopen a ticket but the panel used to create the ticket is not found!"
)
response_module_ticket_reopen_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to reopen a ticket but the ticket is not found!"
)
response_module_ticket_reopen_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to reopen a ticket but the servers settings are not found!"
)
### Close
response_module_ticket_closed = "{datetime} -- **{member}** closed a ticket!"
response_module_ticket_close_failed = "{datetime} -- **{member}** tried to close a ticket but something went wrong!"
response_module_ticket_close_move_failed_full = "{datetime} -- **{member}** closed a ticket but moving the ticket to a closed ticket category failed because the configured categories are full!"
response_module_ticket_close_move_failed_empty = "{datetime} -- **{member}** closed a ticket but moving the ticket to a closed ticket category failed because there are no closed ticket categories configured!"
response_module_ticket_close_failed_not_current_support_engineer = (
    "{datetime} -- **{member}** tried to close a ticket but they are not the current support engineer for that ticket!"
)
response_module_ticket_close_failed_panel_not_found = (
    "{datetime} -- **{member}** tried to close a ticket but the panel used to create the ticket is not found!"
)
response_module_ticket_close_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to close a ticket but the ticket is not found!"
)
response_module_ticket_close_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to close a ticket but the servers settings are not found!"
)
### Claim
response_module_ticket_claimed = "{datetime} -- **{member}** claimed a ticket and will start working on solving it!"
response_module_ticket_claim_failed = "{datetime} -- **{member}** tried to claim a ticket but something went wrong!"
response_module_ticket_claim_failed_not_support_engineer = (
    "{datetime} -- **{member}** tried to claim a ticket but they are not a support engineer!"
)
response_module_ticket_claim_failed_invalid_member = (
    "{datetime} -- **{member}** tried to claim a ticket but they are not a valid member!"
)
response_module_ticket_claim_failed_panel_not_found = (
    "{datetime} -- **{member}** tried to claim a ticket but the panel used to create the ticket is not found!"
)
response_module_ticket_claim_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to claim a ticket but the ticket is not found!"
)
response_module_ticket_claim_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to claim a ticket but the servers settings are not found!"
)
response_module_ticket_claim_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to claim a ticket but they have prevent data collection enabled!"
)
### Transcribe
response_module_ticket_transcribed = "{datetime} -- **{member}** transcribed a ticket!"
response_module_ticket_transcribe_failed = (
    "{datetime} -- **{member}** tried to transcribe a ticket but something went wrong!"
)
response_module_ticket_transcribe_failed_panel_not_found = "{datetime} -- **{member}** tried to transcribe a ticket but the ticket panel used to create the ticket was not found!"
response_module_ticket_transcribe_failed_ticket_not_found = (
    "{datetime} -- **{member}** tried to transcribe a ticket but the ticket was not found!"
)
response_module_ticket_transcribe_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to transcribe a ticket but the server settings where not found!"
)
response_module_ticket_transcribe_failed_not_allowed = "{datetime} -- **{member}** tried to transcribe a ticket but they are not the creator or the current support engineer!"

## Module Serverstats
### Disable
response_module_serverstats_disabled = (
    "{datetime} -- **{member}** has disabled the `serverstats` module! All related settings are removed!"
)
response_module_serverstats_disable_failed = "{datetime} -- **{member}** tried to disable the `serverstats` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_serverstats_enabled = "{datetime} -- **{member}** has enabled the `serverstats` module!"
response_module_serverstats_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `serverstats` module but something went wrong!"
)
### Settings
response_module_serverstats_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `serverstats` module!"
)
response_module_serverstats_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `serverstats` module but something has gone wrong! Not all settings may have been changed!"
### Starboard
response_module_serverstats_starboard_check_edit = (
    "{datetime} -- **{member}** has caused a check for the starboard, causing an edit of an existing message!"
)
response_module_serverstats_starboard_check_create = (
    "{datetime} -- **{member}** has caused a check for the starboard, causing the creation of a new starboard message!"
)
response_module_serverstats_starboard_check_delete = (
    "{datetime} -- **{member}** has caused a check for the starboard, causing the deletion of a starboard message!"
)

### Counters
response_module_serverstats_counters_updated = "{datetime} -- The counters for this server have been updated!"
response_module_serverstats_counter_created = "{datetime} -- **{member}** has created a new counter!"
response_module_serverstats_counter_create_failed = (
    "{datetime} -- **{member}** tried to create a new counter but something went wrong!"
)
response_module_serverstats_counter_create_failed_invalid_counter_type = (
    "{datetime} -- **{member}** tried to create a new counter but they gave an invalid counter type!"
)
response_module_serverstats_counter_create_failed_max_counters_reached = "{datetime} -- **{member}** tried to create a new counter but the maximum number of counters has already been reached!"
response_module_serverstats_counter_create_failed_counters_disabled = (
    "{datetime} -- **{member}** tried to create a new counter but counters are disabled!"
)
response_module_serverstats_counter_deleted = "{datetime} -- **{member}** has deleted a counter!"
response_module_serverstats_counter_delete_failed = (
    "{datetime} -- **{member}** tried to delete a counter but something went wrong!"
)

## Module Socials
### Disable
response_module_socials_disabled = (
    "{datetime} -- **{member}** has disabled the `socials` module! All related settings are removed!"
)
response_module_socials_disable_failed = "{datetime} -- **{member}** tried to disable the `socials` module but something went wrong! Some of the configuration might be changed!"
### Enable
response_module_socials_enabled = "{datetime} -- **{member}** has enabled the `socials` module!"
response_module_socials_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `socials` module but something went wrong!"
)
### Settings
response_module_socials_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `socials` module!"
)
response_module_socials_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `socials` module but something has gone wrong! Not all settings may have been changed!"
### Twitch
response_module_twitch_added = "{datetime} -- **{member}** added Twitch account: `{twitch_account}` to the `socials` module monitored Twitch accounts list!"
response_module_twitch_add_failed = "{datetime} -- **{member}** tried to add Twitch account: `{twitch_account}` to the `socials` module monitored Twitch accounts list but something went wrong!"
response_module_twitch_add_failed_limit_reached = "{datetime} -- **{member}** tried to add Twitch account: `{twitch_account}` to the `socials` module monitored Twitch accounts list but the limit of Twitch accounts is reached!"
response_module_twitch_add_failed_already_added = "{datetime} -- **{member}** tried to add Twitch account: `{twitch_account}` to the `socials` module monitored Twitch accounts list but the Twitch account is already in the list!"
response_module_twitch_add_failed_component_disabled = "{datetime} -- **{member}** tried to add Twitch account: `{twitch_account}` to the `socials` module monitored Twitch accounts list but the Twitch component is disabled!"
response_module_twitch_removed = "{datetime} -- **{member}** removed Twitch account: `{twitch_account}` from the `socials` module monitored Twitch accounts list!"
response_module_twitch_remove_failed = "{datetime} -- **{member}** tried to remove Twitch account: `{twitch_account}` from the `socials` module monitored Twitch accounts list but something went wrong!"
### YouTube
response_module_youtube_added = "{datetime} -- **{member}** added YouTube channel: `{youtube_channel}` to the `socials` module monitored YouTube channel list!"
response_module_youtube_add_failed = "{datetime} -- **{member}** tried to add YouTube channel: `{youtube_channel}` to the `socials` module monitored YouTube channel list but something went wrong!"
response_module_youtube_add_failed_limit_reached = "{datetime} -- **{member}** tried to add YouTube channel: `{youtube_channel}` to the `socials` module monitored YouTube channel list but the limit of YouTube accounts is reached!"
response_module_youtube_add_failed_already_added = "{datetime} -- **{member}** tried to add YouTube channel: `{youtube_channel}` to the `socials` module monitored YouTube channel list but the YouTube account is already in the list!"
response_module_youtube_add_failed_component_disabled = "{datetime} -- **{member}** tried to add YouTube channel: `{youtube_channel}` to the `socials` module monitored YouTube channel list but the YouTube component is disabled!"
response_module_youtube_removed = "{datetime} -- **{member}** removed YouTube channel: `{youtube_channel}` from the `socials` module monitored YouTube channel list!"
response_module_youtube_remove_failed = "{datetime} -- **{member}** tried to remove YouTube channel: `{youtube_channel}` from the `socials` module monitored YouTube channel list but something went wrong!"
### RSS
response_module_rss_added = (
    "{datetime} -- **{member}** added the RSS Feed: `{feed}` to the `socials` module monitored rss feeds list!"
)
response_module_rss_add_failed = "{datetime} -- **{member}** tried to add RSS Feed: `{feed}` to the `socials` module monitored rss feeds list but something went wrong!"
response_module_rss_add_failed_limit_reached = "{datetime} -- **{member}** tried to add RSS Feed: `{feed}` to the `socials` module monitored rss feeds list but the limit of RSS feeds is reached!"
response_module_rss_add_failed_already_added = "{datetime} -- **{member}** tried to add RSS Feed: `{feed}` to the `socials` module monitored rss feeds list but the RSS feeds is already in the list!"
response_module_rss_add_failed_component_disabled = "{datetime} -- **{member}** tried to add RSS Feed: `{feed}` to the `socials` module monitored rss feeds list but the RSS component is disabled!"
response_module_rss_removed = (
    "{datetime} -- **{member}** removed RSS Feed: `{feed}` from the `socials` module monitored rss feeds list!"
)
response_module_rss_remove_failed = "{datetime} -- **{member}** tried to remove RSS Feed: `{feed}` from the `socials` module monitored rss feeds list but something went wrong!"
### Reddit
response_module_reddit_added = (
    "{datetime} -- **{member}** added Subreddit: `{subreddit}` to the `socials` module monitored subreddits list!"
)
response_module_reddit_add_failed = "{datetime} -- **{member}** tried to add Subreddit: `{subreddit}` to the `socials` module monitored subreddits list but something went wrong!"
response_module_reddit_add_failed_limit_reached = "{datetime} -- **{member}** tried to add Subreddit: `{subreddit}` to the `socials` module monitored subreddits list but the limit of Subreddits is reached!"
response_module_reddit_add_failed_already_added = "{datetime} -- **{member}** tried to add Subreddit: `{subreddit}` to the `socials` module monitored subreddits list but the Subreddit is already in the list!"
response_module_reddit_add_failed_component_disabled = "{datetime} -- **{member}** tried to add Subreddit: `{subreddit}` to the `socials` module monitored subreddits list but the reddit component is disabled!"
response_module_reddit_removed = (
    "{datetime} -- **{member}** removed Subreddit: `{subreddit}` from the `socials` module monitored subreddits list!"
)
response_module_reddit_remove_failed = "{datetime} -- **{member}** tried to remove the Subreddit: `{subreddit}` from the `socials` module monitored subreddits list but something went wrong!"

## Module tags
### Disable
response_module_tags_disabled = (
    "{datetime} -- **{member}** has disabled the `tags` module! All related settings are removed!"
)
response_module_tags_disable_failed = "{datetime} -- **{member}** tried to disable the `tags` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_tags_enabled = "{datetime} -- **{member}** has enabled the `tags` module!"
response_module_tags_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `tags` module but something went wrong!"
)
### Create
response_tag_create_success = "{datetime} -- **{member}** has created a new tag. Tag ID: `{tag_id}`!"
response_tag_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a new tag but something went wrong with getting the servers settings!"
)
response_tag_create_failed_invalid_visibility = (
    "{datetime} -- **{member}** tried to create a new tag but provided a wrong visibility!"
)
response_tag_create_failed_limit_reached = (
    "{datetime} -- **{member}** tried to create a new tag but the servers tags limit has been reached!"
)
response_tag_create_failed = "{datetime} -- **{member}** tried to create a tag but something went wrong!"
response_tag_create_failed_names = "{datetime} -- **{member}** tried to create a tag but something went wrong with registering the names. However the tag itself has been created!"
response_tag_create_failed_prevent_data_collection_enabled = (
    "{datetime} -- **{member}** tried to create a tag but they have disabled data collection in this server!"
)
### Delete
response_tag_delete_success = "{datetime} -- **{member}** deleted the tag with ID: `{tag_id}`!"
response_tag_delete_failed_settings_not_found = "{datetime} -- **{member}** tried to delete the tag with ID: `{tag_id}` but something went wrong with getting the servers settings!"
response_tag_delete_failed_no_tag_given = "{datetime} -- **{member}** tried to delete a tag but didn't provide the ID!"
response_tag_delete_failed_no_tag_found = (
    "{datetime} -- **{member}** tried to delete the tag with ID: `{tag_id}` but that tag did not exist!"
)
response_tag_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete the tag with ID: `{tag_id}` but they are not the owner of the tag!"
)
response_tag_delete_failed = (
    "{datetime} -- **{member}** tried to delete the tag with ID: `{tag_id}` but something went wrong!"
)
### Edit
response_tag_edit_success = "{datetime} -- **{member}** edited a tag with ID: `{tag_id}`!"
response_tag_edit_failed_settings_not_found = "{datetime} -- **{member}** tried to edit the tag with ID: `{tag_id}` but something went wrong with getting the servers settings!"
response_tag_edit_failed_no_tag_given = "{datetime} -- **{member}** tried to edit a tag but didn't provide the ID!"
response_tag_edit_failed_no_tag_found = (
    "{datetime} -- **{member}** tried to edit the tag with ID: `{tag_id}` but that tag did not exist!"
)
response_tag_edit_failed_not_owner = (
    "{datetime} -- **{member}** tried to edit the tag with ID: `{tag_id}` but they are not the owner of the tag!"
)
response_tag_edit_failed = (
    "{datetime} -- **{member}** tried to edit a tag with ID: `{tag_id}` but something went wrong!"
)
### Send
response_tag_send_success = "{datetime} -- **{member}** used the tag with ID: `{tag_id}`!"
response_tag_send_failed_settings_not_found = "{datetime} -- **{member}** tried to send the tag with ID: `{tag_id}` but something went wrong with getting the servers settings!"
response_tag_send_failed_module_disabled = (
    "{datetime} -- **{member}** tried to send the tag with ID: `{tag_id}` but the tags module is disabled!"
)
response_tag_send_failed_no_such_tag = (
    "{datetime} -- **{member}** tried to send a tag with ID: `{tag_id}` but it does not exist!"
)
response_tag_send_failed_not_owner_and_private = "{datetime} -- **{member}** tried to send a tag with ID: `{tag_id}` but they are not the owner of the tag and the owner has set the tag to private!"
### Preview
response_tag_preview_success = "{datetime} -- **{member}** has previewed a tag with ID: `{tag_id}`!"
response_tag_preview_failed_settings_not_found = "{datetime} -- **{member}** tried to preview the tag with ID: `{tag_id}` but something went wrong with getting the servers settings!"
response_tag_preview_failed_module_disabled = (
    "{datetime} -- **{member}** tried to preview the tag with ID: `{tag_id}` but the tags module is disabled!"
)
response_tag_preview_failed_no_such_tag = (
    "{datetime} -- **{member}** tried to preview a tag with ID: `{tag_id}` but it does not exist!"
)

## Module verifier
### Disable
response_module_verifier_disabled = (
    "{datetime} -- **{member}** has disabled the `verifier` module! All related settings are removed!"
)
response_module_verifier_disable_failed = "{datetime} -- **{member}** tried to disable the `verifier` module but something went wrong! I have not changed the configuration!"
### Enable
response_module_verifier_enabled = "{datetime} -- **{member}** has enabled the `verifier` module!"
response_module_verifier_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `verifier` module but something went wrong!"
)
### Settings
response_module_verifier_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `verifier` module!"
)
response_module_verifier_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `verifier` module but not all changes could be completed!"
response_module_verifier_settings_change_failed_invalid_verifier_type = "{datetime} -- **{member}** tried to change the settings of the `verifier` module but they did not provide a valid verifier type!"
### Create verification
response_module_verifier_verification_created = "{datetime} -- A verification has been created for: **{member}**!"
response_module_verifier_verification_create_failed = (
    "{datetime} -- Something went wrong while creating a verification for: **{member}**!"
)
response_module_verifier_verification_create_failed_settings_not_found = "{datetime} -- Something went wrong while creating a verification for: **{member}**! The settings of the servers where not found!"
response_module_verifier_verification_create_failed_invalid_member = (
    "{datetime} -- Something went wrong while creating a verification. The target member was not valid!"
)
response_module_verifier_verification_create_failed_not_administrator = "{datetime} -- **{member}** tried to create a verification using the `/verifier entry retrigger` command but they are not an administrator!"
### Handle verifiation
response_module_verifier_verification_handle_success = "{datetime} -- **{member}** has been verified!"
response_module_verifier_verification_handle_failed = (
    "{datetime} -- **{member}** tried to verify themself but something went wrong!"
)
response_module_verifier_verification_handle_failed_not_target_user = "{datetime} -- **{member}** tried to verify themself but they were not the user that needed to verify with the entry!"
response_module_verifier_verification_handle_failed_already_verified = (
    "{datetime} -- **{member}** tried to verify themself but the entry verification was already completed!"
)
response_module_verifier_verification_handle_failed_invalid_member = (
    "{datetime} -- Something went wrong while handling the verification. The target member was not valid!"
)

## Module rules
### Disable
response_module_rules_disabled = (
    "{datetime} -- **{member}** has disabled the `rules` module! All related settings are removed!"
)
response_module_rules_disable_failed = "{datetime} -- **{member}** tried to disable the `rules` module but something went wrong! I have not changed the configuration!"
### Enable
response_module_rules_enabled = "{datetime} -- **{member}** has enabled the `rules` module!"
response_module_rules_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `rules` module but something went wrong!"
)
### Settings
response_module_rules_settings_changed = "{datetime} -- **{member}** has changed the settings of the `rules` module!"
response_module_rules_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `rules` module but not all changes could be completed!"
response_module_rules_settings_change_failed_invalid_rules_denied_action_type = "{datetime} -- **{member}** tried to change the settings of the `rules` module but gave in invalid rules denied action!"
### Rule create
response_module_rules_rule_created = "{datetime} -- **{member}** has created a new rule!"
response_module_rules_rule_create_failed = (
    "{datetime} -- **{member}** tried to create a new rule but something went wrong!"
)
response_module_rules_rule_create_failed_limit_reached = (
    "{datetime} -- **{member}** tried to create a new rule but the limit of rules has already been reached!"
)
response_module_rules_rule_create_failed_not_an_administrator = (
    "{datetime} -- **{member}** tried to create a new rule but they are not an administrator!"
)
response_module_rules_rule_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a new rule but the settings of the server are not found!"
)
### Rule delete
response_module_rules_rule_deleted = "{datetime} -- **{member}** has deleted a rule!"
response_module_rules_rule_delete_failed = "{datetime} -- **{member}** tried to delete a rule but something went wrong!"
response_module_rules_rule_delete_failed_not_an_administrator = (
    "{datetime} -- **{member}** tried to delete a rule but they are not an administrator!"
)
response_module_rules_rule_delete_failed_rule_not_found = (
    "{datetime} -- **{member}** tried to delete a rule but the given rule is not found!"
)
response_module_rules_rule_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete a rule but the servers settings are not found!"
)
### Send check
response_module_rules_send_check_success = "{datetime} -- Checking to send rules for **{member}** has been successful!"
response_module_rules_send_check_failed = "{datetime} -- Checking to send rules for **{member}** failed!"
response_module_rules_send_check_failed_no_rules_found = (
    "{datetime} -- Checking to send rules for **{member}** failed because there are no rules in this server!"
)
response_module_rules_send_check_failed_invalid_member = (
    "{datetime} -- Checking to send rules for **{member}** failed the target member is not valid!"
)
response_module_rules_send_check_failed_not_an_administrator = "{datetime} -- Checking to send rules for **{member}** failed because the initiator of the `/rules retrigger` command is not an administrator!"
response_module_rules_send_check_failed_module_disabled = (
    "{datetime} -- Checking to send rules for **{member}** failed because the `rules` module is disabled!"
)
response_module_rules_send_check_failed_module_status_unknown = (
    "{datetime} -- Checking to send rules for **{member}** failed because the status of the `rules` module is unknown!"
)
response_module_rules_send_check_failed_settings_not_found = (
    "{datetime} -- Checking to send rules for **{member}** failed because the settings of the server are unknown!"
)
### Interaction check
response_module_rules_interaction_check_success = "{datetime} -- Checking interaction with server rules for **{member}** has been successful. Appropriate actions have been taken!"
response_module_rules_interaction_check_failed = (
    "{datetime} -- Checking interaction with server rules for **{member}** failed!"
)
response_module_rules_interaction_check_failed_rules_actions_not_enabled = "{datetime} -- Checking interaction with server rules for **{member}** failed because the rules actions are not enabled in this server!"
response_module_rules_interaction_check_failed_active_entry_not_found = "{datetime} -- Checking interaction with server rules for **{member}** failed because the target member does not have an active rules entry!"
response_module_rules_interaction_check_failed_invalid_member = "{datetime} -- Checking interaction with server rules for **{member}** failed because the target member is not valid!"
response_module_rules_interaction_check_failed_module_disabled = "{datetime} -- Checking interaction with server rules for **{member}** failed because the `rules` module is disabled!"
response_module_rules_interaction_check_failed_module_status_unknown = "{datetime} -- Checking interaction with server rules for **{member}** failed because the status of the `rules` module is unknown!"
response_module_rules_interaction_check_failed_settings_not_found = "{datetime} -- Checking interaction with server rules for **{member}** failed because the servers settings are unknown!"

## Module invite tracker
### Disable
response_module_invite_tracker_disabled = (
    "{datetime} -- **{member}** has disabled the `invite tracker` module! All related settings are removed!"
)
response_module_invite_tracker_disable_failed = "{datetime} -- **{member}** tried to disable the `invite tracker` module but something went wrong! Some configuration might have changed!"
### Enable
response_module_invite_tracker_enabled = "{datetime} -- **{member}** has enabled the `invite tracker` module!"
response_module_invite_tracker_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `invite tracker` module but something went wrong!"
)
### Settings
response_module_invite_tracker_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `invite tracker` module!"
)
response_module_invite_tracker_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `invite tracker` module but not all settings could be changed!"
### Invite create
response_module_invite_tracker_invite_created = "{datetime} -- **{member}** has created a new invite link!"
response_module_invite_tracker_invite_create_failed = (
    "{datetime} -- **{member}** tried to create a new invite link but something went wrong!"
)
response_module_invite_tracker_invite_create_failed_to_save = "{datetime} -- **{member}** created an invite but I was not able to correctly save it to the known invites list and it can therefore not be tracked accuratly!"
response_module_invite_tracker_invite_create_failed_no_invite_found = (
    "{datetime} -- **{member}** may have created an invite but I could not find the invite in the server!"
)
response_module_invite_tracker_invite_create_failed_invalid_max_age = "{datetime} -- **{member}** tried to create a new invite but they didn't provide a correct value for the max age. It must be higher than 0!"
response_module_invite_tracker_invite_create_failed_invalid_max_uses = "{datetime} -- **{member}** tried to create a new invite but they didn't provide a correct value for the max uses. It must be between 0 (for infinite) and 100!"
response_module_invite_tracker_invite_create_failed_not_enough_permissions = (
    "{datetime} -- **{member}** tried to create a new invite but they didn't have enough permissions!"
)
response_module_invite_tracker_invite_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a new invite but it failed because the servers settings are unknown!"
)
response_module_invite_tracker_invite_create_failed_prevent_data_collection = "{datetime} -- **{member}** tried to create a new invite (or created one using discord that could not be saved) but have prevent data collection enabled!"
### Invite delete
response_module_invite_tracker_invite_deleted = "{datetime} -- **{member}** deleted an invite!"
response_module_invite_tracker_invite_delete_failed = "{datetime} -- **{member}** tried to delete an invite!"
response_module_invite_tracker_invite_delete_failed_to_remove = "{datetime} -- **{member}** deleted an invite but I could not remove it from the known invites list. Don't worry this will automatically be dealt with after its set expiry time!"
response_module_invite_tracker_invite_create_failed_not_an_administrator = (
    "{datetime} -- **{member}** tried to delete an invite but they are not a server administrator!"
)
response_module_invite_tracker_invite_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete an invite but it failed because the servers settings are unknown!"
)
### Invite based join
response_module_invite_tracker_joined = (
    "{datetime} -- **{member}** joined the server. They are invited by: **{inviter}**."
)
response_module_invite_tracker_joined_failed_to_track = "{datetime} -- **{member}** joined the server. Inviter: **{inviter}**. The use of the invite link could not be saved and the stats may therefore not be complete for {inviter}!"
response_module_invite_tracker_join_ignored_joined_is_inviter = "{datetime} -- **{member}** joined the server but they were also the inviter, this join will be ignored because prevent_own_invite_code is enabled!"
response_module_invite_tracker_join_failed_no_known_invite_found = (
    "{datetime} -- **{member}** joined the server using an unknown invite, this join will be ignored!"
)
### Invite based leave
response_module_invite_tracker_left = "{datetime} -- **{member}** left the server. They were invited by: **{inviter}**."

## Module Polls
### Disable
response_module_polls_disabled = "{datetime} -- **{member}** has disabled the `polls` module! All related settings are removed any left over polls can safely be removed!"
response_module_polls_disable_failed = "{datetime} -- **{member}** tried to disable the `polls` module but something went wrong! Some of the configuration might be changed!"
### Enable
response_module_polls_enabled = "{datetime} -- **{member}** has enabled the `polls` module!"
response_module_polls_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `polls` module but something went wrong!"
)
### Settings
response_module_polls_settings_changed = "{datetime} -- **{member}** has changed the settings of the `polls` module!"
response_module_polls_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `polls` module but something has gone wrong! Not all settings may have been changed!"
### Create
response_module_polls_poll_created = "{datetime} -- **{member}** has created a new poll!"
response_module_polls_poll_create_failed = "{datetime} -- **{member}** tried to create a poll but something went wrong!"
response_module_polls_poll_create_failed_invalid_discord_poll_wait_duration = "{datetime} -- **{member}** tried to create a discord poll but gave an invalid duration (must be between 1 and 768 hours)!"
response_module_polls_poll_create_failed_invalid_wait_duration = (
    "{datetime} -- **{member}** tried to create a poll but gave an invalid duration!"
)
response_module_polls_poll_create_failed_discord_poll_duration_required = "{datetime} -- **{member}** tried to create a discord poll but didn't provide a duration which is required for Discord polls!"
response_module_polls_poll_create_failed_answer_limit_reached = (
    "{datetime} -- **{member}** tried to create a poll but they went over the answer limit for this poll!"
)
response_module_polls_poll_create_failed_no_answer_provided = "{datetime} -- **{member}** tried to create a poll but they didn't provide an answer. At least one answer is required!"
response_module_polls_poll_create_failed_limit_reached = (
    "{datetime} -- **{member}** tried to create a poll but the poll limit has already been reached!"
)
response_module_polls_poll_create_failed_invalid_answer_type = (
    "{datetime} -- **{member}** tried to create a poll but they didn't provide a valid answer type!"
)
response_module_polls_poll_create_failed_invalid_poll_type = (
    "{datetime} -- **{member}** tried to create a poll but they didn't provide a valid poll type!"
)
response_module_polls_poll_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a poll but failed because the servers settings are unknown!"
)
response_module_polls_poll_create_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to create a poll but they have prevent data collection enabled!"
)
### EDIT
response_module_polls_poll_edited = "{datetime} -- **{member}** has edited a poll!"
response_module_polls_poll_edit_failed = "{datetime} -- **{member}** tried to edit a poll but something went wrong!"
response_module_polls_poll_edit_failed_unable_to_edit_discord_poll = (
    "{datetime} -- **{member}** tried to edit a poll but I can not change Discord polls!"
)
response_module_polls_poll_edit_failed_no_poll_given = (
    "{datetime} -- **{member}** tried to edit a poll but they didn't provide a poll!"
)
response_module_polls_poll_edit_failed_not_owner = (
    "{datetime} -- **{member}** tried to edit a poll but they are not the poll owner!"
)
response_module_polls_poll_edit_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to edit a poll but the servers settings are unknown!"
)
### DELETE
response_module_polls_poll_deleted = "{datetime} -- **{member}** has deleted a poll!"
response_module_polls_poll_delete_failed = "{datetime} -- **{member}** tried to delete a poll but something went wrong!"
response_module_polls_poll_delete_failed_no_poll_given = (
    "{datetime} -- **{member}** tried to delete a poll but they didn't provide a poll!"
)
response_module_polls_poll_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a poll but they are not the owner!"
)
response_module_polls_poll_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete a poll but the servers settings are unknown!"
)
### CLOSE MANUALLY
response_module_polls_poll_closed_manually = "{datetime} -- **{member}** has manually closed a poll!"
response_module_polls_poll_close_failed = (
    "{datetime} -- **{member}** tried to manually close a poll but something went wrong!"
)
response_module_polls_poll_close_failed_not_owner = (
    "{datetime} -- **{member}** tried to manually close a poll but they are not the owner!"
)
response_module_polls_poll_close_failed_no_poll_given = (
    "{datetime} -- **{member}** tried to manually close a poll but they didn't provide a poll!"
)
response_module_polls_poll_close_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to manually close a poll but the servers settings are unknown!"
)
### CLOSE
response_module_polls_poll_closed = "{datetime} -- Poll with ID: {poll_id} has ended!"
### VOTE ADD
response_module_polls_vote_added = "{datetime} -- **{member}** added a vote to a poll!"
response_module_polls_vote_add_failed = (
    "{datetime} -- **{member}** tried to add a vote for a poll but something went wrong!"
)
response_module_polls_vote_add_failed_answer_vote_limit_reached = "{datetime} -- **{member}** tried to add a vote for a poll to an answer but they have already reached the maximum number of votes for that answer!"
response_module_polls_vote_add_failed_answer_no_multi_select = "{datetime} -- **{member}** tried to add a vote for a poll to an answer but they have already voted for another question and multi select is turned off!"
response_module_polls_vote_add_failed_answer_not_found = (
    "{datetime} -- **{member}** tried to add a vote for a poll but the answer that was voted for was not found!"
)
response_module_polls_vote_add_failed_poll_not_found = (
    "{datetime} -- **{member}** tried to add a vote for a poll but the poll was not found!"
)
response_module_polls_vote_add_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to add a vote for a poll but the servers settings are unknown!"
)
response_module_polls_vote_add_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to add a vote for a poll but they have prevent data collection enabled!"
)
### VOTE REMOVE
response_module_polls_vote_removed = "{datetime} -- **{member}** removed a vote to a poll!"
response_module_polls_vote_remove_failed = (
    "{datetime} -- **{member}** tried to remove a vote for a poll but something went wrong!"
)
response_module_polls_vote_remove_failed_answer_vote_limit_reached = "{datetime} -- **{member}** tried to remove a vote for a poll to an answer but they have already reached the maximum number of votes for that answer!"
response_module_polls_vote_remove_failed_answer_no_multi_select = "{datetime} -- **{member}** tried to remove a vote for a poll to an answer but they have already voted for another question and multi select is turned off!"
response_module_polls_vote_remove_failed_answer_not_found = (
    "{datetime} -- **{member}** tried to remove a vote for a poll but the answer that was voted for was not found!"
)
response_module_polls_vote_remove_failed_poll_not_found = (
    "{datetime} -- **{member}** tried to remove a vote for a poll but the poll was not found!"
)
response_module_polls_vote_remove_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to remove a vote for a poll but the servers settings are unknown!"
)
response_module_polls_vote_remove_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to remove a vote for a poll but they have prevent data collection enabled!"
)

## Module remiders
### Disable
response_module_reminders_disabled = "{datetime} -- **{member}** has disabled the `reminders` module! All related settings are removed any left over reminders can safely be removed!"
response_module_reminders_disable_failed = "{datetime} -- **{member}** tried to disable the `reminders` module but something went wrong! Some of the configuration might be changed!"
### Enable
response_module_reminders_enabled = "{datetime} -- **{member}** has enabled the `reminders` module!"
response_module_reminders_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `reminders` module but something went wrong!"
)
### CREATE
response_module_reminders_created = "{datetime} -- **{member}** has created a new reminder!"
response_module_reminders_create_failed = (
    "{datetime} -- **{member}** tried to create a reminder but something went wrong!"
)
response_module_reminders_create_failed_invalid_dm_channel = (
    "{datetime} -- **{member}** tried to create a reminder but gave a DM channel that is not the owners DM channel!"
)
response_module_reminders_create_failed_invalid_run_date = (
    "{datetime} -- **{member}** tried to create a reminder but gave an invalid run date!"
)
response_module_reminders_create_failed_invalid_schedule = (
    "{datetime} -- **{member}** tried to create a reminder but gave invalid schedule info!"
)
response_module_reminders_create_failed_invalid_schedule_type = (
    "{datetime} -- **{member}** tried to create a reminder but gave invalid schedule type!"
)
response_module_reminders_create_failed_invalid_duration = (
    "{datetime} -- **{member}** tried to create a reminder but gave invalid duration!"
)
response_module_reminders_create_failed_scheduled_reminders_limit_reached = "{datetime} -- **{member}** tried to create a scheduled reminder but the limit of scheduled reminders has already been reached!"
response_module_reminders_create_failed_repeated_reminders_limit_reached = "{datetime} -- **{member}** tried to create a repeated reminder but the limit of repeated reminders has already been reached!"
response_module_reminders_create_failed_quick_reminders_limit_reached = "{datetime} -- **{member}** tried to create a quick reminder but the limit of quick reminders has already been reached in this server for this user!"
response_module_reminders_create_failed_not_administrator = (
    "{datetime} -- **{member}** tried to create a repeated or scheduled reminder but they are not an administrator!"
)
response_module_reminders_create_failed_invalid_reminder_type = (
    "{datetime} -- **{member}** tried to create a reminder but they didn't provide a valid reminder type!"
)
response_module_reminders_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a reminder but the servers settings are unknown!"
)
response_module_reminders_create_failed_no_destination = (
    "{datetime} -- **{member}** tried to create a reminder but they didn't provide a valid destination!"
)
response_module_reminders_create_failed_prevent_data_collection_enabled = (
    "{datetime} -- **{member}** tried to create a reminder but they have prevent data collection enabled!"
)
### DELETE
response_module_reminders_deleted = "{datetime} -- **{member}** has deleted a reminder!"
response_module_reminders_delete_failed = (
    "{datetime} -- **{member}** tried to delete a reminder but someting went wrong!"
)
response_module_reminders_delete_failed_not_administrator = (
    "{datetime} -- **{member}** tried to delete a repeated or scheduled reminder but they are not an administrator!"
)
response_module_reminders_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a quick reminder but they are not the owner of the reminder!"
)
response_module_reminders_delete_failed_not_found = (
    "{datetime} -- **{member}** tried to delete a reminder but the reminder is not found!"
)
response_module_reminders_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete a reminder but the servers settings are unknown!"
)
### SEND
response_module_reminders_send = "{datetime} -- I have send a reminder!"
### COMPLETED
response_module_reminders_completed = "{datetime} -- **{member}** has completed a reminder!"
### REMINDED
response_module_reminders_reminded_later = (
    "{datetime} -- **{member}** has marked a reminder as remind later. A new reminder is/will be created!"
)
### INTERACT
response_module_reminders_interact_failed_not_owner = (
    "{datetime} -- **{member}** tried to interact with a reminder but they are not the owner!"
)
response_module_reminders_interact_failed_not_a_quick_reminder = (
    "{datetime} -- **{member}** tried to interact with a reminder but the reminder is not a quick reminder!"
)
response_module_reminders_interact_failed_not_found = (
    "{datetime} -- **{member}** tried to interact with a reminder but the reminder is not found!"
)
response_module_reminders_interact_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to interact with a reminder but the servers settings are unknown!"
)

## Module Giveaways
### Disable
response_module_giveaways_disabled = "{datetime} -- **{member}** has disabled the `giveaways` module! All related settings are removed any left over giveaways can safely be removed!"
response_module_giveaways_disable_failed = "{datetime} -- **{member}** tried to disable the `giveaways` module but something went wrong! Some of the configuration might be changed!"
### Enable
response_module_giveaways_enabled = "{datetime} -- **{member}** has enabled the `giveaways` module!"
response_module_giveaways_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `giveaways` module but something went wrong!"
)
### Settings
response_module_giveaways_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `giveaways` module!"
)
response_module_giveaways_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `giveaways` module but something has gone wrong! Not all settings may have been changed!"
### Create
response_module_giveaway_created = "{datetime} -- **{member}** has created a new giveaway!"
response_module_giveaway_create_failed = (
    "{datetime} -- **{member}** tried to create a new giveaway but something went wrong!"
)
response_module_giveaway_create_failed_unknown_end_delete_time = (
    "{datetime} -- **{member}** tried to create a new giveaway but the end time and/or delete time is unknown!"
)
response_module_giveaway_create_failed_invalid_wait_duration = (
    "{datetime} -- **{member}** tried to create a new giveaway but the given wait duration is invalid!"
)
response_module_giveaway_create_failed_end_time_in_past = (
    "{datetime} -- **{member}** tried to create a new giveaway but the given end time is in the past!"
)
response_module_giveaway_create_failed_max_giveaways_reached = "{datetime} -- **{member}** tried to create a new giveaway but the maximum amount of giveaways has already been reached!"
response_module_giveaway_create_failed_invalid_winner_count = (
    "{datetime} -- **{member}** tried to create a new giveaway but the given winner count must be at least 1!"
)
response_module_giveaway_create_failed_prevent_data_collection_enabled = (
    "{datetime} -- **{member}** tried to create a new giveaway but they have prevent data collection enabled!"
)
response_module_giveaway_create_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to create a new giveaway but the servers settings are unknown!"
)
### Delete
response_module_giveaway_deleted = "{datetime} -- **{member}** has deleted a giveaway!"
response_module_giveaway_delete_failed = (
    "{datetime} -- **{member}** tried to delete a giveaway but something went wrong!"
)
response_module_giveaway_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a giveaway but they are not the owner!"
)
response_module_giveaway_delete_failed_not_found = (
    "{datetime} -- **{member}** tried to delete a giveaway but the giveaway was not found!"
)
response_module_giveaway_delete_failed_no_giveaway_given = (
    "{datetime} -- **{member}** tried to delete a giveaway but the giveaway was not given!"
)
response_module_giveaway_delete_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to delete a giveaway but the servers settings are unknown!"
)
### Edit
response_module_giveaway_edited = "{datetime} -- **{member}** has edited a giveaway!"
response_module_giveaway_edit_failed = "{datetime} -- **{member}** tried to edit a giveaway but something went wrong!"
response_module_giveaway_edit_failed_not_owner = (
    "{datetime} -- **{member}** tried to edit a giveaway but they are not the owner!"
)
response_module_giveaway_edit_failed_not_found = (
    "{datetime} -- **{member}** tried to edit a giveaway but the giveaway was not found!"
)
response_module_giveaway_edit_failed_no_giveaway_given = (
    "{datetime} -- **{member}** tried to edit a giveaway but the giveaway was not given!"
)
response_module_giveaway_edit_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to edit a giveaway but the servers settings are unknown!"
)
response_module_giveaway_edit_failed_invalid_winner_count = (
    "{datetime} -- **{member}** tried to edit a giveaway but the new winner count must be at least 1!"
)
### Reroll
response_module_giveaway_rerolled = "{datetime} -- **{member}** has rerolled a giveaway!"
response_module_giveaway_reroll_failed = (
    "{datetime} -- **{member}** tried to reroll a giveaway but something went wrong!"
)
response_module_giveaway_reroll_failed_not_owner = (
    "{datetime} -- **{member}** tried to reroll a giveaway but they are not the owner!"
)
response_module_giveaway_reroll_failed_not_found = (
    "{datetime} -- **{member}** tried to reroll a giveaway but the giveaway was not found!"
)
response_module_giveaway_reroll_failed_no_giveaway_given = (
    "{datetime} -- **{member}** tried to reroll a giveaway but the giveaway was not given!"
)
response_module_giveaway_reroll_failed_still_active = (
    "{datetime} -- **{member}** tried to reroll a giveaway but the giveaway was still active!"
)
response_module_giveaway_reroll_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to reroll a giveaway but the servers settings are unknown!"
)
### Enter
response_module_giveaway_entered = "{datetime} -- **{member}** has entered a giveaway!"
response_module_giveaway_enter_failed = "{datetime} -- **{member}** tried to enter a giveaway but something went wrong!"
response_module_giveaway_enter_failed_already_entered = (
    "{datetime} -- **{member}** tried to enter a giveaway but they already entered the giveaway!"
)
response_module_giveaway_enter_failed_not_found = (
    "{datetime} -- **{member}** tried to enter a giveaway but the giveaway was not found!"
)
response_module_giveaway_enter_failed_no_giveaway_given = (
    "{datetime} -- **{member}** tried to enter a giveaway but the giveaway was not given!"
)
response_module_giveaway_enter_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to enter a giveaway but they have prevent data collection enabled!"
)
response_module_giveaway_enter_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to enter a giveaway but the servers settings are not found!"
)
### Leave
response_module_giveaway_left = "{datetime} -- **{member}** has left a giveaway!"
response_module_giveaway_leave_failed = "{datetime} -- **{member}** tried to leave a giveaway but something went wrong!"
response_module_giveaway_leave_failed_not_found = (
    "{datetime} -- **{member}** tried to leave a giveaway but the giveaway was not found!"
)
response_module_giveaway_leave_failed_no_giveaway_given = (
    "{datetime} -- **{member}** tried to leave a giveaway but the giveaway was not given!"
)
response_module_giveaway_leave_failed_prevent_data_collection = (
    "{datetime} -- **{member}** tried to leave a giveaway but they have prevent data collection enabled!"
)
response_module_giveaway_leave_failed_settings_not_found = (
    "{datetime} -- **{member}** tried to leave a giveaway but the servers settings are not found!"
)
### Finish
response_module_giveaway_finished = "{datetime} -- The giveaway with ID: `{giveaway_id}` is finished!"
