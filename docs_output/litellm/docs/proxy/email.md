# Email Notifications | liteLLM

On this page

LiteLLM Email Notifications

## Overview​

Send LiteLLM Proxy users emails for specific events.

Category| Details  
---|---  
Supported Events| • User added as a user on LiteLLM Proxy  
• Proxy API Key created for user  
Supported Email Integrations| • Resend API  
• SMTP  
  
## Usage​

info

LiteLLM Cloud: This feature is enabled for all LiteLLM Cloud users, there's no need to configure anything.

### 1\. Configure email integration​

  * SMTP
  * Resend API

Get SMTP credentials to set this up

proxy_config.yaml
    
    
    litellm_settings:  
        callbacks: ["smtp_email"]  
    

Add the following to your proxy env
    
    
    SMTP_HOST="smtp.resend.com"  
    SMTP_TLS="True"  
    SMTP_PORT="587"  
    SMTP_USERNAME="resend"  
    SMTP_SENDER_EMAIL="notifications@alerts.litellm.ai"  
    SMTP_PASSWORD="xxxxx"  
    

Add `resend_email` to your proxy config.yaml under `litellm_settings`

set the following env variables
    
    
    RESEND_API_KEY="re_1234"  
    

proxy_config.yaml
    
    
    litellm_settings:  
        callbacks: ["resend_email"]  
    

### 2\. Create a new user​

On the LiteLLM Proxy UI, go to users > create a new user.

After creating a new user, they will receive an email invite a the email you specified when creating the user.

## Email Templates​

### 1\. User added as a user on LiteLLM Proxy​

This email is send when you create a new user on LiteLLM Proxy.

**How to trigger this event**

On the LiteLLM Proxy UI, go to Users > Create User > Enter the user's email address > Create User.

### 2\. Proxy API Key created for user​

This email is sent when you create a new API key for a user on LiteLLM Proxy.

**How to trigger this event**

On the LiteLLM Proxy UI, go to Virtual Keys > Create API Key > Select User ID

On the Create Key Modal, Select Advanced Settings > Set Send Email to True.

## Customizing Email Branding​

info

Customizing Email Branding is an Enterprise Feature [Get in touch with us for a Free Trial](https://calendly.com/d/4mp-gd3-k5k/litellm-1-1-onboarding-chat)

LiteLLM allows you to customize the:

  * Logo on the Email
  * Email support contact

Set the following in your env to customize your emails
    
    
    EMAIL_LOGO_URL="https://litellm-listing.s3.amazonaws.com/litellm_logo.png"  # public url to your logo  
    EMAIL_SUPPORT_CONTACT="support@berri.ai"                                    # Your company support email  
    

  * Overview
  * Usage
    * 1\. Configure email integration
    * 2\. Create a new user
  * Email Templates
    * 1\. User added as a user on LiteLLM Proxy
    * 2\. Proxy API Key created for user
  * Customizing Email Branding