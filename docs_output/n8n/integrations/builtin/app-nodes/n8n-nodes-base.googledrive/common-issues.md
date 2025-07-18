# Google Drive node common issues | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md "Edit this page")

# Google Drive node common issues#

Here are some common errors and issues with the [Google Drive node](../) and steps to resolve or troubleshoot them.

## Google hasn't verified this app#

If using the OAuth authentication method, you might see the warning **Google hasn't verified this app**. To avoid this, you can create OAuth credentials from the same account you want to authenticate. 

If you need to use credentials generated by another account (by a developer or another third party), follow the instructions in [Google Cloud documentation | Authorization errors: Google hasn't verified this app](https://developers.google.com/nest/device-access/reference/errors/authorization#google_hasnt_verified_this_app).

## Google Cloud app becoming unauthorized#

For Google Cloud apps with **Publishing status** set to **Testing** and **User type** set to **External** , consent and tokens expire after seven days. Refer to [Google Cloud Platform Console Help | Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615?hl=en#zippy=%2Ctesting) for more information. To resolve this, reconnect the app in the n8n credentials modal.

## Google Drive OAuth error#

If using the OAuth authentication method, you may see an error indicating that you can't sign in because the app doesn't meet Google's expectations for keeping apps secure.

Most often, the actual cause of this issue is that the URLs don't match between Google's OAuth configuration and n8n. To avoid this, start by reviewing any links included in Google's error message. This will contain details about the exact error that occurred.

If you are self-hostin n8n, check the n8n configuration items used to construct external URLs. Verify that the [`N8N_EDITOR_BASE_URL`](../../../../../hosting/configuration/environment-variables/deployment/) and [`WEBHOOK_URL`](../../../../../hosting/configuration/configuration-examples/webhook-url/) environment variables use fully qualified domains.

## Get recent files from Google Drive#

To retrieve recent files from Google Drive, you need to sort files by modification time. To do this, you need to search for existing files and retrieve their modification times. Next you can sort the files to find the most recent file and use another Google Drive node target the file by ID.

The process looks like this:

  1. Add a **Google Drive** node to your canvas.
  2. Select the **File/Folder** resource and the **Search** operation.
  3. Enable **Return All** to sort through all files.
  4. Set the **What to Search** filter to **Files**.
  5. In the **Options** , set the **Fields** to **All**.
  6. Connect a **Sort** node to the output of the **Google Drive** node.
  7. Choose **Simple** sort type.
  8. Enter `modifiedTime` as the **Field Name** in the **Fields To Sort By** section.
  9. Choose **Descending** sort order.
  10. Add a **Limit** node to the output of the **Sort** node.
  11. Set **Max Items** to **1** to keep the most recent file.
  12. Connect another **Google Drive** node to the output of the **Limit** node.
  13. Select **File** as the **Resource** and the operation of your choice.
  14. In the **File** selection, choose **By ID**.
  15. Select **Expression** and enter `{{ $json.id }}` as the expression.

[View workflow file](/_workflows/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/get-most-recent-file.json)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top