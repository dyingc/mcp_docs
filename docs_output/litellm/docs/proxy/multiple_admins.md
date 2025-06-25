# ✨ Audit Logs | liteLLM

On this page

As a Proxy Admin, you can check if and when a entity (key, team, user, model) was created, updated, deleted, or regenerated, along with who performed the action. This is useful for auditing and compliance.

LiteLLM tracks changes to the following entities and actions:

  * **Entities:** Keys, Teams, Users, Models
  * **Actions:** Create, Update, Delete, Regenerate

tip

Requires Enterprise License, Get in touch with us [here](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat)

## Usage​

### 1\. Switch on audit Logs​

Add `store_audit_logs` to your litellm config.yaml and then start the proxy
    
    
    litellm_settings:  
      store_audit_logs: true  
    

### 2\. Make a change to an entity​

In this example, we will delete a key.
    
    
    curl -X POST 'http://0.0.0.0:4000/key/delete' \  
        -H 'Authorization: Bearer sk-1234' \  
        -H 'Content-Type: application/json' \  
        -d '{  
            "key": "d5265fc73296c8fea819b4525590c99beab8c707e465afdf60dab57e1fa145e4"  
        }'  
    

### 3\. View the audit log on LiteLLM UI​

On the LiteLLM UI, navigate to Logs -> Audit Logs. You should see the audit log for the key deletion.

## Advanced​

### Attribute Management changes to Users​

Call management endpoints on behalf of a user. (Useful when connecting proxy to your development platform).

## 1\. Set `LiteLLM-Changed-By` in request headers​

Set the 'user_id' in request headers, when calling a management endpoint. [View Full List](https://litellm-api.up.railway.app/#/team%20management).

  * Update Team budget with master key.
  * Attribute change to '[krrish@berri.ai](mailto:krrish@berri.ai)'.

**👉 Key change:** Passing `-H 'LiteLLM-Changed-By: krrish@berri.ai'`
    
    
    curl -X POST 'http://0.0.0.0:4000/team/update' \  
        -H 'Authorization: Bearer sk-1234' \  
        -H 'LiteLLM-Changed-By: krrish@berri.ai' \  
        -H 'Content-Type: application/json' \  
        -d '{  
            "team_id" : "8bf18b11-7f52-4717-8e1f-7c65f9d01e52",  
            "max_budget": 2000  
        }'  
    

## 2\. Emitted Audit Log​
    
    
    {  
       "id": "bd136c28-edd0-4cb6-b963-f35464cf6f5a",  
       "updated_at": "2024-06-08 23:41:14.793",  
       "changed_by": "krrish@berri.ai", # 👈 CHANGED BY  
       "changed_by_api_key": "88dc28d0f030c55ed4ab77ed8faf098196cb1c05df778539800c9f1243fe6b4b",  
       "action": "updated",  
       "table_name": "LiteLLM_TeamTable",  
       "object_id": "8bf18b11-7f52-4717-8e1f-7c65f9d01e52",  
       "before_value": {  
         "spend": 0,  
         "max_budget": 0,  
       },  
       "updated_values": {  
         "team_id": "8bf18b11-7f52-4717-8e1f-7c65f9d01e52",  
         "max_budget": 2000 # 👈 CHANGED TO  
       },  
     }  
    

## API SPEC of Audit Log​

### `id`​

  * **Type:** `String`
  * **Description:** This is the unique identifier for each audit log entry. It is automatically generated as a UUID (Universally Unique Identifier) by default.

### `updated_at`​

  * **Type:** `DateTime`
  * **Description:** This field stores the timestamp of when the audit log entry was created or updated. It is automatically set to the current date and time by default.

### `changed_by`​

  * **Type:** `String`
  * **Description:** The `user_id` that performed the audited action. If `LiteLLM-Changed-By` Header is passed then `changed_by=<value passed for LiteLLM-Changed-By header>`

### `changed_by_api_key`​

  * **Type:** `String`
  * **Description:** This field stores the hashed API key that was used to perform the audited action. If left blank, it defaults to an empty string.

### `action`​

  * **Type:** `String`
  * **Description:** The type of action that was performed. One of "create", "update", or "delete".

### `table_name`​

  * **Type:** `String`
  * **Description:** This field stores the name of the table that was affected by the audited action. It can be one of the following values: `LiteLLM_TeamTable`, `LiteLLM_UserTable`, `LiteLLM_VerificationToken`

### `object_id`​

  * **Type:** `String`
  * **Description:** This field stores the ID of the object that was affected by the audited action. It can be the key ID, team ID, user ID

### `before_value`​

  * **Type:** `Json?`
  * **Description:** This field stores the value of the row before the audited action was performed. It is optional and can be null.

### `updated_values`​

  * **Type:** `Json?`
  * **Description:** This field stores the values of the row that were updated after the audited action was performed

  * Usage
    * 1\. Switch on audit Logs
    * 2\. Make a change to an entity
    * 3\. View the audit log on LiteLLM UI
  * Advanced
    * Attribute Management changes to Users
  * 1\. Set `LiteLLM-Changed-By` in request headers
  * 2\. Emitted Audit Log
  * API SPEC of Audit Log
    * `id`
    * `updated_at`
    * `changed_by`
    * `changed_by_api_key`
    * `action`
    * `table_name`
    * `object_id`
    * `before_value`
    * `updated_values`