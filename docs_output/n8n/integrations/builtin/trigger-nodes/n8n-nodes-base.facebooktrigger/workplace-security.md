# Facebook Trigger Workplace Security object documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md "Edit this page")

# Facebook Trigger Workplace Security object#

Use this object to receive updates when Workplace security events occur, like adding or removing admins, users joining or leaving a Workplace, and more. Refer to [Facebook Trigger](../) for more information on the trigger itself.

Credentials

You can find authentication information for this node [here](../../../credentials/facebookapp/).

Examples and templates

For usage examples and templates to help you get started, refer to n8n's [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/) page.

## Trigger configuration#

To configure the trigger with this Object:

  1. Select the **Credential to connect with**. Select an existing or create a new [Facebook App credential](../../../credentials/facebookapp/).
  2. Enter the **APP ID** of the app connected to your credential. Refer to the [Facebook App credential](../../../credentials/facebookapp/) documentation for more information.
  3. Select **Workplace Security** as the **Object**.
  4. **Field Names or IDs** : By default, the node will trigger on all the available events using the `*` wildcard filter. If you'd like to limit the events, use the `X` to remove the star and use the dropdown or an expression to select the updates you're interested in.
  5. In **Options** , turn on the toggle to **Include Values**. This Object type fails without the option enabled.

## Related resources#

Refer to Meta's [Security](https://developers.facebook.com/docs/workplace/reference/webhooks/#security) Workplace API reference for more information.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top