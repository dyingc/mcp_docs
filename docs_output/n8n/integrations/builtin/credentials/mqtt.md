# MQTT credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/mqtt.md "Edit this page")

# MQTT credentials#

You can use these credentials to authenticate the following nodes:

  * [MQTT](../../app-nodes/n8n-nodes-base.mqtt/)
  * [MQTT Trigger](../../trigger-nodes/n8n-nodes-base.mqtttrigger/)

## Prerequisites#

Install an [MQTT broker](https://mqtt.org/).

MQTT provides a list of Servers/Brokers at [MQTT Software](https://mqtt.org/software/).

## Supported authentication methods#

  * Broker connection

## Related resources#

Refer to [MQTT's documentation](https://mqtt.org/) for more information about the MQTT protocol.

Refer to your broker provider's documentation for more detailed configuration and details.

## Using broker connection#

To configure this credential, you'll need:

  * Your MQTT broker's **Protocol**
  * The **Host**
  * The **Port**
  * A **Username** and **Password** to authenticate with
  * If you're using **SSL** , the relevant certificates and keys

To set things up:

  1. Select the broker's **Protocol** , which determines the URL n8n uses. Options include:
     * **Mqtt** : Begin the URL with the standard `mqtt:` protocol.
     * **Mqtts** : Begin the URL with the secure `mqtts:` protocol.
     * **Ws** : Begin the URL with the WebSocket `ws:` protocol.
  2. Enter your broker **Host**.
  3. Enter the **Port** number n8n should use to connect to the broker host.
  4. Enter the **Username** to log into the broker as.
  5. Enter that user's **Password**.
  6. If you want to receive QoS 1 and 2 messages while offline, turn off the **Clean Session** toggle.
  7. Enter a **Client ID** you'd like the credential to use. If you leave this blank, n8n will generate one for you. You can use a fixed or expression-based Client ID.
     * Client IDs can be useful to identify and track connection access. n8n recommends using something with `n8n` in it for easier auditing.
  8. If your MQTT broker uses SSL, turn the **SSL** toggle on. Once you turn it on:
     1. Select whether to use **Passwordless** connection with certificates, which is like the SASL mechanism EXTERNAL. If turned on:
        1. Select whether to **Reject Unauthorized Certificate** : If turned off, n8n will connect even if the certificate validation fails.
        2. Add an SSL **Client Certificate**.
        3. Add an SSL **Client Key** for the Client Certificate.
     2. One or more SSL **CA Certificates**.

Refer to your MQTT broker provider's documentation for more detailed configuration instructions.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top