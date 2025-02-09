# MODULE TEMPCHANNELS
removed_user = "(removed_user)"
enabled = "Enabled"
disabled = "Disabled"
module_create_a_temporary_channel = "Create a TempChannel"
module_tempchannel_default_tempchannels_creation_category = "{bot_name} Tempchannels"
module_tempchannel_default_voice_category = "{bot_name} Voice"
module_tempchannel_default_text_category = "{bot_name} Text"

# Responses
## Transfer
response_edit_transfer_failed_no_language = "I could not complete the transferral of ownership of the tempchannels because the servers language is not found!"
response_edit_transfer_failed_no_auto_delete = "I could not complete the transferral of ownership of the tempchannels because the servers auto delete is not found!"
response_edit_transfer_failed_no_timezone = "I could not complete the transferral of ownership of the tempchannels because the servers timezone is not found!"
response_edit_transfer_failed_unknown_module_status = "I could not complete the transferral of ownership of the tempchannels because I could not determine the status of the `tempchannels` module!"
response_edit_transfer_failed_module_disabled = "I could not complete the transferral of ownership of the tempchannels because the `tempchannels` module is disabled!"
response_edit_transfer_failed_no_tempchannel_found = "I could not complete the transferral of ownership of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_transfer_failed_not_the_owner = "I could not complete the transferral of ownership of the tempchannels because you are not the owner!"
response_edit_transfer_failed = (
    "Something went wrong while trying to transfer the ownership to {member}!"
)
response_edit_transfer_success = (
    "Ownership of the tempchannels has been transferred. {member} is now the new owner!"
)
## User limit
response_edit_user_limit_failed_no_language = "I could not set the user limit of the tempchannel because the servers language is not found!"
response_edit_user_limit_failed_no_auto_delete = "I could not set the user limit of the tempchannel because the servers auto delete is not found!"
response_edit_user_limit_failed_no_timezone = "I could not set the user limit of the tempchannel because the servers timezone is not found!"
response_edit_user_limit_failed_unknown_module_status = "I could not set the user limit of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_user_limit_failed_module_disabled = "I could not set the user limit of the tempchannel because the `tempchannels` module is disabled!"
response_edit_user_limit_failed_no_tempchannel_found = "I could not set the user limit of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_user_limit_failed_not_the_owner = (
    "I could not set the user limit of the tempchannel because you are not the owner!"
)
response_edit_user_limit_failed_not_in_range = (
    "The new user limit must be between 0 and 99!"
)
response_edit_user_limit_failed = (
    "Something went wrong while trying to set the user limit to {new_limit}!"
)
response_edit_user_limit_success = "The user limit has been set to {new_limit}!"
## Slowmode
response_edit_slowmode_failed_no_language = "I could not set the slowmode of the tempchannel because the servers language is not found!"
response_edit_slowmode_failed_no_auto_delete = "I could not set the slowmode of the tempchannel because the servers auto delete is not found!"
response_edit_slowmode_failed_no_timezone = "I could not set the slowmode of the tempchannel because the servers timezone is not found!"
response_edit_slowmode_failed_unknown_module_status = "I could not set the slowmode of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_slowmode_failed_module_disabled = "I could not set the slowmode of the tempchannel because the `tempchannels` module is disabled!"
response_edit_slowmode_failed_no_tempchannel_found = "I could not set the slowmode of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_slowmode_failed_not_the_owner = (
    "I could not set the slowmode of the tempchannel because you are not the owner!"
)
response_edit_slowmode_failed = (
    "Something went wrong while trying to set the slowmode to {new_slowmode} seconds!"
)
response_edit_slowmode_success = "The slowmode has been set to {new_slowmode} seconds!"
## Region
response_edit_region_failed_no_language = "I could not set the region of the tempchannel because the servers language is not found!"
response_edit_region_failed_no_auto_delete = "I could not set the region of the tempchannel because the servers auto delete is not found!"
response_edit_region_failed_no_timezone = "I could not set the region of the tempchannel because the servers timezone is not found!"
response_edit_region_failed_unknown_module_status = "I could not set the region of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_region_failed_module_disabled = "I could not set the region of the tempchannel because the `tempchannels` module is disabled!"
response_edit_region_failed_no_tempchannel_found = "I could not set the region of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_region_failed_not_the_owner = (
    "I could not set the region of the tempchannel because you are not the owner!"
)
response_edit_region_failed = "Something went wrong while trying to set the region! Is the given region a valid Discord Region ID?"
response_edit_region_success = (
    "The region has been changed. You might notice some reconnecting happen!"
)
## Name
response_edit_name_failed_no_language = "I could not set the name of the tempchannel because the servers language is not found!"
response_edit_name_failed_no_auto_delete = "I could not set the name of the tempchannel because the servers auto delete is not found!"
response_edit_name_failed_no_timezone = "I could not set the name of the tempchannel because the servers timezone is not found!"
response_edit_name_failed_unknown_module_status = "I could not set the name of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_name_failed_module_disabled = "I could not set the name of the tempchannel because the `tempchannels` module is disabled!"
response_edit_name_failed_no_tempchannel_found = "I could not set the name of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_name_failed_not_the_owner = (
    "I could not set the name of the tempchannel because you are not the owner!"
)
response_edit_name_failed = (
    "Something went wrong while trying to change the tempchannels name to {new_name}!"
)
response_edit_name_success = "The name has been changed to {new_name}!"
## Bitrate
response_edit_bitrate_failed_no_language = "I could not set the bitrate of the tempchannel because the servers language is not found!"
response_edit_bitrate_failed_no_auto_delete = "I could not set the bitrate of the tempchannel because the servers auto delete is not found!"
response_edit_bitrate_failed_no_timezone = "I could not set the bitrate of the tempchannel because the servers timezone is not found!"
response_edit_bitrate_failed_unknown_module_status = "I could not set the bitrate of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_bitrate_failed_module_disabled = "I could not set the bitrate of the tempchannel because the `tempchannels` module is disabled!"
response_edit_bitrate_failed_no_tempchannel_found = "I could not set the bitrate of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_bitrate_failed_not_the_owner = (
    "I could not set the bitrate of the tempchannel because you are not the owner!"
)
response_edit_bitrate_failed_not_in_range = "The new bitrate must be between 8 and 96!"
response_edit_bitrate_failed = "Something went wrong while trying to change the tempchannels bitrate to {new_bitrate} kbps!"
response_edit_bitrate_success = "The bitrate has been changed to {new_bitrate} kbps!"
## Age restriction
response_edit_age_restriction_failed_no_language = "I could not set the age restriction of the tempchannel because the servers language is not found!"
response_edit_age_restriction_failed_no_auto_delete = "I could not set the age restriction of the tempchannel because the servers auto delete is not found!"
response_edit_age_restriction_failed_no_timezone = "I could not set the age restriction of the tempchannel because the servers timezone is not found!"
response_edit_age_restriction_failed_unknown_module_status = "I could not set the age restriction of the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_age_restriction_failed_module_disabled = "I could not set the age restriction of the tempchannel because the `tempchannels` module is disabled!"
response_edit_age_restriction_failed_no_tempchannel_found = "I could not set the age restriction of the tempchannels because I couldn't find a tempchannel with the given ID!"
response_edit_age_restriction_failed_not_the_owner = "I could not set the age restriction of the tempchannel because you are not the owner!"
response_edit_age_restriction_failed = "Something went wrong while trying to set the tempchannels age restriction to `{status}`!"
response_edit_age_restriction_success = (
    "The age restriction has been changed to `{status}`!"
)
## Delete
response_edit_delete_failed_no_language = (
    "I could not delete the tempchannel set because the servers language is not found!"
)
response_edit_delete_failed_no_auto_delete = "I could not delete the tempchannel set because the servers auto delete is not found!"
response_edit_delete_failed_no_timezone = (
    "I could not delete the tempchannel set because the servers timezone is not found!"
)
response_edit_delete_failed_unknown_module_status = "I could not delete the tempchannel set because I could not determine the status of the `tempchannels` module!"
response_edit_delete_failed_module_disabled = "I could not delete the tempchannel set because the `tempchannels` module is disabled!"
response_edit_delete_failed_no_tempchannel_found = "I could not delete the tempchannel set because I couldn't find a tempchannel with the given ID!"
response_edit_delete_failed_not_the_owner = (
    "I could not delete the tempchannel set because you are not the owner!"
)
response_edit_delete_failed = (
    "Something went wrong while trying to delete the tempchannel set!"
)
response_edit_delete_success = "The tempchannel set has been deleted!"
## Claim
response_edit_claim_failed_no_language = "I could not complete the claim of the tempchannel set because the servers language is not found!"
response_edit_claim_failed_no_auto_delete = "I could not complete the claim of the tempchannel set because the servers auto delete is not found!"
response_edit_claim_failed_no_timezone = "I could not complete the claim of the tempchannel set because the servers timezone is not found!"
response_edit_claim_failed_unknown_module_status = "I could not complete the claim of the tempchannel set because I could not determine the status of the `tempchannels` module!"
response_edit_claim_failed_module_disabled = "I could not complete the claim of the tempchannel set because the `tempchannels` module is disabled!"
response_edit_claim_failed_no_tempchannel_found = "I could not complete the claim of the tempchannel set because I couldn't find a tempchannel with the given ID!"
response_edit_claim_failed_owner_linked = "I could not complete the claim of the tempchannel set because there is still an owner linked!"
response_edit_claim_failed = (
    "Something went wrong while trying to claim the tempchannel set!"
)
response_edit_claim_success = (
    "The tempchannel set has been claimed! You are now the owner!"
)
## Remove trust rule
response_edit_remove_trust_rule_failed_no_language = "I could not remove the trust rule from the tempchannel because the servers language is not found!"
response_edit_remove_trust_rule_failed_no_auto_delete = "I could not remove the trust rule from the tempchannel because the servers auto delete is not found!"
response_edit_remove_trust_rule_failed_no_timezone = "I could not remove the trust rule from the tempchannel because the servers timezone is not found!"
response_edit_remove_trust_rule_failed_unknown_module_status = "I could not remove the trust rule from the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_remove_trust_rule_failed_module_disabled = "I could not remove the trust rule from the tempchannel because the `tempchannels` module is disabled!"
response_edit_remove_trust_rule_failed_no_tempchannel_found = "I could not remove the trust rule from the tempchannel because I couldn't find a tempchannel with the given ID!"
response_edit_remove_trust_rule_failed_not_the_owner = "I could not remove the trust rule from the tempchannel because you are not the owner!"
response_edit_remove_trust_rule_failed = (
    "Something went wrong while trying to remove the trust rule from the tempchannel!"
)
response_edit_remove_trust_rule_success = "The trust rule has been removed!"
## Remove block rule
response_edit_remove_block_rule_failed_no_language = "I could not remove the block rule from the tempchannel because the servers language is not found!"
response_edit_remove_block_rule_failed_no_auto_delete = "I could not remove the block rule from the tempchannel because the servers auto delete is not found!"
response_edit_remove_block_rule_failed_no_timezone = "I could not remove the block rule from the tempchannel because the servers timezone is not found!"
response_edit_remove_block_rule_failed_unknown_module_status = "I could not remove the block rule from the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_remove_block_rule_failed_module_disabled = "I could not remove the block rule from the tempchannel because the `tempchannels` module is disabled!"
response_edit_remove_block_rule_failed_no_tempchannel_found = "I could not remove the block rule from the tempchannel because I couldn't find a tempchannel with the given ID!"
response_edit_remove_block_rule_failed_not_the_owner = "I could not remove the block rule from the tempchannel because you are not the owner!"
response_edit_remove_block_rule_failed = (
    "Something went wrong while trying to remove the block rule from the tempchannel!"
)
response_edit_remove_block_rule_success = "The block rule has been removed!"
## Add trust rule
response_edit_add_trust_rule_failed_no_language = "I could not add the trust rule to the tempchannel because the servers language is not found!"
response_edit_add_trust_rule_failed_no_auto_delete = "I could not add the trust rule to the tempchannel because the servers auto delete is not found!"
response_edit_add_trust_rule_failed_no_timezone = "I could not add the trust rule to the tempchannel because the servers timezone is not found!"
response_edit_add_trust_rule_failed_unknown_module_status = "I could not add the trust rule to the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_add_trust_rule_failed_module_disabled = "I could not add the trust rule to the tempchannel because the `tempchannels` module is disabled!"
response_edit_add_trust_rule_failed_no_tempchannel_found = "I could not add the trust rule to the tempchannel because I couldn't find a tempchannel with the given ID!"
response_edit_add_trust_rule_failed_not_the_owner = (
    "I could not add the trust rule to the tempchannel because you are not the owner!"
)
response_edit_add_trust_rule_failed = (
    "Something went wrong while trying to add the trust rule to the tempchannel!"
)
response_edit_add_trust_rule_success = "The trust rule has been addd!"
## Add block rule
response_edit_add_block_rule_failed_no_language = "I could not add the block rule to the tempchannel because the servers language is not found!"
response_edit_add_block_rule_failed_no_auto_delete = "I could not add the block rule to the tempchannel because the servers auto delete is not found!"
response_edit_add_block_rule_failed_no_timezone = "I could not add the block rule to the tempchannel because the servers timezone is not found!"
response_edit_add_block_rule_failed_unknown_module_status = "I could not add the block rule to the tempchannel because I could not determine the status of the `tempchannels` module!"
response_edit_add_block_rule_failed_module_disabled = "I could not add the block rule to the tempchannel because the `tempchannels` module is disabled!"
response_edit_add_block_rule_failed_no_tempchannel_found = "I could not add the block rule to the tempchannel because I couldn't find a tempchannel with the given ID!"
response_edit_add_block_rule_failed_not_the_owner = (
    "I could not add the block rule to the tempchannel because you are not the owner!"
)
response_edit_add_block_rule_failed = (
    "Something went wrong while trying to add the block rule to the tempchannel!"
)
response_edit_add_block_rule_success = "The block rule has been added!"
