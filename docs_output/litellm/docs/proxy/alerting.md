# Alerting / Webhooks | liteLLM

On this page

Get alerts for:

Category| Alert Type  
---|---  
**LLM Performance**|  Hanging API calls, Slow API calls, Failed API calls, Model outage alerting  
**Budget & Spend**| Budget tracking per key/user, Soft budget alerts, Weekly & Monthly spend reports per Team/Tag  
**System Health**|  Failed database read/writes  
**Daily Reports**|  Top 5 slowest LLM deployments, Top 5 LLM deployments with most failed requests, Weekly & Monthly spend per Team/Tag  
  
Works across:

  * Slack
  * Discord
  * Microsoft Teams

## Quick Start​

Set up a slack alert channel to receive alerts from proxy.

### Step 1: Add a Slack Webhook URL to env​

Get a slack webhook url from <https://api.slack.com/messaging/webhooks>

You can also use Discord Webhooks, see here

Set `SLACK_WEBHOOK_URL` in your proxy env to enable Slack alerts.
    
    
    export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/<>/<>/<>"  
    

### Step 2: Setup Proxy​
    
    
    general_settings:   
        alerting: ["slack"]  
        alerting_threshold: 300 # sends alerts if requests hang for 5min+ and responses take 5min+   
        spend_report_frequency: "1d" # [Optional] set as 1d, 2d, 30d .... Specify how often you want a Spend Report to be sent  
          
        # [OPTIONAL ALERTING ARGS]  
        alerting_args:  
            daily_report_frequency: 43200  # 12 hours in seconds  
            report_check_interval: 3600    # 1 hour in seconds  
            budget_alert_ttl: 86400        # 24 hours in seconds  
            outage_alert_ttl: 60           # 1 minute in seconds  
            region_outage_alert_ttl: 60    # 1 minute in seconds  
            minor_outage_alert_threshold: 5   
            major_outage_alert_threshold: 10  
            max_outage_alert_list_size: 1000  
            log_to_console: false  
          
    

Start proxy
    
    
    $ litellm --config /path/to/config.yaml  
    

### Step 3: Test it!​
    
    
    curl -X GET 'http://0.0.0.0:4000/health/services?service=slack' \  
    -H 'Authorization: Bearer sk-1234'  
    

## Advanced​

### Redacting Messages from Alerts​

By default alerts show the `messages/input` passed to the LLM. If you want to redact this from slack alerting set the following setting on your config
    
    
    general_settings:  
      alerting: ["slack"]  
      alert_types: ["spend_reports"]   
      
    litellm_settings:  
      redact_messages_in_exceptions: True  
    

### Soft Budget Alerts for Virtual Keys​

Use this to send an alert when a key/team is close to it's budget running out

Step 1. Create a virtual key with a soft budget

Set the `soft_budget` to 0.001
    
    
    curl -X 'POST' \  
      'http://localhost:4000/key/generate' \  
      -H 'accept: application/json' \  
      -H 'x-goog-api-key: sk-1234' \  
      -H 'Content-Type: application/json' \  
      -d '{  
      "key_alias": "prod-app1",  
      "team_id": "113c1a22-e347-4506-bfb2-b320230ea414",  
      "soft_budget": 0.001  
    }'  
    

Step 2. Send a request to the proxy with the virtual key
    
    
    curl http://0.0.0.0:4000/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer sk-Nb5eCf427iewOlbxXIH4Ow" \  
    -d '{  
      "model": "openai/gpt-4",  
      "messages": [  
        {  
          "role": "user",  
          "content": "this is a test request, write a short poem"  
        }  
      ]  
    }'  
      
    

Step 3. Check slack for Expected Alert

### Add Metadata to alerts​

Add alerting metadata to proxy calls for debugging.
    
    
    import openai  
    client = openai.OpenAI(  
        api_key="anything",  
        base_url="http://0.0.0.0:4000"  
    )  
      
    # request sent to model set on litellm proxy, `litellm --model`  
    response = client.chat.completions.create(  
        model="gpt-4o",  
        messages = [],   
        extra_body={  
            "metadata": {  
                "alerting_metadata": {  
                    "hello": "world"  
                }  
            }  
        }  
    )  
    

**Expected Response**

### Select specific alert types​

Set `alert_types` if you want to Opt into only specific alert types. When alert_types is not set, all Default Alert Types are enabled.

👉 **See all alert types here**
    
    
    general_settings:  
      alerting: ["slack"]  
      alert_types: [  
        "llm_exceptions",  
        "llm_too_slow",  
        "llm_requests_hanging",  
        "budget_alerts",  
        "spend_reports",  
        "db_exceptions",  
        "daily_reports",  
        "cooldown_deployment",  
        "new_model_added",  
      ]   
    

### Map slack channels to alert type​

Use this if you want to set specific channels per alert type

**This allows you to do the following**
    
    
    llm_exceptions -> go to slack channel #llm-exceptions  
    spend_reports -> go to slack channel #llm-spend-reports  
    

Set `alert_to_webhook_url` on your config.yaml

  * 1 channel per alert
  * multiple channels per alert

    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    general_settings:   
      master_key: sk-1234  
      alerting: ["slack"]  
      alerting_threshold: 0.0001 # (Seconds) set an artificially low threshold for testing alerting  
      alert_to_webhook_url: {  
        "llm_exceptions": "https://hooks.slack.com/services/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",  
        "llm_too_slow": "https://hooks.slack.com/services/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",  
        "llm_requests_hanging": "https://hooks.slack.com/services/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",  
        "budget_alerts": "https://hooks.slack.com/services/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",  
        "db_exceptions": "https://hooks.slack.com/services/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",  
        "daily_reports": "https://hooks.slack.com/services/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",  
        "spend_reports": "https://hooks.slack.com/services/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",  
        "cooldown_deployment": "https://hooks.slack.com/services/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",  
        "new_model_added": "https://hooks.slack.com/services/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",  
        "outage_alerts": "https://hooks.slack.com/services/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",  
      }  
      
    litellm_settings:  
      success_callback: ["langfuse"]  
    

Provide multiple slack channels for a given alert type
    
    
    model_list:  
      - model_name: gpt-4  
        litellm_params:  
          model: openai/fake  
          api_key: fake-key  
          api_base: https://exampleopenaiendpoint-production.up.railway.app/  
      
    general_settings:   
      master_key: sk-1234  
      alerting: ["slack"]  
      alerting_threshold: 0.0001 # (Seconds) set an artificially low threshold for testing alerting  
      alert_to_webhook_url: {  
        "llm_exceptions": ["os.environ/SLACK_WEBHOOK_URL", "os.environ/SLACK_WEBHOOK_URL_2"],  
        "llm_too_slow": ["https://webhook.site/7843a980-a494-4967-80fb-d502dbc16886", "https://webhook.site/28cfb179-f4fb-4408-8129-729ff55cf213"],  
        "llm_requests_hanging": ["os.environ/SLACK_WEBHOOK_URL_5", "os.environ/SLACK_WEBHOOK_URL_6"],  
        "budget_alerts": ["os.environ/SLACK_WEBHOOK_URL_7", "os.environ/SLACK_WEBHOOK_URL_8"],  
        "db_exceptions": ["os.environ/SLACK_WEBHOOK_URL_9", "os.environ/SLACK_WEBHOOK_URL_10"],  
        "daily_reports": ["os.environ/SLACK_WEBHOOK_URL_11", "os.environ/SLACK_WEBHOOK_URL_12"],  
        "spend_reports": ["os.environ/SLACK_WEBHOOK_URL_13", "os.environ/SLACK_WEBHOOK_URL_14"],  
        "cooldown_deployment": ["os.environ/SLACK_WEBHOOK_URL_15", "os.environ/SLACK_WEBHOOK_URL_16"],  
        "new_model_added": ["os.environ/SLACK_WEBHOOK_URL_17", "os.environ/SLACK_WEBHOOK_URL_18"],  
        "outage_alerts": ["os.environ/SLACK_WEBHOOK_URL_19", "os.environ/SLACK_WEBHOOK_URL_20"],  
      }  
      
    litellm_settings:  
      success_callback: ["langfuse"]  
    

Test it - send a valid llm request - expect to see a `llm_too_slow` alert in it's own slack channel
    
    
    curl -i http://localhost:4000/v1/chat/completions \  
      -H "Content-Type: application/json" \  
      -H "Authorization: Bearer sk-1234" \  
      -d '{  
        "model": "gpt-4",  
        "messages": [  
          {"role": "user", "content": "Hello, Claude gm!"}  
        ]  
    }'  
    

### MS Teams Webhooks​

MS Teams provides a slack compatible webhook url that you can use for alerting

##### Quick Start​

  1. [Get a webhook url](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=newteams%2Cdotnet#create-an-incoming-webhook) for your Microsoft Teams channel

  2. Add it to your .env

    
    
    SLACK_WEBHOOK_URL="https://berriai.webhook.office.com/webhookb2/...6901/IncomingWebhook/b55fa0c2a48647be8e6effedcd540266/e04b1092-4a3e-44a2-ab6b-29a0a4854d1d"  
    

  3. Add it to your litellm config

    
    
    model_list:   
        model_name: "azure-model"  
        litellm_params:  
            model: "azure/gpt-35-turbo"  
            api_key: "my-bad-key" # 👈 bad key  
      
    general_settings:   
        alerting: ["slack"]  
        alerting_threshold: 300 # sends alerts if requests hang for 5min+ and responses take 5min+   
    

  4. Run health check!

Call the proxy `/health/services` endpoint to test if your alerting connection is correctly setup.
    
    
    curl --location 'http://0.0.0.0:4000/health/services?service=slack' \  
    --header 'Authorization: Bearer sk-1234'  
    

**Expected Response**

### Discord Webhooks​

Discord provides a slack compatible webhook url that you can use for alerting

##### Quick Start​

  1. Get a webhook url for your discord channel

  2. Append `/slack` to your discord webhook - it should look like

    
    
    "https://discord.com/api/webhooks/1240030362193760286/cTLWt5ATn1gKmcy_982rl5xmYHsrM1IWJdmCL1AyOmU9JdQXazrp8L1_PYgUtgxj8x4f/slack"  
    

  3. Add it to your litellm config

    
    
    model_list:   
        model_name: "azure-model"  
        litellm_params:  
            model: "azure/gpt-35-turbo"  
            api_key: "my-bad-key" # 👈 bad key  
      
    general_settings:   
        alerting: ["slack"]  
        alerting_threshold: 300 # sends alerts if requests hang for 5min+ and responses take 5min+   
      
    environment_variables:  
        SLACK_WEBHOOK_URL: "https://discord.com/api/webhooks/1240030362193760286/cTLWt5ATn1gKmcy_982rl5xmYHsrM1IWJdmCL1AyOmU9JdQXazrp8L1_PYgUtgxj8x4f/slack"  
    

## [BETA] Webhooks for Budget Alerts​

**Note** : This is a beta feature, so the spec might change.

Set a webhook to get notified for budget alerts.

  1. Setup config.yaml

Add url to your environment, for testing you can use a link from [here](https://webhook.site/)
    
    
    export WEBHOOK_URL="https://webhook.site/6ab090e8-c55f-4a23-b075-3209f5c57906"  
    

Add 'webhook' to config.yaml
    
    
    general_settings:   
      alerting: ["webhook"] # 👈 KEY CHANGE  
    

  2. Start proxy

    
    
    litellm --config /path/to/config.yaml  
      
    # RUNNING on http://0.0.0.0:4000  
    

  3. Test it!

    
    
    curl -X GET --location 'http://0.0.0.0:4000/health/services?service=webhook' \  
    --header 'Authorization: Bearer sk-1234'  
    

**Expected Response**
    
    
    {  
      "spend": 1, # the spend for the 'event_group'  
      "max_budget": 0, # the 'max_budget' set for the 'event_group'  
      "token": "88dc28d0f030c55ed4ab77ed8faf098196cb1c05df778539800c9f1243fe6b4b",  
      "user_id": "default_user_id",  
      "team_id": null,  
      "user_email": null,  
      "key_alias": null,  
      "projected_exceeded_data": null,  
      "projected_spend": null,  
      "event": "budget_crossed", # Literal["budget_crossed", "threshold_crossed", "projected_limit_exceeded"]  
      "event_group": "user",  
      "event_message": "User Budget: Budget Crossed"  
    }  
    

### API Spec for Webhook Event​

  * `spend` _float_ : The current spend amount for the 'event_group'.

  * `max_budget` _float or null_ : The maximum allowed budget for the 'event_group'. null if not set.

  * `token` _str_ : A hashed value of the key, used for authentication or identification purposes.

  * `customer_id` _str or null_ : The ID of the customer associated with the event (optional).

  * `internal_user_id` _str or null_ : The ID of the internal user associated with the event (optional).

  * `team_id` _str or null_ : The ID of the team associated with the event (optional).

  * `user_email` _str or null_ : The email of the internal user associated with the event (optional).

  * `key_alias` _str or null_ : An alias for the key associated with the event (optional).

  * `projected_exceeded_date` _str or null_ : The date when the budget is projected to be exceeded, returned when 'soft_budget' is set for key (optional).

  * `projected_spend` _float or null_ : The projected spend amount, returned when 'soft_budget' is set for key (optional).

  * `event` _Literal["budget_crossed", "threshold_crossed", "projected_limit_exceeded"]_ : The type of event that triggered the webhook. Possible values are:

    * "spend_tracked": Emitted whenever spend is tracked for a customer id.
    * "budget_crossed": Indicates that the spend has exceeded the max budget.
    * "threshold_crossed": Indicates that spend has crossed a threshold (currently sent when 85% and 95% of budget is reached).
    * "projected_limit_exceeded": For "key" only - Indicates that the projected spend is expected to exceed the soft budget threshold.
  * `event_group` _Literal["customer", "internal_user", "key", "team", "proxy"]_ : The group associated with the event. Possible values are:

    * "customer": The event is related to a specific customer
    * "internal_user": The event is related to a specific internal user.
    * "key": The event is related to a specific key.
    * "team": The event is related to a team.
    * "proxy": The event is related to a proxy.
  * `event_message` _str_ : A human-readable description of the event.

## Region-outage alerting (✨ Enterprise feature)​

info

[Get a free 2-week license](https://forms.gle/P518LXsAZ7PhXpDn8)

Setup alerts if a provider region is having an outage.
    
    
    general_settings:  
        alerting: ["slack"]  
        alert_types: ["region_outage_alerts"]   
    

By default this will trigger if multiple models in a region fail 5+ requests in 1 minute. '400' status code errors are not counted (i.e. BadRequestErrors).

Control thresholds with:
    
    
    general_settings:  
        alerting: ["slack"]  
        alert_types: ["region_outage_alerts"]   
        alerting_args:  
            region_outage_alert_ttl: 60 # time-window in seconds  
            minor_outage_alert_threshold: 5 # number of errors to trigger a minor alert  
            major_outage_alert_threshold: 10 # number of errors to trigger a major alert  
    

## **All Possible Alert Types**​

👉 **Here is how you can set specific alert types**

LLM-related Alerts

Alert Type| Description| Default On  
---|---|---  
`llm_exceptions`| Alerts for LLM API exceptions| ✅  
`llm_too_slow`| Notifications for LLM responses slower than the set threshold| ✅  
`llm_requests_hanging`| Alerts for LLM requests that are not completing| ✅  
`cooldown_deployment`| Alerts when a deployment is put into cooldown| ✅  
`new_model_added`| Notifications when a new model is added to litellm proxy through /model/new| ✅  
`outage_alerts`| Alerts when a specific LLM deployment is facing an outage| ✅  
`region_outage_alerts`| Alerts when a specific LLM region is facing an outage. Example us-east-1| ✅  
  
Budget and Spend Alerts

Alert Type| Description| Default On  
---|---|---  
`budget_alerts`| Notifications related to budget limits or thresholds| ✅  
`spend_reports`| Periodic reports on spending across teams or tags| ✅  
`failed_tracking_spend`| Alerts when spend tracking fails| ✅  
`daily_reports`| Daily Spend reports| ✅  
`fallback_reports`| Weekly Reports on LLM fallback occurrences| ✅  
  
Database Alerts

Alert Type| Description| Default On  
---|---|---  
`db_exceptions`| Notifications for database-related exceptions| ✅  
  
Management Endpoint Alerts - Virtual Key, Team, Internal User

Alert Type| Description| Default On  
---|---|---  
`new_virtual_key_created`| Notifications when a new virtual key is created| ❌  
`virtual_key_updated`| Alerts when a virtual key is modified| ❌  
`virtual_key_deleted`| Notifications when a virtual key is removed| ❌  
`new_team_created`| Alerts for the creation of a new team| ❌  
`team_updated`| Notifications when team details are modified| ❌  
`team_deleted`| Alerts when a team is deleted| ❌  
`new_internal_user_created`| Notifications for new internal user accounts| ❌  
`internal_user_updated`| Alerts when an internal user's details are changed| ❌  
`internal_user_deleted`| Notifications when an internal user account is removed| ❌  
  
## `alerting_args` Specification​

Parameter| Default| Description  
---|---|---  
`daily_report_frequency`| 43200 (12 hours)| Frequency of receiving deployment latency/failure reports in seconds  
`report_check_interval`| 3600 (1 hour)| How often to check if a report should be sent (background process) in seconds  
`budget_alert_ttl`| 86400 (24 hours)| Cache TTL for budget alerts to prevent spam when budget is crossed  
`outage_alert_ttl`| 60 (1 minute)| Time window for collecting model outage errors in seconds  
`region_outage_alert_ttl`| 60 (1 minute)| Time window for collecting region-based outage errors in seconds  
`minor_outage_alert_threshold`| 5| Number of errors that trigger a minor outage alert (400 errors not counted)  
`major_outage_alert_threshold`| 10| Number of errors that trigger a major outage alert (400 errors not counted)  
`max_outage_alert_list_size`| 1000| Maximum number of errors to store in cache per model/region  
`log_to_console`| false| If true, prints alerting payload to console as a `.warning` log.  
  
  * Quick Start
    * Step 1: Add a Slack Webhook URL to env
    * Step 2: Setup Proxy
    * Step 3: Test it!
  * Advanced
    * Redacting Messages from Alerts
    * Soft Budget Alerts for Virtual Keys
    * Add Metadata to alerts
    * Select specific alert types
    * Map slack channels to alert type
    * MS Teams Webhooks
    * Discord Webhooks
  * [BETA] Webhooks for Budget Alerts
    * API Spec for Webhook Event
  * Region-outage alerting (✨ Enterprise feature)
  * **All Possible Alert Types**
  * `alerting_args` Specification