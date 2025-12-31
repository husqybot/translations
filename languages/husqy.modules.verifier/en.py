# MODULE VERIFIER
removed_user = "(removed_user)"
module_verifier_default_verify_click_to_pass_label = "Click to verify"  # noqa: S105
module_verifier_default_verify_passphrase_label = "Enter passphrase"  # noqa: S105
module_verifier_default_verify_web_label = "Verify on web"
module_verifier_default_content = """{
  "embeds": [
    {
      "title": "Please verify yourself!",
      "description": "In order to join <server_name> they have required verification of new members. Please verify yourself using the actions below.",
      "color": 661809
    }
  ]
}"""
module_verifier_default_content_completed = """{
  "embeds": [
    {
      "title": "Verification completed!",
      "description": "Thank you for completing the verification. Enjoy the stay in <server_name>.",
      "color": 661809
    }
  ]
}"""
module_verifier_passphrase_form_title = "Enter the passphrase"  # noqa: S105
module_verifier_passphrase_form_passphrase_label = "Passphrase:"  # noqa: S105
response_verification_created = "The verification entry has been created!"
response_verification_creation_failed = "Creating the verification entry has failed!"
response_verification_creation_failed_no_language = (
    "Unable to create verification entry because the servers language is unknown!"
)
response_verification_creation_failed_no_timezone = (
    "Unable to create verification entry because the servers timezone is unknown!"
)
response_verification_creation_failed_no_auto_delete = (
    "Unable to create verification entry because the servers auto delete is unknown!"
)
response_verification_failed_not_administrator = (
    "Creating the verification entry has failed, you do not have administrator permissions!"
)
