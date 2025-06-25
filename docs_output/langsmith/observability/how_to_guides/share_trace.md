# Share or unshare a trace publicly | 🦜️🛠️ LangSmith

caution

Sharing a trace publicly will make it accessible to anyone with the link. Make sure you're not sharing sensitive information.

If your self-hosted or hybrid LangSmith deployment is within a VPC, then the public link is accessible only to members authenticated within your VPC. For enhanced security, we recommend configuring your instance with a private URL accessible only to users with access to your network.

To share a trace publicly, simply click on the **Share** button in the upper right hand side of any trace view. ![](/assets/images/share_trace-15a34368c102d00cc213dd6608935fcc.png)

This will open a dialog where you can copy the link to the trace.

Shared traces will be accessible to anyone with the link, even if they don't have a LangSmith account. They will be able to view the trace, but not edit it.

To "unshare" a trace, either

  1. Click on **Unshare** by click on **Public** in the upper right hand corner of any publicly shared trace, then **Unshare** in the dialog. ![](/assets/images/unshare_trace-9e00bf94f8b9056b2676a2f4dd5ae661.png)

  2. Navigate to your organization's list of publicly shared traces, either by clicking on **Settings** -> **Shared URLs** or [this link](https://smith.langchain.com/settings/shared), then click on **Unshare** next to the trace you want to unshare. ![](/assets/images/unshare_trace_list-2c9ae0fc85ad285b0620ab08d128f79b.png)

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)