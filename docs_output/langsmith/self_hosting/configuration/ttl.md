# TTL and Data Retention | 🦜️🛠️ LangSmith

On this page

LangSmith Self-Hosted allows enablement of automatic TTL and Data Retention of traces. This can be useful if you're complying with data privacy regulations, or if you want to have more efficient space usage and auto cleanup of your traces. Traces will also have their data retention period automatically extended based on certain actions or run rule applications. For more details on Data Retention, take a look at the section on auto-upgrades in the [data retention guide](/administration/concepts#data-retention).

## Requirements​

You can configure retention through helm or environment variable settings. There are a few options that are configurable:

  * _Enabled:_ Whether data retention is enabled or disabled. If enabled, via the UI you can your default organization and project TTL tiers to apply to traces (see [data retention guide](/administration/concepts#data-retention) for details).
  * _Retention Periods:_ You can configure system-wide retention periods for shortlived and longlived traces. Once configured, you can manage the retention level at each project as well as set an organization-wide default for new projects.

  * Helm
  * Docker

    
    
    config:  
      ttl:  
        enabled: true  
        ttl_period_seconds:  
          # -- TTL seconds - 400 day longlived and 14 day shortlived  
          longlived: "34560000"  
          shortlived: "1209600"  
    
    
    
    # In your .env file  
    FF_TRACE_TIERS_ENABLED=true  
    TRACE_TIER_TTL_DURATION_SEC_MAP='{"longlived": 34560000, "shortlived": 1209600}'  
    

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Requirements

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)