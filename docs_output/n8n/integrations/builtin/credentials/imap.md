# IMAP credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/imap/index.md "Edit this page")

# IMAP credentials#

You can use these credentials to authenticate the following nodes:

  * [IMAP Email](../../core-nodes/n8n-nodes-base.emailimap/)

## Prerequisites#

Create an email account on a service with IMAP support.

## Supported authentication methods#

  * User account

## Related resources#

Internet Message Access Protocol (IMAP) is a standard protocol for receiving email. Most email providers offer instructions on setting up their service with IMAP; refer to your provider's IMAP instructions.

## Using user account#

To configure this credential, you'll need:

  * A **User** name: The email address you're retrieving email for.
  * A **Password** : Either the password you use to check email or an app password. Your provider will tell you whether to use your own password or to generate an app password.
  * A **Host** : The IMAP host address for your email provider, often formatted as `imap.<provider>.com`. Check with your provider.
  * A **Port** number: The default is port `993`. Use this port unless your provider or email administrator tells you to use something different.

Choose whether to use **SSL/TLS** and whether to **Allow Self-Signed Certificates**.

### Provider instructions#

Refer to the quickstart guides for these common email providers.

#### Gmail#

Refer to [Gmail](gmail/).

#### Outlook.com#

Refer to [Outlook.com](outlook/).

#### Yahoo#

Refer to [Yahoo](yahoo/).

### My provider isn't listed#

If your email provider isn't listed here, search for their `IMAP settings` or `IMAP instructions`.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top