# Gmail node Label Operations documentation | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md "Edit this page")

# Gmail node Label Operations#

Use the Label operations to create, delete, or get a label or list labels in Gmail. Refer to the [Gmail node](../) for more information on the Gmail node itself.

## Create a label#

Use this operation to create a new label.

Enter these parameters:

  * Select the **Credential to connect with** or create a new one.
  * **Resource** : Select **Label**.
  * **Operation** : Select **Create**.
  * **Name** : Enter a display name for the label.

### Create label options#

Use these options to further refine the node's behavior:

  * **Label List Visibility** : Sets the visibility of the label in the label list in the Gmail web interface. Choose from:
    * **Hide** : Don't show the label in the label list.
    * **Show** (default): Show the label in the label list.
    * **Show if Unread** : Show the label if there are any unread messages with that label.
  * **Message List Visibility** : Sets the visibility of messages with this label in the message list in the Gmail web interface. Choose whether to **Show** or **Hide** messages with this label.

Refer to the [Gmail API Method: users.labels.create](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/create) documentation for more information.

## Delete a label#

Use this operation to delete an existing label.

Enter these parameters:

  * Select the **Credential to connect with** or create a new one.
  * **Resource** : Select **Label**.
  * **Operation** : Select **Delete**.
  * **Label ID** : Enter the ID of the label you want to delete.

Refer to the [Gmail API Method: users.labels.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/delete) documentation for more information.

## Get a label#

Use this operation to get an existing label.

Enter these parameters:

  * Select the **Credential to connect with** or create a new one.
  * **Resource** : Select **Label**.
  * **Operation** : Select **Get**.
  * **Label ID** : Enter the ID of the label you want to get.

Refer to the [Gmail API Method: users.labels.get](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/get) documentation for more information.

## Get Many labels#

Use this operation to get two or more labels.

Enter these parameters:

  * Select the **Credential to connect with** or create a new one.
  * **Resource** : Select **Label**.
  * **Operation** : Select **Get Many**.
  * **Return All** : Choose whether the node returns all labels (turned on) or only up to a set limit (turned off).
  * **Limit** : Enter the maximum number of labels to return. Only used if you've turned off **Return All**.

Refer to the [Gmail API Method: users.labels.list](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list) documentation for more information.

## Common issues#

For common errors or issues and suggested resolution steps, refer to [Common Issues](../common-issues/).

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top