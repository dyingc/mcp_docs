# User management SMTP, and two-factor authentication environment variables | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/configuration/environment-variables/user-management-smtp-2fa.md "Edit this page")

# User management SMTP, and two-factor authentication environment variables#

File-based configuration

You can add `_FILE` to individual variables to provide their configuration in a separate file. Refer to [Keeping sensitive data in separate files](../../configuration-methods/#keeping-sensitive-data-in-separate-files) for more details.

Refer to [User management](../../user-management-self-hosted/) for more information on setting up user management and emails.

Variable | Type | Default | Description  
---|---|---|---  
`N8N_EMAIL_MODE` | String | `smtp` | Enable emails.  
`N8N_SMTP_HOST` | String | - | _your_SMTP_server_name_  
`N8N_SMTP_PORT` | Number | - | _your_SMTP_server_port_  
`N8N_SMTP_USER` | String | - | _your_SMTP_username_  
`N8N_SMTP_PASS` | String | - | _your_SMTP_password_  
`N8N_SMTP_OAUTH_SERVICE_CLIENT` | String | - | If using 2LO with a service account this is your client ID  
`N8N_SMTP_OAUTH_PRIVATE_KEY` | String | - | If using 2LO with a service account this is your private key  
`N8N_SMTP_SENDER` | String | - | Sender email address. You can optionally include the sender name. Example with name: _N8N`<contact@n8n.com>`_  
`N8N_SMTP_SSL` | Boolean | `true` | Whether to use SSL for SMTP (true) or not (false).  
`N8N_SMTP_STARTTLS` | Boolean | `true` | Whether to use STARTTLS for SMTP (true) or not (false).  
`N8N_UM_EMAIL_TEMPLATES_INVITE` | String | - | Full path to your HTML email template. This overrides the default template for invite emails.  
`N8N_UM_EMAIL_TEMPLATES_PWRESET` | String | - | Full path to your HTML email template. This overrides the default template for password reset emails.  
`N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | - | Overrides the default HTML template for notifying users that a workflow was shared. Provide the full path to the template.  
`N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | - | Overrides the default HTML template for notifying users that a credential was shared. Provide the full path to the template.  
`N8N_USER_MANAGEMENT_JWT_SECRET` | String | - | Set a specific JWT secret. By default, n8n generates one on start.  
`N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` | Number | 168 | Set an expiration date for the JWTs in hours.  
`N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS` | Number | 0 | How many hours before the JWT expires to automatically refresh it. 0 means 25% of `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS`. -1 means it will never refresh, which forces users to log in again after the period defined in `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS`.  
`N8N_MFA_ENABLED` | Boolean | `true` | Whether to enable two-factor authentication (true) or disable (false). n8n ignores this if existing users have 2FA enabled.  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top