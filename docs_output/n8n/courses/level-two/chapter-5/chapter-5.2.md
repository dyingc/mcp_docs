# Workflow 2 | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-two/chapter-5/chapter-5.2.md "Edit this page")

# Workflow 2: Generating reports#

In this workflow, you will merge data from different sources, transform binary data, generate files, and send notifications about them. The final workflow should look like this:

![Workflow 2 for aggregating data and generating files](/_images/courses/level-two/chapter-five/workflow2.png)_Workflow 2 for aggregating data and generating files_

To make things easier, let's split the workflow into three parts.

## Part 1: Getting data from different sources#

The first part of the workflow consists of five nodes:

![Workflow 1: Getting data from different sources](/_images/courses/level-two/chapter-five/workflow2_1.png)_Workflow 1: Getting data from different sources_

  1. Use the [**HTTP Request node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to get data from the API endpoint that stores company data. Configure the following node parameters:

     * **Method** : Get
     * **URL** : The **Dataset URL** you received in the email when you signed up for this course.
     * **Authentication** : Generic Credential Type
       * **Generic Auth Type** : Header Auth
       * **Credentials for Header Auth** : The Header Auth name and Header Auth value you received in the email when you signed up for this course.
     * **Send Headers** : Toggle to true
       * **Specify Headers** : Select `Using Fields Below`
       * **Name** : `unique_id`
       * **Value** : The unique ID you received in the email when you signed up for this course.
  2. Use the [**Airtable node**](../../../../integrations/builtin/app-nodes/n8n-nodes-base.airtable/) to list data from the `customers` table (where you updated the fields `region` and `subregion`).

  3. Use the [**Merge node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.merge/) to merge data from the Airtable and HTTP Request node, based on matching the input fields for `customerID`.
  4. Use the [**Sort node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.sort/) to sort data by `orderPrice` in descending order.

Quiz questions

  * What's the name of the employee assigned to customer 1?
  * What's the order status of customer 2?
  * What's the highest order price?

## Part 2: Generating file for regional sales#

The second part of the workflow consists of four nodes:

![Workflow 2: Generating file for regional sales](/_images/courses/level-two/chapter-five/workflow2_2.png)_Workflow 2: Generating file for regional sales_

  1. Use the [**If node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.if/) to filter to only display orders from the region `Americas`.
  2. Use the [**Convert to File**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.converttofile/) to transform the incoming data from JSON to binary format. Convert each item to a separate file. (Bonus points if you can figure out how to name each report based on the orderID!)
  3. Use the [**Gmail node**](../../../../integrations/builtin/app-nodes/n8n-nodes-base.gmail/) (or another email node) to send the files using email to an address you have access to. Note that you need to add an attachment with the data property.
  4. Use the [**Discord node**](../../../../integrations/builtin/app-nodes/n8n-nodes-base.discord/) to send a message in the n8n Discord channel `#course-level-two`. In the node, configure the following parameters:
     * **Webhook URL** : The Discord URL you received in the email when you signed up for this course.
     * **Text** : "I sent the file using email with the label ID `{label ID}`. My ID: " followed by the unique ID emailed to you when you registered for this course.   
Note that you need to replace the text in curly braces `{}` with [expressions](../../../../glossary/#expression-n8n) that reference the data from the nodes.

Quiz questions

  * How many orders are assigned to the `Americas` region?
  * What's the total price of the orders in the `Americas` region?
  * How many items does the **Write Binary File node** return?

## Part 3: Generating files for total sales#

The third part of the workflow consists of five nodes:

![Workflow 3: Generating files for total sales](/_images/courses/level-two/chapter-five/workflow2_3.png)_Workflow 3: Generating files for total sales_

  1. Use the [**Loop Over Items node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/) to split data from the Item Lists node into batches of 5.
  2. Use the [**Set node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.set/) to set four values, referenced with expressions from the previous node: `customerEmail`, `customerRegion`, `customerSince`, and `orderPrice`.
  3. Use the [**Date & Time node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.datetime/) to change the date format of the field `customerSince` to the format MM/DD/YYYY.
     * Set the **Include Input Fields** option to keep all the data together.
  4. Use the [**Convert to File node**](../../../../integrations/builtin/core-nodes/n8n-nodes-base.converttofile/) to create a CSV spreadsheet with the file name set as the expression: `{{$runIndex > 0 ? 'file_low_orders':'file_high_orders'}}`.
  5. Use the [**Discord node**](../../../../integrations/builtin/app-nodes/n8n-nodes-base.discord/) to send a message in the n8n Discord channel `#course-level-two`. In the node, configure the following parameters:
     * **Webhook URL** : The Discord URL you received in the email when you signed up for this course.
     * **Text** : "I created the spreadsheet `{file name}`. My ID:" followed by the unique ID emailed to you when you registered for this course.   
Note that you need to replace `{file name}` with an expression that references data from the previous **Convert to File node**.  

Quiz questions

  * What's the lowest order price in the first batch of items?
  * What's the formatted date of customer 7?
  * How many items does the **Convert to File node** return?

Show me the solution

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:
    
    
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
     94
     95
     96
     97
     98
     99
    100
    101
    102
    103
    104
    105
    106
    107
    108
    109
    110
    111
    112
    113
    114
    115
    116
    117
    118
    119
    120
    121
    122
    123
    124
    125
    126
    127
    128
    129
    130
    131
    132
    133
    134
    135
    136
    137
    138
    139
    140
    141
    142
    143
    144
    145
    146
    147
    148
    149
    150
    151
    152
    153
    154
    155
    156
    157
    158
    159
    160
    161
    162
    163
    164
    165
    166
    167
    168
    169
    170
    171
    172
    173
    174
    175
    176
    177
    178
    179
    180
    181
    182
    183
    184
    185
    186
    187
    188
    189
    190
    191
    192
    193
    194
    195
    196
    197
    198
    199
    200
    201
    202
    203
    204
    205
    206
    207
    208
    209
    210
    211
    212
    213
    214
    215
    216
    217
    218
    219
    220
    221
    222
    223
    224
    225
    226
    227
    228
    229
    230
    231
    232
    233
    234
    235
    236
    237
    238
    239
    240
    241
    242
    243
    244
    245
    246
    247
    248
    249
    250
    251
    252
    253
    254
    255
    256
    257
    258
    259
    260
    261
    262
    263
    264
    265
    266
    267
    268
    269
    270
    271
    272
    273
    274
    275
    276
    277
    278
    279
    280
    281
    282
    283
    284
    285
    286
    287
    288
    289
    290
    291
    292
    293
    294
    295
    296
    297
    298
    299
    300
    301
    302
    303
    304
    305
    306
    307
    308
    309
    310
    311
    312
    313
    314
    315
    316
    317
    318
    319
    320
    321
    322
    323
    324
    325
    326
    327
    328
    329
    330
    331
    332
    333
    334
    335
    336
    337
    338
    339
    340
    341
    342
    343
    344
    345
    346
    347
    348
    349
    350
    351
    352
    353
    354
    355
    356
    357
    358
    359
    360
    361
    362
    363
    364
    365
    366
    367
    368
    369
    370
    371
    372
    373
    374
    375
    376
    377
    378
    379
    380
    381
    382
    383
    384
    385
    386
    387
    388
    389
    390
    391
    392
    393
    394
    395
    396
    397
    398
    399
    400
    401
    402
    403
    404
    405
    406
    407
    408
    409
    410
    411
    412
    413
    414
    415
    416
    417
    418
    419
    420
    421
    422
    423
    424
    425
    426
    427
    428
    429
    430
    431
    432
    433
    434
    435
    436
    437
    438
    439
    440
    441
    442
    443
    444
    445
    446
    447
    448
    449
    450
    451
    452
    453
    454
    455
    456
    457
    458
    459
    460
    461
    462
    463
    464
    465
    466
    467
    468
    469
    470
    471
    472
    473
    474
    475
    476
    477
    478
    479
    480
    481
    482
    483
    484
    485
    486
    487
    488
    489
    490
    491
    492

| 
    
    
    {
    "meta": {
        "templateCredsSetupCompleted": true,
        "instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"
    },
    "nodes": [
        {
        "parameters": {
            "sendTo": "bart@n8n.io",
            "subject": "Your TPS Reports",
            "emailType": "text",
            "message": "Please find your TPS report attached.",
            "options": {
            "attachmentsUi": {
                "attachmentsBinary": [
                {}
                ]
            }
            }
        },
        "id": "d889eb42-8b34-4718-b961-38c8e7839ea6",
        "name": "Gmail",
        "type": "n8n-nodes-base.gmail",
        "typeVersion": 2.1,
        "position": [
            2100,
            500
        ],
        "credentials": {
            "gmailOAuth2": {
            "id": "HFesCcFcn1NW81yu",
            "name": "Gmail account 7"
            }
        }
        },
        {
        "parameters": {},
        "id": "c0236456-40be-4f8f-a730-e56cb62b7b5c",
        "name": "When clicking \"Execute workflow\"",
        "type": "n8n-nodes-base.manualTrigger",
        "typeVersion": 1,
        "position": [
            780,
            600
        ]
        },
        {
        "parameters": {
            "url": "https://internal.users.n8n.cloud/webhook/level2-erp",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": true,
            "headerParameters": {
            "parameters": [
                {
                "name": "unique_id",
                "value": "recFIcD6UlSyxaVMQ"
                }
            ]
            },
            "options": {}
        },
        "id": "cc106fa0-6630-4c84-aea4-a4c7a3c149e9",
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.1,
        "position": [
            1000,
            500
        ],
        "credentials": {
            "httpHeaderAuth": {
            "id": "qeHdJdqqqaTC69cm",
            "name": "Course L2 Credentials"
            }
        }
        },
        {
        "parameters": {
            "operation": "search",
            "base": {
            "__rl": true,
            "value": "apprtKkVasbQDbFa1",
            "mode": "list",
            "cachedResultName": "All your base",
            "cachedResultUrl": "https://airtable.com/apprtKkVasbQDbFa1"
            },
            "table": {
            "__rl": true,
            "value": "tblInZ7jeNdlUOvxZ",
            "mode": "list",
            "cachedResultName": "Course L2, Workflow 1",
            "cachedResultUrl": "https://airtable.com/apprtKkVasbQDbFa1/tblInZ7jeNdlUOvxZ"
            },
            "options": {}
        },
        "id": "e5ae1927-b531-401c-9cb2-ecf1f2836ba6",
        "name": "Airtable",
        "type": "n8n-nodes-base.airtable",
        "typeVersion": 2,
        "position": [
            1000,
            700
        ],
        "credentials": {
            "airtableTokenApi": {
            "id": "MIplo6lY3AEsdf7L",
            "name": "Airtable Personal Access Token account 4"
            }
        }
        },
        {
        "parameters": {
            "mode": "combine",
            "mergeByFields": {
            "values": [
                {
                "field1": "customerID",
                "field2": "customerID"
                }
            ]
            },
            "options": {}
        },
        "id": "1cddc984-7fca-45e0-83b8-0c502cb4c78c",
        "name": "Merge",
        "type": "n8n-nodes-base.merge",
        "typeVersion": 2.1,
        "position": [
            1220,
            600
        ]
        },
        {
        "parameters": {
            "sortFieldsUi": {
            "sortField": [
                {
                "fieldName": "orderPrice",
                "order": "descending"
                }
            ]
            },
            "options": {}
        },
        "id": "2f55af2e-f69b-4f61-a9e5-c7eefaad93ba",
        "name": "Sort",
        "type": "n8n-nodes-base.sort",
        "typeVersion": 1,
        "position": [
            1440,
            600
        ]
        },
        {
        "parameters": {
            "conditions": {
            "options": {
                "caseSensitive": true,
                "leftValue": "",
                "typeValidation": "strict"
            },
            "conditions": [
                {
                "id": "d3afe65c-7c80-4caa-9d1c-33c62fbc2197",
                "leftValue": "={{ $json.region }}",
                "rightValue": "Americas",
                "operator": {
                    "type": "string",
                    "operation": "equals",
                    "name": "filter.operator.equals"
                }
                }
            ],
            "combinator": "and"
            },
            "options": {}
        },
        "id": "2ed874a9-5bcf-4cc9-9b52-ea503a562892",
        "name": "If",
        "type": "n8n-nodes-base.if",
        "typeVersion": 2,
        "position": [
            1660,
            500
        ]
        },
        {
        "parameters": {
            "operation": "toJson",
            "mode": "each",
            "options": {
            "fileName": "=report_orderID_{{ $('If').item.json.orderID }}.json"
            }
        },
        "id": "d93b4429-2200-4a84-8505-16266fedfccd",
        "name": "Convert to File",
        "type": "n8n-nodes-base.convertToFile",
        "typeVersion": 1.1,
        "position": [
            1880,
            500
        ]
        },
        {
        "parameters": {
            "authentication": "webhook",
            "content": "I sent the file using email with the label ID  and wrote the binary file {file name}. My ID: 123",
            "options": {}
        },
        "id": "26f43f2c-1422-40de-9f40-dd2d80926b1c",
        "name": "Discord",
        "type": "n8n-nodes-base.discord",
        "typeVersion": 2,
        "position": [
            2320,
            500
        ],
        "credentials": {
            "discordWebhookApi": {
            "id": "WEBrtPdoLrhlDYKr",
            "name": "L2 Course Discord Webhook account"
            }
        }
        },
        {
        "parameters": {
            "batchSize": 5,
            "options": {}
        },
        "id": "0fa1fbf6-fe77-4044-a445-c49a1db37dec",
        "name": "Loop Over Items",
        "type": "n8n-nodes-base.splitInBatches",
        "typeVersion": 3,
        "position": [
            1660,
            700
        ]
        },
        {
        "parameters": {
            "assignments": {
            "assignments": [
                {
                "id": "ce839b80-c50d-48f5-9a24-bb2df6fdd2ff",
                "name": "customerEmail",
                "value": "={{ $json.customerEmail }}",
                "type": "string"
                },
                {
                "id": "0c613366-3808-45a2-89cc-b34c7b9f3fb7",
                "name": "region",
                "value": "={{ $json.region }}",
                "type": "string"
                },
                {
                "id": "0f19a88c-deb0-4119-8965-06ed62a840b2",
                "name": "customerSince",
                "value": "={{ $json.customerSince }}",
                "type": "string"
                },
                {
                "id": "a7e890d6-86af-4839-b5df-d2a4efe923f7",
                "name": "orderPrice",
                "value": "={{ $json.orderPrice }}",
                "type": "number"
                }
            ]
            },
            "options": {}
        },
        "id": "09b8584c-4ead-4007-a6cd-edaa4669a757",
        "name": "Edit Fields",
        "type": "n8n-nodes-base.set",
        "typeVersion": 3.3,
        "position": [
            1880,
            700
        ]
        },
        {
        "parameters": {
            "operation": "formatDate",
            "date": "={{ $json.customerSince }}",
            "options": {
            "includeInputFields": true
            }
        },
        "id": "c96fae90-e080-48dd-9bff-3e4506aafb86",
        "name": "Date & Time",
        "type": "n8n-nodes-base.dateTime",
        "typeVersion": 2,
        "position": [
            2100,
            700
        ]
        },
        {
        "parameters": {
            "options": {
            "fileName": "={{$runIndex > 0 ? 'file_low_orders':'file_high_orders'}}"
            }
        },
        "id": "43dc8634-2f16-442b-a754-89f47c51c591",
        "name": "Convert to File1",
        "type": "n8n-nodes-base.convertToFile",
        "typeVersion": 1.1,
        "position": [
            2320,
            700
        ]
        },
        {
        "parameters": {
            "authentication": "webhook",
            "content": "I created the spreadsheet {file name}. My ID: 123",
            "options": {}
        },
        "id": "05da1c22-d1f6-4ea6-9102-f74f9ae2e9d3",
        "name": "Discord1",
        "type": "n8n-nodes-base.discord",
        "typeVersion": 2,
        "position": [
            2540,
            700
        ],
        "credentials": {
            "discordWebhookApi": {
            "id": "WEBrtPdoLrhlDYKr",
            "name": "L2 Course Discord Webhook account"
            }
        }
        }
    ],
    "connections": {
        "Gmail": {
        "main": [
            [
            {
                "node": "Discord",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "When clicking \"Execute workflow\"": {
        "main": [
            [
            {
                "node": "HTTP Request",
                "type": "main",
                "index": 0
            },
            {
                "node": "Airtable",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "HTTP Request": {
        "main": [
            [
            {
                "node": "Merge",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Airtable": {
        "main": [
            [
            {
                "node": "Merge",
                "type": "main",
                "index": 1
            }
            ]
        ]
        },
        "Merge": {
        "main": [
            [
            {
                "node": "Sort",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Sort": {
        "main": [
            [
            {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
            },
            {
                "node": "If",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "If": {
        "main": [
            [
            {
                "node": "Convert to File",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Convert to File": {
        "main": [
            [
            {
                "node": "Gmail",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Loop Over Items": {
        "main": [
            null,
            [
            {
                "node": "Edit Fields",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Edit Fields": {
        "main": [
            [
            {
                "node": "Date & Time",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Date & Time": {
        "main": [
            [
            {
                "node": "Convert to File1",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Convert to File1": {
        "main": [
            [
            {
                "node": "Discord1",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Discord1": {
        "main": [
            [
            {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
            }
            ]
        ]
        }
    },
    "pinData": {}
    }
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top