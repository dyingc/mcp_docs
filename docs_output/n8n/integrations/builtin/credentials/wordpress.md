# WordPress credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/wordpress.md "Edit this page")

# WordPress credentials#

You can use these credentials to authenticate the following nodes:

  * [WordPress](../../app-nodes/n8n-nodes-base.wordpress/)

## Prerequisites#

  * Create a [WordPress](https://wordpress.com/) account or deploy WordPress on a server.

## Supported authentication methods#

  * Basic auth

## Related resources#

Refer to [WordPress's API documentation](https://developer.wordpress.com/docs/api/) for more information about the service.

## Using basic auth#

To configure this credential, you'll need:

  * Your WordPress **Username**
  * A WordPress application **Password**
  * Your **WordPress URL**
  * Decide whether to **Ignore SSL Issues**

Using this credential involves three steps:

  1. Enable two-step authentication.
  2. Create an application password.
  3. Set up the credential.

Refer to the detailed instructions below for each step.

### Enable two-step authentication#

To generate an application password, you must first enable Two-Step Authentication in WordPress. If you've already done this, skip to the next section.

  1. Open your WordPress [profile](https://wordpress.com/me).
  2. Select **Security** from the left menu.
  3. Select **Two-Step Authentication**. The **Two-Step Authentication** page opens.
  4. If Two-Step Authentication isn't enabled, you must enable it.
  5. Choose whether to enable it using an authenticator app or SMS codes and follow the on-screen instructions.

Refer to WordPress's [Enable Two-Step Authentication](https://wordpress.com/support/security/two-step-authentication/) for detailed instructions.

### Create an application password#

With Two-Step Authentication enabled, you can now generate an application password:

  1. From the WordPress **Security >** [**Two-Step Authentication**](https://wordpress.com/me/security/two-step) page, select **\+ Add new application password** in the **Application passwords** section.
  2. Enter an **Application name** , like `n8n integration`.
  3. Select **Generate Password**.
  4. Copy the password it generates. You'll use this in your n8n credential.

### Set up the credential#

Congratulations! You're now ready to set up your n8n credential:

  1. Enter your WordPress **Username** in your n8n credential.
  2. Enter the application password you copied above as the **Password** in your n8n credential.
  3. Enter the URL of your WordPress site as the **WordPress URL**.
  4. Optional: Use the **Ignore SSL Issues** to choose whether you want the n8n credential to connect even if SSL certificate validation fails (turned on) or whether to respect SSL certificate validation (turned off).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top