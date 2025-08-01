# TOTP | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/core-nodes/n8n-nodes-base.totp.md "Edit this page")

# TOTP#

The TOTP node provides a way to generate a TOTP (time-based one-time password).

Credentials

Refer to [TOTP credentials](../../credentials/totp/) for guidance on setting up authentication. 

## Node parameters#

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](../../../../advanced-ai/examples/using-the-fromai-function/).

Configure this node with these parameters.

### Credential to connect with#

Select or create a [TOTP credential](../../credentials/totp/) for the node to use.

### Operation#

**Generate Secret** is the only operation currently supported.

## Node options#

Use these **Options** to further configure the node.

### Algorithm#

Select the HMAC hashing algorithm to use. Default is SHA1.

### Digits#

Enter the number of digits in the generated code. Default is `6`.

### Period#

Enter how many seconds the TOTP is valid for. Default is `30`.

## Templates and examples#

[Browse TOTP integration templates](https://n8n.io/integrations/totp/), or [search all templates](https://n8n.io/workflows/)

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top