# MODULE LOGGING CONFIGURATION
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
## Audio
### Join
response_join_success = "{datetime} -- **{member}** joined me to {channel}!"
response_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` but something went wrong!"
response_join_failed_not_enough_permissions = (
    "{datetime} -- **{member}** tried joining me to a channel where I don't have enough permissions for!"
)
response_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel which I don't know! If this issue persist, please contact my support!"
response_join_failed_no_channel_given = (
    "{datetime} -- **{member}** tried joining me to a channel but didn't provide a channel for me to join!"
)
### Leave
response_leave_success = "{datetime} -- **{member}** made me leave the voice channel!"
response_leave_failed = "{datetime} -- **{member}** tried to make me leave the voice channel! But something went wrong!"
response_music_events_leave = "{datetime} -- I left the voice channel, all users left!"
### Stop
response_stop_success = "{datetime} -- **{member}** stopped audio playback!"
response_stop_failed = "{datetime} -- **{member}** tried to stop audio playback but something went wrong!"
### Pause
response_pause_success = "{datetime} -- **{member}** paused audio playback!"
response_pause_failed = "{datetime} -- **{member}** tried to pause audio playback but something went wrong!"
response_pause_failed_radio_playing = (
    "{datetime} -- **{member}** tried to pause the audio playback but a radio station is playing!"
)
response_pause_failed_nothing_playing = (
    "{datetime} -- **{member}** tried to pause audio playback but there was nothing playing!"
)
### Resume
response_resume_success = "{datetime} -- **{member}** resumed audio playback!"
response_resume_failed = "{datetime} -- **{member}** tried to resume audio playback but something went wrong!"
response_resume_failed_radio_playing = "{datetime} -- **{member}** tried to resume a radio station!"
response_resume_failed_nothing_playing = (
    "{datetime} -- **{member}** tried to resume audio playback! But there was nothing playing!"
)
### Shuffle
response_music_shuffle_success = "{datetime} -- **{member}** shuffled the queue!"
response_music_shuffle_failed = "{datetime} -- **{member}** tried to shuffle the queue but something went wrong!"
response_music_shuffle_playing_radio = (
    "{datetime} -- **{member}** tried to shuffle the queue but there was a radio station playing!"
)
response_music_shuffle_not_playing_anything = (
    "{datetime} -- **{member}** tried to shuffle the queue! But there was nothing to shuffle!"
)
### Skip
response_music_skip_song_success = "{datetime} -- **{member}** skipped a song!"
response_music_skip_stop_failed = "{datetime} -- **{member}** tried to stop audio playback because there was nothing left in the queue after a skip but something went wrong!"
response_music_skip_nothing_to_skip = "{datetime} -- **{member}** tried to skip a song! But there was nothing to skip!"
response_music_skip_failed_radio_playing = (
    "{datetime} -- **{member}** tried to skip audio playback but radio is playing!"
)
response_music_skip_loop_enabled = "{datetime} -- **{member}** tried to skip a song but loop was enabled!"
### Seek
response_music_seek_success = "{datetime} -- **{member}** jumped the track tp `{time}`!"
response_music_seek_failed_radio_playing = (
    "{datetime} -- **{member}** tried to forward a radio station but this is not possible!"
)
response_music_seek_nothing_playing = (
    "{datetime} -- **{member}** tried to forward a song but there was nothing playing!"
)
response_music_seek_wrong_time_format = (
    "{datetime} -- **{member}** tried to seek a track but gave me an invalid time format!"
)
### Restart Song
response_music_restart_success = "{datetime} -- **{member}** restarted the current playing song!"
response_music_restart_failed_radio_playing = (
    "{datetime} -- **{member}** tried to restart a radio station but this is not possible!"
)
response_music_restart_nothing_playing = (
    "{datetime} -- **{member}** tried to restart the song but there is no song playing!"
)
### Nowplaying
response_nowplaying_requested = "{datetime} -- **{member}** requested the now playing song!"
response_nowplaying_not_playing_anything = (
    "{datetime} -- **{member}** requested the playing song but nothing was playing!"
)
### Queue
response_queue_requested = "{datetime} -- **{member}** requested the queue!"
response_queue_request_failed_queue_empty = (
    "{datetime} -- **{member}** requested the queue but there was nothing in the queue!"
)
### Loop
response_loop_enabled = "{datetime} -- **{member}** has `enabled` loop!"
response_loop_disabled = "{datetime} -- **{member}** has `disabled` loop!"
response_loop_failed_radio_playing = (
    "{datetime} -- **{member}** tried to roggle loop but there is a radio station playing!"
)
response_loop_failed_queue_empty = "{datetime} -- **{member}** tried to toggle loop! But there is nothing playing!"
response_loop_failed_not_in_voicechannel = (
    "{datetime} -- **{member}** tried to loop but they are not in the (right) voice channel!"
)
### Volume
response_volume_changed = "{datetime} -- **{member}** has changed the volume to `{level}%`!"
### Play music
response_music_play_added_song = "{datetime} -- **{member}** added a song to the queue!"
response_music_play_added_playlist = "{datetime} -- **{member}** added a playlist to the queue!"
response_music_play_failed_song = (
    "{datetime} -- **{member}** tried adding a song to the queue but something went wrong!"
)
response_music_play_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL but I am not allowed to!"
)
response_music_play_failed_radio_playing = (
    "{datetime} -- **{member}** tried playing a song/playlist/album but I am playing radio!"
)
response_music_play_join_failed = (
    "{datetime} -- **{member}** tried joining me to `{channel}` by playing music but something went wrong!"
)
response_music_play_join_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried joining me to a channel by playing music but I don't know that channel!"
)
response_music_play_join_failed_no_suitable_channel = (
    "{datetime} -- **{member}** tried to add a song/playlist/album to the queue but neither off us are in a channel!"
)
### Play tts
response_music_playtts_added_song = (
    "{datetime} -- **{member}** added a text-to-speech message to the queue! Message: `{tts_message}`!"
)
response_music_playtts_failed_song = (
    "{datetime} -- **{member}** tried to use a text-to-speech message but something went wrong!"
)
response_music_playtts_failed_radio_playing = (
    "{datetime} -- **{member}** tried playing a text-to-speech message but I am playing radio!"
)
response_music_playtts_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing a text-to-speech message but something went wrong!"
response_music_playtts_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing a text-to-speech message but I don't know that channel!"
response_music_playtts_join_failed_no_suitable_channel = (
    "{datetime} -- **{member}** tried to add a text-to-speech message but neither off us are in a channel!"
)
### Play radio
response_radio_play_success = "{datetime} -- **{member}** played radiostation: `{radiostation}`! Provided by TuneIn!"
response_radio_play_failed = (
    "{datetime} -- **{member}** tried playing radiostation: `{radiostation}` but something went wrong!"
)
response_radio_play_failed_http_error = (
    "{datetime} -- **{member}** tried playing radiostation: `{radiostation}` but I got status code: `{status_code}`!"
)
response_radio_play_failed_already_playing = (
    "{datetime} -- **{member}** tried to listen to radio but there was already something playing!"
)
response_radio_play_join_failed = (
    "{datetime} -- **{member}** tried joining me to `{channel}` by playing radio but something went wrong!"
)
response_radio_play_join_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried joining me to a channel by playing radio but I don't know that channel!"
)
response_radio_play_join_failed_no_suitable_channel = (
    "{datetime} -- **{member}** tried to play a radiostation but neither off us are in a channel!"
)
### Playnext
response_music_playnext_added_song = "{datetime} -- **{member}** added a song to the queue after the current song!"
response_music_playnext_added_playlist = (
    "{datetime} -- **{member}** added a playlist to the queue after the current song!"
)
response_music_playnext_failed_song = (
    "{datetime} -- **{member}** tried adding a song to the queue after the current song but something went wrong!"
)
response_music_playnext_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL but I am not allowed to!"
)
response_music_playnext_failed_radio_playing = (
    "{datetime} -- **{member}** tried playing a song/playlist/album after the current song but I was playing radio!"
)
response_music_playnext_join_failed = (
    "{datetime} -- **{member}** tried joining me to `{channel}` by playing music but something went wrong!"
)
response_music_playnext_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing a song using the playnext command but I don't know that channel!"
response_music_playnext_join_failed_no_suitable_channel = (
    "{datetime} -- **{member}** tried to add a song using the playnext command but neither off us are in a channel!"
)
### Remove
response_music_remove_removed_song = "{datetime} -- **{member}** removed a song from the queue!"
response_music_remove_removed_playlist = "{datetime} -- **{member}** removed a playlist from the queue!"
response_music_remove_failed_song = (
    "{datetime} -- **{member}** tried to remove a song from the queue but something went wrong!"
)
response_music_remove_failed_no_youtube = (
    "{datetime} -- **{member}** tried removing a YouTube URL but I am not allowed to"
)
response_music_remove_failed_radio_playing = (
    "{datetime} -- **{member}** tried to remove a song from the queue but I am playing radio!"
)
response_music_remove_failed_nothing_to_remove = (
    "{datetime} -- **{member}** tried to remove a song from the queue but there was nothing to remove!"
)
### Search
response_platform_searched = "{datetime} -- **{member}** searched {platform}!"
response_search_no_results_found = "{datetime} -- **{member}** searched YouTube or SoundCloud with the query: `{query}` but I didn't find any related results!"

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
### Support
response_support = "{datetime} -- **{member}** has requested information regarding my support using `/info support`!"

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

## Reminders
### Add
response_reminder_add_failed_not_a_valid_wait_duration = (
    "{datetime} -- **{member}** tried to add a reminder but the provided wait duration was an invalid format!"
)
response_reminder_add_dm_destination_is_not_target_user = "{datetime} -- **{member}** tried to add a reminder but they provided a DM of a user who is not the target user as the destination!"
response_reminder_add_not_a_url = (
    "{datetime} -- **{member}** tried to add a reminder but the provided linked message was not a valid URL!"
)
response_reminder_added = "{datetime} -- **{member}** added a new reminder!"
response_reminder_add_failed = "{datetime} -- **{member}** tried to add a new reminder but something went wrong!"
### Delete
response_reminder_deleted = "{datetime} -- **{member}** deleted one of their reminders!"
response_reminder_delete_failed_not_target_user = (
    "{datetime} -- **{member}** tried to delete a reminder but they aren't the target user!"
)
response_reminder_delete_failed_no_reminder_found = (
    "{datetime} -- **{member}** tried to delete a reminder but I didn't find a remidner with the specified ID!"
)
response_reminder_delete_failed = "{datetime} -- **{member}** tried to delete a reminder but something went wrong!"
### List
response_reminder_list_requested = "{datetime} -- **{member}** requested their reminders!"
response_reminder_list_no_reminders = (
    "{datetime} -- **{member}** requested their reminders but they don't have any reminders!"
)
## Utils
### Color view
response_color_viewed_success = "{datetime} -- **{member}** has viewed a color with the HEX or RGB value: `{color}`!"
response_color_viewed_failed = "{datetime} -- **{member}** tried to view a color but something went wrong!"
response_color_viewed_failed_only_one_value_allowed = (
    "{datetime} -- **{member}** tried to view a color but inserted both a HEX and RGB value!"
)
response_color_viewed_failed_no_values_given = (
    "{datetime} -- **{member}** tried to view a color but didn't insert a HEX or RGB value!"
)
### Custom embed
response_custom_embed_create = "{datetime} -- **{member}** started creating their own embed!"
response_custom_embed_finished = "{datetime} -- **{member}** created a custom embed!"
response_custom_embed_finished_timeout = "{datetime} -- **{member}** created a custom embed but a timeout was reached!"
response_custom_embed_send_success = "{datetime} -- **{member}** sent a custom embed to {channel}!"
response_custom_embed_send_failed_not_a_text_channel = (
    "{datetime} -- **{member}** tried sending a custom embed but didn't gave a valid text channel!"
)
response_custom_embed_send_failed_not_enough_permissions = (
    "{datetime} -- **{member}** tried sending a custom embed but I don't have enough permissions for that channel!"
)
response_custom_embed_send_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried sending a custom embed to a channel I don't know!"
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
### Domain
response_domain_validate_safety_success_not_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is NOT a safe URL!"
)
response_domain_validate_safety_success_is_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is a safe URL!"
)
response_domain_validate_safety_failed_http_code = (
    "{datetime} -- **{member}** tried to check the safety of `{domain}` but got HTTP error: {http_code}!"
)
### QR
response_qr_generate_success = "{datetime} -- **{member}** has generated a QR-code!"
### Convert
response_time_converted_success = "{datetime} -- **{member}** converted: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds to seconds: `{total_seconds}`!"

## Mod_user
### Ban_Create
response_user_events_banned = "{datetime} -- **{member}** has banned `{user}`!\n`[Reason]` -- {reason}"
response_ban_create_failed = "{datetime} -- **{member}** tried to ban `{user}` but something went wrong!"
response_ban_create_failed_no_bot_ban = "{datetime} -- **{member}** tried to ban `{user}` but this is a bot!"
### Ban_Delete
response_user_events_unbanned = "{datetime} -- **{member}** has unbanned `{user}`!\n`[Reason]` -- {reason}"
response_ban_delete_failed = "{datetime} -- **{member}** tried to unban `{user}` but something went wrong!"
response_ban_delete_failed_no_bot_unban = "{datetime} -- **{member}** tried to unban `{user}` but this is a bot!"
### Warn_Create
response_warn_create_success = (
    "{datetime} -- **{member}** warned `{user}` and added `{points} points` to their profile!\n`[Reason]` -- {reason}"
)
response_warn_create_failed = "{datetime} -- **{member}** tried to warn `{user}` but something went wrong!"
response_warn_create_failed_no_bot_warn = "{datetime} -- **{member}** tried to warn `{user}` but this is a bot!"
### Warn_Delete
response_warn_delete_success = "{datetime} -- **{member}** deleted a warn from `{user}` and removed `{points} points` from their profile!\n`[Reason]` -- {reason}"
response_warn_delete_failed = (
    "{datetime} -- **{member}** tried to delete a warn from `{user}` but something went wrong!"
)
response_warn_delete_failed_no_bot_warn_delete = (
    "{datetime} -- **{member}** tried to delete a warn from `{user}` but this is a bot!"
)
### Kick
response_user_kicked = "{datetime} -- **{member}** has kicked `{user}`!\n`[Reason]` -- {reason}"
response_kick_failed = "{datetime} -- **{member}** tried to kick {user} but something went wrong!"
response_kick_failed_no_bot_kick = "{datetime} -- **{member}** tried to kick {user} but this is a bot!"
### Vckick
response_vckick_success = "{datetime} -- **{member}** has kicked {user} from a voice channel!\n`[Reason]` -- {reason}"
response_vckick_failed = (
    "{datetime} -- **{member}** tried to kick {user} from a voice channel but something went wrong!"
)
### Move
response_move_success = "{datetime} -- **{member}** has moved {user} to {channel}!\n`[Reason]` -- {reason}"
response_move_failed = "{datetime} -- **{member}** tried to move {user} to {channel}! But something went wrong!"
response_move_failed_missing_permissions = (
    "{datetime} -- **{member}** tried to move {user} to {channel} but either I or this user is missing permissions!"
)
response_move_failed_user_not_in_a_voice_channel = (
    "{datetime} -- **{member}** tried to move {user} to {channel} but this user is not in a voice channel!"
)
### Tempmute
response_tempmute_success = "{datetime} -- **{member}** temporary muted {user} for `{seconds} seconds`!"
response_tempmute_failed = "{datetime} -- **{member}** tried to temporary mute {user} but something went wrong!"
response_tempmute_failed_no_bot_tempmute = (
    "{datetime} -- **{member}** tried to temporary mute {user} but this is a bot!"
)
### Temptimeout
response_temptimeout_success = "{datetime} -- **{member}** has temporary timedout {user} for `{seconds} seconds`!"
response_temptimeout_failed = "{datetime} -- **{member}** tried to temporary timeout {user} but something went wrong!"
response_temptimeout_failed_no_bot_temptimeout = (
    "{datetime} -- **{member}** tried to temporary timeout {user} but this is a bot!"
)
### Server Muted
response_user_guild_muted = "{datetime} -- **{member}** got server muted!"
### Server Unmuted
response_user_guild_unmuted = "{datetime} -- **{member}** got server unmuted!"
### Server Deafend
response_user_guild_deafend = "{datetime} -- **{member}** got server deafend!"
### Server Undeafend
response_user_guild_undeafend = "{datetime} -- **{member}** got server undeafend!"
### User Deafend
response_user_deafend = "{datetime} -- **{member}** self deafend!"
### User Undeafend
response_user_undeafend = "{datetime} -- **{member}** self undeafend!"
### User Muted
response_user_muted = "{datetime} -- **{member}** self muted!"
### User Unmuted
response_user_unmuted = "{datetime} -- **{member}** self unmuted!"
### User stream started
response_user_stream_started = "{datetime} -- **{member}** started streaming their screen!"
### User stream stopped
response_user_stream_stopped = "{datetime} -- **{member}** stopped streaming their screen!"
### User camera started
response_user_camera_stream_started = "{datetime} -- **{member}** turned on their camera!"
### User camera stopped
response_user_camera_stream_stopped = "{datetime} -- **{member}** turned off their camera!"

## Mod_Server
### Unlock
response_unlock_success = "{datetime} -- **{member}** unlocked {channel}!"
response_unlock_failed = "{datetime} -- **{member}** tried to unlock {channel} but something went wrong!"
response_unlock_failed_not_a_text_channel = (
    "{datetime} -- **{member}** tried to unlock {channel} but the given channel is not a text channel!"
)
response_unlock_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried to unlock a channel which I don't know!"
)
### Lock
response_lock_success = "{datetime} -- **{member}** locked {channel}!"
response_lock_failed = "{datetime} -- **{member}** tried to lock {channel} but something went wrong!"
response_lock_failed_not_a_text_channel = (
    "{datetime} -- **{member}** tried to lock {channel} but the given channel is not a text channel!"
)
response_lock_failed_channel_not_recognised = "{datetime} -- **{member}** tried to lock a channel which I don't know!"
### Slowmode
response_slowmode_set_success = "{datetime} -- **{member}** set slowmode for `{channel}` to `{delay} seconds`!"
response_slowmode_set_failed = (
    "{datetime} -- **{member}** tried to set slowmode for `{channel}` but something went wrong!"
)
response_slowmode_set_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried to set slowmode for a channel which I don't know!"
)
### Clear_Messages
response_clear_messages_finished = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}`! I have deleted `{amount_deleted}` messages!"
response_clear_messages_failed_over_14_days = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in {channel} but (some) messages are over 14 days old!"
response_clear_messages_invalid_channel = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}` but this is not a text channel!"
response_clear_messages_failed_channel_not_recognised = (
    "{datetime} -- **{member}** requested the deletion of `{amount}` messages in a channel I don't know!"
)
### Channel_Delete
response_channel_deleted = (
    "{datetime} -- **{member}** deleted the channel `{channel_name} - {channel_id}`!\n`[Reason]` -- {reason}"
)
response_channel_delete_failed = (
    "{datetime} -- **{member}** tried deleting the channel `{channel}` but something went wrong!"
)
### Channel_Create
response_channel_create_failed = "{datetime} -- **{member}** tried to create a `{channel_type}` but something went wrong! Does this server support this channel type?"
response_channel_created = "{datetime} -- **{member}** created a `{channel_type}` -> {channel}!\n`[Reason]` -- {reason}"
### Role_Delete
response_role_deleted = "{datetime} -- **{member}** deleted the role `{role_name} - {role_id}`!\n`[Reason]` -- {reason}"
response_role_delete_failed = "{datetime} -- **{member}** tried deleting the role `{role}` but something went wrong!"
### Role_Create
response_role_created = "{datetime} -- **{member}** created a `Role` -> {role}!\n`[Reason]` -- {reason}"
response_role_create_failed = (
    "{datetime} -- **{member}** tried to create a `Role` with the name `{role_name}` but something went wrong!"
)
### Channel_Leave
response_user_left_voice_channel = "{datetime} -- **{member}** left {channel}!"
### Channel_Move
response_user_moved_voice_channel = "{datetime} -- **{member}** moved from {from_channel} to {to_channel}!"
### Channel_Join
response_user_joined_voice_channel = "{datetime} -- **{member}** joined {channel}!"
### Channel_Update
response_channel_updated = "{datetime} -- **{member}** updated the channel {channel}!\n`[Reason]` -- {reason}"
### Role_Update
response_role_updated = "{datetime} -- **{member}** updated the role {role}!\n`[Reason]` -- {reason}"

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
response_module_tempchannels_transfer_failed_member_is_bot = "{datetime} -- **{member}** tried to transfer ownership of a tempchannel but the new owner is a bot!"
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
response_module_tickets_disabled = "{datetime} -- **{member}** has disabled the `tickets` module! All related settings are removed! The `ticket` module channels and roles should be removed, if this is not the case, these can safely be removed!"
response_module_tickets_disable_failed = "{datetime} -- **{member}** tried to disable the `tickets` module but something went wrong! Some of the configuration might be changed!!"
### Enable
response_module_tickets_enabled = "{datetime} -- **{member}** has enabled the `tickets` module!"
response_module_tickets_enable_failed = (
    "{datetime} -- **{member}** tried to enable the `tickets` module but something went wrong!"
)
### Settings
response_module_tickets_settings_changed = (
    "{datetime} -- **{member}** has changed the settings of the `tickets` module!"
)
response_module_tickets_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `tickets` module but something has gone wrong! Not all settings may have been changed!"

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
