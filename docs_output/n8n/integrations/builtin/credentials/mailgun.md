# Mailgun credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/mailgun.md "Edit this page")

# Mailgun credentials#

You can use these credentials to authenticate the following nodes:

  * [Mailgun](../../app-nodes/n8n-nodes-base.mailgun/)

## Prerequisites#

  * Create a [Mailgun](https://www.mailgun.com/) account.
  * [Add and verify a domain](https://help.mailgun.com/hc/en-us/articles/360026833053-Domain-Verification-Setup-Guide) in Mailgun or use the provided sandbox domain for testing.

## Supported authentication methods#

  * API key

## Related resources#

Refer to [Mailgun's API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/intro/) for more information about the service.

## Using API key#

To configure this credential, you'll need:

  * An **API Domain** : If your Mailgun account is based in Europe, select **api.eu.mailgun.net** ; otherwise, select **api.mailgun.net**. Refer to [Mailgun Base URLs](https://documentation.mailgun.com/docs/mailgun/api-reference/intro/#base-url) for more information.
  * An **Email Domain** : Enter the email sending domain you're working with. If you have multiple sending domains, refer to Working with multiple email domains for more information.
  * An **API Key** : View your API key in **Settings > API Keys**. Refer to [Mailgun's API Authentication documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/) for more detailed instructions.

## Working with multiple email domains#

If your Mailgun account includes multiple sending domains, create a separate credential for each email domain you're working with.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top