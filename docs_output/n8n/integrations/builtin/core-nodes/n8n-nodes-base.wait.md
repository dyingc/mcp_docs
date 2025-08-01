# Wait | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.wait.md "Edit this page")

# Wait#

Use the Wait node pause your workflow's execution. When the workflow pauses it offloads the execution data to the database. When the resume condition is met, the workflow reloads the data and the execution continues.

## Operations#

The Wait node can **Resume** on the following conditions:

  * **After Time Interval**: The node waits for a certain amount of time.
  * **At Specified Time**: The node waits until a specific time.
  * **On Webhook Call**: The node waits until it receives an HTTP call.
  * **On Form Submitted**: The node waits until it receives a form submission.

Refer to the more detailed sections below for more detailed instructions.

### After Time Interval#

Wait for a certain amount of time.

This parameter includes two more fields:

  * **Wait Amount** : Enter the amount of time to wait.
  * **Wait Unit** : Select the unit of measure for the **Wait Amount**. Choose from:
    * **Seconds**
    * **Minutes**
    * **Hours**
    * **Days**

Refer to Time-based operations for more detail on how these intervals work and the timezone used.

### At Specified Time#

Wait until a specific date and time to continue. Use the date and time picker to set the **Date and Time**.

Refer to Time-based operations for more detail on the timezone used.

### On Webhook Call#

This parameter enables your workflows to resume when the Wait node receives an HTTP call.

The webhook URL that resumes the execution when called is generated at runtime. The Wait node provides the `$execution.resumeUrl` variable so that you can reference and send the yet-to-be-generated URL wherever needed, for example to a third-party service or in an email. 

When the workflow executes, the Wait node generates the resume URL and the webhook(s) in your workflow using the `$execution.resumeUrl`. This generated URL is unique to each execution, so your workflow can contain multiple Wait nodes and as the webhook URL is called it will resume each Wait node sequentially.

For this **Resume** style, set more parameters listed below.

#### Authentication#

Select if and how incoming resume-webhook-requests to `$execution.resumeUrl` should be authenticated. Options include:

  * **Basic Auth** : Use basic authentication. Select or enter a new **Credential for Basic Auth** to use.
  * **Header Auth** : Use header authentication. Select or enter a new **Credential for Header Auth** to use.
  * **JWT Auth** : Use JWT authentication. Select or enter a new **Credential for JWT Auth** to use.
  * **None** : Don't use authentication.

Auth reference

Refer to the [Webhook node | Authentication documentation](../n8n-nodes-base.webhook/#supported-authentication-methods) for more information on each auth type.

#### HTTP Method#

Select the HTTP method the webhook should use. Refer to the [Webhook node | HTTP Method documentation](../n8n-nodes-base.webhook/#http-method) for more information.

#### Response Code#

Enter the Response Code the webhook should return. You can use common codes or enter a custom code.

#### Respond#

Set when and how to respond to the webhook from these options:

  * **Immediately** : Respond as soon as the node executes.
  * **When Last Node Finishes** : Return the response code and the data output from the last node executed in the workflow. If you select this option, also set:
    * **Response Data** : Select what data should be returned and what format to use. Options include:
      * **All Entries** : Returns all the entries of the last node in an array.
      * **First Entry JSON** : Return the JSON data of the first entry of the last node in a JSON object.
      * **First Entry Binary** : Return the binary data of the first entry of the last node in a binary file.
      * **No Response Body** : Return with no body.
  * **Using 'Respond to Webhook' Node** : Respond as defined in the [Respond to Webhook](../n8n-nodes-base.respondtowebhook/) node.

#### Limit Wait Time#

Set whether the workflow will automatically resume execution after a specific limit type (turned on) or not (turned off). If turned on, also set:

  * **Limit Type** : Select what type of limit to enforce from these options:
    * **After Time Interval** : Wait for a certain amount of time.
      * Enter the limit's **Amount** of time.
      * Select the limit's **Unit** of time.
    * **At Specified Time** : Wait until a specific date and time to resume.
      * **Max Date and Time** : Use the date and time picker to set the specified time the node should resume.

#### On Webhook Call options#

  * **Binary Property** : Enter the name of the binary property to write the data of the received file to. This option's only relevant if binary data is received.
  * **Ignore Bots** : Set whether to ignore requests from bots like link previewers and web crawlers (turned on) or not (turned off).
  * **IP(s) Whitelist** : Enter IP addresses here to limit who (or what) can invoke the webhook URL. Enter a comma-separated list of allowed IP addresses. Access from IPs outside the whitelist throws a 403 error. If left blank, all IP addresses can invoke the webhook URL.
  * **No Response Body** : Set whether n8n should send a body in the response (turned off) or prevent n8n from sending a body in the response (turned on).
  * **Raw Body** : Set whether to return the body in a raw format like JSON or XML (turned on) or not (turned off).
  * **Response Data** : Enter any custom data you want to send in the response.
  * **Response Headers** : Send more headers in the webhook response. Refer to [MDN Web Docs | Response header](https://developer.mozilla.org/en-US/docs/Glossary/Response_header) to learn more about response headers.
  * **Webhook Suffix** : Enter a suffix to append to the resume URL. This is useful for creating unique webhook URLs for each Wait node when a workflow contains multiple Wait nodes. Note that the generated `$resumeWebhookUrl` won't automatically include this suffix, you must manually append it to the webhook URL before exposing it.

#### On Webhook Call limitations#

There are some limitations to keep in mind when using On Webhook Call:

  * Partial executions of your workflow changes the `$resumeWebhookUrl`, so be sure that the node sending this URL to your desired third-party runs in the same execution as the Wait node.

### On Form Submitted#

Wait for a form submission before continuing. Set up these parameters:

#### Form Title#

Enter the title to display at the top of the form.

#### Form Description#

Enter a form description to display beneath the title. This description can help prompt the user on how to complete the form.

#### Form Fields#

Set up each field you want to appear on your form using these parameters:

  * **Field Label** : Enter the field label you want to appear in the form.
  * **Field Type** : Select the type of field to display in the form. Choose from:
    * **Date**
    * **Dropdown List** : Enter each dropdown options in the **Field Options**.
      * **Multiple Choice** : Select whether the user can select a single dropdown option (turned off) or multiple dropdown options (turned on)
    * **Number**
    * **Password**
    * **Text**
    * **Textarea**
  * **Required Field** : Set whether the user must complete this field in order to submit the form (turned on) or if the user can submit the form without completing it (turned off).

#### Respond When#

Set when to respond to the form submission. Choose from:

  * **Form Is Submitted** : Respond as soon as this node receives the form submission.
  * **Workflow Finishes** : Respond when the last node of this workflow finishes.
  * **Using 'Respond to Webhook' Node** : Respond when the [Respond to Webhook](../n8n-nodes-base.respondtowebhook/) node executes.

#### Limit Wait Time#

Set whether the workflow will automatically resume execution after a specific limit type (turned on) or not (turned off).

If turned on, also set: * **Limit Type** : Select what type of limit to enforce from these options: * **After Time Interval** : Wait for a certain amount of time. * Enter the limit's **Amount** of time. * Select the limit's **Unit** of time. * **At Specified Time** : Wait until a specific date and time to resume. * **Max Date and Time** : Use the date and time picker to set the specified time the node should resume.

#### On Form Response options#

  * **Form Response** : Choose how and what you want the form to **Respond With** from these options:
    * **Form Submitted Text** : The form displays whatever text is entered in **Text to Show** after a user fills out the form. Use this option if you want to display a confirmation message.
    * **Redirect URL** : The form will redirect the user to the **URL to Redirect to** after they fill out the form. This must be a valid URL.
  * **Webhook Suffix** : Enter a suffix to append to the resume URL. This is useful for creating unique webhook URLs for each Wait node when a workflow contains multiple Wait nodes. Note that the generated `$resumeWebhookUrl` won't automatically include this suffix, you must manually append it to the webhook URL before exposing it.

## Templates and examples#

**Scrape business emails from Google Maps without the use of any third party APIs**

by Akram Kadri

[View template details](https://n8n.io/workflows/2567-scrape-business-emails-from-google-maps-without-the-use-of-any-third-party-apis/)

**Fully Automated AI Video Generation & Multi-Platform Publishing**

by Juan Carlos Cavero Gracia

[View template details](https://n8n.io/workflows/3442-fully-automated-ai-video-generation-and-multi-platform-publishing/)

**Respond to WhatsApp Messages with AI Like a Pro!**

by Jimleuk

[View template details](https://n8n.io/workflows/2466-respond-to-whatsapp-messages-with-ai-like-a-pro/)

[Browse Wait integration templates](https://n8n.io/integrations/wait/), or [search all templates](https://n8n.io/workflows/)

## Time-based operations#

For the time-based resume operations, note that:

  * For wait times less than 65 seconds, the workflow doesn't offload execution data to the database. Instead, the process continues to run and the execution resumes after the specified interval passes.
  * The n8n server time is always used regardless of the timezone setting. Workflow timezone settings, and any changes made to them, don't affect the Wait node interval or specified time. 

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top