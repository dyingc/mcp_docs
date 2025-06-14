# Choose a node building style | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/creating-nodes/plan/choose-node-method.md "Edit this page")

# Choose your node building approach#

n8n has two node-building styles, declarative and programmatic.

You should use the declarative style for most nodes. This style:

  * Uses a JSON-based syntax, making it simpler to write, with less risk of introducing bugs.
  * Is more future-proof.
  * Supports integration with REST APIs.

The programmatic style is more verbose. You must use the programmatic style for:

  * Trigger nodes
  * Any node that isn't REST-based. This includes nodes that need to call a GraphQL API and nodes that use external dependencies.
  * Any node that needs to transform incoming data.
  * Full versioning. Refer to [Node versioning](../../build/reference/node-versioning/) for more information on types of versioning.

## Data handling differences#

The main difference between the declarative and programmatic styles is how they handle incoming data and build API requests. The programmatic style requires an `execute()` method, which reads incoming data and parameters, then builds a request. The declarative style handles this using the `routing` key in the `operations` object. Refer to [Node base file](../../build/reference/node-base-files/) for more information on node parameters and the `execute()` method.

## Syntax differences#

To understand the difference between the declarative and programmatic styles, compare the two code snippets below. This example creates a simplified version of the SendGrid integration, called "FriendGrid." The following code snippets aren't complete: they emphasize the differences in the node building styles.

In programmatic style:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    93

| 
    
    
    import {
    	IExecuteFunctions,
    	INodeExecutionData,
    	INodeType,
    	INodeTypeDescription,
    	IRequestOptions,
    } from 'n8n-workflow';
    
    // Create the FriendGrid class
    export class FriendGrid implements INodeType {
      description: INodeTypeDescription = {
        displayName: 'FriendGrid',
        name: 'friendGrid',
        . . .
        properties: [
          {
            displayName: 'Resource',
            . . .
          },
          {
            displayName: 'Operation',
            name: 'operation',
            type: 'options',
            displayOptions: {
              show: {
                  resource: [
                  'contact',
                  ],
              },
            },
            options: [
              {
                name: 'Create',
                value: 'create',
                description: 'Create a contact',
              },
            ],
            default: 'create',
            description: 'The operation to perform.',
          },
          {
            displayName: 'Email',
            name: 'email',
            . . .
          },
          {
            displayName: 'Additional Fields',
            // Sets up optional fields
          },
        ],
    };
    
      async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
        let responseData;
        const resource = this.getNodeParameter('resource', 0) as string;
        const operation = this.getNodeParameter('operation', 0) as string;
        //Get credentials the user provided for this node
        const credentials = await this.getCredentials('friendGridApi') as IDataObject;
    
        if (resource === 'contact') {
          if (operation === 'create') {
          // Get email input
          const email = this.getNodeParameter('email', 0) as string;
          // Get additional fields input
          const additionalFields = this.getNodeParameter('additionalFields', 0) as IDataObject;
          const data: IDataObject = {
              email,
          };
    
          Object.assign(data, additionalFields);
    
          // Make HTTP request as defined in https://sendgrid.com/docs/api-reference/
          const options: IRequestOptions = {
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${credentials.apiKey}`,
            },
            method: 'PUT',
            body: {
                contacts: [
                data,
                ],
            },
            url: `https://api.sendgrid.com/v3/marketing/contacts`,
            json: true,
          };
          responseData = await this.helpers.httpRequest(options);
          }
        }
        // Map data to n8n data
        return [this.helpers.returnJsonArray(responseData)];
      }
    }
      
  
---|---  
  
In declarative style:
    
    
     1
     2
     3
     4
     5
     6
     7
     8
     9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74

| 
    
    
    import { INodeType, INodeTypeDescription } from 'n8n-workflow';
    
    // Create the FriendGrid class
    export class FriendGrid implements INodeType {
      description: INodeTypeDescription = {
        displayName: 'FriendGrid',
        name: 'friendGrid',
        . . .
        // Set up the basic request configuration
        requestDefaults: {
          baseURL: 'https://api.sendgrid.com/v3/marketing'
        },
        properties: [
          {
            displayName: 'Resource',
            . . .
          },
          {
            displayName: 'Operation',
            name: 'operation',
            type: 'options',
            displayOptions: {
              show: {
                resource: [
                  'contact',
                ],
              },
            },
            options: [
              {
                name: 'Create',
                value: 'create',
                description: 'Create a contact',
                // Add the routing object
                routing: {
                  request: {
                    method: 'POST',
                    url: '=/contacts',
                    send: {
                      type: 'body',
                      properties: {
                        email: {{$parameter["email"]}}
                      }
                    }
                  }
                },
                // Handle the response to contact creation
                output: {
                  postReceive: [
                    {
                      type: 'set',
                      properties: {
                        value: '={{ { "success": $response } }}'
                      }
                    }
                  ]
                }
              },
            ],
            default: 'create',
            description: 'The operation to perform.',
          },
          {
            displayName: 'Email',
            . . .
          },
          {
            displayName: 'Additional Fields',
            // Sets up optional fields
          },
        ],
      }
      // No execute method needed
    }
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top