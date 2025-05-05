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
no_modules_enabled = "There are no modules enabled"
no_modules_disabled = "There are no modules disabled"
no_stats_enabled = "There are no statistics enabled"
no_stats_disabled = "There are no statistics disabled"
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
allowed = "Allowed"
not_allowed = "Not allowed"
# Dicts
CHANNEL_TYPES = {
    "DM": "DM channel",
    "GROUP_DM": "Group DM channel",
    "GUILD_CATEGORY": "Category channel",
    "GUILD_NEWS": "News channel",
    "GUILD_STAGE": "Stage channel",
    "GUILD_TEXT": "Text channel",
    "GUILD_VOICE": "Voice channel",
    "GUILD_FORUM": "Forum channel",
}
CHANNEL_TYPES_INT = {
    1: "DM channel",
    3: "Group DM channel",
    4: "Category channel",
    5: "News channel",
    13: "Stage channel",
    0: "Text channel",
    2: "Voice channel",
    15: "Forum channel",
}
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
    "log_audio_seek": "Audio seeked to timestamp",
    "log_audio_join": "Bot joins channel",
    "log_audio_leave": "Bot leaves channel",
    "log_audio_stop": "Audio playback stopped",
    "log_audio_skip": "Song skipped",
    "log_audio_pause": "Audio paused",
    "log_audio_resume": "Audio resumed",
    "log_audio_nowplaying": "Now playing requested",
    "log_audio_queue": "Queue requested",
    "log_audio_loop": "Audio looped",
    "log_music_play": "Song added",
    "log_music_tts": "Text-to-Speech added",
    "log_music_playnext": "Song added next",
    "log_music_remove": "Song removed",
    "log_music_shuffle": "Queue shuffled",
    "log_music_search": "Song searched",
    "log_radio_play": "Radio played",
    "log_support": "Support commands",
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
    "log_audio_volume": "Audio volume changes",
    "log_audio_restart": "Song restarted",
    "log_giveaway_create": "Giveaway create",
    "log_giveaway_delete": "Giveaway delete",
    "log_giveaway_reroll": "Giveaway reroll",
    "log_domain_validated": "Domain validated",
    "log_qr_generated": "QR-code generated",
    "log_time_converted": "Time converted to seconds",
    "log_voice_message_transcribe": "Voice message transcribed",
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
}


# ------------------------------------------------------------------------- #
# GLOBAL ERRORS #
# ------------------------------------------------------------------------- #
error_response_not_recognised = (
    "Oops! I do not recogise this entity! If this issue persists, please contact our support!"
)
# ------------------------------------------------------------------------- #
# EVENTS - FUNCTIONS #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# Mod_User #
# ------------------------------------------------------------------------- #
# Embeds
user_events_ban_create_embed_title = "You have been banned!"
user_events_ban_create_embed_description = "You have been banned from `{guild}`!\n\n[Reason] -- {reason}"
user_events_ban_delete_embed_title = "You have been unbanned!"
user_events_ban_delete_embed_description = "You have been unbanned from `{guild}`!\n\n[Reason] -- {reason}"
user_events_kick_embed_title = "You have been kicked!"
user_events_kick_embed_description = "You have been kicked from `{guild}`!\n\n[Reason] -- {reason}"

# ------------------------------------------------------------------------- #
# FUNCTIONS #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# Audio #
# ------------------------------------------------------------------------- #
# Responses
response_join_failed_no_channel_given = (
    "Oops! It looks like you aren't in a voice channel! Please join one first or give the channel as an argument!"
)
response_join_failed = "Oops! Something went wrong while trying to join `{channel}`!"
response_join_success = "I joined {channel}!"
response_leave_failed = "Oops! Something went wrong while trying to leave!"
response_leave_success = "I left the channel!"
response_stop_failed = "Oops! Something went wrong while trying to stop audio playback!"
response_stop_success = "I stopped audio playback!"
response_pause_failed_nothing_playing = "There is nothing to pause!"
response_pause_failed_radio_playing = (
    "Oops! It looks like radio station is playing, I can't pause those since it is live!"
)
response_pause_failed = "Oops! Something went wrong while trying to pause audio playback!"
response_pause_success = "I have paused audio playback!"
response_resume_failed_nothing_playing = "There is nothing to resume!"
response_resume_failed_radio_playing = "Oops! It looks like radio station is playing, these can't be resumed!"
response_resume_failed = "Oops! Something went wrong while trying to resume the audio!"
response_resume_success = "I have resumed audio playback!"
response_music_shuffle_not_playing_anything = "Oops! It looks like there is nothing to shuffle!"
response_music_shuffle_playing_radio = "Oops! I can't shuffle when a radio station is playing!"
response_music_shuffle_failed = "Oops! Something went wrong while trying to shuffle the queue!"
response_music_shuffle_success = "I have shuffled the queue!"
response_music_skip_failed = "Something went wrong while trying to skip!"
response_music_skip_loop_enabled = "I can't skip because loop is `enabled`! Please disable loop and try again"
response_music_skip_failed_radio_playing = "I am sorry! I can't skip a radio station!"
response_music_skip_nothing_to_skip = "There is nothing to skip!"
response_music_skip_song_success = "I have skipped `{title}`."
response_music_seek_failed = "Something went wrong while trying to seek the song to the timestamp!"
response_music_seek_wrong_time_format = "I am sorry! The time is in the wrong format!"
response_music_seek_nothing_playing = "There is nothing playing!"
response_music_seek_failed_radio_playing = "I am sorry! I can't forward a radio station!"
response_music_seek_success = "I have jumped to `{time}`!"
response_music_restart_failed = "Something went wrong whule trying to restart the song!"
response_music_restart_nothing_playing = "I am sorry! I can't restart a song because there is no song playing!"
response_music_restart_failed_radio_playing = "I am sorry! I can't restart a radio station!"
response_music_restart_success = "I have restarted the song!"
response_nowplaying_failed = "Something went wrong while trying to get the currently playing song!"
response_nowplaying_not_playing_anything = "I am not playing anything!"
response_queue_failed = "Something went wrong while trying to get the queue!"
response_queue_empty = "There is nothing in the queue."
response_queue_timeout_reached = "The queue timeout, please initiate the command again!"
response_loop_failed_not_in_voicechannel = (
    "Oops! I can't loop because it looks like you are not in the (right) voice channel!"
)
response_loop_failed = "Something went wrong while enabling loop!"
response_loop_failed_queue_empty = "Oops! I can't toggle loop because there is nothing playing!"
response_loop_failed_radio_playing = "I can't toggle loop because radio is playing!"
response_loop_disabled = "I have `disabled` loop!"
response_loop_enabled = "I have `enabled` loop!"
response_volume_changed = "I have changed the volume to `{level}%`!"
response_music_play_failed = "Oops! Something went wrong while trying to add the song/playlist/album to the queue!"
response_music_play_failed_radio_playing = (
    "Oops! It looks like a radio station is playing! Please stop this before trying to play a different song!"
)
response_music_play_adding_song_playlist_album = "I am adding the song/playlist/album to the queue."
response_music_play_failed_no_youtube = "Oops! I am not allowed to play YouTube URLs!"
response_music_play_added_playlist = "I have added the playlist to the queue, enjoy!"
response_music_play_added_song = "I have added `{title}` to the queue, enjoy!"
response_music_playtts_failed = "Oops! Something went wrong while trying to add the text-to-speech message!"
response_music_playtts_failed_radio_playing = (
    "Oops! It looks like a radio station is playing! Please stop this before trying to use a text-to-speech message!"
)
response_music_playtts_adding_song_playlist_album = "I am adding the text-to-speech message to the queue."
response_music_playtts_added_song = "I have added the text-to-speech message!"
response_radio_play_failed_http_error = (
    "Oops! Something went wrong while trying to play `{radiostation}`! Got status code: `{status_code}`"
)
response_radio_play_failed = "Oops! Something went wrong while trying to play `{radiostation}`!"
response_radio_play_success = "Playing `{radiostation}`! Provided by TuneIn!"
response_music_remove_failed_nothing_to_remove = "Oops! It looks like there is nothing to remove!"
response_music_remove_failed = "Oops! Something went wrong while trying to remove the song/playlist/album!"
response_music_remove_failed_radio_playing = "Oops! I can't delete the song! I am playing radio!"
response_music_remove_removing_song_playlist_album = "I am removing the song/playlist/album from the queue."
response_music_remove_failed_no_youtube = "Oops! I am not allowed to remove YouTube URLs!"
response_music_remove_removed_playlist = "I have removed the playlist from the queue!"
response_music_remove_removed_song = "I have removed the song from the queue!"
response_search_no_results_found = "I am sorry! I didn't find any results for the query: `{query}`!"
response_music_playradio_failed_already_playing = (
    "I am sorry! It looks like there is already something playing, please stop this first to listing to radio!"
)
# Embeds
nowplaying_embed_title = "Now playing"
nowplaying_embed_field_title_radio = "Radiostation"
nowplaying_embed_field_title_title = "Title"
nowplaying_embed_field_title_artist = "Artist"
nowplaying_embed_field_title_position = "Position"
queue_embed_title = "Queue"
queue_embed_field_title_now_playing = "Now playing"
queue_embed_field_value_now_playing_loop_enabled = "Loop is `enabled` therefore this song will also show next in queue!"
queue_embed_field_title_queue = "Queue"
queue_embed_field_value_queue = "There is nothing else in the queue!"
search_yt_embed_title = "YouTube search results"
search_yt_embed_field_title_top_5 = "Top five results:"
search_sc_embed_title = "SoundCloud search results"
search_sc_embed_field_title_top_5 = "Top five results:"
search_deezer_embed_title = "Deezer search results:"
search_deezer_embed_field_title_top_5 = "Top five results:"
search_am_embed_title = "Apple Music search results:"
search_am_embed_field_title_top_5 = "Top five results:"
search_sp_embed_title = "Spotify search results:"
search_sp_embed_field_title_top_5 = "Top five results:"

# ------------------------------------------------------------------------- #
# Info #
# ------------------------------------------------------------------------- #
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
stats_functions_giveaways_enabled = "Function giveaways stats"
# Responses
support_embed_title = "{bot_name} Support"
support_embed_description = (
    "If you are in need of support, please follow one of the links below and contact us! We would like to help you!"
)
response_info_failed = "Something went wrong while getting the information!"
response_info_bot_module_logging_disabled = "The `Logging` module is disabled!"
response_info_bot_module_welcoming_disabled = "The `Welcoming` module is disabled!"
response_info_bot_module_tempchannels_disabled = "The `Tempchannels` module is disabled!"
response_info_bot_module_tempchannels_enabled = "The `Tempchannels` module is enabled. Please use the `/tempchannels list` command to get information about creation channels or active tempchannels or ask your server administrator!"
response_info_bot_module_socials_disabled = "The `Socials` module is disabled!"
response_info_bot_module_reactionroles_disabled = "The `Reactionroles` module is disabled!"
response_info_bot_module_reactionroles_enabled = "The `Reactionroles` module is enabled but details about this module can not be viewed in Discord. Please ask a server administrator for more information about this module!"
response_info_bot_module_tickets_disabled = "The `Tickets` module is disabled!"
response_info_bot_module_tickets_enabled = "The `Tickets` module is enabled but details about this module can not be viewed in Discord. Please ask a server administrator for more information about this module!"
response_info_bot_module_autoresponder_disabled = "The `Autoresponder` module is disabled!"
response_info_bot_module_tags_disabled = "The `Tags` module is disabled!"
response_info_bot_module_tags_enabled = "The `Tags` module is enabled! Please use the `/tags list` command to get information about the tags or ask your server administrator!"
response_info_bot_module_verifier_disabled = "The `Verifier` module is disabled!"
response_info_bot_module_rules_disabled = "The `Rules` module is disabled!"
response_info_bot_module_invite_tracker_disabled = "The `Invite tracker` module is disabled!"
response_info_bot_module_polls_disabled = "The `Polls` module is disabled!"
response_info_bot_module_polls_enabled = "The `Polls` module is enabled! Please use the `polls` commands to get information about the polls or ask your server administrator!"
response_info_bot_module_reminders_disabled = "The `Reminders` module is disabled!"
response_info_bot_module_reminders_enabled = "The `Reminders` module is enabled! Please use the `/reminders list` command to get information about the reminders or ask your server administrator!"
response_module_autoresponder_no_info = "The `Autoresponder` module does not have information available! For the status of the `Autoresponder` module, please check the General info page!"
response_info_bot_module_serverstats_disabled = "The `Serverstats` module is disabled!"
response_info_timeout = "The info command reached a timeout!"
response_info_reddit_list_failed = "Something went wrong while trying to get an overview of all monitored Subreddits in this server, returning to info socials view."
response_info_twitch_list_failed = "Something went wrong while trying to get an overview of all monitored Twitch accounts in this server, returning to info socials view."
response_info_rss_list_failed = "Something went wrong while trying to get an overview of all monitored RSS feeds in this server, returning to info socials view."
response_info_youtube_list_failed = "Something went wrong while trying to get an overview of all monitored YouTube channels in this server, returning to info socials view."
response_info_autoresponder_list_failed = "Something went wrong while trying to get an overview of all autoresponder entries in this server, returning to info autoresponder view."
response_info_welcoming_responses_list_failed = "Something went wrong while trying to get an overview of all welcoming responses in this server, returning to info welcoming view."
response_info_welcoming_timedroles_list_failed = "Something went wrong while trying to get an overview of all welcoming timedroles in this server, returning to info welcoming view."
# Embeds
info_bot_embed_title = "Welcome to {bot_name}!"
info_bot_embed_discription = "Hi! Welcome to the `{bot_name}` information panel! Here you will find all settings done for this server, the current version and some external links! Make sure to have a look around!\n\n *Note: Use the navigation buttons below to view module info.*"
info_bot_embed_field_title_language = "Language:"
info_bot_embed_field_title_gmt = "Timezone:"
info_bot_embed_field_title_unit_system = "Unit system:"
info_bot_embed_field_title_auto_delete = "Automatically delete bot messages after:"
info_bot_embed_field_value_auto_delete = "seconds"
info_bot_embed_field_title_max_warns = "Max warning points:"
info_bot_embed_field_value_max_warns = "points (per user)"
info_bot_embed_field_title_auto_kick = "Auto kick:"
info_bot_embed_field_title_auto_kick_role = "Auto kick role:"
info_bot_embed_field_title_modules_enabled = "Enabled Modules:"
info_bot_embed_field_title_modules_disabled = "Disabled Modules:"
info_bot_embed_field_title_logging_channel = "Logging Channel:"
info_bot_embed_field_title_logging_events_1 = "Events that are logged (1/5):"
info_bot_embed_field_title_logging_events_2 = "Events that are logged (2/5):"
info_bot_embed_field_title_logging_events_3 = "Events that are logged (3/5):"
info_bot_embed_field_title_logging_events_4 = "Events that are logged (4/5):"
info_bot_embed_field_title_logging_events_5 = "Events that are logged (5/5):"
info_bot_embed_field_title_enabled_components = "Enabled components:"
info_bot_embed_field_title_welcoming_welcome_messages_dm_randomized = "Welcome DM responses randomized:"
info_bot_embed_field_title_welcoming_welcome_messages_randomized = "Welcome channel responses randomized:"
info_bot_embed_field_title_welcoming_leave_messages_randomized = "Leave channel responses randomized:"
info_bot_embed_field_title_welcoming_welcome_messages_dm_response_id = "Welcome DM response ID:"
info_bot_embed_field_title_welcoming_welcome_messages_response_id = "Welcome channel response ID:"
info_bot_embed_field_title_welcoming_leave_messages_response_id = "Leave channel response ID:"
info_bot_embed_field_title_welcoming_welcome_messages_channel = "Welcome message in server channel:"
info_bot_embed_field_title_welcoming_leave_messages_channel = "Leave message in server channel:"
info_bot_embed_field_title_welcoming_role_add_role = "Autorole roles:"
info_bot_embed_field_title_welcoming_responses_list = "Current server responses:"
info_bot_embed_field_title_socials_monitor_reddit = "Monitor Reddit:"
info_bot_embed_field_title_socials_monitor_rss = "Monitor RSS Feeds:"
info_bot_embed_field_title_socials_monitor_twitch = "Monitor Twitch accounts:"
info_bot_embed_field_title_socials_monitor_youtube = "Monitor YouTube channels:"
info_bot_embed_field_title_verifier_type = "Verifier type:"
info_bot_embed_field_title_verifier_channel = "Channel:"
info_bot_embed_field_title_verifier_role_ids = "Verifier role IDs:"
info_bot_embed_field_title_verifier_is_embed = "Starting message is embed:"
info_bot_embed_field_title_verifier_success_is_embed = "Completed message is embed:"
info_bot_embed_field_title_verifier_content = "Starting message:"
info_bot_embed_field_title_verifier_completed_content = "Completed message:"
info_bot_embed_field_title_verifier_passphrase = "Passphrase:"
info_bot_embed_field_title_verifier_passphrase_hidden = "Passphrase is not shown, please refer to the Husqy dashboard!"
info_bot_embed_field_title_rules_channel = "Rules channel:"
info_bot_embed_field_title_rules_message = "Rules message:"
info_bot_embed_field_title_rules_actions_enabled = "Actions enabled:"
info_bot_embed_field_title_rules_denied_action = "Denied action:"
info_bot_embed_field_title_rules_accepted_role_ids = "Accepted roles:"
info_bot_embed_field_title_rules_denied_role_ids = "Denied roles:"
info_bot_embed_field_title_invite_tracker_join_message_is_embed = "Join messages is embed"
info_bot_embed_field_title_invite_tracker_leave_message_is_embed = "Leave messages is embed"
info_bot_embed_field_title_invite_tracker_join_messages_channel = "Join messages channel"
info_bot_embed_field_title_invite_tracker_leave_messages_channel = "Leave messages channel"
info_bot_embed_field_title_invite_tracker_join_message_content = "Join message"
info_bot_embed_field_title_invite_tracker_leave_message_content = "Leave message"
info_bot_embed_field_title_invite_tracker_prevent_own_invite_code = "Prevent own invite code from counting"
module_socials_reddit_embed_field_list = "Monitored Subreddits:"
module_socials_reddit_embed_field_list_empty = "No Subreddits monitored"
module_socials_rss_embed_field_list = "Monitored RSS Feeds:"
module_socials_rss_embed_field_list_empty = "No RSS Feeds monitored"
module_socials_twitch_embed_field_list = "Monitored Twitch accounts:"
module_socials_twitch_embed_field_list_empty = "No Twitch accounts monitored"
module_socials_youtube_embed_field_list = "Monitored YouTube channels:"
module_socials_youtube_embed_field_list_empty = "No YouTube channels monitored"
info_bot_embed_field_title_tickets_support_role = "Ticket Support Role"
info_bot_embed_field_title_tickets_creation_category = "Creation Category"
info_bot_embed_field_title_tickets_creation_channel = "Creation Channel"
info_bot_embed_field_title_tickets_creation_message = "Creation Message"
info_bot_embed_field_title_tickets_thread_mode = "Thread mode"
info_bot_embed_field_title_tickets_post_channel = "Post channel"
info_bot_embed_field_title_tickets_is_custom_creation_message = "Custom creation is message?"
info_bot_embed_field_title_tickets_is_custom_creation_embed = "Custom creation is embed?"
info_bot_embed_field_title_tickets_is_custom_creation_content = "Custom creation content"
info_bot_embed_field_title_tickets_is_custom_creation_modal = "Custom creation modal"
info_bot_embed_field_title_tickets_default_types = "Used default types"
info_bot_embed_field_title_tickets_custom_types = "Used custom types"
info_channel_embed_title = "Information about {channel}"
info_channel_embed_description = "Hi! Welcome to the `{channel}` information panel!"
info_channel_embed_field_title_channel = "Channel:"
info_channel_embed_field_title_channelid = "Channel ID:"
info_channel_embed_field_title_channeltype = "Channel Type:"
info_channel_embed_field_title_createdat = "Channel created at:"
info_role_embed_title = "Information about {role}"
info_role_embed_description = "Hi! Welcome to the `{role}` information panel!"
info_role_embed_field_title_role = "Role:"
info_role_embed_field_title_roleid = "Role ID:"
info_role_embed_field_title_rolepos = "Role position (Up ^):"
info_role_embed_field_title_createdat = "Role created at:"
info_role_embed_field_title_permissions = "Permissions of this role:"
info_role_embed_field_value_permissions_1_value = "Permissions value: "
info_server_embed_title = "Information about {guild}"
info_server_embed_no_description = "Hi! Welcome to `{guild}` information panel! There is no server description set!"
info_server_embed_field_title_owner = "Owner:"
info_server_embed_field_title_ownerid = "Owner ID:"
info_server_embed_field_title_afkchannel = "AFK Channel:"
info_server_embed_field_title_member_count = "Member count:"
info_server_embed_field_title_channels = "Channel count:"
info_server_embed_field_title_roles = "Role count:"
info_server_embed_field_title_members = "Members (excl. Bots):"
info_server_embed_field_title_createdat = "Server created at:"
info_user_embed_title = "Information about {user}"
info_user_embed_description = (
    "Hi! Welcome to the `{user}` information panel! This user has `{warn_points} warnings` in this server!"
)
info_user_embed_field_title_user = "User:"
info_user_embed_field_title_userid = "User ID:"
info_user_embed_field_title_userdiscriminator = "Discriminator:"
info_user_embed_field_title_userisbot = "Is bot:"
info_user_embed_field_title_userismute = "Is muted:"
info_user_embed_field_title_userisdeaf = "Is deafend:"
info_user_embed_field_title_joinedat = "Joined Server at:"
info_user_embed_field_title_createdat = "Joined Discord at:"
info_user_embed_field_title_roles = "Roles:"
info_bot_embed_field_title_serverstats_counter_panel_enabled = "Counter Panel:"
info_bot_embed_field_title_serverstats_counter_panel_category = "Counter Panel Category:"
info_bot_embed_field_title_serverstats_panel_member_count = "Member Count panel:"
info_bot_embed_field_title_serverstats_panel_online_member_count = "Online Member Count panel:"
info_bot_embed_field_title_serverstats_panel_online_members_with_role = "Online with role panel:"
info_bot_embed_field_title_serverstats_panel_boost = "Boost panel"
info_bot_embed_field_title_serverstats_starboard_enabled = "Starboard:"
info_bot_embed_field_title_serverstats_starboard_channel = "Starboard Channel:"
info_bot_embed_field_title_serverstats_starboard_count = "Starboard minimum stars:"
info_bot_embed_field_title_serverstats_enabled_stats = "Enabled stats:"
info_bot_embed_field_title_serverstats_disabled_stats = "Disabled stats:"
info_bot_embed_field_title_autoresponder_list = "Current autoresponder entries:"
info_embed_title = "Info"
info_embed_description_select_channel = "Please select the channel you want info about."
info_embed_description_select_role = "Please select the role you want info about."
info_embed_description_select_user = "Please select the user you want info about."
autoresponder_list = "Autoresponder list"
welcoming_responses_list = "Responses list"
welcoming_timedroles_list = "Timedroles list"

# ------------------------------------------------------------------------- #
# Misc #
# ------------------------------------------------------------------------- #
higher_lower_higher = "Higher"
higher_lower_equal = "Equal"
higher_lower_lower = "Lower"
rps_rock = "Rock"
rps_paper = "Paper"
rps_scissors = "Scissors"
# Responses
response_games_heads_or_tails_heads = "It's `heads`!"
response_games_heads_or_tails_tails = "It's `tails`!"
response_rps_timeout = "{user} didn't respond quick enough. The game has timed out!"
response_rps_users_turn = "{user}, your turn!"
response_rps_winner = "Congratulations {user}! You won the Rock, Paper, Scissors game!"
response_higher_lower_timeout = "The Higher/Lower game has timed out!"
response_ping_success = "Pong! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
response_transcribe_success = "***Transcription:*** ```{transcribed_message}```"
response_transcribe_failed = "Something went wrong while trying to transcribe the message!"
# Embeds
rps_embed_title = "Rock, Paper, Scissors game"
rps_embed_user_ones_turn = "{user_one} is choosing...\n {user_two} is waiting..."
rps_embed_user_twos_turn = "{user_one} is waiting...\n {user_two} is choosing..."
higher_lower_embed_title = "Higher/Lower"
higher_lower_embed_description = "Hello {member}! I have picked a number between 0 and 100! Do you think this number is higher, lower or equal to `{hint_number}`?"
higher_lower_embed_description_win = "Congratulations {member}! You are **correct**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
higher_lower_embed_description_loss = "Too bad {member}! You are **wrong**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
response_meme_getting_meme = "I am getting your meme, please wait!"

# ------------------------------------------------------------------------- #
# Mod_Server #
# ------------------------------------------------------------------------- #
reason_default_channel_lock = "**{member}** asked for channel lock -> {reason}"
reason_default_channel_unlock = "**{member}** asked for channel unlock -> {reason}"
# Responses
response_channel_create_success = "I have created the `{channel_type}`! -> {channel}."
response_channel_create_failed = "I am sorry! Something went wrong while trying to create the channel!"
response_channel_create_news_stage_forum_failed = (
    "I am sorry! Something went wrong while trying to create the channel! Does this server support this channel type?"
)
response_channel_delete_failed = "I am sorry! Something went wrong while trying to delete the `{channel}`!"
response_channel_delete_success = "I have deleted `{channel}`!"
response_clear_messages_failed_over_14_days = "I am sorry! I can't bulk delete messages that are over 14 days old!"
response_slowmode_set_failed = "Something went wrong while trying to set slowmode for `{channel}` to `{delay} seconds`!"
response_slowmode_set_success = "I have set the slowmode in `{channel}` to `{delay} seconds`!"
response_lock_failed = "I am sorry! Something went wrong while trying to lock {channel}!"
response_lock_success = "I have locked {channel}!"
response_unlock_failed = "I am sorry! Something went wrong while trying to unlock {channel}!"
response_unlock_success = "I have unlocked {channel}!"
response_role_create_failed = "I am sorry! Something went wrong while trying to create the role!"
response_role_create_success = "I have created the `{role_name}` role! -> {role}."
response_role_delete_failed = "I am sorry! Something went wrong while trying to delete the `{role}`!"
response_role_delete_success = "I have deleted `{role}`!"
# Embeds
clear_messages_started_embed_title = "Clear messages process started!"
clear_messages_started_embed_description = "Clear messages process is started. Depening on the amount of messages to delete, this can take some time! Please wait!"
clear_messages_embed_footer = "Command initialized by: {member}"
clear_messages_finished_embed_title = "Clear messages process finished!"
clear_messages_finished_embed_description = (
    "Clear messages process is finished! I have deleted a total of `{amount}` messages!"
)

# ------------------------------------------------------------------------- #
# Mod_User #
# ------------------------------------------------------------------------- #
kick_default_reason = "**{member}** asked for kick -> {reason}"
vckick_default_reason = "**{member}** asked for vckick -> {reason}"
move_default_reason = "**{member}** asked for move -> {reason}"
tempmute_default_reason = "**{member}** asked for tempmute -> {reason}"
temptimeout_default_reason = "**{member}** asked for temptimeout -> {reason}"
reason_auto_kick_role_added_warn = "*User reached/went over maximum warning limit set for this server!*"
reason_auto_kick_role_removed_warn = "*User is not longer over maximum warning limit set for this server!*"
# Responses
response_ban_create_failed_no_bot_ban = "I am sorry! I can't ban a bot!"
response_ban_create_failed = "I am sorry! Something went wrong while trying to ban `{user}`!"
response_ban_create_success = "I have banned `{user}`!"
response_ban_delete_failed_no_bot_unban = "I am sorry! I can't unban a bot!"
response_ban_delete_failed = "I am sorry! Something went wrong while trying to unban `{user}`!"
response_ban_delete_success = "I have unbanned `{user}`!"
response_kick_failed_no_bot_kick = "I am sorry! I can't kick a bot!"
response_kick_failed = "I am sorry! Something went wrong while trying to kick {user}!"
response_kick_success = "I have kicked {user}!"
response_vckick_failed = "I am sorry! Something went wrong while trying to kick {user} from the voice channel!"
response_vckick_success = "I have kicked {user} from the voice channel!"
response_move_failed_user_not_in_a_voice_channel = "{user} is not in a voice channel!"
response_move_failed_missing_permissions = "I am sorry! It looks like either I or the user is missing permissions!"
response_move_failed = "I am sorry! Something went wrong while trying to move {user} to {channel}!"
response_move_success = "I have moved {user} to {channel}!"
response_tempmute_failed_no_bot_tempmute = "I am sorry! I can't temporary mute a bot!"
response_tempmute_failed = "I am sorry! Something went wrong while trying to temporary mute {user}!"
response_tempmute_success = "I have temporary muted {user} for `{seconds} seconds`!"
response_temptimeout_failed_no_bot_temptimeout = "I am sorry! I can't temporary timeout a bot!"
response_temptimeout_failed = "I am sorry! Something went wrong while trying to temporary timeout {user}!"
response_temptimeout_success = "I have temporary timedout {user} for `{seconds} seconds`!"
response_warn_create_failed_no_bot_warn = "I am sorry! I can't warn a bot!"
response_warn_create_failed = "I am sorry! Something went wrong while trying to warn `{member}`!"
response_warn_create_success = "I have warned `{user}`!"
response_warn_delete_failed_no_bot_warn_delete = "I am sorry! I can't delete a warn from bot!"
response_warn_delete_failed = "I am sorry! Something went wrong while trying to delete a warn from `{member}`!"
response_warn_delete_success = "I have deleted a warn from `{user}`!"
# Embeds
warn_create_to_user_embed_title = "You have been warned!"
warn_create_to_user_embed_description = "You have been warned in `{guild}`! They have added `{points} points` to your profile!\nYour total points: {total} points!\n\n[Reason] -- {reason}"
warn_delete_to_user_embed_title = "Warning revoked!"
warn_delete_to_user_embed_description = "A previous warning in `{guild}` has been revoked! They have removed `{points} points` from your profile!\nYour total points: {total} points!\n\n[Reason] -- {reason}"

# ------------------------------------------------------------------------- #
# Privacy #
# ------------------------------------------------------------------------- #
privacy_data_collection = "Change data collection preferences"
privacy_get_data = "Get your data"
privacy_delete_data = "Delete your data"
privacy_shared_servers = "Get servers shared with {bot_name}"
privacy_enable_data_collection = "Enable data collection"
privacy_disable_data_collection = "Disable data collection"
privacy_delete_my_data = "Delete my data"
privacy_delete_my_data_cancel = "Cancel action"
# Responses
response_privacy_timeout = "The privacy command reached a timeout! Nothing will be changed!"
response_data_collection_enabled = (
    "Data collection in this server is now `enabled`. You will return to the main privacy configurator view."
)
response_data_collection_disabled = (
    "Data collection in this server is now `disabled`. You will return to the main privacy configurator view."
)
response_delete_started = "The deletion has started! You will soon return to the main privacy configurator view."
# Embeds
privacy_embed_title_shared = "{bot_name} privacy configurator"
privacy_embed_description = "Welcome to the {bot_name} privacy configurator.\nCurrently, {bot_name} is `{status}` to collect data from you in this server!"
privacy_embed_field_1_name = "About this configurator"
privacy_embed_field_1_value = "This privacy configurator is the place to configure your privacy related settings in {bot_name}.\n\nYou are free to retrieve your data and delete this data and instruct {bot_name} to not collect your data to deliver its services.\n`BEWARE: Deleting your data or restricting {bot_name} in collecting your data will result in loss of functionality for you and may result in loss of functionality or configuration changes to Husqy for other server members!`\n\nPlease use the buttons below to configure or get your privacy settings! If you are getting you data, beware that it may take a few seconds before it starts showing up!\n\nIf you have any further questions, please visit: {bot_website} or contact our support!"
privacy_embed_field_2_name = "Note"
privacy_embed_field_2_value = "- {bot_name} does not store all data, some data (like sent messages, f.e. mentions in the logging channel) will still exist in Discord, please contact the server administrator if you want to remove these entries.\n- Not all data can be deleted, some data is required (f.e. for settings the data collection preference or warnings)."
privacy_embed_footer_value = "DISCLAIMER: This configurator works on a per server basis! Want to get or delete information in other servers, use this privacy configurator in the other servers!"
privacy_embed_shared_servers_description = "Below you can find the list of server you share with {bot_name}!"
privacy_embed_shared_servers_field_1_name = "Shared servers list:"
privacy_embed_data_collection_description = "Here you can change your data collection preferences for {bot_name}. Please select, using the buttons below, which action you want to perform.\n\n- **Disable data collection:** This option prevents {bot_name} from collecting your information to provide you with its services (IN THIS SERVER).\n`BEWARE: restricting {bot_name} in collecting your data will result in loss of functionality for you and may result in loss of functionality`\n- **Enable data collection:** This option allows {bot_name} to collect your information to provide you with its services (IN THIS SERVER).\n"
privacy_embed_get_data_description = "We have gathered the amount of times your user ID, username, user nickname, user global name and user display name occur in the data we know.\n`BEWARE: Your nickname, global name, display name and username may all have the same value!`\n\n It is split across the different services, please use the buttons below to page through the amount of occurences per service.\n"
privacy_embed_get_data_global_description = (
    "For global {bot_name} data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_global_something_went_wrong = (
    "Something went wrong while checking you references for global {bot_name} data."
)
privacy_embed_get_data_modules_logging_description = (
    "For the {bot_name} logging module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_logging_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} logging module data."
)
privacy_embed_get_data_modules_autoresponder_description = (
    "For the {bot_name} autoreponder module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_autoresponder_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} autoresponder module data."
)
privacy_embed_get_data_modules_tempchannels_description = (
    "For the {bot_name} tempchannels module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_tempchannels_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} tempchannels module data."
)
privacy_embed_get_data_modules_welcoming_description = (
    "For the {bot_name} welcoming module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_welcoming_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} welcoming module data."
)
privacy_embed_get_data_modules_reactionroles_description = (
    "For the {bot_name} reactionroles module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_reactionroles_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} reactionroles module data."
)
privacy_embed_get_data_modules_tickets_description = (
    "For the {bot_name} tickets module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_tickets_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} tickets module data."
)
privacy_embed_get_data_modules_serverstats_description = (
    "For the {bot_name} serverstats module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_serverstats_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} serverstats module data."
)
privacy_embed_get_data_modules_socials_description = (
    "For the {bot_name} socials module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_socials_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} socials module data."
)
privacy_embed_get_data_modules_tags_description = (
    "For the {bot_name} tags module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_tags_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} tags module data."
)
privacy_embed_get_data_modules_verifier_description = (
    "For the {bot_name} verifier module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_verifier_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} verifier module data."
)
privacy_embed_get_data_modules_rules_description = (
    "For the {bot_name} rules module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_rules_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} rules module data."
)
privacy_embed_get_data_modules_invite_tracker_description = (
    "For the {bot_name} invite tracker module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_invite_tracker_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} invite tracker module data."
)
privacy_embed_get_data_functions_giveaways_description = (
    "For the {bot_name} giveaways functions data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_functions_giveaways_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} giveaways functions data."
)
privacy_embed_get_data_modules_reminders_description = (
    "For the {bot_name} reminders module data related to this server, we have found the following:\n{data}"
)
privacy_embed_get_data_modules_reminders_something_went_wrong = (
    "Something went wrong while checking you references for the {bot_name} reminders module data."
)
privacy_embed_delete_data_description = "Here you can choose to delete your data {bot_name} has related to you. Please select, using the buttons below, which action you want to perform.\n\n- **Cancel:** Returns to the main privacy configurator view and doesn't remove any data.\n- **Delete my data:** This option starts the deletion of you data (where possible) immediately (IN THIS SERVER).\n`BEWARE: deleting your data can result in loss of functionality for you and may result in loss of functionality for others.`\n"

# ------------------------------------------------------------------------- #
# Giveaway #
# ------------------------------------------------------------------------- #
# Responses
response_giveaway_list_failed = "Something went wrong while fetching this servers giveaways!"
response_giveaway_list_no_giveaways = "You don't have any active giveaways in this server!"
response_giveaway_list_timeout = "Giveaway list reached a timeout!"
response_giveaway_creating = "I am creating the giveaway, please wait!"
response_giveaway_deleting = "I am deleting the giveaway, please wait!"
response_giveaway_rerolling = "I am rerolling the giveaway, please wait!"
# Embeds
giveaway_list_embed_title = "Your giveaways"
giveaway_list_embed_description = "You have {giveaways} giveaways! Showing your active giveaways:"
giveaway_list_embed_field_giveaways = "Your giveways (Active/Finished):"

# ------------------------------------------------------------------------- #
# Utils #
# ------------------------------------------------------------------------- #
custom_embed_edit_color = "Edit color"
custom_embed_edit_title = "Edit title"
custom_embed_edit_description = "Edit description"
custom_embed_edit_footer_text = "Edit footer text"
custom_embed_edit_field = "Edit field"
custom_embed_add_inline_field = "Add inline field"
custom_embed_add_non_inline_field = "Add non-inline field"
custom_embed_edit_thumbnail_image_field = "Edit thumbnail or image"
custom_embed_thumbnail_none = "None"
custom_embed_thumbnail_avatar = "My Avatar"
custom_embed_thumbnail_banner = "My Banner"
custom_embed_thumbnail_custom_url = "Custom URL"
custom_embed_thumbnail = "Thumbnail"
custom_embed_image_none = "None"
custom_embed_image_avatar = "My Avatar"
custom_embed_image_banner = "My Banner"
custom_embed_image_custom_url = "Custom URL"
custom_embed_image = "Image"
custom_embed_reset = "Reset"
custom_embed_finish = "Finish"
custom_embed_edit_color_new_color = "New color"
custom_embed_edit_color_new_color_description = "New color (HEX code: f.e. #0a1931)"
custom_embed_edit_title_new_title = "New title"
custom_embed_edit_description_new_description = "New description"
custom_embed_edit_footer_text_new_footer_text = "New footer text"
custom_embed_edit_field_select_field = "Which field no.? Count Left>Right | Up>Down"
custom_embed_edit_field_new_title = "New field title (empty = no change)"
custom_embed_edit_field_new_description = "New field description (empty = remove)!"
custom_embed_add_inline_field_new_title = "Inline field title"
custom_embed_add_inline_field_new_value = "Inline field value"
custom_embed_add_non_inline_field_new_title = "Non-inline field title"
custom_embed_add_non_inline_field_new_value = "Non-inline field value"
custom_embed_thumbnail_custom_url_modal_title = "Thumbnail Custom URL"
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
custom_modal_change_title_new_title = "New title"
custom_modal_add_text_field_text_field_title = "Field title"
custom_modal_add_text_field_text_field_description = "Field description"
custom_modal_add_text_field_text_field_type = "Field type (Long/Short)"
custom_modal_add_text_field_text_field_required = "Required (True/False)"
custom_modal_add_text_field_title = "Text field"
# Responses
response_color_viewed_failed_no_values_given = "I am sorry! I require one value, either the HEX value or the RGB value!"
response_color_viewed_failed_only_one_value_allowed = (
    "I am sorry! You are only allowed to insert one of the two values!"
)
response_color_viewed_failed = "I am sorry! Something went wrong while trying to view the color!"
response_custom_embed_finished_timeout = (
    "The custom embed creation reached a timeout! The JSON of your embed is: ```{embed_json}```"
)
response_custom_embed_finished = "The custom embed creation is finished, the JSON of your embed is: ```{embed_json}```"
response_custom_embed_send_success = "I have sent the custom embed to {channel}"
response_custom_modal_finished = (
    "The custom modal creation is finished, the JSON of your modal is: \n```{modal_json}```"
)
response_custom_modal_preview = "By pressing Continue I will show the preview of the custom modal! This modal can be interacted with but no data will be saved!"
response_custom_modal_preview_failed = "The custom modal preview reached a timeout!"
response_custom_modal_preview_failed_canceled = "The custom modal preview was canceled!"
response_custom_modal_preview_success = "Custom modal has been previewed!"
response_domain_validate_safety_success_is_safe = "🟩 The domain is safe!"
response_domain_validate_safety_success_not_safe = "🟥 The domain is NOT safe!"
response_domain_validate_safety_failed_http_code = "Something went wrong while checking the domain, got HTTP error: {http_code}! Please try again later! If this issue persists, please contact our support!"
response_time_converted_success = (
    "{days} days, {hours} hours, {minutes} minutes and {seconds} seconds totals to `{total_seconds}` seconds!"
)
# Embeds
color_view_embed_title = "Color"
color_view_embed_description = "Here is the color you requested, with color value: `{color}`"
custom_embed_default_embed_title = "Custom embed creation"
custom_embed_default_embed_description = (
    "Welcome to the custom embed creation. Using the buttons below, you can configure this embed and retrieve the JSON."
)
custom_modal_default_embed_title = "Custom modal creation"
custom_modal_embed_description = "Welcome to the custom modal creation. Using the buttons below, you can configure the modal and preview it. When finished, select Finish to retrieve the JSON.\n **When previewing the modal, press cancel or fill in the form and press submit to continue modal creation!**"
qr_generate_embed_title = "Your QR-code"
qr_generate_embed_footer = "QR generated by: {member}!"

# ------------------------------------------------------------------------- #
# MODULES #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# LOGGING #
# ------------------------------------------------------------------------- #
response_module_logging_settings_failed = "Something went wrong while getting the settings of the `logging` module!"

# ------------------------------------------------------------------------- #
# WELCOMING #
# ------------------------------------------------------------------------- #
response_module_welcoming_settings_failed = "Something went wrong while getting the settings of the `welcoming` module!"
module_welcoming_welcome_messages_dm = "Welcome messages DM"
module_welcoming_welcome_messages = "Welcome messages channel"
module_welcoming_leave_messages = "Leave messages channel"
module_welcoming_autorole = "Autorole"
module_welcoming_timedroles = "Timedroles"

# ------------------------------------------------------------------------- #
# TICKETS #
# ------------------------------------------------------------------------- #
response_module_tickets_settings_failed = "Something went wrong while getting the settings of the `tickets` module!"
tickets_transfer_select_new_support_engineer = "Please select the new support engineer for this ticket!"

# ------------------------------------------------------------------------- #
# SERVERSTATS #
# ------------------------------------------------------------------------- #
response_module_serverstats_settings_failed = (
    "Something went wrong while getting the settings of the `serverstats` module!"
)

# ------------------------------------------------------------------------- #
# TAGS #
# ------------------------------------------------------------------------- #
response_tags_edit_provide_content = "Please provide the new content of the tag by sending the new content in the chat."
response_tags_create_provide_content = "Please provide the tags content of the tag by sending the content in the chat."
response_tags_list_failed = "Something went wrong while getting the list of tags!"
response_tags_list_no_tags = "There are no tags based on the given selection!"
response_tags_list_timeout = "Tags list reached a timeout."
# Embeds
tags_list_embed_title = "Tags list"
tags_list_embed_description = "Here are the tags based on your selected! Tag count: {tags}!"
tags_list_embed_field_tags = "Tags based on selection:"

# ------------------------------------------------------------------------- #
# SOCIALS #
# ------------------------------------------------------------------------- #
module_socials_reddit_list = "Get Subreddit list"
module_socials_rss_list = "Get RSS Feed list"
module_socials_twitch_list = "Get Twitch account list"
module_socials_youtube_list = "Get YouTube channel list"
# Responses
response_socials_component_list_failed = (
    "Something went wrong while getting the entries list of the {component} component of the `socials` module!"
)
response_socials_component_list_failed_component_disabled = (
    "The {component} component of the `socials` module is disabled!"
)
response_socials_component_list_no_entries = (
    "There are no entries for the {component} component of the `socials` module!"
)
# Embeds
socials_component_list_embed_title = "Socials {component} list"
socials_component_list_embed_description = "Here are the entries! Entry count: {entries}!"
socials_component_list_embed_field_entries = "Entries:"

# ------------------------------------------------------------------------- #
# TEMPCHANNELS #
# ------------------------------------------------------------------------- #
response_tempchannels_list_failed = "Something went wrong while getting the list. Is the list type valid?"
response_tempchannels_list_timeout = "The tempchannel list reached a timeout!"
response_tempchannels_list_creation_channels_failed = (
    "Something went wrong while gettint the list of creation channels!"
)
response_tempchannels_list_tempchannels_failed = "Something went wrong while gettint the list of tempchannels!"
response_tempchannels_list_no_items = "There are no items based on the request list type and selection."
# Embeds
tempchannels_list_embed_title = "{list_type} list"
tempchannels_list_embed_description = "Here are the {list_type} based on your selection! Item count: {items}!"
tempchannels_list_embed_field_creation_channels = "Creation channels:"
tempchannels_list_embed_field_tempchannels = "Tempchannels:"


# ------------------------------------------------------------------------- #
# VERIFIER #
# ------------------------------------------------------------------------- #
response_module_verifier_settings_failed = "Something went wrong while getting the settings of the `verifier` module!"

# ------------------------------------------------------------------------- #
# RULES #
# ------------------------------------------------------------------------- #
response_module_rules_settings_failed = "Something went wrong while getting the settings of the `rules` module!"
response_rules_list_failed = "Something went wrong while getting the list of rules!"
response_rules_list_no_rules = "There are no rules in this server!"
response_rules_list_timeout = "Rules list reached a timeout."
# Embeds
rules_list_embed_title = "Rules list"
rules_list_embed_description = "Here are the servers rules! Rule count: {rules}!"
rules_list_embed_field_rules = "Rules:"

# ------------------------------------------------------------------------- #
# INVITE_TRACKER #
# ------------------------------------------------------------------------- #
response_module_invite_tracker_settings_failed = (
    "Something went wrong while getting the settings of the `invite tracker` module!"
)
response_invite_link_failed = "Something went wrong while fetching the servers shared invite link!"
response_invite_link_failed_no_invite_link_configured = "This server has not set a shared invite link!"
response_invite_link_list_failed = "Something went wrong while fetching the server known invite link list!"
response_invite_links_list_empty = "There are not known invite links in this server!"
response_invite_links_list_timeout = "The invite tracker list reached a timeout!"
response_invite_link_stats_failed = "Something went wrong while fetching the stats for the inviter!"
module_invite_tracker_join_messages = "Join messages"
module_invite_tracker_leave_messages = "Leave message"
# Embeds
invite_link_embed_title = "Server invite link"
invite_link_embed_description = "Do you want to invite other friends? Please use the following invite link:\n {link}"
invite_link_list_embed_title = "Invite links"
invite_link_list_embed_description = "Here are the known invite links! Invite link count: {invite_links}!"
invite_link_list_embed_field_invite_links = "Invite links:"
invite_link_stats_embed_title = "Invite tracker stats"
invite_link_stats_embed_description = (
    "{member} has a total of {total_invites} over the pas 31 days! View the details below!"
)
invite_link_stats_embed_field_details = "Stats details:"

# ------------------------------------------------------------------------- #
# POLLS #
# ------------------------------------------------------------------------- #
polls_determine_action_timeout = (
    "The poll vote determine action has reached a timeout. No vote will be placed or removed!"
)
polls_response_choose_poll_action = "What action do you want to perform on the answer? Add = Add vote & Remove = Remove all of your votes for that answer."
response_poll_details_failed = "Something went wrong while getting the details of the poll!"
response_poll_provide_details_failed = (
    "Timeout while waiting for details of the poll answer! Cancelling poll create....."
)
response_poll_add_answer = "Do you want to add an extra answer to the list? Please keep in mind the answer limits of the server, these will only be checked when finishing this command."
response_poll_provide_answer_text = (
    "Please provide the text of the answer by sending it in the chat. Please only insert the answer text in one line."
)
response_poll_provide_answer_emoji = (
    "Please provide the emoji of the answer by sending it in the chat. Please only send the emoji."
)
response_poll_provide_answer_label = (
    "Please provide the label of the answer by sending it in the chat. Please only send the emoji."
)
response_poll_provide_answer_description = (
    "Please provide the description of the answer by sending it in the chat. Please only send the emoji."
)
response_poll_add_label_to_answer = (
    "Do you want to add a label to the button? If no, an emoji is required. If yes, an emoji is optional."
)
response_poll_add_description_to_answer = "Do you want to add a description to the button (not visible in discord)?"
response_poll_add_emoji_to_answer = "Do you want to add a emoji to the button?"

# Embeds
poll_until_manually_closed = "`until manually closed`"
no_description_given = "No description given"
poll_description = "Poll is active for: {countdown}!\n`{description}`"
poll_answers_embed_field = "Poll answers:"
poll_footer = "Poll ID: {poll_id}. Poll provided by Husqy!"
poll_results_embed_field = "Poll results:"
poll_voters_embed_field = "Voters:"
poll_footer = "Poll ID: {poll_id}. Poll provided by Husqy!"

# ------------------------------------------------------------------------- #
# Reminders #
# ------------------------------------------------------------------------- #
# Responses
response_reminders_new_duration = (
    "Please provide the new duration for the reminder. Please use format: {delay}{d/h/m/s} - f.e. 1h or 20m)"
)
response_reminder_adding = "I am adding the reminder, please wait!"
response_reminder_deleting = "I am deleting the reminder, please wait!"
response_reminder_list_failed = "Something went wrong while fetching the reminders based on your selection!"
response_reminder_list_no_reminders = "There are no reminders in this server based on your selection!"
response_reminder_list_timeout = "Reminder list reached a timeout!"
response_quick_reminder_create_failed = "When creating a quick reminder. You cannot have destination_member and destination_channel both. You must choose between a DM (destination_member) or a channel (destination_channel)."
# Embeds
reminder_list_embed_title = "Reminders list"
reminder_list_embed_description = "Here are the reminder based on your selection! Reminder count: {reminders}!"
reminder_list_embed_field_reminders = "Reminders based on selection:"
