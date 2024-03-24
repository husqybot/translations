# MODULE LOGGING CONFIGURATION
response_module_logging_enabled = "{datetime} -- **{member}** has enabled the `logging` module! I will now log all supported events to the new logging channel!"
response_module_logging_disabled = "{datetime} -- **{member}** has disabled the `logging` module! All related settings are removed!"
response_module_logging_disable_failed = "{datetime} -- **{member}** tried to disable the `logging` module but something went wrong! I have not changed the configuration!"
response_module_logging_settings_change_failed = "{datetime} -- **{member}** tried to change the settings of the `logging` module but something went wrong! I have not changed the configuration!"
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
response_join_failed_not_a_voice_channel = "{datetime} -- **{member}** tried joining me to a channel but didn't gave a valid voice channel!"
response_join_failed_not_enough_permissions = "{datetime} -- **{member}** tried joining me to a channel where I don't have enough permissions for!"
response_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel which I don't know! If this issue persist, please contact my support!"
response_join_failed_no_channel_given = "{datetime} -- **{member}** tried joining me to a channel but didn't provide a channel for me to join!"
### Leave
response_leave_success = "{datetime} -- **{member}** made me leave the voice channel!"
response_leave_failed = "{datetime} -- **{member}** tried to make me leave the voice channel! But something went wrong!"
response_music_events_leave = "{datetime} -- I left the voice channel, all users left!"
### Stop
response_stop_success = "{datetime} -- **{member}** stopped audio playback!"
response_stop_failed = (
    "{datetime} -- **{member}** tried to stop audio playback but something went wrong!"
)
### Pause
response_pause_success = "{datetime} -- **{member}** paused audio playback!"
response_pause_failed = (
    "{datetime} -- **{member}** tried to pause audio playback but something went wrong!"
)
response_pause_failed_radio_playing = "{datetime} -- **{member}** tried to pause the audio playback but a radio station is playing!"
response_pause_failed_nothing_playing = "{datetime} -- **{member}** tried to pause audio playback but there was nothing playing!"
### Resume
response_resume_success = "{datetime} -- **{member}** resumed audio playback!"
response_resume_failed = "{datetime} -- **{member}** tried to resume audio playback but something went wrong!"
response_resume_failed_radio_playing = (
    "{datetime} -- **{member}** tried to resume a radio station!"
)
response_resume_failed_nothing_playing = "{datetime} -- **{member}** tried to resume audio playback! But there was nothing playing!"
### Shuffle
response_music_shuffle_success = "{datetime} -- **{member}** shuffled the queue!"
response_music_shuffle_failed = (
    "{datetime} -- **{member}** tried to shuffle the queue but something went wrong!"
)
response_music_shuffle_playing_radio = "{datetime} -- **{member}** tried to shuffle the queue but there was a radio station playing!"
response_music_shuffle_not_playing_anything = "{datetime} -- **{member}** tried to shuffle the queue! But there was nothing to shuffle!"
### Skip
response_music_skip_song_success = "{datetime} -- **{member}** skipped a song!"
response_music_skip_stop_failed = "{datetime} -- **{member}** tried to stop audio playback because there was nothing left in the queue after a skip but something went wrong!"
response_music_skip_nothing_to_skip = (
    "{datetime} -- **{member}** tried to skip a song! But there was nothing to skip!"
)
response_music_skip_failed_radio_playing = (
    "{datetime} -- **{member}** tried to skip audio playback but radio is playing!"
)
response_music_skip_loop_enabled = (
    "{datetime} -- **{member}** tried to skip a song but loop was enabled!"
)
### Seek
response_music_seek_success = "{datetime} -- **{member}** jumped the track tp `{time}`!"
response_music_seek_failed_radio_playing = "{datetime} -- **{member}** tried to forward a radio station but this is not possible!"
response_music_seek_nothing_playing = (
    "{datetime} -- **{member}** tried to forward a song but there was nothing playing!"
)
response_music_seek_wrong_time_format = "{datetime} -- **{member}** tried to seek a track but gave me an invalid time format!"
### Restart Song
response_music_restart_success = (
    "{datetime} -- **{member}** restarted the current playing song!"
)
response_music_restart_failed_radio_playing = "{datetime} -- **{member}** tried to restart a radio station but this is not possible!"
response_music_restart_nothing_playing = (
    "{datetime} -- **{member}** tried to restart the song but there is no song playing!"
)
### Nowplaying
response_nowplaying_requested = (
    "{datetime} -- **{member}** requested the now playing song!"
)
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
response_loop_failed_radio_playing = "{datetime} -- **{member}** tried to roggle loop but there is a radio station playing!"
response_loop_failed_queue_empty = (
    "{datetime} -- **{member}** tried to toggle loop! But there is nothing playing!"
)
response_loop_failed_not_in_voicechannel = "{datetime} -- **{member}** tried to loop but they are not in the (right) voice channel!"
### Volume
response_volume_changed = (
    "{datetime} -- **{member}** has changed the volume to `{level}%`!"
)
### Play music
response_music_play_added_song = "{datetime} -- **{member}** added a song to the queue!"
response_music_play_added_playlist = (
    "{datetime} -- **{member}** added a playlist to the queue!"
)
response_music_play_failed_song = "{datetime} -- **{member}** tried adding a song to the queue but something went wrong!"
response_music_play_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL but I am not allowed to!"
)
response_music_play_failed_radio_playing = "{datetime} -- **{member}** tried playing a song/playlist/album but I am playing radio!"
response_music_play_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing music but something went wrong!"
response_music_play_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing music but I don't know that channel!"
response_music_play_join_failed_no_suitable_channel = "{datetime} -- **{member}** tried to add a song/playlist/album to the queue but neither off us are in a channel!"
### Play tts
response_music_playtts_added_song = "{datetime} -- **{member}** added a text-to-speech message to the queue! Message: `{tts_message}`!"
response_music_playtts_failed_song = "{datetime} -- **{member}** tried to use a text-to-speech message but something went wrong!"
response_music_playtts_failed_radio_playing = "{datetime} -- **{member}** tried playing a text-to-speech message but I am playing radio!"
response_music_playtts_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing a text-to-speech message but something went wrong!"
response_music_playtts_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing a text-to-speech message but I don't know that channel!"
response_music_playtts_join_failed_no_suitable_channel = "{datetime} -- **{member}** tried to add a text-to-speech message but neither off us are in a channel!"
### Play radio
response_radio_play_success = "{datetime} -- **{member}** played radiostation: `{radiostation}`! Provided by TuneIn!"
response_radio_play_failed = "{datetime} -- **{member}** tried playing radiostation: `{radiostation}` but something went wrong!"
response_radio_play_failed_http_error = "{datetime} -- **{member}** tried playing radiostation: `{radiostation}` but I got status code: `{status_code}`!"
response_radio_play_failed_already_playing = "{datetime} -- **{member}** tried to listen to radio but there was already something playing!"
response_radio_play_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing radio but something went wrong!"
response_radio_play_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing radio but I don't know that channel!"
response_radio_play_join_failed_no_suitable_channel = "{datetime} -- **{member}** tried to play a radiostation but neither off us are in a channel!"
### Playnext
response_music_playnext_added_song = (
    "{datetime} -- **{member}** added a song to the queue after the current song!"
)
response_music_playnext_added_playlist = (
    "{datetime} -- **{member}** added a playlist to the queue after the current song!"
)
response_music_playnext_failed_song = "{datetime} -- **{member}** tried adding a song to the queue after the current song but something went wrong!"
response_music_playnext_failed_no_youtube = (
    "{datetime} -- **{member}** tried playing a YouTube URL but I am not allowed to!"
)
response_music_playnext_failed_radio_playing = "{datetime} -- **{member}** tried playing a song/playlist/album after the current song but I was playing radio!"
response_music_playnext_join_failed = "{datetime} -- **{member}** tried joining me to `{channel}` by playing music but something went wrong!"
response_music_playnext_join_failed_channel_not_recognised = "{datetime} -- **{member}** tried joining me to a channel by playing a song using the playnext command but I don't know that channel!"
response_music_playnext_join_failed_no_suitable_channel = "{datetime} -- **{member}** tried to add a song using the playnext command but neither off us are in a channel!"
### Remove
response_music_remove_removed_song = (
    "{datetime} -- **{member}** removed a song from the queue!"
)
response_music_remove_removed_playlist = (
    "{datetime} -- **{member}** removed a playlist from the queue!"
)
response_music_remove_failed_song = "{datetime} -- **{member}** tried to remove a song from the queue but something went wrong!"
response_music_remove_failed_no_youtube = (
    "{datetime} -- **{member}** tried removing a YouTube URL but I am not allowed to"
)
response_music_remove_failed_radio_playing = "{datetime} -- **{member}** tried to remove a song from the queue but I am playing radio!"
response_music_remove_failed_nothing_to_remove = "{datetime} -- **{member}** tried to remove a song from the queue but there was nothing to remove!"
### Search
response_platform_searched = "{datetime} -- **{member}** searched {platform}!"
response_search_no_results_found = "{datetime} -- **{member}** searched YouTube or SoundCloud with the query: `{query}` but I didn't find any related results!"

## Giveaways
### Create
response_giveaway_created = "{datetime} -- **{member}** has created a giveaway!"
response_giveaway_create_failed_not_a_valid_time = "{datetime} -- **{member}** tried to create a giveaway but they gave me an invalid time duration!"
### Delete
response_giveaway_delete = "{datetime} -- **{member}** has deleted a giveaway!"
response_giveaway_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a giveaway but they are not the owner!"
)
response_giveaway_delete_failed_no_giveaway_found = "{datetime} -- **{member}** tried to delete a giveaway but I don't know of a giveaway with the given ID!"
### List
response_giveaway_list_requested = (
    "{datetime} -- **{member}** has requested their giveaways in this server!"
)
response_giveaway_list_no_giveaways = "{datetime} -- **{member}** tried to list their giveaways in this server but they don't have any!"
### Reroll
response_giveaway_reroll = (
    "{datetime} -- **{member}** has rerolled a winner for a giveaway!"
)
response_giveaway_reroll_failed_no_winner_yet = "{datetime} -- **{member}** tried to reroll a winner for a giveaway but there is no winner yet!"
response_giveaway_reroll_failed_not_owner = "{datetime} -- **{member}** tried to reroll a winner for a giveaway but they are not the owner!"
response_giveaway_reroll_failed_no_giveaway_found = "{datetime} -- **{member}** tried to reroll a winner for a giveaway but there is no giveaway with the given ID!"

## General
### Info
response_info_bot_requested = "{datetime} -- **{member}** requested my information!"
response_info_user_requested = (
    "{datetime} -- **{member}** requested information about {user}!"
)
response_info_role_requested = (
    "{datetime} -- **{member}** requested information about the role {role}!"
)
response_info_channel_requested = (
    "{datetime} -- **{member}** requested information about the channel `{channel}`!"
)
response_info_channel_requested_failed_channel_not_recognised = (
    "{datetime} -- **{member}** requested information about a channel I don't know!"
)
response_info_server_requested = (
    "{datetime} -- **{member}** requested information about the server!"
)
response_module_socials_twitch_list = (
    "{datetime} -- **{member}** requested the Twitch account list!"
)
response_module_socials_rss_list = (
    "{datetime} -- **{member}** requested the RSS Feed list!"
)
response_module_socials_reddit_list = (
    "{datetime} -- **{member}** requested the Subreddit list!"
)
### Ping
response_ping_requested = "{datetime} -- **{member}** used `/ping`! REST Latency: `{rest_latency} ms` - Gateway Latency: `{gateway_latency} ms`."
### Invite link
response_invite_link_requested = (
    "{datetime} -- **{member}** requested the configured invite link!"
)
response_invite_link_not_set = (
    "{datetime} -- **{member}** requested the configured invite link but none was set!"
)
### Support
response_support = (
    "{datetime} -- **{member}** has requested information regarding my support!"
)

## Misc
### Games
response_games_played_heads_or_tails = (
    "{datetime} -- **{member}** played `Heads or Tails`!"
)
response_games_played_rps = "{datetime} -- **{member}** played `Rock/Paper/Scissors` against {opponent}! The winner is {winner}!"
response_games_played_higher_lower_played_won = (
    "{datetime} -- **{member}** played `Higher/Lower` and won!"
)
response_games_played_higher_lower_played_loss = (
    "{datetime} -- **{member}** played `Higher/Lower` and lost!"
)
### Meme
response_meme_success = "{datetime} -- **{member}** requested a meme!"
### Transcribe audio message
response_transcribe_failed = "{datetime} -- **{member}** tried to transcribe a voice message but something went wrong!"
response_transcribe_success = "{datetime} -- **{member}** transcribed a voice message!"

## Polls
### Clear votes
response_poll_clear_votes_failed_no_poll_found = "{datetime} -- **{member}** tried to delete a poll but the given poll ID was not found!"
response_poll_clear_votes = (
    "{datetime} -- **{member}** cleared their votes from a poll!"
)
### Create
response_poll_created = "{datetime} -- **{member}** created a poll!"
response_poll_create_failed_no_time = "{datetime} -- **{member}** tried to create a timed poll but they didn't insert a time duration!"
response_poll_create_failed_not_a_valid_time = "{datetime} -- **{member}** tried to create a timed poll but they gave an invalid time duration!"
response_poll_create_failed_anwers_in_wrong_order = "{datetime} -- **{member}** tried to create a poll but the extra answers are not in order (if more than the required two anwers are used, make sure it is in the order answer3, answer4 and answer5)!"
### Delete
response_poll_delete = "{datetime} -- **{member}** deleted a poll!"
response_poll_delete_failed_not_owner = (
    "{datetime} -- **{member}** tried to delete a poll but they are not the owner!"
)
response_poll_delete_failed_no_poll_found = "{datetime} -- **{member}** tried to delete a poll but the given poll ID was not found!"
### Details
response_poll_details_requested = (
    "{datetime} -- **{member}** requested the details/results of a poll!"
)
### List
response_poll_list_requested = "{datetime} -- **{member}** requested their poll list!"
response_polls_list_no_polls = "{datetime} -- **{member}** requested their poll list but they don't have any active polls!"
### Stop
response_poll_stop = "{datetime} -- **{member}** stopped a poll!"
response_poll_stop_failed_not_owner = (
    "{datetime} -- **{member}** tried to stop a poll but they are not the owner!"
)
response_poll_stop_failed_no_poll_found = "{datetime} -- **{member}** tried to stop a poll but the given poll ID was not found!"

## Reminders
### Add
response_reminder_add_failed_not_a_valid_wait_duration = "{datetime} -- **{member}** tried to add a reminder but the provided wait duration was an invalid format!"
response_reminder_add_dm_destination_is_not_target_user = "{datetime} -- **{member}** tried to add a reminder but they provided a DM of a user who is not the target user as the destination!"
response_reminder_add_not_a_url = "{datetime} -- **{member}** tried to add a reminder but the provided linked message was not a valid URL!"
response_reminder_added = "{datetime} -- **{member}** added a new reminder!"
### Delete
response_reminder_deleted = (
    "{datetime} -- **{member}** tried to deleted one of their reminders!"
)
response_reminder_delete_failed_not_target_user = "{datetime} -- **{member}** tried to delete a reminder but they aren't the target user!"
response_reminder_delete_failed_no_reminder_found = "{datetime} -- **{member}** tried to delete a reminder but I didn't find a remidner with the specified ID!"
### List
response_reminder_list_requested = (
    "{datetime} -- **{member}** requested their reminders!"
)
response_reminder_list_no_reminders = "{datetime} -- **{member}** requested their reminders but they don't have any reminders!"

## Tags
### Create
response_tag_create_success = (
    "{datetime} -- **{member}** has created a tag named `{tag_name}`!"
)
response_tag_create_failed = "{datetime} -- **{member}** tried to create a tag named `{tag_name}` but something went wrong!"
response_tag_create_failed_already_exists = "{datetime} -- **{member}** tried to create a tag named `{tag_name}` but that name already exists!"
### Delete
response_tag_delete_success = "{datetime} -- **{member}** deleted the tag `{tag_name}`!"
response_tag_delete_failed = "{datetime} -- **{member}** tried to delete the tag `{tag_name}` but something went wrong!"
response_tag_delete_failed_tag_does_not_exist = "{datetime} -- **{member}** tried to delete the tag `{tag_name}` but that tag did not exist!"
### Edit
response_tag_edit_success = (
    "{datetime} -- **{member}** edited a tag named `{tag_name}`!"
)
response_tag_edit_failed = "{datetime} -- **{member}** tried to edit a tag named `{tag_name}` but something went wrong!"
response_tag_edit_failed_tag_does_not_exist = "{datetime} -- **{member}** tried to edit a tag named `{tag_name}` but that tag does not exist!"
### List
response_tags_list_requested = "{datetime} -- **{member}** viewed the list of tags!"
response_tags_list_empty = "{datetime} -- **{member}** tried to view the list of tags but there are no tags available in this server!"
### Send
response_tag_send_success = "{datetime} -- **{member}** used the tag `{tag_name}`!"
response_tag_send_failed_no_such_tag = "{datetime} -- **{member}** tried to send a tag with the name `{tag_name}` but it does not exist!"

## Utils
### Color view
response_color_viewed_success = "{datetime} -- **{member}** has viewed a color with the HEX or RGB value: `{color}`!"
response_color_viewed_failed = (
    "{datetime} -- **{member}** tried to view a color but something went wrong!"
)
response_color_viewed_failed_only_one_value_allowed = "{datetime} -- **{member}** tried to view a color but inserted both a HEX and RGB value!"
response_color_viewed_failed_no_values_given = "{datetime} -- **{member}** tried to view a color but didn't insert a HEX or RGB value!"
### Custom embed
response_custom_embed_create = (
    "{datetime} -- **{member}** started creating their own embed!"
)
response_custom_embed_finished = "{datetime} -- **{member}** created a custom embed!"
response_custom_embed_finished_timeout = (
    "{datetime} -- **{member}** created a custom embed but a timeout was reached!"
)
response_custom_embed_send_success = (
    "{datetime} -- **{member}** sent a custom embed to {channel}!"
)
response_custom_embed_send_failed_not_a_text_channel = "{datetime} -- **{member}** tried sending a custom embed but didn't gave a valid text channel!"
response_custom_embed_send_failed_not_enough_permissions = "{datetime} -- **{member}** tried sending a custom embed but I don't have enough permissions for that channel!"
response_custom_embed_send_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried sending a custom embed to a channel I don't know!"
)
### Custom modal
response_custom_modal_create = (
    "{datetime} -- **{member}** started creating their own modal!"
)
response_custom_modal_finished = "{datetime} -- **{member}** created a custom modal!"
response_custom_modal_finished_timeout = (
    "{datetime} -- **{member}** created a custom modal but a timeout was reached!"
)
response_custom_modal_preview_success = (
    "{datetime} -- **{member}** previewed a custom modal!"
)
response_custom_modal_preview_failed_canceled = (
    "{datetime} -- **{member}** tried to preview a custom modal but canceled it!"
)
response_custom_modal_preview_failed = "{datetime} -- **{member}** tried to preview a custom modal but a timeout was reached!"
### Domain
response_domain_validate_safety_success_not_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is NOT a safe URL!"
)
response_domain_validate_safety_success_is_safe = (
    "{datetime} -- **{member}** checked the safety of `{domain}`! It is a safe URL!"
)
response_domain_validate_safety_failed_http_code = "{datetime} -- **{member}** tried to check the safety of `{domain}` but got HTTP error: {http_code}!"
### QR
response_qr_generate_success = "{datetime} -- **{member}** has generated a QR-code!"
### Convert
response_time_converted_success = "{datetime} -- **{member}** converted: {days} days, {hours} hours, {minutes} minutes and {seconds} seconds to seconds: `{total_seconds}`!"

## Mod_user
### Ban_Create
response_user_events_banned = (
    "{datetime} -- **{member}** has banned `{user}`!\n`[Reason]` -- {reason}"
)
response_ban_create_failed = (
    "{datetime} -- **{member}** tried to ban `{user}` but something went wrong!"
)
response_ban_create_failed_no_bot_ban = (
    "{datetime} -- **{member}** tried to ban `{user}` but this is a bot!"
)
### Ban_Delete
response_user_events_unbanned = (
    "{datetime} -- **{member}** has unbanned `{user}`!\n`[Reason]` -- {reason}"
)
response_ban_delete_failed = (
    "{datetime} -- **{member}** tried to unban `{user}` but something went wrong!"
)
response_ban_delete_failed_no_bot_unban = (
    "{datetime} -- **{member}** tried to unban `{user}` but this is a bot!"
)
### Warn_Create
response_warn_create_success = "{datetime} -- **{member}** warned `{user}` and added `{points} points` to their profile!\n`[Reason]` -- {reason}"
response_warn_create_failed = (
    "{datetime} -- **{member}** tried to warn `{user}` but something went wrong!"
)
response_warn_create_failed_no_bot_warn = (
    "{datetime} -- **{member}** tried to warn `{user}` but this is a bot!"
)
### Warn_Delete
response_warn_delete_success = "{datetime} -- **{member}** deleted a warn from `{user}` and removed `{points} points` from their profile!\n`[Reason]` -- {reason}"
response_warn_delete_failed = "{datetime} -- **{member}** tried to delete a warn from `{user}` but something went wrong!"
response_warn_delete_failed_no_bot_warn_delete = (
    "{datetime} -- **{member}** tried to delete a warn from `{user}` but this is a bot!"
)
### Kick
response_user_kicked = (
    "{datetime} -- **{member}** has kicked `{user}`!\n`[Reason]` -- {reason}"
)
response_kick_failed = (
    "{datetime} -- **{member}** tried to kick {user} but something went wrong!"
)
response_kick_failed_no_bot_kick = (
    "{datetime} -- **{member}** tried to kick {user} but this is a bot!"
)
### Vckick
response_vckick_success = "{datetime} -- **{member}** has kicked {user} from a voice channel!\n`[Reason]` -- {reason}"
response_vckick_failed = "{datetime} -- **{member}** tried to kick {user} from a voice channel but something went wrong!"
### Move
response_move_success = (
    "{datetime} -- **{member}** has moved {user} to {channel}!\n`[Reason]` -- {reason}"
)
response_move_failed = "{datetime} -- **{member}** tried to move {user} to {channel}! But something went wrong!"
response_move_failed_missing_permissions = "{datetime} -- **{member}** tried to move {user} to {channel} but either I or this user is missing permissions!"
response_move_failed_user_not_in_a_voice_channel = "{datetime} -- **{member}** tried to move {user} to {channel} but this user is not in a voice channel!"
response_move_failed_not_a_voice_channel = "{datetime} -- **{member}** tried to move {user} to {channel} but this channel is not a voice channel!"
### Tempmute
response_tempmute_success = (
    "{datetime} -- **{member}** temporary muted {user} for `{seconds} seconds`!"
)
response_tempmute_failed = "{datetime} -- **{member}** tried to temporary mute {user} but something went wrong!"
response_tempmute_failed_no_bot_tempmute = (
    "{datetime} -- **{member}** tried to temporary mute {user} but this is a bot!"
)
### Temptimeout
response_temptimeout_success = (
    "{datetime} -- **{member}** has temporary timedout {user} for `{seconds} seconds`!"
)
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
response_user_stream_started = (
    "{datetime} -- **{member}** started streaming their screen!"
)
### User stream stopped
response_user_stream_stopped = (
    "{datetime} -- **{member}** stopped streaming their screen!"
)
### User camera started
response_user_camera_stream_started = (
    "{datetime} -- **{member}** turned on their camera!"
)
### User camera stopped
response_user_camera_stream_stopped = (
    "{datetime} -- **{member}** turned off their camera!"
)

## Mod_Server
### Unlock
response_unlock_success = "{datetime} -- **{member}** unlocked {channel}!"
response_unlock_failed = (
    "{datetime} -- **{member}** tried to unlock {channel} but something went wrong!"
)
response_unlock_failed_not_a_text_channel = "{datetime} -- **{member}** tried to unlock {channel} but the given channel is not a text channel!"
response_unlock_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried to unlock a channel which I don't know!"
)
### Lock
response_lock_success = "{datetime} -- **{member}** locked {channel}!"
response_lock_failed = (
    "{datetime} -- **{member}** tried to lock {channel} but something went wrong!"
)
response_lock_failed_not_a_text_channel = "{datetime} -- **{member}** tried to lock {channel} but the given channel is not a text channel!"
response_lock_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried to lock a channel which I don't know!"
)
### Slowmode
response_slowmode_set_success = (
    "{datetime} -- **{member}** set slowmode for `{channel}` to `{delay} seconds`!"
)
response_slowmode_set_failed = "{datetime} -- **{member}** tried to set slowmode for `{channel}` but something went wrong!"
response_slowmode_set_failed_channel_not_recognised = (
    "{datetime} -- **{member}** tried to set slowmode for a channel which I don't know!"
)
### Clear_Messages
response_clear_messages_finished = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}`! I have deleted `{amount_deleted}` messages!"
response_clear_messages_failed_over_14_days = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in {channel} but (some) messages are over 14 days old!"
response_clear_messages_invalid_channel = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in `{channel}` but this is not a text channel!"
response_clear_messages_failed_channel_not_recognised = "{datetime} -- **{member}** requested the deletion of `{amount}` messages in a channel I don't know!"
### Channel_Delete
response_channel_deleted = "{datetime} -- **{member}** deleted the channel `{channel_name} - {channel_id}`!\n`[Reason]` -- {reason}"
response_channel_delete_failed = "{datetime} -- **{member}** tried deleting the channel `{channel}` but something went wrong!"
### Channel_Create
response_channel_create_failed = "{datetime} -- **{member}** tried to create a `{channel_type}` but something went wrong! Does this server support this channel type?"
response_channel_created = "{datetime} -- **{member}** created a `{channel_type}` -> {channel}!\n`[Reason]` -- {reason}"
### Role_Delete
response_role_deleted = "{datetime} -- **{member}** deleted the role `{role_name} - {role_id}`!\n`[Reason]` -- {reason}"
response_role_delete_failed = "{datetime} -- **{member}** tried deleting the role `{role}` but something went wrong!"
### Role_Create
response_role_created = (
    "{datetime} -- **{member}** created a `Role` -> {role}!\n`[Reason]` -- {reason}"
)
response_role_create_failed = "{datetime} -- **{member}** tried to create a `Role` with the name `{role_name}` but something went wrong!"
### Channel_Leave
response_user_left_voice_channel = "{datetime} -- **{member}** left {channel}!"
### Channel_Move
response_user_moved_voice_channel = (
    "{datetime} -- **{member}** moved from {from_channel} to {to_channel}!"
)
### Channel_Join
response_user_joined_voice_channel = "{datetime} -- **{member}** joined {channel}!"
### Channel_Update
response_channel_updated = (
    "{datetime} -- **{member}** updated the channel {channel}!\n`[Reason]` -- {reason}"
)
### Role_Update
response_role_updated = (
    "{datetime} -- **{member}** updated the role {role}!\n`[Reason]` -- {reason}"
)

## Module Autoresponder
### Disable
response_module_autoresponder_disabled = "{datetime} -- **{member}** has disabled the `autoresponder` module! All related settings are removed!"
response_module_autoresponder_disable_failed = "{datetime} -- **{member}** tried to disable the `autoresponder` module but something went wrong! I have not changed the configuration!"
### Enable
response_module_autoresponder_enabled = "{datetime} -- **{member}** has enabled the `autoresponder` module!"
response_module_autoresponder_enable_failed = "{datetime} -- **{member}** tried to enable the `autoresponder` module but something went wrong!"
### Create
response_module_autoresponder_create_entry_success = "{datetime} -- **{member}** has created an entry for the `autoresponder` module!"
response_module_autoresponder_create_entry_failed = "{datetime} -- **{member}** tried to create an entry for the `autoresponder` module but something went wrong!"
### Delete
response_module_autoresponder_delete_entry_success = "{datetime} -- **{member}** has deleted an entry from the `autoresponder` module!"
response_module_autoresponder_create_entry_failed = "{datetime} -- **{member}** tried to delete an entry from the `autoresponder` module but something went wrong!"

## Module Tempchannel
### tempchannel edit
response_tempchannel_edit_failed_not_a_temporary_channel = "{datetime} -- **{member}** tried to edit a temporary channel but the inserted channel isn't a temporary channel!"
### tempchannel edit user_limit
response_tempchannel_edit_user_limit_success = "{datetime} -- **{member}** changed the user limit of a temporary channel to `{user_limit} users`!"
response_tempchannel_edit_user_limit_off_success = (
    "{datetime} -- **{member}** turned off the user limit of a temporary channel!"
)
response_tempchannel_edit_user_limit_failed = "{datetime} -- **{member}** tried to change the user limit of a temporary channel but something went wrong!"
response_tempchannel_edit_user_limit_failed_not_a_valid_range = "{datetime} -- **{member}** tried to change the user limit of a temporary channel but the number wasn't in the valid range (0 - 99)!"
response_tempchannel_edit_user_limit_failed_not_a_valid_number = "{datetime} -- **{member}** tried to change the user limit of a temporary channel but didn't insert a valid number!"
### tempchannel edit transfer
response_tempchannel_edit_transfer_success = (
    "{datetime} -- **{member}** transferred ownership of a temporary channel!"
)
response_tempchannel_edit_transfer_failed = "{datetime} -- **{member}** tried to transfer ownership of a temporary channel but something went wrong!"
response_tempchannel_edit_transfer_failed_not_a_valid_member = "{datetime} -- **{member}** tried to transfer ownership of a temporary channel but didn't insert a valid server memmber!"
response_tempchannel_edit_transfer_cancelled = "{datetime} -- **{member}** cancelled the ownership transfer of a temporary channel!"
### Slowmode
response_tempchannel_edit_slowmode_success = "{datetime} -- **{member}** changed the slowmode delay of a temporary channel to `{slowmode} seconds`!"
response_tempchannel_edit_slowmode_off_success = (
    "{datetime} -- **{member}** turned off the slowmode of a temporary channel!"
)
response_tempchannel_edit_slowmode_failed = "{datetime} -- **{member}** tried to change the slowmode delay of a temporary channel but something went wrong!"
response_tempchannel_edit_slowmode_failed_not_a_valid_number = "{datetime} -- **{member}** tried to change the slowmode delay of a temporary channel but didn't insert a valid number!"
### Onlyfor
response_tempchannel_onlyfor_block_success = (
    "{datetime} -- **{member}** has limited a temporary channel to a role!"
)
response_tempchannel_onlyfor_block_failed = "{datetime} -- **{member}** tried to limit a temporary channel to a role but something went wrong!"
### Block
response_tempchannel_edit_block_success = (
    "{datetime} -- **{member}** has blocked users from a temporary channel!"
)
response_tempchannel_edit_block_failed = "{datetime} -- **{member}** tried to block one or more users from a temporary channel but something went wrong!"
### Unblock
response_tempchannel_edit_unblock_success = (
    "{datetime} -- **{member}** has unblocked users from a temporary channel!"
)
response_tempchannel_edit_unblock_failed = "{datetime} -- **{member}** tried to unblock one or more users from a temporary channel but something went wrong!"
### Claim
response_tempchannel_edit_claim_success = (
    "{datetime} -- **{member}** claimed ownership of a temporary channel!"
)
response_tempchannel_edit_claim_failed = "{datetime} -- **{member}** tried to claim ownership of a temporary channel but something went wrong!"
response_tempchannel_edit_claim_cancelled = (
    "{datetime} -- **{member}** cancelled the ownership claim of a temporary channel!"
)
response_tempchannel_edit_claim_not_possible = "{datetime} -- **{member}** tried to claim ownership of a temporary channel but there was still an owner!"
### Name
response_tempchannel_edit_name_success = (
    "{datetime} -- **{member}** changed the name of a temporary channel to `{name}`!"
)
response_tempchannel_edit_name_failed = "{datetime} -- **{member}** tried to edit the name of a temporary channel but something went wrong!"
### Disable
response_module_tempchannel_disabled = "{datetime} -- **{member}** has disabled the `tempchannel` module! All related settings are removed!"
response_module_tempchannel_disable_failed = "{datetime} -- **{member}** tried to disable the `tempchannel` module but something went wrong! I have not changed the configuration!"
### Enable
response_module_tempchannel_enabled = "{datetime} -- **{member}** has enabled the `tempchannel` module!"
response_module_tempchannel_enable_failed = "{datetime} -- **{member}** tried to enable the `tempchannel` module but something went wrong!"
