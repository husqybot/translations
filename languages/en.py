# ------------------------------------------------------------------------- #
# GLOBAL VARIABLES #
# ------------------------------------------------------------------------- #
# Footer
embed_footer = (
    "Info requested by: {member}! This embed will show for {auto_delete} seconds!"
)
# Logging translations
log_errors = "Errors"
log_info = "Info requests"
log_settings_changed = "Setting changes"
log_channel_create = "Channel creations"
log_channel_delete = "Channel deletions"
log_channel_update = "Channel updates"
log_clear_messages = "Clear messages"
log_slowmode = "Slowmode changes"
log_channel_lock = "Channel locked"
log_channel_unlock = "Channel unlocked"
log_channel_join = "Joined voice channel"
log_channel_leave = "Left voice channel"
log_channel_move = "Moved voice channel"
log_role_create = "Role creations"
log_role_delete = "Role deletions"
log_role_update = "Role updates"
log_reaction_roles_create = "Reaction Role creations"
log_reaction_roles_delete = "Reaction Role deletions"
log_reaction_roles_info = "Reaction Role info requests"
log_user_warn_create = "Warn create"
log_user_warn_delete = "Warn delete"
log_kick_events = "Kicked users"
log_vckick = "User kicked from VC"
log_move = "User moved to different VC by command"
log_ban_create = "Bans"
log_ban_delete = "Unbans"
log_tempmute = "Tempmute command"
log_temptimeout = "Temptimeout command"
log_games = "Games played"
log_audio_join = "Bot joins channel"
log_audio_leave = "Bot leaves channel"
log_audio_stop = "Audio playback stopped"
log_audio_skip = "Song skipped"
log_audio_pause = "Audio paused"
log_audio_resume = "Audio resumed"
log_audio_nowplaying = "Now playing requested"
log_audio_queue = "Queue requested"
log_audio_loop = "Audio looped"
log_music_play = "Song added"
log_music_tts = "Text-to-Speech added"
log_music_playnext = "Song added next"
log_music_remove = "Song removed"
log_music_shuffle = "Queue shuffled"
log_music_search = "Song searched"
log_radio_play = "Radio played"
log_support = "Support commands"
log_modules = "Module changes"
log_tempchannels = "Tempchannel events"
log_customembed_send = "Custom Embeds Sent"
log_customembed_create = "Custom Embeds Creations"
log_custommodal_create = "Custom Modal Creations"
log_custommodal_preview = "Cuustom Modal Previewed"
log_reminder_add = "Reminders added"
log_reminder_delete = "Reminders deleted"
log_reminder_list = "Reminders list requested"
log_tag_create = "Tag created"
log_tag_edit = "Tag edited"
log_tag_delete = "Tag deleted"
log_tag_used = "Tag used"
log_tag_list = "Tag list"
log_poll_create = "Poll create"
log_poll_delete = "Poll delete"
log_poll_stop = "Poll stop"
log_poll_details = "Poll details"
log_poll_list = "Poll list"
log_poll_clear_votes = "Poll clear votes"
log_reddit_add = "Subreddit added"
log_reddit_remove = "Subreddit removed"
log_reddit_list = "Subreddit list"
log_autoresponder_response_created = "Autoresponder response created"
log_autoresponder_response_deleted = "Autoresponder response deleted"
log_autoresponder_response_list = "Autoresponder response list"
log_user_server_muted = "User got server muted"
log_user_server_unmuted = "User got server unmuted"
log_user_server_deafend = "User got server deafend"
log_user_server_undeafend = "User got server undeafend"
log_user_deafend = "User self deafend"
log_user_undeafend = "User self undeafend"
log_user_muted = "User self muted"
log_user_unmuted = "User self unmuted"
log_user_stream_started = "User started streaming"
log_user_stream_stopped = "User stopped streaming"
log_user_camera_stream_started = "User turned on camera"
log_user_camera_stream_stopped = "User turned off camera"
log_color_viewed = "Color viewed"
log_audio_volume = "Audio volume changes"
log_giveaway_create = "Giveaway create"
log_giveaway_delete = "Giveaway delete"
log_giveaway_list = "Giveaway list"
log_giveaway_reroll = "Giveaway reroll"
log_domain_validated = "Domain validated"
log_qr_generated = "QR-code generated"
log_time_converted = "Time converted to seconds"
log_voice_message_transcribe = "Voice message transcribed"
log_rss_add = "RSS Feed added"
log_rss_remove = "RSS Feed removed"
log_rss_list = "RSS Feed list"
log_twitch_add = "Twitch account added"
log_twitch_remove = "Twitch account removed"
log_twitch_list = "Twitch account list"
log_meme = "Meme requests"
# Other
all = "All"
selection = "Selection"
minimal = "Minimal"
complete = "Complete"
custom = "Custom"
default = "Default"
unknown = "Unknown"
no_nickname = "No nickname"
no_displayname = "No display name"
no_timeout_for_user = "Not timed-out"
deafend = "Deafend"
not_deafend = "Not deafend"
muted = "Muted"
not_muted = "Not muted"
pending = "Pending"
not_pending = "Not pending"
yes = "Yes"
no = "No"
embed = "Embed"
message = "Message"
messages = "Messages"
commands = "Commands"
reaction = "Reaction"
enabled = "Enabled"
disabled = "Disabled"
enable = "Enable"
no_modules_enabled = "There are no modules enabled"
disable = "Disable"
no_modules_disabled = "There are no modules disabled"
continue_message = "Continue"
cancel_message = "Cancel"
not_in_use = "Not in use!"
no_reason_specified = "*No reason specified!*"
variables_server = "Server variables"
variables_user = "User variables"
variables_channel = "Channel variables"
variables_other = "Other variables"
status_open = "Open"
status_closed = "Closed"
no_url = "No URL available"
no_author = "No author available"
create = "Create"
select = "Select"
jump_to_message = "Jump to message!"
message_id = "Message ID"
back = "Back"
website = "Website"
support_server = "Support Server"
dashboard = "Dashboard"
api = "API"
allowed = "Allowed"
not_allowed = "Not allowed"
# Dicts
STATUS_CODES = {
    "200": "API Request OK!",
    "400": "Bad Request",
    "401": "Unauthorized",
    "403": "API Request Forbidden",
    "404": "API Request Not Found",
    "429": "Too many requests",
    "503": "API Unavailable",
}
CHANNEL_TYPES = {
    "DM": "DM channel",
    "GROUP_DM": "Group DM channel",
    "GUILD_CATEGORY": "Category channel",
    "GUILD_NEWS": "News channel",
    "GUILD_STAGE": "Stage channel",
    "GUILD_STORE": "Store channel",
    "GUILD_TEXT": "Text channel",
    "GUILD_VOICE": "Voice channel",
    "GUILD_FORUM": "Forum channel",
}

# ------------------------------------------------------------------------- #
# GLOBAL ERRORS #
# ------------------------------------------------------------------------- #
error_response_not_enough_permissions_for_channel = (
    "Oops! It looks like I don't have enough permissions to use that channel!"
)
error_response_not_enough_permissions_for_message = (
    "Oops! It looks like I don't have enough permissions to use that message!"
)
error_response_not_a_text_channel = (
    "Oops! It looks like that the given channel is not a text channel!"
)
error_response_not_a_voice_channel = (
    "Oops! It looks like that the given channel is not a voice channel!"
)
error_response_not_a_category_channel = (
    "Oops! It looks like that the given channel is not a category channel!"
)
error_response_not_a_valid_id = (
    "Oops! It looks like that the given value is not an valid ID!"
)
error_response_not_a_valid_emoji = (
    "Oops! It looks like that the given emoji is not a valid emoji!"
)
error_response_invalid_int_found_in_list = (
    "Oops! It looks like that a value is not a valid integer/number!"
)
error_response_not_a_url = "Oops! It looks like the given string is not a URL!"
error_response_not_recognised = "Oops! I do not recogise this entity! If this issue persists, please contact our support!"

# ------------------------------------------------------------------------- #
# EVENTS - FUNCTIONS #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# Audio #
# ------------------------------------------------------------------------- #
# Log Responses
log_response_music_events_leave = (
    "{datetime} -- I left the voice channel, all users left!"
)

# ------------------------------------------------------------------------- #
# Mod_Server #
# ------------------------------------------------------------------------- #
# Log Responses
log_response_channel_events_channel_created = "{datetime} -- **{member}** created a `{channel_type}` -> {channel}!\n`[Reason]` -- {reason}"
log_response_channel_events_channel_deleted = "{datetime} -- **{member}** deleted the channel `{channel_name} - {channel_id}`!\n`[Reason]` -- {reason}"
log_response_channel_events_channel_updated = (
    "{datetime} -- **{member}** updated the channel {channel}!\n`[Reason]` -- {reason}"
)
log_response_role_events_role_created = (
    "{datetime} -- **{member}** created a `Role` -> {role}!\n`[Reason]` -- {reason}"
)
log_response_role_events_role_deleted = "{datetime} -- **{member}** deleted the role `{role_name} - {role_id}`!\n`[Reason]` -- {reason}"
log_response_role_events_role_updated = (
    "{datetime} -- **{member}** updated the role {role}!\n`[Reason]` -- {reason}"
)

# ------------------------------------------------------------------------- #
# Mod_User #
# ------------------------------------------------------------------------- #
# Log Responses
log_response_user_events_banned = (
    "{datetime} -- **{member}** has banned `{user}`!\n`[Reason]` -- {reason}"
)
log_response_user_events_unbanned = (
    "{datetime} -- **{member}** has unbanned `{user}`!\n`[Reason]` -- {reason}"
)
log_response_user_events_kicked = (
    "{datetime} -- **{member}** has kicked `{user}`!\n`[Reason]` -- {reason}"
)
# Embeds
user_events_ban_create_embed_title = "You have been banned!"
user_events_ban_create_embed_description = (
    "You have been banned from `{guild}`!\n\n[Reason] -- {reason}"
)
user_events_ban_delete_embed_title = "You have been unbanned!"
user_events_ban_delete_embed_description = (
    "You have been unbanned from `{guild}`!\n\n[Reason] -- {reason}"
)
user_events_kick_embed_title = "You have been kicked!"
user_events_kick_embed_description = (
    "You have been kicked from `{guild}`!\n\n[Reason] -- {reason}"
)

# ------------------------------------------------------------------------- #
# EVENTS - MODULES #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# LOGGING #
# ------------------------------------------------------------------------- #
# Log Responses
log_response_user_left_voice_channel = "{datetime} -- **{member}** left {channel}!"
log_response_user_left_voice_channel_tempchannel = (
    "{datetime} -- **{member}** left a tempchannel named: `{channel}`!"
)
log_response_user_moved_voice_channel = (
    "{datetime} -- **{member}** moved from {from_channel} to {to_channel}!"
)
log_response_user_moved_voice_channel_tempchannel_to = "{datetime} -- **{member}** moved from {from_channel} to a tempchannel named: `{to_channel}`!"
log_response_user_moved_voice_channel_tempchannel_from = "{datetime} -- **{member}** moved from a tempchannel named `{from_channel}` to {to_channel}!"
log_response_user_moved_voice_channel_tempchannel = "{datetime} -- **{member}** moved from a tempchannel named: `{from_channel}` to a tempchannel named `{to_channel}`!"
log_response_user_joined_voice_channel = "{datetime} -- **{member}** joined {channel}!"
log_response_user_joined_voice_channel_tempchannel = (
    "{datetime} -- **{member}** joined a tempchannel named: `{channel}`!"
)
log_response_user_guild_muted = "{datetime} -- **{member}** got server muted!"
log_response_user_guild_unmuted = "{datetime} -- **{member}** got server unmuted!"
log_response_user_guild_deafend = "{datetime} -- **{member}** got server deafend!"
log_response_user_guild_undeafend = "{datetime} -- **{member}** got server undeafend!"
log_response_user_deafend = "{datetime} -- **{member}** self deafend!"
log_response_user_undeafend = "{datetime} -- **{member}** self undeafend!"
log_response_user_muted = "{datetime} -- **{member}** self muted!"
log_response_user_unmuted = "{datetime} -- **{member}** self unmuted!"
log_response_user_stream_started = (
    "{datetime} -- **{member}** started streaming their screen!"
)
log_response_user_stream_stopped = (
    "{datetime} -- **{member}** stopped streaming their screen!"
)
log_response_user_camera_stream_started = (
    "{datetime} -- **{member}** turned on their camera!"
)
log_response_user_camera_stream_stopped = (
    "{datetime} -- **{member}** turned off their camera!"
)

# ------------------------------------------------------------------------- #
# TICKETS #
# ------------------------------------------------------------------------- #
# Responses
response_ticket_created = "your ticket has been created!"
response_ticket_created_support = "would you mind looking at this?"
# Embeds
module_tickets_new_ticket_embed_title = "New Ticket!"
module_tickets_new_ticket_embed_description = (
    "{user} created a new ticket!\n Ticket type: {ticket_type}"
)
module_tickets_new_ticket_embed_footer = (
    "Ticket ID: {ticket_id} | Tickets provided by: {bot_name}"
)

# ------------------------------------------------------------------------- #
# FUNCTIONS #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# Audio #
# ------------------------------------------------------------------------- #
# Responses
response_join_failed_no_channel_given = "Oops! It looks like you aren't in a voice channel! Please join one first or give the channel as an argument!"
response_join_failed = "Oops! Something went wrong while trying to join `{channel}`!"
response_join_success = "I joined {channel}!"
response_leave_failed = "Oops! Something went wrong while trying to leave!"
response_leave_success = "I left the channel!"
response_stop_failed = "Oops! Something went wrong while trying to stop audio playback!"
response_stop_success = "I stopped audio playback!"
response_pause_failed_nothing_playing = "There is nothing to pause!"
response_pause_failed_radio_playing = "Oops! It looks like radio station is playing, I can't pause those since it is live!"
response_pause_failed = (
    "Oops! Something went wrong while trying to pause audio playback!"
)
response_pause_success = "I have paused audio playback!"
response_resume_failed_nothing_playing = "There is nothing to resume!"
response_resume_failed_radio_playing = (
    "Oops! It looks like radio station is playing, these can't be resumed!"
)
response_resume_failed = "Oops! Something went wrong while trying to resume the audio!"
response_resume_success = "I have resumed audio playback!"
response_music_shuffle_not_playing_anything = (
    "Oops! It looks like there is nothing to shuffle!"
)
response_music_shuffle_playing_radio = (
    "Oops! I can't shuffle when a radio station is playing!"
)
response_music_shuffle_failed = (
    "Oops! Something went wrong while trying to shuffle the queue!"
)
response_music_shuffle_success = "I have shuffled the queue!"
response_music_skip_nothing_to_skip = "There is nothing to skip!"
response_music_skip_loop_enabled = (
    "I can't skip because loop is `enabled`! Please disable loop and try again"
)
response_music_skip_failed_radio_playing = "I am sorry! I can't skip a radio station!"
response_music_skip_nothing_to_skip = "There is nothing to skip!"
response_music_skip_stop_failed = (
    "Oops! Something went wrong while trying to stop audio playback!"
)
response_music_skip_song_success = "I have skipped `{title}`."
response_music_seek_wrong_time_format = "I am sorry! The time is in the wrong format!"
response_music_seek_nothing_playing = "There is nothing playing!"
response_music_seek_failed_radio_playing = (
    "I am sorry! I can't forward a radio station!"
)
response_music_seek_success = "I have jumped to `{time}`!"
response_music_restart_nothing_playing = (
    "I am sorry! I can't restart a song because there is no song playing!"
)
response_music_restart_failed_radio_playing = (
    "I am sorry! I can't restart a radio station!"
)
response_music_restart_success = "I have restarted the song!"
response_nowplaying_not_playing_anything = "I am not playing anything!"
response_queue_empty = "There is nothing in the queue."
response_queue_timeout_reached = "The queue timeout, please initiate the command again!"
response_loop_failed_not_in_voicechannel = (
    "Oops! I can't loop because it looks like you are not in the (right) voice channel!"
)
response_loop_failed_queue_empty = (
    "Oops! I can't toggle loop because there is nothing playing!"
)
response_loop_failed_radio_playing = "I can't toggle loop because radio is playing!"
response_loop_disabled = "I have `disabled` loop!"
response_loop_enabled = "I have `enabled` loop!"
response_volume_changed = "I have changed the volume to `{level}%`!"
response_join_failed_no_suitable_channel = "Oops! I didn't find a suitable voice channel. Please join a voice channel first or make me join a channel!"
response_music_play_join_failed = (
    "Oops! Something went wrong while trying to join `{channel}`!"
)
response_music_play_failed = "Oops! Something went wrong while trying to add the song/playlist/album to the queue!"
response_music_play_failed_radio_playing = "Oops! It looks like a radio station is playing! Please stop this before trying to play a different song!"
response_music_play_adding_song_playlist_album = (
    "I am adding the song/playlist/album to the queue."
)
response_music_play_failed_no_youtube = "Oops! I am not allowed to play YouTube URLs!"
response_music_play_added_playlist = "I have added the playlist to the queue, enjoy!"
response_music_play_added_song = "I have added `{title}` to the queue, enjoy!"
response_music_playtts_join_failed = (
    "Oops! Something went wrong while trying to join `{channel}`!"
)
response_music_playtts_failed = (
    "Oops! Something went wrong while trying to add the text-to-speech message!"
)
response_music_playtts_failed_radio_playing = "Oops! It looks like a radio station is playing! Please stop this before trying to use a text-to-speech message!"
response_music_playtts_adding_song_playlist_album = (
    "I am adding the text-to-speech message to the queue."
)
response_music_playtts_added_song = "I have added the text-to-speech message!"
response_radio_play_join_failed = (
    "Oops! Something went wrong while trying to join `{channel}`!"
)
response_radio_play_failed_http_error = "Oops! Something went wrong while trying to play `{radiostation}`! Got status code: `{status_code}`"
response_radio_play_failed = (
    "Oops! Something went wrong while trying to play `{radiostation}`!"
)
response_radio_play_success = "Playing `{radiostation}`! Provided by TuneIn!"
response_music_playnext_failed = "Oops! Something went wrong while trying to add the song/playlist/album to the queue after the current song!"
response_music_playnext_failed_radio_playing = "Oops! It looks like a radio station is playing! Please stop this before trying to add a song after the current playing song!"
response_music_playnext_adding_song_playlist_album = (
    "I am adding the song/playlist/album to the queue after the current playing song."
)
response_music_playnext_failed_no_youtube = (
    "Oops! I am not allowed to play YouTube URLs!"
)
response_music_playnext_added_playlist = (
    "I have added the playlist to the queue after the current song, enjoy!"
)
response_music_playnext_added_song = (
    "I have added `{title}` to the queue after the current song, enjoy!"
)
response_music_remove_failed_nothing_to_remove = (
    "Oops! It looks like there is nothing to remove!"
)
response_music_remove_failed = (
    "Oops! Something went wrong while trying to remove the song/playlist/album!"
)
response_music_remove_failed_radio_playing = (
    "Oops! I can't delete the song! I am playing radio!"
)
response_music_remove_removing_song_playlist_album = (
    "I am removing the song/playlist/album from the queue."
)
response_music_remove_failed_no_youtube = (
    "Oops! I am not allowed to remove YouTube URLs!"
)
response_music_remove_failed = (
    "Oops! Something went wrong while trying to remove the song/playlist/album!"
)
response_music_remove_removed_playlist = "I have removed the playlist from the queue!"
response_music_remove_removed_song = "I have removed the song from the queue!"
response_search_no_results_found = (
    "I am sorry! I didn't find any results for the query: `{query}`!"
)
response_music_playradio_failed = (
    "I am sorry! Something went wrong while trying to play radio!"
)
response_music_playradio_failed_already_playing = "I am sorry! It looks like there is already something playing, please stop this first to listing to radio!"
# Log Responses
log_response_join_failed_no_channel_given = (
    "{datetime} -- **{member}** tried joining me but didn't gave me a channel to join!"
)
log_response_join_failed_not_enough_privileges = "{datetime} -- **{member}** tried joining me to a channel where I don't have enough permissions for!"
log_response_join_failed_not_a_voice_channel = "{datetime} -- **{member}** tried joining me to a channel but didn't gave a valid voice channel!"
log_response_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}`! But something went wrong!"
log_response_join_success = "{datetime} -- **{member}** joined me to {channel}!"
log_response_leave_failed = "{datetime} -- **{member}** tried to make me leave the voice channel! But something went wrong!"
log_response_leave_success = (
    "{datetime} -- **{member}** made me leave the voice channel!"
)
log_response_stop_failed = (
    "{datetime} -- **{member}** tried to stop audio playback! But something went wrong!"
)
log_response_stop_success = "{datetime} -- **{member}** stopped audio playback!"
log_response_pause_failed_nothing_playing = "{datetime} -- **{member}** tried to pause audio playback! But there was nothing playing!"
log_response_pause_failed_radio_playing = (
    "{datetime} -- **{member}** tried to pause a radio station!"
)
log_response_pause_failed = "{datetime} -- **{member}** tried to pause audio playback! But something went wrong!"
log_response_pause_success = "{datetime} -- **{member}** paused audio playback!"
log_response_resume_failed_nothing_playing = "{datetime} -- **{member}** tried to resume audio playback! But there was nothing playing!"
log_response_resume_failed_radio_playing = (
    "{datetime} -- **{member}** tried to resume a radio station!"
)
log_response_resume_failed = "{datetime} -- **{member}** tried to resume audio playback! But something went wrong!"
log_response_resume_success = "{datetime} -- **{member}** resumed audio playback!"
log_response_music_shuffle_not_playing_anything = "{datetime} -- **{member}** tried to shuffle the queue! But there was nothing to shuffle!"
log_response_music_shuffle_playing_radio = "{datetime} -- **{member}** tried to shuffle the queue! But there was a radio station playing!"
log_response_music_shuffle_failed = (
    "{datetime} -- **{member}** tried to shuffle the queue! But something went wrong!"
)
log_response_music_shuffle_success = "{datetime} -- **{member}** shuffled the queue!"
log_response_music_skip_nothing_to_skip = (
    "{datetime} -- **{member}** tried to skip a song! But there was nothing to skip!"
)
log_response_music_skip_loop_enabled = (
    "{datetime} -- **{member}** tried to skip a song! But loop was enabled!"
)
log_response_music_skip_failed_radio_playing = (
    "{datetime} -- **{member}** tried to skip audio playback! But radio is playing!"
)
log_response_music_skip_nothing_to_skip = (
    "{datetime} -- **{member}** tried to skip a song! But there was nothing to skip!"
)
log_response_music_skip_stop_failed = "{datetime} -- **{member}** tried to stop audio playback because there was nothing left in the queue after a skip! But something went wrong!"
log_response_music_skip_song_success = "{datetime} -- **{member}** skipped a song!"
log_response_music_seek_wrong_time_format = (
    "{datetime} -- **{member}** tried to seek a track! But gave an invalid time format!"
)
log_response_music_seek_nothing_playing = (
    "{datetime} -- **{member}** tried to forward a song! But there was nothing playing!"
)
log_response_music_seek_failed_radio_playing = "{datetime} -- **{member}** tried to forward a radio station! But this is not possible!"
log_response_music_seek_success = (
    "{datetime} -- **{member}** jumped the track tp `{time}`!"
)
log_response_music_restart_nothing_playing = "{datetime} -- **{member}** tried to restart the song! But there is no song playing!"
log_response_music_restart_failed_radio_playing = "{datetime} -- **{member}** tried to restart a radio station! But this is not possible!"
log_response_music_restart_success = (
    "{datetime} -- **{member}** restarted the current playing song!"
)
log_response_nowplaying_not_playing_anything = (
    "{datetime} -- **{member}** requested the playing song! But nothing was playing!"
)
log_response_nowplaying_requested = (
    "{datetime} -- **{member}** requested the now playing song!"
)
log_response_queue_requested = "{datetime} -- **{member}** requested the queue!"
log_response_loop_failed_not_in_voicechannel = "{datetime} -- **{member}** tried to loop! But they are not in the (right) voice channel!"
log_response_loop_failed_queue_empty = (
    "{datetime} -- **{member}** tried to toggle loop! But there is nothing playing!"
)
log_response_loop_failed_radio_playing = "{datetime} -- **{member}** tried to roggle loop! But there is a radio station playing!"
log_response_loop_disabled = "{datetime} -- **{member}** has `disabled` loop!"
log_response_loop_enabled = "{datetime} -- **{member}** has `enabled` loop!"
log_response_volume_changed = (
    "{datetime} -- **{member}** has changed the volume to `{level}%`!"
)
log_response_join_failed_no_suitable_channel = "{datetime} -- **{member}** tried to add a song/playlist/album to the queue but neither off us is in a channel!"
log_response_music_play_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing music! But something went wrong!"
log_response_music_play_failed_song = "{datetime} -- **{member}** tried adding a song to the queue! But something went wrong!"
log_response_music_play_failed_radio_playing = "{datetime} -- **{member}** tried playing a song/playlist/album! But I was playing radio!"
log_response_music_play_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL! But I am not allowed to!"
)
log_response_music_play_added_playlist = (
    "{datetime} -- **{member}** added a playlist to the queue!"
)
log_response_music_play_added_song = (
    "{datetime} -- **{member}** added a song to the queue!"
)
log_response_music_playtts_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing a text-to-speech message! But something went wrong!"
log_response_music_playtts_failed_song = "{datetime} -- **{member}** tried to use a text-to-speech message! But something went wrong!"
log_response_music_playtts_failed_radio_playing = "{datetime} -- **{member}** tried playing a text-to-speech message! But I was playing radio!"
log_response_music_playtts_added_song = "{datetime} -- **{member}** added a text-to-speech message to the queue! Message: `{tts_message}`!"
log_response_radio_play_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing radio! But something went wrong!"
log_response_radio_play_failed_http_error = "{datetime} -- **{member}** tried playing radiostation: `{radiostation}`! But got status code: `{status_code}`!"
log_response_radio_play_failed = "{datetime} -- **{member}** tried playing radiostation: `{radiostation}`! But something went wrong!"
log_response_radio_play_success = "{datetime} -- **{member}** played radiostation: `{radiostation}`! Provided by TuneIn!"
log_response_music_playnext_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing music! But something went wrong!"
log_response_music_playnext_failed_song = "{datetime} -- **{member}** tried adding a song to the queue after the current song! But something went wrong!"
log_response_music_playnext_failed_radio_playing = "{datetime} -- **{member}** tried playing a song/playlist/album after the current song! But I was playing radio!"
log_response_music_playnext_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL! But I am not allowed to!"
)
log_response_music_playnext_failed_song = "{datetime} -- **{member}** tried adding a song to the queue after the current song! But something went wrong!"
log_response_music_play_added_playlist = (
    "{datetime} -- **{member}** added a playlist to the queue!"
)
log_response_music_playnext_added_song = (
    "{datetime} -- **{member}** added a song to the queue after the current song!"
)
log_response_music_remove_failed_nothing_to_remove = "{datetime} -- **{member}** tried to remove a song from the queue! But there was nothing to remove!"
log_response_music_remove_failed_song = "{datetime} -- **{member}** tried to remove a song from the queue! But something went wrong!"
log_response_music_remove_failed_radio_playing = "{datetime} -- **{member}** tried to remove a song from the queue! But I was playing radio!"
log_response_music_remove_failed_no_youtube = (
    "{datetime} -- **{member}** tried removing a YouTube URL! But I am not allowed to"
)
log_response_music_remove_failed_song = "{datetime} -- **{member}** tried to remove a song from the queue! But something went wrong!"
log_response_music_remove_removed_playlist = (
    "{datetime} -- **{member}** removed a playlist from the queue!"
)
log_response_music_remove_removed_song = (
    "{datetime} -- **{member}** removed a song from the queue!"
)
log_response_search_no_results_found = "{datetime} -- **{member}** searched YouTube or SoundCloud with the query: `{query}`! But there were no results found!"
log_response_platform_searched = "{datetime} -- **{member}** searched {platform}!"
log_response_music_playradio_failed = (
    "{datetime} -- **{member}** tried to listen to radio! But something went wrong!"
)
log_response_music_playradio_failed_already_playing = "{datetime} -- **{member}** tried to listen to radio! But there was already something playing!"
# Embeds
nowplaying_embed_title = "Now playing"
nowplaying_embed_field_title_radio = "Radiostation"
nowplaying_embed_field_title_added_by = "Added by"
nowplaying_embed_field_title_title = "Title"
nowplaying_embed_field_title_artist = "Artist"
nowplaying_embed_field_title_position = "Position"
queue_embed_title = "Queue"
queue_embed_field_title_now_playing = "Now playing"
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
bot_general = "General info"
module_logging = "Logging module"
module_greetings = "Greetings module"
module_tempchannels = "Temporary Channels module"
module_socials = "Socials module"
module_reaction_roles = "Reaction Roles module"
module_autoresponder = "Autoresponder module"
module_tickets = "Tickets module"
module_ticket_view_types = "View ticket types"
module_ticket_view_generals_settings = "View settings"
module_serverstats = "ServerStats module"
bot_info = "Bot info"
server_info = "Server info"
channel_info = "Channel info"
role_info = "Role info"
user_info = "User info"
server_stats = "Server statistics"
user_stats = "User statistics"
last_24h = "Last 24 hours"
last_7d = "Last 7 days"
last_30d = "Last 30 days"
no_stats = "No stats available!"
# Responses
response_info_bot_module_logging_disabled = "The `Logging` module is disabled!"
response_info_bot_module_greetings_disabled = "The `Greetings` module is disabled!"
response_info_bot_module_tempchannels_disabled = (
    "The `TempChannels` module is disabled!"
)
response_info_bot_module_socials_disabled = "The `Socials` module is disabled!"
response_module_socials_reddit_list_empty = (
    "I am not monitoring any Subreddits in this server!"
)
response_module_socials_rss_list_empty = (
    "I am not monitoring any RSS Feeds in this server!"
)
response_module_socials_twitch_list_empty = (
    "I am not monitoring any Twitch accounts in this server!"
)
response_info_bot_module_reaction_roles_disabled = (
    "The `Reaction Roles` module is disabled!"
)
response_invite_link_not_set = "The server has not set an invite link for users to use!"
response_info_bot_module_tickets_disabled = "The `Tickets` module is disabled!"
response_module_autoresponder_no_info = "The `Autoresponder` module does not have information available! For the status of the `Autoresponder` module, please check the General info page!"
response_info_bot_module_serverstats_disabled = "The `ServerStats` module is disabled!"
response_info_timeout = "The info command reached a timeout!"
# Log Responses
log_response_module_socials_reddit_list = (
    "{datetime} -- **{member}** requested the Subreddit list!"
)
log_response_module_socials_rss_list = (
    "{datetime} -- **{member}** requested the RSS Feed list!"
)
log_response_module_socials_twitch_list = (
    "{datetime} -- **{member}** requested the Twitch account list!"
)
log_response_info_bot_requested = "{datetime} -- **{member}** requested my information!"
log_response_info_channel_requested_failed = "{datetime} -- **{member}** requested information about a channel! But someting went wrong!"
log_response_info_channel_requested = (
    "{datetime} -- **{member}** requested information about the channel: `{channel}`!"
)
log_response_invite_link_not_set = (
    "{datetime} -- **{member}** requested the configured invite link! but none was set!"
)
log_response_invite_link_requested = (
    "{datetime} -- **{member}** requested the configured invite link!"
)
log_response_info_role_requested = (
    "{datetime} -- **{member}** requested information about the role: {role}!"
)
log_response_info_server_requested = (
    "{datetime} -- **{member}** requested information about the server!"
)
log_response_info_user_requested = (
    "{datetime} -- **{member}** requested information about {user}!"
)
# Embeds
info_bot_embed_title = "Welcome to {bot_name}! {version}"
info_bot_embed_discription = "Hi! Welcome to the `{bot_name}` information panel! Here you will find all settings done for this server, the current version and some external links! Make sure to have a look around!\n\n *Note: Use the navigation buttons below to view system metrics.*"
info_bot_embed_field_title_language = "Language:"
info_bot_embed_field_title_gmt = "Timezone:"
info_bot_embed_field_title_unit_system = "Unit system:"
info_bot_embed_field_title_auto_delete = "Automatically delete bot messages after:"
info_bot_embed_field_value_auto_delete = "seconds"
info_bot_embed_field_title_max_warns = "Max warning points:"
info_bot_embed_field_value_max_warns = "points (per user)"
info_bot_embed_field_title_auto_kick = "Auto kick:"
info_bot_embed_field_title_auto_kick_role = "Auto kick role:"
info_bot_embed_field_title_send_poll_results_in_chat = "Send poll results in chat:"
info_bot_embed_field_title_poll_save_timeout = "Poll save timeout:"
info_bot_embed_field_title_modules_enabled = "Enabled Modules:"
info_bot_embed_field_title_modules_disabled = "Disabled Modules:"
info_bot_embed_field_title_resources = "Resources:"
info_bot_embed_field_value_resources_1_name = "Invite {bot_name}"
info_bot_embed_field_value_resources_1_value = "Add {bot_name} to your own server!"
info_bot_embed_field_value_resources_2_name = "{bot_name} website"
info_bot_embed_field_value_resources_2_value = "Visit our website!"
info_bot_embed_field_value_resources_3_name = "{bot_name} Support Server"
info_bot_embed_field_value_resources_3_value = "Join our Support Server!"
info_bot_embed_field_value_resources_4_name = "Discords website"
info_bot_embed_field_value_resources_4_value = "Visit Discords website!"
info_bot_embed_field_title_logging_channel = "Logging Channel:"
info_bot_embed_field_title_logging_events_1 = "Events that are logged (1/3):"
info_bot_embed_field_title_logging_events_2 = "Events that are logged (2/3):"
info_bot_embed_field_title_logging_events_3 = "Events that are logged (3/3):"
info_bot_embed_field_title_enabled_components = "Enabled components:"
info_bot_embed_field_title_greetings_in_guild_embed = "Embed for in server greetings:"
info_bot_embed_field_title_greetings_to_user_embed = "Embed for user DM greetings:"
info_bot_embed_field_title_leave_taking_in_guild_embed = (
    "Embed for in server leave taking:"
)
info_bot_embed_field_title_greetings_in_guild_channel = "Greetings in server channel:"
info_bot_embed_field_title_leave_taking_in_guild_channel = (
    "Leave taking in server channel:"
)
info_bot_embed_field_title_greetings_in_guild_content = "Greetings content in server:"
info_bot_embed_field_title_greetings_to_user_content = "Greetings content to users:"
info_bot_embed_field_title_greetings_role_add_role = "Role that gets added to users:"
info_bot_embed_field_title_leave_taking_in_guild_content = (
    "Leave taking content in server:"
)
info_bot_embed_field_title_tempchannels_voice_create_channel = (
    "Channel to create temporary channel:"
)
info_bot_embed_field_title_tempchannels_voice_category = (
    "The category where voice channels are created:"
)
info_bot_embed_field_title_tempchannels_create_text = "Create text channels:"
info_bot_embed_field_title_tempchannels_text_category = (
    "The category where text channels are created:"
)
info_bot_embed_field_title_tempchannels_voice_channel_name = (
    "Name of the voice channels that get created:"
)
info_bot_embed_field_title_tempchannels_text_channel_name = (
    "Name of the text channels that get created:"
)
info_bot_embed_field_title_socials_monitor_reddit = "Monitor Reddit:"
info_bot_embed_field_title_socials_monitor_reddit_channel = "Reddit updates channel:"
info_bot_embed_field_title_socials_monitor_reddit_mention_everyone = (
    "Reddit mention everyone:"
)
info_bot_embed_field_title_socials_monitor_rss = "Monitor RSS Feeds:"
info_bot_embed_field_title_socials_monitor_rss_channel = "RSS Feeds updates channel:"
info_bot_embed_field_title_socials_monitor_rss_mention_everyone = (
    "RSS Feeds mention everyone:"
)
info_bot_embed_field_title_socials_monitor_twitch = "Monitor Twitch accounts:"
info_bot_embed_field_title_socials_monitor_twitch_channel = (
    "Twitch accounts updates channel:"
)
info_bot_embed_field_title_socials_monitor_twitch_mention_everyone = (
    "Twitch accounts mention everyone:"
)
info_bot_embed_field_title_reaction_roles_delete_unrelated = "Delete unrelated emoji's"
info_bot_embed_field_title_reaction_roles_remove_role_from_users_on_delete = (
    "Remove roles from users on reactions role delete:"
)
module_socials_reddit_embed_description_list = (
    "Below you can find the list of all subreddits being monitored."
)
module_socials_reddit_embed_field_list = "Monitored Subreddits:"
module_socials_rss_embed_description_list = (
    "Below you can find the list of all RSS Feeds being monitored."
)
module_socials_rss_embed_field_list = "Monitored RSS Feeds:"
module_socials_twitch_embed_description_list = (
    "Below you can find the list of all Twitch accounts being monitored."
)
module_socials_twitch_embed_field_list = "Monitored Twitch accounts:"
info_bot_embed_field_title_tickets_support_role = "Ticket Support Role"
info_bot_embed_field_title_tickets_creation_category = "Creation Category"
info_bot_embed_field_title_tickets_creation_channel = "Creation Channel"
info_bot_embed_field_title_tickets_creation_message = "Creation Message"
info_bot_embed_field_title_tickets_thread_mode = "Thread mode"
info_bot_embed_field_title_tickets_post_channel = "Post channel"
info_bot_embed_field_title_tickets_is_custom_creation_message = (
    "Custom creation is message?"
)
info_bot_embed_field_title_tickets_is_custom_creation_embed = (
    "Custom creation is embed?"
)
info_bot_embed_field_title_tickets_is_custom_creation_content = (
    "Custom creation content"
)
info_bot_embed_field_title_tickets_is_custom_creation_modal = "Custom creation modal"
info_bot_embed_field_title_tickets_default_types = "Used default types"
info_bot_embed_field_title_tickets_custom_types = "Used custom types"
info_bot_embed_field_title_reaction_roles_delete_unrelated = "Delete unrelated emoji's"
info_bot_embed_field_title_reaction_roles_remove_role_from_users_on_delete = (
    "Remove roles from users on reactions role delete:"
)
info_channel_embed_title = "Information about {channel}"
info_channel_embed_description = "Hi! Welcome to the `{channel}` information panel!"
info_channel_embed_field_title_channel = "Channel:"
info_channel_embed_field_title_channelid = "Channel ID:"
info_channel_embed_field_title_channeltype = "Channel Type:"
info_channel_embed_field_title_createdat = "Channel created at:"
invite_link_embed_title = "Server invite link"
invite_link_embed_description = "Do you want to invite other friends? Please use the following invite link:\n {link}"
info_role_embed_title = "Information about {role}"
info_role_embed_description = "Hi! Welcome to the `{role}` information panel!"
info_role_embed_field_title_role = "Role:"
info_role_embed_field_title_roleid = "Role ID:"
info_role_embed_field_title_rolepos = "Role position (Up ^):"
info_role_embed_field_title_createdat = "Role created at:"
info_role_embed_field_title_permissions = "Permissions of this role:"
info_role_embed_field_value_permissions_1_value = "Permissions value: "
info_server_embed_title = "Information about {guild}"
info_server_embed_no_description = (
    "Hi! Welcome to `{guild}` information panel! There is no server description set!"
)
info_server_embed_field_title_owner = "Owner:"
info_server_embed_field_title_ownerid = "Owner ID:"
info_server_embed_field_title_afkchannel = "AFK Channel:"
info_server_embed_field_title_member_count = "Member count:"
info_server_embed_field_title_channels = "Channel count:"
info_server_embed_field_title_roles = "Role count:"
info_server_embed_field_title_members = "Members (excl. Bots):"
info_server_embed_field_title_createdat = "Server created at:"
info_server_embed_serverstats_title = "Serverstats for {guild}"
info_server_embed_serverstats_description = "Hi! Welcome to the `{guild}` serverstats panel! Showing stats for the `{timeframe}`"
info_server_embed_serverstats_command_usage_most_used_command = "Most used command:"
info_server_embed_serverstats_command_usage_most_used_command_count = "Times used:"
info_server_embed_serverstats_command_usage_total_command_count = "Total commands used:"
info_server_embed_serverstats_command_usage_component_disabled = (
    "Command Usage component is disabled"
)
info_server_embed_serverstats_message_statistics_most_used_channel = (
    "Most used channel:"
)
info_server_embed_serverstats_message_statistics_most_active_author = (
    "Most active author:"
)
info_server_embed_serverstats_message_statistics_total_message_count = (
    "Total server messages:"
)
info_server_embed_serverstats_message_statistics_component_disabled = (
    "Message Statistics component is disabled"
)
info_user_embed_title = "Information about {user}"
info_user_embed_description = "Hi! Welcome to the `{user}` information panel! This user has `{warn_points} warnings` in this server!"
info_user_embed_field_title_user = "User:"
info_user_embed_field_title_userid = "User ID:"
info_user_embed_field_title_userdiscriminator = "Discriminator:"
info_user_embed_field_title_userisbot = "Is bot:"
info_user_embed_field_title_userismute = "Is muted:"
info_user_embed_field_title_userisdeaf = "Is deafend:"
info_user_embed_field_title_joinedat = "Joined Server at:"
info_user_embed_field_title_createdat = "Joined Discord at:"
info_user_embed_field_title_roles = "Roles:"
info_user_embed_serverstats_title = "Serverstats for {user}"
info_user_embed_serverstats_description = (
    "Hi! Welcome to the `{user}` serverstats panel! Showing stats for the `{timeframe}`"
)
info_user_embed_serverstats_command_usage_most_used_command = "Most used command:"
info_user_embed_serverstats_command_usage_most_used_command_count = "Times used:"
info_user_embed_serverstats_command_usage_total_command_count = "Total commands used:"
info_user_embed_serverstats_command_usage_component_disabled = (
    "Command Usage component is disabled"
)
info_user_embed_serverstats_message_statistics_most_used_channel = "Most used channel:"
info_user_embed_serverstats_message_statistics_messages_sent_in_channel = (
    "Messages sent in channel:"
)
info_user_embed_serverstats_message_statistics_total_messages = "Total messages sent:"
info_user_embed_serverstats_message_statistics_component_disabled = (
    "Message Statistics component is disabled"
)
info_bot_embed_field_title_serverstats_counter_panel_enabled = "Counter Panel:"
info_bot_embed_field_title_serverstats_counter_panel_category = (
    "Counter Panel Category:"
)
info_bot_embed_field_title_serverstats_panel_member_count = "Member Count panel:"
info_bot_embed_field_title_serverstats_panel_online_member_count = (
    "Online Member Count panel:"
)
info_bot_embed_field_title_serverstats_panel_online_members_with_role = (
    "Online with role panel:"
)
info_bot_embed_field_title_serverstats_panel_boost = "Boost panel"
info_bot_embed_field_title_serverstats_starboard_enabled = "Starboard:"
info_bot_embed_field_title_serverstats_starboard_channel = "Starboard Channel:"
info_bot_embed_field_title_serverstats_starboard_count = "Starboard minimum stars:"
info_embed_title = "Info"
info_embed_description = "Please select the component you want info about."
info_embed_description_select_channel = "Please select the channel you want info about."
info_embed_description_select_role = "Please select the role you want info about."
info_embed_description_select_user = "Please select the user you want info about."

# ------------------------------------------------------------------------- #
# Misc #
# ------------------------------------------------------------------------- #
higher_lower_higher = "Higher"
higher_lower_equal = "Equal"
higher_lower_lower = "Lower"
# Responses
response_games_heads_or_tails_heads = "It's `heads`!"
response_games_heads_or_tails_tails = "It's `tails`!"
response_rps_timeout = "{user} didn't respond quick enough. The game has timed out!"
response_rps_users_turn = "{user}, your turn!"
response_rps_winner = "Congratulations {user}! You won the Rock, Paper, Scissors game!"
response_higher_lower_timeout = "The Higher/Lower game has timed out!"
response_host_information_failed = (
    "Oops! Something went wrong while trying to retrieve host information!"
)
response_host_information_timeout = "The host information reached a timeout!"
response_ping_success = (
    "Pong! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
)
response_transcribe_success = "***Transcription:*** ```{transcribed_message}```"
response_transcribe_failed = (
    "Something went wrong while trying to transcribe the message!"
)
# Log Responses
log_response_games_played = "{datetime} -- **{member}** played `{game}`!"
log_response_games_played_rps = "{datetime} -- **{member}** played `{game}` against {opponent}! The winner is {winner}!"
log_response_host_information_failed = "{datetime} -- **{member}** tried to retrieve host information! But something went wrong!"
log_response_host_information = "{datetime} -- **{member}** requested host information!"
log_response_ping_requested = "{datetime} -- **{member}** used `/ping`! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
log_response_transcribe_success = (
    "{datetime} -- **{member}** transcribed a voice message!"
)
log_response_transcribe_failed = "{datetime} -- **{member}** tried to transcribe a voice message! But something went wrong!"
log_response_higher_lower_played_won = (
    "{datetime} -- **{member}** played `{game}` and won!"
)
log_response_higher_lower_played_loss = (
    "{datetime} -- **{member}** played `{game}` and won!"
)
log_response_meme_success = "{datetime} -- **{member}** requested a meme!"
# Embeds
rps_embed_title = "Rock, Paper, Scissors game"
rps_embed_user_ones_turn = "{user_one} is choosing...\n {user_two} is waiting..."
rps_embed_user_twos_turn = "{user_one} is waiting...\n {user_two} is choosing..."
higher_lower_embed_title = "Higher/Lower"
higher_lower_embed_description = "Hello {member}! I have picked a number between 0 and 100! Do you think this number is higher, lower or equal to `{hint_number}`?"
higher_lower_embed_description_win = "Congratulations {member}! You are **correct**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
higher_lower_embed_description_loss = "Too bad {member}! You are **wrong**!\n\nThe secret number was {secret_number}\nThe hint number was {hint_number}\nYou chose {chosen_option}"
host_embed_title = "24 hours host information"
host_embed_cpu_description = "A CPU (Central Processing Unit) is responsible for oricessing and executing a set of instructions and act as the brain of a device."
host_embed_field_cpu_high = "Processor high:"
host_embed_field_cpu_avg = "Processor average:"
host_embed_field_cpu_low = "Processor low:"
host_embed_graph = "Last 24 hours graph:"
host_embed_ram_description = "Memory is the electronic holding place for the instructions and data a computer needs to reach quickly."
host_embed_field_ram_high = "Memory high:"
host_embed_field_ram_avg = "Memory average:"
host_embed_field_ram_low = "Memory low:"
host_embed_disk_description = "Storage is a process through which digital data is saved within a data storage device."
host_embed_field_disk_high = "Storage high:"
host_embed_field_disk_avg = "Storage average:"
host_embed_field_disk_low = "Storage low:"
host_embed_rest_latency_description = "Latency is a measure of delay. In a network, latency measures the time it takes for some data to get to its destination across the network"
host_embed_field_rest_latency_high = "REST latency high:"
host_embed_field_rest_latency_avg = "REST latency average:"
host_embed_field_rest_latency_low = "REST latency low:"
host_embed_gateway_latency_description = "Latency is a measure of delay. In a network, latency measures the time it takes for some data to get to its destination across the network"
host_embed_field_gateway_latency_high = "Gateway latency high:"
host_embed_field_gateway_latency_avg = "Gateway latency average:"
host_embed_field_gateway_latency_low = "Gateway latency low:"
meme_footer = "Visit to Reddit to view top new memes!"

# ------------------------------------------------------------------------- #
# Mod_Server #
# ------------------------------------------------------------------------- #
reason_default_channel_lock = "**{member}** asked for channel lock -> {reason}"
reason_default_channel_unlock = "**{member}** asked for channel unlock -> {reason}"
# Responses
response_channel_create_success = "I have created the `{channel_type}`! -> {channel}."
response_channel_create_failed = (
    "I am sorry! Something went wrong while trying to create the channel!"
)
response_channel_create_news_stage_forum_failed = "I am sorry! Something went wrong while trying to create the channel! Does this server support this channel type?"
response_channel_delete_failed = (
    "I am sorry! Something went wrong while trying to delete the `{channel}`!"
)
response_channel_delete_success = "I have deleted `{channel}`!"
response_clear_messages_failed_over_14_days = (
    "I am sorry! I can't bulk delete messages that are over 14 days old!"
)
response_slowmode_set_failed = "Something went wrong while trying to set slowmode for `{channel}` to `{delay} seconds`!"
response_slowmode_set_success = (
    "I have set the slowmode in `{channel}` to `{delay} seconds`!"
)
response_lock_failed = (
    "I am sorry! Something went wrong while trying to lock {channel}!"
)
response_lock_success = "I have locked {channel}!"
response_unlock_failed = (
    "I am sorry! Something went wrong while trying to unlock {channel}!"
)
response_unlock_success = "I have unlocked {channel}!"
response_role_create_failed = (
    "I am sorry! Something went wrong while trying to create the role!"
)
response_role_create_success = "I have created the `{role_name}` role! -> {role}."
response_role_delete_failed = (
    "I am sorry! Something went wrong while trying to delete the `{role}`!"
)
response_role_delete_success = "I have deleted `{role}`!"
# Log Responses
log_response_channel_create_failed = "{datetime} -- **{member}** tried to create a `{channel_type}`! But something went wrong!"
log_response_channel_create_news_stage_forum_failed = "{datetime} -- **{member}** tried to create a `{channel_type}`! But something went wrong! Does this server support this channel type?"
log_response_channel_delete_failed = "{datetime} -- **{member}** tried deleting the channel `{channel}`! But something went wrong!"
log_response_clear_messages_failed_over_14_days = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in {channel}! But (some) messages are over 14 days old!"
log_response_clear_messages_failed = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in {channel}! But something went wrong!"
log_response_clear_messages_invalid_channel = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}`! But this is not a text channel!"
log_response_clear_messages_finished = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}`! I have deleted `{amount_deleted}` messages!"
log_response_slowmode_set_failed = "{datetime} -- **{member}** tried to set slowmode for `{channel}`! But something went wrong!"
log_response_slowmode_set_success = (
    "{datetime} -- **{member}** set slowmode for `{channel}` to `{delay} seconds`!"
)
log_response_lock_failed_not_a_text_channel = "{datetime} -- **{member}** tried to lock {channel}! But the given channel is not a text channel!"
log_response_lock_failed = (
    "{datetime} -- **{member}** tried to lock {channel}! But something went wrong!"
)
log_response_lock_success = "{datetime} -- **{member}** locked {channel}!"
log_response_unlock_failed_not_a_text_channel = "{datetime} -- **{member}** tried to unlock {channel}! But the given channel is not a text channel!"
log_response_unlock_failed = (
    "{datetime} -- **{member}** tried to unlock {channel}! But something went wrong!"
)
log_response_unlock_success = "{datetime} -- **{member}** unlocked {channel}!"
log_response_role_create_failed = "{datetime} -- **{member}** tried to create a `Role` with the name `{role_name}`! But something went wrong!"
log_response_role_delete_failed = "{datetime} -- **{member}** tried deleting the role `{role}`! But something went wrong!"
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
reason_auto_kick_role_added_warn = (
    "*User reached/went over maximum warning limit set for this server!*"
)
reason_auto_kick_role_removed_warn = (
    "*User is not longer over maximum warning limit set for this server!*"
)
# Responses
response_ban_create_failed_no_bot_ban = "I am sorry! I can't ban a bot!"
response_ban_create_failed = (
    "I am sorry! Something went wrong while trying to ban `{user}`!"
)
response_ban_create_success = "I have banned `{user}`!"
response_ban_delete_failed_no_bot_unban = "I am sorry! I can't unban a bot!"
response_ban_delete_failed = (
    "I am sorry! Something went wrong while trying to unban `{user}`!"
)
response_ban_delete_success = "I have unbanned `{user}`!"
response_kick_failed_no_bot_kick = "I am sorry! I can't kick a bot!"
response_kick_failed = "I am sorry! Something went wrong while trying to kick {user}!"
response_kick_success = "I have kicked {user}!"
response_vckick_failed = "I am sorry! Something went wrong while trying to kick {user} from the voice channel!"
response_vckick_success = "I have kicked {user} from the voice channel!"
response_move_failed_user_not_in_a_voice_channel = "{user} is not in a voice channel!"
response_move_failed_missing_permissions = (
    "I am sorry! It looks like either I or the user is missing permissions!"
)
response_move_failed = (
    "I am sorry! Something went wrong while trying to move {user} to {channel}!"
)
response_move_success = "I have moved {user} to {channel}!"
response_tempmute_failed_no_bot_tempmute = "I am sorry! I can't temporary mute a bot!"
response_tempmute_failed = (
    "I am sorry! Something went wrong while trying to temporary mute {user}!"
)
response_tempmute_success = "I have temporary muted {user} for `{seconds} seconds`!"
response_temptimeout_failed_no_bot_temptimeout = (
    "I am sorry! I can't temporary timeout a bot!"
)
response_temptimeout_failed = (
    "I am sorry! Something went wrong while trying to temporary timeout {user}!"
)
response_temptimeout_success = (
    "I have temporary timedout {user} for `{seconds} seconds`!"
)
response_warn_create_failed_no_bot_warn = "I am sorry! I can't warn a bot!"
response_warn_create_failed = (
    "I am sorry! Something went wrong while trying to warn `{member}`!"
)
response_warn_create_success = "I have warned `{user}`!"
response_warn_delete_failed_no_bot_warn_delete = (
    "I am sorry! I can't delete a warn from bot!"
)
response_warn_delete_failed = (
    "I am sorry! Something went wrong while trying to delete a warn from `{member}`!"
)
response_warn_delete_success = "I have deleted a warn from `{user}`!"
# Log Responses
log_response_ban_create_failed_no_bot_ban = (
    "{datetime} -- **{member}** tried to ban `{user}`! But this is a bot!"
)
log_response_ban_create_failed = (
    "{datetime} -- **{member}** tried to ban `{user}`! But something went wrong!"
)
log_response_ban_delete_failed_no_bot_unban = (
    "{datetime} -- **{member}** tried to unban `{user}`! But this is a bot!"
)
log_response_ban_delete_failed = (
    "{datetime} -- **{member}** tried to unban `{user}`! But something went wrong!"
)
log_response_kick_failed_no_bot_kick = (
    "{datetime} -- **{member}** tried to kick {user}! But this is a bot!"
)
log_response_kick_failed = (
    "{datetime} -- **{member}** tried to kick {user}! But something went wrong!"
)
log_response_vckick_failed = "{datetime} -- **{member}** tried to kick {user} from a voice channel! But something went wrong!"
log_response_vckick_success = "{datetime} -- **{member}** has kicked {user} from a voice channel!\n`[Reason]` -- {reason}"
log_response_move_failed_not_a_voice_channel = "{datetime} -- **{member}** tried to move {user} to {channel}! But this channel is not a voice channel!"
log_response_move_failed_user_not_in_a_voice_channel = "{datetime} -- **{member}** tried to move {user} to {channel}! But this user is not in a voice channel!"
log_response_move_failed_missing_permissions = "{datetime} -- **{member}** tried to move {user} to {channel}! But either I or this user is missing permissions!"
log_response_move_failed = "{datetime} -- **{member}** tried to move {user} to {channel}! But something went wrong!"
log_response_move_success = (
    "{datetime} -- **{member}** has moved {user} to {channel}!\n`[Reason]` -- {reason}"
)
log_response_tempmute_failed_no_bot_tempmute = (
    "{datetime} -- **{member}** tried to temporary mute {user}! But this is a bot!"
)
log_response_tempmute_failed = "{datetime} -- **{member}** tried to temporary mute {user}! But something went wrong!"
log_response_tempmute_success = (
    "{datetime} -- **{member}** temporary muted {user} for `{seconds} seconds`!"
)
log_response_temptimeout_failed_no_bot_temptimeout = (
    "{datetime} -- **{member}** tried to temporary timeout {user}! But this is a bot!"
)
log_response_temptimeout_failed = "{datetime} -- **{member}** tried to temporary timeout {user}! But something went wrong!"
log_response_temptimeout_success = (
    "{datetime} -- **{member}** has temporary timedout {user} for `{seconds} seconds`!"
)
log_response_warn_create_failed_no_bot_warn = (
    "{datetime} -- **{member}** tried to warn `{user}`! But this is a bot!"
)
log_response_warn_create_failed = (
    "{datetime} -- **{member}** tried to warn `{user}`! But something went wrong!"
)
log_response_warn_create_success = "{datetime} -- **{member}** warned `{user}` and added `{points} points` to their profile!\n`[Reason]` -- {reason}"
log_response_warn_delete_failed_no_bot_warn_delete = "{datetime} -- **{member}** tried to delete a warn from `{user}`! But this is a bot!"
log_response_warn_delete_failed = "{datetime} -- **{member}** tried to delete a warn from `{user}`! But something went wrong!"
log_response_warn_delete_success = "{datetime} -- **{member}** deleted a warn from `{user}` and removed `{points} points` from their profile!\n`[Reason]` -- {reason}"
# Embeds
warn_create_to_user_embed_title = "You have been warned!"
warn_create_to_user_embed_description = "You have been warned in `{guild}`! They have added `{points} points` to your profile!\nYour total points: {total} points!\n\n[Reason] -- {reason}"
warn_delete_to_user_embed_title = "Warning revoked!"
warn_delete_to_user_embed_description = "A previous warning in `{guild}` has been revoked! They have removed `{points} points` from your profile!\nYour total points: {total} points!\n\n[Reason] -- {reason}"

# ------------------------------------------------------------------------- #
# Polls #
# ------------------------------------------------------------------------- #
# Responses
response_poll_clear_votes_failed_no_poll_found = "I didn't find a poll with that ID!"
response_poll_clear_votes = "I have cleared your votes!"
response_poll_create_failed_anwers_in_wrong_order = "The answers are not in the right order! (if more than the required two anwers are used, make sure it is in the order answer3, answer4 and answer5)!"
response_poll_create_failed_exceeded_max_choices = "The maximum amount of choices per person in this configuration is {max_choices} choices!"
response_poll_create_failed_not_a_valid_time = "The given time duration is not in the valid format, please use the format {delay}{h/m/s} - f.e. 1h or 20m"
response_poll_create_failed_no_time = (
    "When using a Timed poll, please insert the time for it to be active!"
)
response_poll_created = "I have created the poll."
response_poll_delete_failed_no_poll_found = "I didn't find a poll with that ID!"
response_poll_delete_failed_not_owner = (
    "You can't delete this poll since you are not the owner!"
)
response_poll_delete = "I have deleted the poll!"
response_poll_details_timeout = "The poll details timed out!"
response_polls_list_no_polls = "You do not have any active polls in this server!"
response_poll_list_timeout = "The poll list timed out!"
response_poll_stop_failed_no_poll_found = "I didn't find a poll with that ID!"
response_poll_stop_failed_not_owner = (
    "You can't stop this poll since you are not the owner!"
)
response_poll_stop = "The poll is closed!"
# Log Responses
log_response_poll_clear_votes_failed_no_poll_found = "{datetime} -- **{member}** tried to delete a poll! But the given poll ID was not found!"
log_response_poll_clear_votes = (
    "{datetime} -- **{member}** cleared their votes from a poll!"
)
log_response_poll_create_failed_anwers_in_wrong_order = "{datetime} -- **{member}** tried to create a poll! But the extra answers are not in order (if more than the required two anwers are used, make sure it is in the order answer3, answer4 and answer5)!"
log_response_poll_create_failed_exceeded_max_choices = "{datetime} -- **{member}** tried to create a poll! But the maximum amount of choices per person exceeded the maximum amount!"
log_response_poll_create_failed_not_a_valid_time = "{datetime} -- **{member}** tried to create a timed poll! But they gave an invalid time duration!"
log_response_poll_create_failed_no_time = "{datetime} -- **{member}** tried to create a timed poll! But they didn't insert a time duration!"
log_response_poll_create_failed = (
    "{datetime} -- **{member}** tried to create a poll! But something went wrong!"
)
log_response_poll_created = "{datetime} -- **{member}** created a poll!"
log_response_poll_delete_failed_no_poll_found = "{datetime} -- **{member}** tried to delete a poll! But the given poll ID was not found!"
log_response_poll_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a poll! But they are not the owner!"
)
log_response_poll_delete_failed = (
    "{datetime} -- **{member}** tried to delete a poll! But something went wrong!"
)
log_response_poll_delete = "{datetime} -- **{member}** deleted a poll!"
log_response_poll_details_requested = (
    "{datetime} -- **{member}** requested the details/results of a poll!"
)
log_response_polls_list_no_polls = "{datetime} -- **{member}** requested their poll list! But they don't have any active polls!"
log_response_poll_list_requested = (
    "{datetime} -- **{member}** requested their poll list!"
)
log_response_poll_stop_failed_no_poll_found = "{datetime} -- **{member}** tried to stop a poll! But the given poll ID was not found!"
log_response_poll_stop_failed_not_owner = (
    "{datetime} -- **{member}** tried to stop a poll! But they are not the owner!"
)
log_response_poll_stop_failed = (
    "{datetime} -- **{member}** tried to stop a poll! But something went wrong!"
)
log_response_poll_stop = "{datetime} -- **{member}** stopped a poll!"
# Embeds
poll_embed_title = "New poll"
poll_embed_choices = "Choices:"
poll_embed_footer = "Poll ID: {poll_id} - Poll by: {owner}"
poll_details_embed_title = "Poll details/results"
poll_details_embed_poll_id = "Poll ID:"
poll_details_embed_is_finished = "Is finished:"
poll_details_embed_poll_owner = "Poll owner:"
poll_details_embed_question = "Question:"
poll_details_channel = "Channel:"
poll_details_settings = "Poll settings:"
poll_details_settings_anonymous = "Anonymous:"
poll_details_settings_max_choices = "Maximum choices:"
poll_details_settings_per_person = "per person"
poll_details_embed_member_view_no_votes = "No votes for this answer!"
poll_details_embed_redacted_anonymous_poll = "This is an anonymous poll!"
poll_details_embed_answers = "Answers:"
poll_details_embed_results = "Results:"
poll_details_embed_total_votes = "Total votes:"
poll_list_embed_title = "Active polls"
poll_list_embed_description = "You have {polls} polls! Showing your active polls:"
poll_list_embed_field_polls = "Your active polls:"

# ------------------------------------------------------------------------- #
# Privacy #
# ------------------------------------------------------------------------- #
privacy_data_overview = "View my data"
privacy_data_collection = "Data collection"
privacy_data_collection_enable_all = "Allow data collection in all servers"
privacy_data_collection_enable_specific = "Allow data collection in this servers"
privacy_data_collection_disable_all = "Disallow data collection in all servers"
privacy_data_collection_disable_specific = "Disallow data collection in this server"
privacy_data_collection_quick_delete_server = "Quick data delete (this server)"
privacy_data_collection_quick_delete_all = "Quick data delete (all servers)"
# Responses
response_privacy_timeout = (
    "The privacy command reached a timeout! Nothing will be changed!"
)
response_privacy_allow_all_servers_failed = "I am sorry! Something went wrong while allowing {bot_name} to collect your data in all servers you share with {bot_name}!"
response_privacy_allow_specific_server_failed = "I am sorry! Something went wrong while allowing {bot_name} to collect your data in this server!"
response_privacy_disable_all_servers_failed = "I am sorry! Something went wrong while disallowing {bot_name} to collect your data in all servers you share with {bot_name}!"
response_privacy_disable_specific_server_failed = "I am sorry! Something went wrong while disallowing {bot_name} to collect your data in this server!"
response_privacy_allow_all_servers_success = "Your privacy configuration has changed! {bot_name} is now allowed to collect your data in servers you share with {bot_name}!"
response_privacy_allow_specific_server_success = "Your privacy configuration has changed! {bot_name} is now allowed to collect your data in this server!"
response_privacy_disable_all_servers_success = "Your privacy configuration has changed! {bot_name} is now disallowed to collect your data in servers you share with {bot_name}!"
response_privacy_disable_specific_server_success = "Your privacy configuration has changed! {bot_name} is now disallowed to collect your data in this server!"
# Log Responses
# Embeds
privacy_embed_title = "{bot_name} privacy configurator"
privacy_embed_description = "Welcome to the {bot_name} privacy configurator. This is the place to configure your privacy settings for this server or for all servers at once! Currently, {bot_name} is `{status}` to collect data from you in this server!\n\nThe data that is shown using this command is ALL data {bot_name} has of you to provide you with its services. Important to know, the data shown in this command is ALL data across ALL servers you share with {bot_name}. You are free to delete this data or (dis)allow {bot_name} of gathering more data using this configurator but beware: any changes in these settings or in the data can result in loss of functionality, loss of existing services or other inconvinience for you, and in some cases, the servers you are in!\n\n Some data (f.e. some channel names or mentions in the logging channel) are not saved, so if you personal data is used in these names, descriptions, etc. you need to contact the servers administrator to change this!\n\n If you have any further questions about {bot_name} and privacy, please visit https://husqy.xyz/ for more info!"
privacy_embed_data_collection_description = (
    "Please select which action you want to perform."
)
privacy_embed_data_collection_field_1_value = "This option turns data collection by {bot_name} ON for you in all servers you share with {bot_name}."
privacy_embed_data_collection_field_2_value = (
    "This option turns data collection by {bot_name} ON for you in this server)."
)
privacy_embed_data_collection_field_3_value = "This option turns data collection by {bot_name} OFF for you in all servers you share with {bot_name}. This will also delete all data associated with you and these servers."
privacy_embed_data_collection_field_4_value = "This option turns data collection by {bot_name} OFF for you in this server. This will also delete all data associated with you and this servers."
privacy_embed_data_overview_description = "Your data has been found in association with **{bot_service}** a total of `{total_times} times`.\n\nUser ID: `{user_id_times} times`\nUsername: `{username_times} times`"
privacy_embed_data_overview_description_home = "All shown data is the data that {bot_name} has stored of you to deliver you its services. It is important to know that this data is across all servers you share with {bot_name}.\n\nUsing the buttons below you can search through all services Husqy offer and find out how much data {bot_name} has saved."
privacy_embed_data_overview_footer = (
    "NOTE: The data shown is across ALL servers shared with {bot_name}!"
)
privacy_embed_data_collection_validation_delete = (
    "Are you sure you want to delete the data? This action can not be reversed!"
)
privacy_embed_data_collection_validation_delete_confirmed = "The delete action has been requested and will be executed, it can take some time before your data is deleted! If you think that not all of your data has been deleted, please contact our support!"
privacy_embed_data_collection_validation_delete_cancelled = (
    "The delete action has been cancelled! No data will be deleted!"
)

# ------------------------------------------------------------------------- #
# Reminders #
# ------------------------------------------------------------------------- #
reminder_delete = "☑"
reminder_repeat = "🔁"
# Responses
response_reminder_timeout = "Response timeout, reminder deleted!"
response_reminder_deleted = "I have deleted the reminder!"
response_reminder_when_to_repeat = "When would you like me to repeat the reminder (Please use format: {delay}{h/m/s} - f.e. 1h or 20m)?"
response_reminder_repeat_created = "I have created the repeated reminder!"
response_reminder_add_failed_not_a_valid_wait_duration = (
    "I am sorry! It looks like the wait duration has an invalid format!"
)
response_reminder_added = "I have added the reminder!"
response_reminder_delete_failed_no_reminder_found = (
    "I am sorry! I didn't find a reminder with that ID!"
)
response_reminder_delete_failed_not_target_user = "I am sorry! You are not the target of the reminder! Only the target user can delete their own reminder!"
response_reminder_deleted = "I have deleted the reminder!"
response_reminder_list_no_reminders = "There are no reminders in this server!"
response_reminder_list_timeout = "Reminder list reached a timeout!"
response_reminder_add_dm_destination_is_not_target_user = "The destination of the reminder can't be the DM of a user who is not the target user."
# Log Responses
log_response_reminder_add_failed_not_a_valid_wait_duration = "{datetime} -- **{member}** tried to add a reminder! But the provided wait duration was an invalid format!"
log_response_reminder_add_not_a_url = "{datetime} -- **{member}** tried to add a reminder! But the provided linked message was not a valid URL!"
log_response_reminder_add_dm_destination_is_not_target_user = "{datetime} -- **{member}** tried to add a reminder! But they provided a DM of a user who is not the target user as the destination!"
log_response_reminder_add_failed = (
    "{datetime} -- **{member}** tried to add a reminder! But something went wrong!"
)
log_response_reminder_added = "{datetime} -- **{member}** added a new reminder!"
log_response_reminder_delete_failed_no_reminder_found = "{datetime} -- **{member}** tried to delete a reminder! But I didn't find a remidner with the specified ID!"
log_response_reminder_delete_failed_not_target_user = "{datetime} -- **{member}** tried to delete a reminder! But they aren't the target user!"
log_response_reminder_delete_failed = (
    "{datetime} -- **{member}** tried to delete a reminder! But something went wrong!"
)
log_response_reminder_deleted = (
    "{datetime} -- **{member}** tried to deleted one of their reminders!"
)
log_response_reminder_list_no_reminders = "{datetime} -- **{member}** requested their reminders but they don't have any reminders!"
log_response_reminder_list_requested = (
    "{datetime} -- **{member}** requested their reminders!"
)
# Embeds
reminder_embed_title = "Reminder"
reminder_embed_field_title_linked_message = "Linked Message:"
reminder_embed_field_value_linked_message = "Jump to message"
reminder_list_embed_title = "Reminders"
reminder_list_embed_description = (
    "There are {reminders} reminders in this server! Showing active reminders:"
)
reminder_list_embed_field_reminders = "Reminders:"

# ------------------------------------------------------------------------- #
# Giveaway #
# ------------------------------------------------------------------------- #
# Responses
response_giveaway_create_failed_not_a_valid_time = "The given time duration is not in the valid format, please use the format {delay}{h/m/s} - f.e. 1h or 20m"
response_giveaway_created = "I have created the giveaway!"
giveaway_ended_winner = (
    "Congratulations {winner}! You have won the giveaway! Your prize: `{prize}`"
)
response_giveaway_ended_no_winner = "The giveaway with the prize: `{prize}` has ended! Sadly there were no participants and thus no winners."
response_giveaway_delete_failed_no_giveaway_found = "There is no giveaway with that ID."
response_giveaway_delete_failed_not_owner = (
    "You can't delete the giveaway because you are not the owner."
)
response_giveaway_delete = "I have deleted the giveaway!"
response_giveaway_list_no_giveaways = (
    "You don't have any active giveaways in this server!"
)
response_giveaway_reroll_failed_no_giveaway_found = "There is no giveaway with that ID."
response_giveaway_reroll_failed_not_owner = (
    "You can't reroll a winner for this giveaway because you are not the owner."
)
response_giveaway_reroll = "I have chosen a new winner!"
response_giveaway_reroll_failed_no_winner_yet = (
    "You can't reroll this giveaway because there is no winner yet!"
)
# Log Responses
log_response_giveaway_create_failed_not_a_valid_time = "{datetime} -- **{member}** tried to create a giveaway! But they gave an invalid time duration!"
log_response_giveaway_create_failed = (
    "{datetime} -- **{member}** tried to create a giveaway! But something went wrong!"
)
log_response_giveaway_created = "{datetime} -- **{member}** has created a giveaway!"
log_response_giveaway_delete_failed_no_giveaway_found = "{datetime} -- **{member}** tried to delete a giveaway! But there is no giveaway with the given ID!"
log_response_giveaway_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a giveaway! But they are not the owner!"
)
log_response_giveaway_delete_failed = (
    "{datetime} -- **{member}** tried to delete a giveaway! But something went wrong!"
)
log_response_giveaway_delete = "{datetime} -- **{member}** has deleted a giveaway!"
log_response_giveaway_list_no_giveaways = "{datetime} -- **{member}** tried to list their giveaways in this server! But they don't have any!"
log_response_giveaway_list_requested = (
    "{datetime} -- **{member}** has requested their giveaways in this server!"
)
log_response_giveaway_reroll_failed_no_giveaway_found = "{datetime} -- **{member}** tried to reroll a winner for a giveaway! But there is no giveaway with the given ID!"
log_response_giveaway_reroll_failed_not_owner = "{datetime} -- **{member}** tried to reroll a winner for a giveaway! But they are not the owner!"
log_response_giveaway_reroll_failed = "{datetime} -- **{member}** tried to reroll a winner for a giveaway! But something went wrong!"
log_response_giveaway_reroll = (
    "{datetime} -- **{member}** has rerolled a winner for a giveaway!"
)
log_response_giveaway_reroll_failed_no_winner_yet = "{datetime} -- **{member}** tried to reroll a winner for a giveaway! But there is no winner yet!"
# Embeds
giveaway_embed_title = "Active giveaway: {prize}!"
giveaway_embed_title_finished = "Finished giveaway: {prize}!"
giveaway_embed_footer = "Giveaway ID: {giveaway_id} - Giveaway by: {owner}"
giveaway_embed_details_field_title = "Giveaway details:"
giveaway_embed_details_field_value = "Giveaway is active for: {countdown}\n Giveaway participants: {participants}\n Giveaway winner count: {winner_count}"
giveaway_list_embed_title = "Your giveaways"
giveaway_list_embed_description = (
    "You have {giveaways} giveaways! Showing your active giveaways:"
)
giveaway_list_embed_field_giveaways = "Your giveways (Active/Finished):"

# ------------------------------------------------------------------------- #
# Settings Update #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_settings_updated = (
    "{datetime} -- **{member}** has updated the settings wrong!"
)

# ------------------------------------------------------------------------- #
# Support #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_support = (
    "{datetime} -- **{member}** has requested information regarding my support!"
)
# Embeds
support_embed_title = "{bot_name} Support"
support_embed_description = "If you are in need of support, please follow one of the links below and contact us! We would like to help you!"

# ------------------------------------------------------------------------- #
# Tags #
# ------------------------------------------------------------------------- #
# Responses
response_tag_create_failed_already_exists = "A tag with that name already exists!"
response_tag_create_fetch_message = "Please send the content of the tag!"
response_tag_create_timeout = "The tag creation timed out!"
response_tag_create_success = "I have created the tag!"
response_tag_delete_failed_tag_does_not_exist = "That tag does not exist!"
response_tag_delete_failed = "Something went wrong while trying to delete the tag!"
response_tag_delete_success = "I have deleted the tag!"
response_tag_edit_failed_tag_does_not_exist = "That tag does not exist!"
response_tag_edit_fetch_message = "Please send the new content of the tag. Note: This will overwrite the current content!"
response_tag_edit_failed = "Something went wrong while trying to edit the tag!"
response_tag_edit_success = "The tag is edited!"
response_tag_send_failed_no_such_tag = "There is no tag with that name!"
response_tags_list_empty = "There are currently no tags available in this server!"
# Log Responses
log_response_tag_create_failed = "{datetime} -- **{member}** tried to create a tag named `{tag_name}`! But something went wrong!"
log_response_tag_create_failed_already_exists = "{datetime} -- **{member}** tried to create a tag named `{tag_name}`! But that name already exists!"
log_response_tag_create_success = (
    "{datetime} -- **{member}** has created a tag named `{tag_name}`!"
)
log_response_tag_delete_failed_tag_does_not_exist = "{datetime} -- **{member}** tried to delete the tag `{tag_name}`! But that tag did not exist!"
log_response_tag_delete_failed = "{datetime} -- **{member}** tried to delete the tag `{tag_name}`! But something went wrong!"
log_response_tag_delete_success = (
    "{datetime} -- **{member}** deleted the tag `{tag_name}`!"
)
log_response_tag_edit_failed_tag_does_not_exist = "{datetime} -- **{member}** tried to edit a tag named `{tag_name}`! But that tag does not exist!"
log_response_tag_edit_failed = "{datetime} -- **{member}** tried to edit a tag named `{tag_name}`! But something went wrong!"
log_response_tag_edit_success = (
    "{datetime} -- **{member}** edited a tag named `{tag_name}`!"
)
log_response_tag_send_failed_no_such_tag = "{datetime} -- **{member}** tried to send a tag with the name `{tag_name}`! But it does not exist!"
log_response_tag_send_success = "{datetime} -- **{member}** used the tag `{tag_name}`!"
log_response_tags_list_empty = "{datetime} -- **{member}** tried to view the list of tags! But there are no tags available in this server!"
log_response_tags_list_requested = "{datetime} -- **{member}** viewed the list of tags!"
# Embeds
tag_list_embed_title = "Tags"
tag_list_embed_description = "There are {tags} tags available! Showing availble tags:"
tag_list_embed_field_tags = "Available tags:"

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
custom_modal_create_this_can_be_safely_removed = "<NOTE: Everything inside the (double) quotation marks can be safely removed! The trailing , too>"
custom_modal_change_title_new_title = "New title"
custom_modal_add_text_field_text_field_title = "Field title"
custom_modal_add_text_field_text_field_description = "Field description"
custom_modal_add_text_field_text_field_type = "Field type (Long/Short)"
custom_modal_add_text_field_title = "Text field"
# Responses
response_color_viewed_failed_no_values_given = (
    "I am sorry! I require one value, either the HEX value or the RGB value!"
)
response_color_viewed_failed_only_one_value_allowed = (
    "I am sorry! You are only allowed to insert one of the two values!"
)
response_color_viewed_failed = (
    "I am sorry! Something went wrong while trying to view the color!"
)
response_custom_embed_finished_timeout = "The custom embed creation reached a timeout! The JSON of your embed is: ```{embed_json}```"
response_custom_embed_finished = "The custom embed creation is finished, the JSON of your embed is: ```{embed_json}```"
response_custom_embed_create_starting = "Within a few seconds, you can start to create your own embed (only you can see this) and retrieve the JSON code of it. This JSON code can be used in different {bot_name} commands!\n Note: If you cancel a modal response, there is a change new interactions will fail, please wait up to 60 seconds for this issue to go away!"
response_custom_embed_send_success = "I have sent the custom embed to {channel}"
response_custom_modal_finished = "The custom modal creation is finished, the JSON of your modal is: \n```{modal_json}```"
response_custom_modal_create_starting = "Within a few seconds, you can start to create your own modal (only you can see this) and retrieve the JSON code of it. This JSON code can be used in different {bot_name} commands!\n Note: If you cancel a modal response, there is a change new interactions will fail, please wait up to 60 seconds for this issue to go away!"
response_custom_modal_preview = "By pressing Continue I will show the preview of the custom modal! This modal can be interacted with but no data will be saved!"
response_custom_modal_preview_failed = "The custom modal preview reached a timeout!"
response_custom_modal_preview_failed_canceled = "The custom modal preview was canceled!"
response_custom_modal_preview_success = "Custom modal has been previewed!"
response_domain_validate_safety_success_is_safe = "🟩 The domain is safe!"
response_domain_validate_safety_success_not_safe = "🟥 The domain is NOT safe!"
response_domain_validate_safety_failed_http_code = "Something went wrong while checking the domain, got HTTP error: {http_code}! Please try again later! If this issue persists, please contact our support!"
response_time_converted_success = "{days} days, {hours} hours, {minutes} minutes and {seconds} seconds totals to `{total_seconds}` seconds!"
# Log Responses
log_response_color_viewed_failed_no_values_given = "{datetime} -- **{member}** tried to view a color! But didn't insert a HEX or RGB value!"
log_response_color_viewed_failed_only_one_value_allowed = "{datetime} -- **{member}** tried to view a color! But inserted both a HEX and RGB value!"
log_response_color_viewed_failed = (
    "{datetime} -- **{member}** tried to view a color! But something went wrong!"
)
log_response_color_viewed_success = "{datetime} -- **{member}** has viewed a color with the HEX or RGB value: `{color}`!"
log_response_custom_embed_finished_timeout = (
    "{datetime} -- **{member}** created a custom embed! But a timeout was reached!"
)
log_response_custom_embed_finished = (
    "{datetime} -- **{member}** created a custom embed!"
)
log_response_custom_embed_create = (
    "{datetime} -- **{member}** started creating their own embed!"
)
log_response_custom_embed_send_failed = (
    "{datetime} -- **{member}** tried sending a custom embed! But something went wrong!"
)
log_response_custom_embed_send_failed_not_enough_permissions = "{datetime} -- **{member}** tried sending a custom embed but I don't have enough permissions for that channel!"
log_response_custom_embed_send_failed_not_a_text_channel = "{datetime} -- **{member}** tried sending a custom embed but didn't gave a valid text channel!"
log_response_custom_embed_send_success = (
    "{datetime} -- **{member}** sent a custom embed to {channel}!"
)
log_response_custom_modal_finished_timeout = (
    "{datetime} -- **{member}** created a custom modal! But a timeout was reached!"
)
log_response_custom_modal_finished = (
    "{datetime} -- **{member}** created a custom modal!"
)
log_response_custom_modal_create = (
    "{datetime} -- **{member}** started creating their own modal!"
)
log_response_custom_modal_preview_failed = "{datetime} -- **{member}** tried to preview a custom modal! But a timeout was reached!"
log_response_custom_modal_preview_failed_canceled = (
    "{datetime} -- **{member}** tried to preview a custom modal! But canceled it!"
)
log_response_custom_modal_preview_success = (
    "{datetime} -- **{member}** previewed a custom modal!"
)
log_response_domain_validate_safety_failed_http_code = "{datetime} -- **{member}** tried to check the safety of `{domain}`! But got HTTP error: {http_code}!"
log_response_domain_validate_safety_success_is_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is a safe URL!"
)
log_response_domain_validate_safety_success_not_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is NOT a safe URL!"
)
log_response_qr_generate_success = "{datetime} -- **{member}** has generated a QR-code!"
log_response_time_converted_success = "{datetime} -- **{member}** converted: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds to seconds: `{total_seconds}`!"
# Embeds
color_view_embed_title = "Color"
color_view_embed_description = (
    "Here is the color you requested, with color value: `{color}`"
)
custom_embed_default_embed_title = "Custom embed creation"
custom_embed_default_embed_description = "Welcome to the custom embed creation. Using the buttons below, you can configure this embed and retrieve the JSON."
custom_modal_default_embed_title = "Custom modal creation"
custom_modal_embed_description = "Welcome to the custom modal creation. Using the buttons below, you can configure the modal and preview it. When finished, select Finish to retrieve the JSON.\n **When previewing the modal, press cancel or fill in the form and press submit to continue modal creation!**"
qr_generate_embed_title = "Your QR-code"
qr_generate_embed_footer = "QR generated by: {member}!"

# ------------------------------------------------------------------------- #
# MODULES #
# ------------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #
# Module General #
# ------------------------------------------------------------------------- #
# Responses
# Embeds
module_configuration_wizard_embed_footer = (
    "Currently configuring: {module}, timeout: {timeout}"
)

# ------------------------------------------------------------------------- #
# Module Disable #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_settings_module_disable_success = "{datetime} -- **{member}** has disabled the `{module}` module! All related settings are removed!"

# ------------------------------------------------------------------------- #
# LOGGING #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_settings_module_enable_logging_success = "{datetime} -- **{member}** has enabled the `Logging` module! ALL events will now be logged!"
log_response_settings_module_configure_logging_all_events_failed = "{datetime} -- **{member}** tried to change the configuration of the `Logging` module! But something went wrong!"
log_response_settings_module_configure_logging_all_events_success = (
    "{datetime} -- **{member}** changed the configuration of the `Logging` module!"
)
# Embeds

# ------------------------------------------------------------------------- #
# GREETINGS #
# ------------------------------------------------------------------------- #
module_greetings_in_guild = "In server greetings"
module_greetings_to_user = "User DM Greetings"
module_greetings_role_add = "Role on join"
module_greetings_leave_taking_in_guild = "In server leave taking"
# Responses
# Log Responses
log_response_settings_module_enable_greetings_success = (
    "{datetime} -- **{member}** has enabled the `Greetings` module!"
)
log_response_settings_module_configure_greetings_all_success = (
    "{datetime} -- **{member}** changed the settings of the `Greetings` module!"
)
# Embeds

# ------------------------------------------------------------------------- #
# TEMPCHANNELS #
# ------------------------------------------------------------------------- #
module_tempchannel_default_voice_category = "{bot_name} Voice"
module_create_a_temporary_channel = "Create a TempChannel"
tempchannels_edit_name = "Change channel name"
tempchannels_edit_user_limit = "Change channel user limit"
tempchannels_edit_slowmode = "Change channel slowmode delay"
tempchannels_claim = "Claim ownership"
tempchannels_transfer = "Transfer ownership"
tempchannels_block_access = "Block users"
tempchannels_unblock_access = "Unblock users"
tempchannels_onlyfor = "Only for {role}"
# Responses
response_tempchannel_edit_failed_not_a_temporary_channel = (
    "I am sorry! The selected channel isn't a temporary channel!"
)
response_tempchannel_edit_timeout = (
    "The editing of the temporary channel failed, the timeout was reached!"
)
response_tempchannel_edit_block_failed = (
    "I am sorry! Something went wrong while trying to block the user(s)!"
)
response_tempchannel_edit_block_success = (
    "I have blocked the user(s) from the temporary channel!"
)
response_tempchannel_edit_unblock_failed = (
    "I am sorry! Something went wrong while trying to unblock the user(s)!"
)
response_tempchannel_edit_unblock_success = (
    "I have unblocked the user(s) from the temporary channel!"
)
response_tempchannel_edit_claim_not_possible = "You cannot claim ownership of this temporary channel because this channel already has an owner. The owner is {owner}, they can transfer the channel to you they wish!"
response_tempchannel_edit_claim_cancelled = "I have cancelled the ownership claim!"
response_tempchannel_edit_claim_failed = "I am sorry! Something went wrong while trying to claim ownership of the temporary channel!"
response_tempchannel_edit_claim_success = (
    "You have claimed ownership of the temporary channel!"
)
response_tempchannel_edit_name_failed = "I am sorry! Something went wrong while trying to rename the temporary channel to `{name}`!"
response_tempchannel_edit_name_success = (
    "I have changed the name of the temporary channel to `{name}`!"
)
response_tempchannel_onlyfor_block_failed = "I am sorry! Something went wrong while trying to limit the temporary channel to the role!"
response_tempchannel_onlyfor_block_success = (
    "I have limited the the temporary channel to the role!"
)
response_tempchannel_edit_slowmode_failed_not_a_valid_number = (
    "I am sorry! The given input is not a valid number!"
)
response_tempchannel_edit_slowmode_failed = "I am sorry! Something went wrong while trying to set the slowmode delay of the temporary channel to `{slowmode} seconds`!"
response_tempchannel_edit_slowmode_success = "I have changed the slowmode delay of the temporary channel to `{slowmode} seconds`!"
response_tempchannel_edit_slowmode_off_success = "I have turned off slowmode!"
response_tempchannel_edit_transfer_cancelled = (
    "I have cancelled the ownership transfer!"
)
response_tempchannel_edit_transfer_failed_not_a_valid_member = (
    "I am sorry! The inserted ID doesn't look like a valid server member!"
)
response_tempchannel_edit_transfer_failed = (
    "I am sorry! Something went wrong while trying to transfer the ownership!"
)
response_tempchannel_edit_transfer_success = "I have transferred ownership to {member}!"
response_tempchannel_edit_user_limit_failed_not_a_valid_number = (
    "I am sorry! The given input is not a valid number!"
)
response_tempchannel_edit_user_limit_failed_not_a_valid_range = (
    "I am sorry! The target user limit must be between 0 and 99!"
)
response_tempchannel_edit_user_limit_failed = "I am sorry! Something went wrong while trying to set the user limit of the temporary channel to `{user_limit} users`!"
response_tempchannel_edit_user_limit_success = (
    "I have changed the user limit of the temporary channel to `{user_limit} users`!"
)
response_tempchannel_edit_user_limit_off_success = "I have turned off the user limit!"
# Log Responses
log_response_settings_module_enable_tempchannel_success = (
    "{datetime} -- **{member}** has enabled the `Tempchannels` module!"
)
log_response_settings_module_configure_tempchannel_all_success = (
    "{datetime} -- **{member}** changed the settings of the `TempChannel` module!"
)
log_response_tempchannel_edit_failed_not_a_temporary_channel = "{datetime} -- **{member}** tried to edit a temporary channel! But the inserted channel isn't a temporary channel!"
log_response_tempchannel_edit_block_failed = "{datetime} -- **{member}** tried to block one or more users from a temporary channel! But something went wrong!"
log_response_tempchannel_edit_block_success = (
    "{datetime} -- **{member}** has blocked users from a temporary channel!"
)
log_response_tempchannel_edit_unblock_failed = "{datetime} -- **{member}** tried to unblock one or more users from a temporary channel! But something went wrong!"
log_response_tempchannel_edit_unblock_success = (
    "{datetime} -- **{member}** has unblocked users from a temporary channel!"
)
log_response_tempchannel_edit_claim_not_possible = "{datetime} -- **{member}** tried to claim ownership of a temporary channel! But there was still an owner!"
log_response_tempchannel_edit_claim_cancelled = (
    "{datetime} -- **{member}** cancelled the ownership claim of a temporary channel!"
)
log_response_tempchannel_edit_claim_failed = "{datetime} -- **{member}** tried to claim ownership of a temporary channel! But something went wrong!"
log_response_tempchannel_edit_claim_success = (
    "{datetime} -- **{member}** claimed ownership of a temporary channel!"
)
log_response_tempchannel_edit_name_failed = "{datetime} -- **{member}** tried to edit the name of a temporary channel! But something went wrong!"
log_response_tempchannel_edit_name_success = (
    "{datetime} -- **{member}** changed the name of a temporary channel to `{name}`!"
)
log_response_tempchannel_onlyfor_block_failed = "{datetime} -- **{member}** tried to limit a temporary channel to a role! But something went wrong!"
log_response_tempchannel_onlyfor_block_success = (
    "{datetime} -- **{member}** has limited a temporary channel to a role!"
)
log_response_tempchannel_edit_slowmode_failed_not_a_valid_number = "{datetime} -- **{member}** tried to change the slowmode delay of a temporary channel! But didn't insert a valid number!"
log_response_tempchannel_edit_slowmode_failed = "{datetime} -- **{member}** tried to change the slowmode delay of a temporary channel! But something went wrong!"
log_response_tempchannel_edit_slowmode_success = "{datetime} -- **{member}** changed the slowmode delay of a temporary channel to `{slowmode} seconds`!"
log_response_tempchannel_edit_slowmode_off_success = (
    "{datetime} -- **{member}** turned off the slowmode of a temporary channel!"
)
log_response_tempchannel_edit_transfer_cancelled = "{datetime} -- **{member}** cancelled the ownership transfer of a temporary channel!"
log_response_tempchannel_edit_transfer_failed_not_a_valid_member = "{datetime} -- **{member}** tried to transfer ownership of a temporary channel! But didn't insert a valid server memmber!"
log_response_tempchannel_edit_transfer_failed = "{datetime} -- **{member}** tried to transfer ownership of a temporary channel! But something went wrong!"
log_response_tempchannel_edit_transfer_success = (
    "{datetime} -- **{member}** transferred ownership of a temporary channel!"
)
log_response_tempchannel_edit_user_limit_failed_not_a_valid_number = "{datetime} -- **{member}** tried to change the user limit of a temporary channel! But didn't insert a valid number!"
log_response_tempchannel_edit_user_limit_failed_not_a_valid_range = "{datetime} -- **{member}** tried to change the user limit of a temporary channel! But the number wasn't in the valid range (0 - 99)!"
log_response_tempchannel_edit_user_limit_failed = "{datetime} -- **{member}** tried to change the user limit of a temporary channel! But something went wrong!"
log_response_tempchannel_edit_user_limit_success = "{datetime} -- **{member}** changed the user limit of a temporary channel to `{user_limit} users`!"
log_response_tempchannel_edit_user_limit_off_success = (
    "{datetime} -- **{member}** turned off the user limit of a temporary channel!"
)
# Embeds
tempchannels_edit_embed_title = "Temporary Channel edit wizard"
tempchannels_edit_embed_description = (
    "Please select the attribute of the channel you want to edit!"
)
tempchannels_edit_embed_footer = "Editing: {channel}, timeout: {timeout}"
tempchannels_edit_block_embed_title = "Temporary channel block users"
tempchannels_edit_block_embed_description = "Please select the user(s) you want to block from this channel (there is a max. of 25 users, if you want to block more users, please run the command again!)!\nIf the user is not there, please start typing for autocomplete!"
tempchannels_edit_unblock_embed_title = "Temporary channel unblock users"
tempchannels_edit_unblock_embed_description = "Please select the user(s) you want to unblock from this channel (there is a max. of 25 users, if you want to unblock more users, please run the command again!)!\nIf the user is not there, please start typing for autocomplete!"
tempchannels_edit_claim_embed_title = "Temporary channel claim ownership"
tempchannels_edit_claim_embed_description = (
    "Are you sure you want to claim ownership of the following channels: {channels}"
)
tempchannels_edit_name_embed_title = "Temporary channel name change"
tempchannels_edit_name_embed_description = (
    "Please enter the new name to give the channel!"
)
tempchannels_edit_onlyfor_embed_title = "Temporary channel onlyfor role"
tempchannels_edit_onlyfor_embed_description = "Please select the role you want to allow to this channel, other roles will be blocked! \nIf the role is not there, please start typing for autocomplete!"
tempchannels_edit_slowmode_embed_title = "Temporary channel (text) slowmode change"
tempchannels_edit_slowmode_embed_description = "Please enter the new slowmode delay (in seconds) of the channel! If you don't want slowmode, please insert 0!"
tempchannels_edit_transfer_embed_title = "Temporary channel transfer ownership"
tempchannels_edit_transfer_embed_description = (
    "Are you sure you want to transfer ownership of the following channels: {channels}"
)
tempchannels_edit_transfer_user_embed_description = "Please select the user you want to transfer ownership to! \nIf the user is not there, please start typing for autocomplete!"
tempchannels_edit_user_limit_embed_title = "Temporary channel (voice) user limit change"
tempchannels_edit_user_limit_embed_description = "Please enter the new user limit of the channel! If you don't want a limit, please insert 0!"

# ------------------------------------------------------------------------- #
# SOCIALS #
# ------------------------------------------------------------------------- #
module_socials_reddit_list = "Get Subreddit list"
module_socials_reddit_new_post = (
    "Hey @everyone! There is a new post in **{subreddit}**: {subreddit_link_to_post}"
)
module_socials_rss_list = "Get RSS Feed list"
module_socials_rss_new_entry = (
    "Hey @everyone! There is a new entry on {url}, check below!"
)
module_socials_twitch_list = "Get Twitch account list"
module_socials_twitch_account_live = (
    "Hey @everyone! **{twitch_account}** is live: {twitch_live_link}"
)
# Responses
# Log Responses
log_response_settings_module_enable_socials_success = (
    "{datetime} -- **{member}** has enabled the `Socials` module!"
)
log_response_settings_module_configure_socials_all_success = (
    "{datetime} -- **{member}** has changed the settings of the `Socials` module!"
)
log_response_module_socials_reddit_add_failed_maximum_reached = "{datetime} -- **{member}** tried to add a Subreddit to the list! But the maximum number of Subreddits is already reached!"
log_response_module_socials_reddit_add_failed_already_added = "{datetime} -- **{member}** tried to add `{subreddit}` to the Subreddit list! But this account is already in the list!"
log_response_module_socials_reddit_add_success = (
    "{datetime} -- **{member}** added `{subreddit}` to the Subreddit list!"
)
log_response_module_socials_reddit_remove_success = (
    "{datetime} -- **{member}** removed `{subreddit}` to the Subreddit list!"
)
log_response_module_socials_rss_add_failed_maximum_reached = "{datetime} -- **{member}** tried to add a RSS Feed to the list! But the maximum number of RSS Feeds is already reached!"
log_response_module_socials_rss_add_failed_already_added = "{datetime} -- **{member}** tried to add `{url}` to the RSS Feed list! But this url is already in the list!"
log_response_module_socials_rss_add_success = (
    "{datetime} -- **{member}** added `{url}` to the RSS Feed list!"
)
log_response_module_socials_rss_remove_success = (
    "{datetime} -- **{member}** removed `{url}` to the RSS Feed list!"
)
log_response_module_socials_twitch_add_failed_maximum_reached = "{datetime} -- **{member}** tried to add a Twitch account to the list! But the maximum number of Twitch accounts is already reached!"
log_response_module_socials_twitch_add_failed_already_added = "{datetime} -- **{member}** tried to add `{twitch_account}` to the Twitch account list! But this account is already in the list!"
log_response_module_socials_twitch_add_success = (
    "{datetime} -- **{member}** added `{twitch_account}` to the Twitch account list!"
)
log_response_module_socials_twitch_remove_success = (
    "{datetime} -- **{member}** removed `{twitch_account}` to the Twitch account list!"
)
# Embeds
module_socials_reddit_embed_title = "Reddit configuration"
module_socials_rss_embed_title = "RSS Feed configuration"
module_socials_rss_new_embed_description = (
    "**Title:** {rss_title}\n\n**Description:**\n{rss_description}..."
)
module_socials_twitch_embed_title = "Twitch account configuration"


# ------------------------------------------------------------------------- #
# REACTION ROLES #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_settings_module_enable_reaction_roles_success = (
    "{datetime} -- **{member}** has enabled the `Reaction Roles` module!"
)
log_response_settings_module_configure_reaction_roles_all_success = (
    "{datetime} -- **{member}** has changed the settings of the `Reacion Roles` module!"
)
log_response_reactionrole_add_failed = (
    "{datetime} -- **{member}** tried to add a reaction role! But something went wrong!"
)
log_response_reactionrole_add_success = (
    "{datetime} -- **{member}** add a reaction role in {channel}!"
)
log_response_reactionrole_delete_failed = "{datetime} -- **{member}** tried to delete a reaction role! But something went wrong!"
log_response_reactionrole_delete_success = (
    "{datetime} -- **{member}** deleted a reaction role in {channel}!"
)
# Embeds

# ------------------------------------------------------------------------- #
# AUTORESPONDER #
# ------------------------------------------------------------------------- #
# Responses
# Log Responses
log_response_settings_module_enable_autoresponder_success = (
    "{datetime} -- **{member}** has enabled the `Autoresponder` module!"
)
log_response_settings_module_autoresponder_configuration_failed = "{datetime} -- **{member}** tried to add a new entry to the `Autoresponder` module! But something went wrong!"
log_response_settings_module_autoresponder_configuration_success = (
    "{datetime} -- **{member}** has added an entry to the `Autoresponder` module!"
)
log_response_settings_module_autoresponder_configuration_delete_failed = "{datetime} -- **{member}** tried to delete an entry from the `Autoresponder` module! But something went wrong!"
log_response_settings_module_autoresponder_configuration_delete_success = (
    "{datetime} -- **{member}** has deleted an entry from the `Autoresponder` module!"
)
# Embeds

# ------------------------------------------------------------------------- #
# TICKETS #
# ------------------------------------------------------------------------- #
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
module_tickets_role_used_for_ticket_module = "This role will be used for the Ticket Module, please DO NOT remove this role from the server without reconfiguring the Ticket Module!"
module_tickets_channel_used_for_ticket_module = "This channel will be used for the Ticket Module, please DO NOT remove this channel from the server without reconfiguring the Ticket Module!"
module_tickets_default_ticket_category = "{bot_name} Tickets"
module_tickets_create_a_ticket = "create-a-ticket"
module_tickets_view_tickets = "view-tickets"
module_tickets_default_modal = """{'custom_id': '260666db-aa41-422d-b7ae-4b906cd35054', 'title': 'New ticket', 'components': ["{'type': 1, 'components': [{'type': 4, 'style': 1, 'custom_id': 'bf835028-1c56-4537-b4d2-bfa667135d19', 'label': 'Ticket title', 'placeholder': 'Please insert the title of your ticket'}]}", "{'type': 1, 'components': [{'type': 4, 'style': 2, 'custom_id': '78f400da-f670-411e-9658-9b109a46cbbc', 'label': 'Ticket description', 'placeholder': 'Please describe why you are submitting this ticket'}]}"]}"""
module_tickets_default_ticket_creation_message = """{"title": "Create a ticket", "description": "If you are experiencing problems or are in need of help, feel free to create a ticket!", "footer": {"text": "Tickets made possible by: Husqy"}}"""
module_tickets_please_select_default_type_to_create = (
    "Please select a default type to create a ticket"
)
module_tickets_please_select_custom_type_to_create = (
    "Please select a custom type to create a ticket"
)
# Responses
# Log Responses
log_response_ticket_module_enabled = (
    "{datetime} -- **{member}** has enabled the `Ticket` Module!"
)
log_response_ticket_module_configured = (
    "{datetime} -- **{member}** has changed the configuration of the `Ticket` Module!"
)
# Embeds

# ------------------------------------------------------------------------- #
# SERVERSTATS #
# ------------------------------------------------------------------------- #
module_serverstats_default_category_name = "{bot_name} Counter Panel"
module_serverstats_default_member_count_name = "👥 Members: {value}"
module_serverstats_default_online_member_count_name = "🟢 Online: {value}"
module_serverstats_default_online_member_count_with_role_name = "{role_name}: {value}"
module_serverstats_default_boost_number_name = "🚀 Boosters: {value}"
starboard_message = "You're a ⭐! x{value}!"
# Responses
# #  Log Responses
log_response_settings_module_serverstats_change_all_success = "{datetime} -- **{member}** has changed the configuration of the `ServerStats` module!"
log_response_settings_module_enable_serverstats_success = (
    "{datetime} -- **{member}** has enabled the `ServerStats` module!"
)
#  Embeds
