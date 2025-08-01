# LangSmith Release Notes | 🦜️🛠️ LangSmith

On this page

note

**Reminder: API keys prefixed with`ls__` have been disabled in favor of `lsv2...` style keys as of LangSmith Helm release v0.8.** For more information see [the Admin concepts guide.](https://docs.smith.langchain.com/administration/concepts#api-keys)

## Week of October 28, 2024 - LangSmith v0.8​

Release notes are available at our [new changelog](https://changelog.langchain.com/?categories=cat_ZWTyLBFVqdtSq).

## Week of August 26, 2024 - LangSmith v0.7​

This release adds a number of new features, improves the performance of the Threads view, and adds password authentication support and adds support for setting a default Time To Live (TTL) on LangSmith traces.

### New Features since v0.6.0​

  * [Resource tags to organize your Workspace in LangSmith](https://changelog.langchain.com/announcements/resource-tags-to-organize-your-workspace-in-langsmith)
  * [Generate synthetic examples to enhance a LangSmith dataset](https://changelog.langchain.com/announcements/generate-synthetic-examples-to-enhance-a-langsmith-dataset)
  * [Enhanced trace comparison view and saveable custom trace filters](https://changelog.langchain.com/announcements/trace-comparison-view-saving-custom-trace-filters)
  * [Defining, validating and updating dataset schemas](https://changelog.langchain.com/announcements/define-validate-and-update-dataset-schemas-in-langsmith)
  * [Multiple annotators can review a run in LangSmith](https://changelog.langchain.com/announcements/multiple-annotators-can-review-a-run-in-langsmith)
  * [Support for filtering runs within the trace view](https://changelog.langchain.com/announcements/filtering-runs-within-the-trace-view)
  * [Enhanced key-value search](https://changelog.langchain.com/announcements/enhanced-key-value-search-matching-inputs-and-outputs)
  * [Webhook notifications for run rules](https://changelog.langchain.com/announcements/set-up-webhook-notifications-for-run-rules)
  * [Support for comparing multiple prompts and model configurations side-by-side in the LangSmith Playground](https://changelog.langchain.com/announcements/build-prompts-faster-and-compare-in-langsmith-playground)
  * [Support for storing the model and configuration when saving a Prompt](https://changelog.langchain.com/announcements/store-the-model-and-configuration-when-saving-a-prompt)

### Performance and Reliability Changes​

  * Improved performance of Threads view for very large projects
  * Improved error handling in cases where the Clickhouse database is temporarily unavailable

### Infrastructure Changes​

  * Added a Helm configuration option for Time To Live for traces. When set, this setting will apply only to net-new ingested traces and by changing this setting, _traces will be automatically and irrevocably deleted from Clickhouse after expiration of the TTL._ For more details see [TTL and Data Retention](/self_hosting/configuration/ttl). You may also need to change/audit your project default TTL settings.
  * Added configuration option to enable `blobStorage`. This will move run inputs, outputs, errors, manifests, extras, and events to blob storage to lower load on ClickHouse/reduce disk usage. Currently only S3 and GCP are supported. For more details see [Enable Blob Storage](/self_hosting/configuration/blob_storage).
  * Default Resource/Limits for all resources. Note that you may need to tweak your cluster settings.
    * By default we will use:
      * 16 CPU
      * 64 GB RAM
      * You will need a node that can fit 4 CPU/16 GB RAM
    * To override these settings you can manually configure resources requests/limits yourself
  * Turned bundled `Redis` persistence on by default. If you are using the bundled version of `redis` you may need to recreate your `Redis` StatefulSet if you had not previously turned on persistence.
  * Updated `clickhouseMigration` command to wait for clickhouse initialization prior to running migrations.
  * Deprecation of `<domain>/api-hub url`. You can now use the `<domain>/api` url for all api interactions. This will be fully removed in the v0.8 release so make sure to migrate any apps using the previous url.
  * Health checks added to `queue` pods.
  * Updates to the `nginx` config.
  * Removed the OpenAI key configuration option.

### Admin Changes​

  * Added support for simple password authentication. For more details see [Email/password a.k.a. basic auth](/self_hosting/configuration/basic_auth)
    * **Note that at this time there is no migration path from simple to OIDC authentication** — we are working on this migration path for a subsequent release.
  * Added support to disable personal orgs.
  * Added support to disable org creation.
  * Added config option to allow workspace admins to add workspace users.
  * We have delayed deprecation of the v1 API Keys prefixed with `ls__` until the v0.8 release of LangSmith which should happen on or around October 1. Please update your API keys to Service Keys prefixed with `lsv2__sk` at your earliest convenience.

### Deprecation notices​

With the release of v0.7:

  * The LangChain Hub SDK is now deprecated and its functionality folded into the [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk).
  * LangSmith v0.6.x and earlier are now in maintenance mode and may only receive critical security fixes.

## Week of June 17, 2024 - LangSmith v0.6​

LangSmith v0.6 improves run rules performance and reliability, adds support for multiple Workspaces within an Organization, custom models in Playground, and significant enhancements to Evaluations.

### New Features since v0.5​

  * Dataset splits for evaluation and filtering/editing dataset examples. [Learn More...](https://blog.langchain.dev/week-of-5-27-langchain-release-notes/#datasetsplits)
  * You can now run multiple repetitions of your experiment in LangSmith. [Learn More...](https://blog.langchain.dev/week-of-5-27-langchain-release-notes/#repetitions)
  * Off-the-shelf online evaluator prompts to catch bad retrieval and hallucinations for RAG. [Learn More...](https://blog.langchain.dev/week-of-5-27-langchain-release-notes/#onlineevaluatorprompts)
  * Manage private prompts without a handle. [Learn More...](https://blog.langchain.dev/week-of-5-27-langchain-release-notes/#privateprompts)
  * Workspaces in LangSmith for improved collaboration & organization. [Learn More...](https://blog.langchain.dev/week-of-6-10-langchain-release-notes/#workspaces)
  * Enter the playground from scratch instead of from a trace or a prompt. [Learn More...](https://blog.langchain.dev/week-of-6-10-langchain-release-notes/#playground-from-scratch)
  * Variable mapping for online evaluator prompts. [Learn More...](https://blog.langchain.dev/week-of-6-10-langchain-release-notes/#variable-mapping)
  * Custom Model support in Playground. [Learn More...](https://docs.smith.langchain.com/how_to_guides/custom_endpoint)

### Performance and Reliability Changes​

  * Improved performance of run rules especially in cases where rule execution may exceed the interval of rule execution.
  * Reduced run rule interval from 5 minutes to 1 minute resulting in more frequent application of rules
  * Improved performance when querying Hub via the SDK. NOTE: Accessing these improvements requires v0.1.20 or greater of the [Hub SDK](https://github.com/langchain-ai/hub-sdk)

### Infrastructure changes​

  * [Docker Compose only] The default port has changed from 80 to 1980.
  * [Helm] The playground image start command has changed. If you are using a custom Helm chart, you may need to review the configuration for Playground and adjust your Helm config accordingly.
  * [Helm] Added the ability to configure your probes in the `values.yaml` file. This allows you to adjust the readiness and liveness probes for the LangSmith services. You may need to adjust these if you had changed container ports.
  * [Helm] Added ArgoCD `PostSync` annotations to hook jobs to ensure that the jobs are run properly in ArgoCD. You may need to remove this annotation if you were previously setting it manually.
  * Updated Clickhouse from v23.9 to v24.2 NOTE: Applies only to environments using the LangSmith-provided Clickhouse.

### Admin changes​

  * Added support for Workspaces. See the [Admin concepts guide](/administration/concepts#workspaces) for more details.
  * Added global setting `orgCreationDisabled` to `values.yaml` to disable creation of new Organizations.
  * Added support for custom TLS certificates for the Azure OpenAI model provider. See the [how-to guide](/self_hosting/configuration/custom_tls_certificates) for more details.

### Deprecation notices​

With the release of v0.6:

  * LangSmith v0.5.x and earlier are now in maintenance mode and may only receive critical security fixes.

## Week of May 13, 2024 - LangSmith v0.5​

LangSmith v0.5 improves performance and reliability, adds features to improve regression testing, production monitoring and automation, and implements Role-Based Access Controls (RBAC).

### Breaking changes[](https://docs.smith.langchain.com/self_hosting/release_notes#breaking-changes)​

  * We will be dropping support for API keys in favor of personal access tokens (PATs) and Service Keys. We recommend using PATs and Service Keys for all new integrations. **API keys prefixed with`ls__` will NO LONGER work as of LangSmith Helm release v0.7 to be released in August 2024.**

### New Features since v0.4​

  * Role-Based Access Controls. See: <https://blog.langchain.dev/access-control-updates-for-langsmith/>
  * Improved regression testing experience. See: <https://blog.langchain.dev/regression-testing/>
  * Improved production monitoring and automation: See: <https://blog.langchain.dev/langsmith-production-logging-automations/>

### Performance and Reliability Changes​

  * Split ingest, session deletion, and automation jobs to execute within separate resource pools.

### Infrastructure changes​

  * As of LangSmith v0.4, Clickhouse persistence now uses `50Gi` of storage by default. You can adjust this by changing the `clickhouse.statefulSet.persistence.size` value in your `values.yaml` file.
    * If your existing configuration cannot support 50Gi, you may need to resize your existing storage class or set `clickhouse.statefulSet.persistence.size` to the previous default value of `8Gi`.
    * It is **strongly** recommend that you monitor the consumption of storage on your Clickhouse volume to ensure the volume does not near full capacity, which may cause run ingest to behave erratically.
  * New Platform-Backend service used internally. This service also uses it’s own image. You may need to adjust your helm `values` files accordingly.

### Admin changes​

  * Added new Role-Based Access Controls. For more details see the [Admin](/administration/concepts) and [Set Up Access Control](/administration/how_to_guides/organization_management/set_up_access_control) sections of the docs.
  * Introduction of PATs and Service Keys. Old API keys have been migrated to service keys.

### Deprecation notices​

With the release of v0.5:

  * LangSmith v0.4.x and earlier are now in maintenance mode and may only receive critical security fixes.

## Week of March 25, 2024 - LangSmith v0.4​

LangSmith 0.4 improves performance and reliability, implements a new asynchronous queue worker to optimize run ingests, and an API key salt parameter.

### Breaking changes​

  * This release adds an API key salt parameter. This previously defaulted to your LangSmith License Key. **For updates from earlier versions you should set this parameter to your license key to ensure backwards compatibility.** Using a new api key salt will invalidate all existing api keys.
  * This release makes Clickhouse persistence use 50Gi of storage by default. You can adjust this by changing the `clickhouse.statefulSet.persistence.size` value in your `values.yaml` file.
    * If your existing configuration does not configure persistence already, you will need to resize your existing pvc or set `clickhouse.statefulSet.persistence.size` to the previous default value of `8Gi`.

### Performance and Reliability Changes​

  * Implemented a new asynchronous queue worker and cached token encodings to improve performance when ingesting traces, reducing the delay between ingest and display in the LangSmith UI.

### Infrastructure changes​

  * Some our image repositories have been updated. You can see the root repositories in our `values.yaml` file and may need to update mirrors to pick up the new images.
  * Clickhouse persistence now uses 50Gi of storage by default. You can adjust this by changing the `clickhouse.statefulSet.persistence.size` value in your `values.yaml` file.
    * If your existing configuration cannot support 50Gi, you may need to resize your existing storage class or set `clickhouse.statefulSet.persistence.size` to the previous default value of `8Gi`.
  * Consolidation of hubBackend and backend services. We now use one service to serve both of these endpoints. This should not impact your application.

### Admin changes​

  * Added an API key salt parameter in `values.yml`. This can be set to a custom value and changing it will invalidate all existing api keys.
  * Changed the OAuth flow to leverage Access Tokens instead of OIDC ID tokens. This change should not impact the end user experience.
  * Added scripts to enable feature flags in self-hosted environments for use in previewing pre-release features. Details are available at <https://github.com/langchain-ai/helm/blob/main/charts/langsmith/docs/ADD-FEATURE-FLAG.md>

### Deprecation notices​

With the release of 0.4:

  * LangSmith 0.3.x and earlier are now in maintenance mode and may only receive critical security fixes.

## Week of Februrary 21, 2024 - LangSmith v0.3​

LangSmith 0.3 improves performance and reliability, adds improved monitoring charts group by metadata and tag, and adds cost tracking.

### Breaking changes​

  * This release will drop the postgres run tables - if you are making a migration from LangSmith v0.1 and wish to retain run data, you must first update to v0.2 and perform a data migration. See <https://github.com/langchain-ai/helm/blob/main/charts/langsmith/docs/UPGRADE-0.2.x.md> for additional details

### Performance and Reliability Changes​

  * Continued performance when ingesting traces, reducing the delay between ingest and display in the LangSmith UI.

### Admin changes​

  * None

### Deprecation notices​

With the release of 0.3:

  * LangSmith 0.2.x and earlier are now in maintenance mode and may only receive critical security fixes.

## Week of January 29, 2024 - LangSmith v0.2​

LangSmith 0.2 improves performance and reliability, adds a updated interface for reviewing trace data, and adds support for batch processing of traces.

### Requirements​

  * This release requires `langsmith-sdk` version ≥ `0.0.71` (Python) and ≥ `0.0.56` (JS/TS) to support changes in pagination of API results. Older versions will only return the first 100 results when querying an endpoint.

### Breaking changes​

  * The search syntax for metadata in runs has changed and limits support for nested JSON to a single level. If you are supplying custom metadata in traces, you should flatten your metadata structure in order to allow it to be searchable, (e.g. `{"user_id": ..., "user_name":...,}`) and then search using `has(metadata, '{"user_name": ...}')`

### Performance and Reliability Changes​

  * Improved performance when ingesting traces, reducing the delay between ingest and display in the LangSmith UI.
  * Improved performance for updates and deletes on annotation labels.
  * Added pagination of API responses.
  * Fixed an issue impacting natural language searches.

### Infrastructure Changes​

  * Added the `clickhouse` database service. Run results will now be stored in ClickHouse instead of Postgres to improve performance and scalability and reduce delays in the time it takes for runs to appear in LangSmith.
    * Note that if you wish to retain access to run data in the Langsmith UI after updating, a data migration will need to be performed. Details are available at <https://github.com/langchain-ai/helm/blob/main/charts/langsmith/docs/UPGRADE-0.2.x.md>

### Admin changes​

  * Increased the maximum number of users per organization from 5 to 100 for new organizations.

### Deprecation notices​

With the release of 0.2:

  * LangSmith 0.1.x is now in maintenance mode and may only receive critical security fixes.

* * *

#### Was this page helpful?

  

#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

  * Week of October 28, 2024 - LangSmith v0.8
  * Week of August 26, 2024 - LangSmith v0.7
    * New Features since v0.6.0
    * Performance and Reliability Changes
    * Infrastructure Changes
    * Admin Changes
    * Deprecation notices
  * Week of June 17, 2024 - LangSmith v0.6
    * New Features since v0.5
    * Performance and Reliability Changes
    * Infrastructure changes
    * Admin changes
    * Deprecation notices
  * Week of May 13, 2024 - LangSmith v0.5
    * Breaking changes
    * New Features since v0.4
    * Performance and Reliability Changes
    * Infrastructure changes
    * Admin changes
    * Deprecation notices
  * Week of March 25, 2024 - LangSmith v0.4
    * Breaking changes
    * Performance and Reliability Changes
    * Infrastructure changes
    * Admin changes
    * Deprecation notices
  * Week of Februrary 21, 2024 - LangSmith v0.3
    * Breaking changes
    * Performance and Reliability Changes
    * Admin changes
    * Deprecation notices
  * Week of January 29, 2024 - LangSmith v0.2
    * Requirements
    * Breaking changes
    * Performance and Reliability Changes
    * Infrastructure Changes
    * Admin changes
    * Deprecation notices

  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)