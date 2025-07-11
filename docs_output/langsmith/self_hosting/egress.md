# egress | 🦜️🛠️ LangSmith

On this page

Version Requirement

This section only applies to customers who are not running in offline mode and assumes you are using a self-hosted LangSmith instance serving version 0.9.0 or later. Previous versions of LangSmith did not have this feature.

Self-Hosted LangSmith instances store all information locally and will never send sensitive information outside of your network. We currently only track platform usage for billing purposes according to the entitlements in your order. In order to better remotely support our customers, we do require egress to `https://beacon.langchain.com`.

In the future, we will be introducing support diagnostics to help us ensure that the LangSmith platform is running at an optimal level within your environment.

Important

**This will require egress to`https://beacon.langchain.com` from your network.**

Generally, data that we send to Beacon can be categorized as follows:

  * Subscription Metrics
    * Subscription metrics are used to determine level of access and utilization of LangSmith. This includes, but are not limited to:
      * Number of traces
      * Seats allocated per contract
      * Seats in currently use
  * Operational Metadata
    * This metadata will contain and collect the above subscription metrics to assist with remote support, allowing the LangChain team to diagnose and troubleshoot performance issues more effectively and proactively.

## Example Payloads​

In an effort to maximize transparency, we provide sample payloads here:

### License Verification​

**Endpoint:**

`POST beacon.langchain.com/v1/beacon/verify`

**Request:**
    
    
    {  
      "license: "<YOUR_LICENSE_KEY>"  
    }  
    

**Response:**
    
    
    {  
      "token": "Valid JWT" //Short-lived JWT token to avoid repeated license checks  
    }  
    

### Usage Reporting​

**Endpoint:**

`POST beacon.langchain.com/v1/beacon/ingest-traces`

**Request:**
    
    
    {  
      "license": "<YOUR_LICENSE_KEY>",  
      "trace_transactions": [  
        {  
          "id": "af28dfea-5358-463d-a2dc-37df1da72498",  
          "tenant_id": "3a1c2b6f-4430-4b92-8a5b-79b8b567bbc1",  
          "session_id": "b26ae531-cdb3-42a5-8bcf-05355199fe27",  
          "trace_count": 5,  
          "start_insertion_time": "2025-01-06T10:00:00Z",  
          "end_insertion_time": "2025-01-06T11:00:00Z",  
          "start_interval_time": "2025-01-06T09:00:00Z",  
          "end_interval_time": "2025-01-06T10:00:00Z",  
          "status": "completed",  
          "num_failed_send_attempts": 0,  
          "transaction_type": "type1",  
          "organization_id": "c5b5f53a-4716-4326-8967-d4f7f7799735"  
        }  
      ]  
    }  
    

**Response:**
    
    
    {  
      "inserted_count": 1 //Number of transactions successfully ingested  
    }  
    

## Our Commitment​

LangChain will not store any sensitive information in the Subscription Metrics or Operational Metadata. Any data collected will not be shared with a third party. If you have any concerns about the data being sent, please reach out to your account team.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Example Payloads
    * License Verification
    * Usage Reporting
  * Our Commitment

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)