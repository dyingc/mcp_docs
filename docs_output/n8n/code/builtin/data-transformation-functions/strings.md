# Data transformation functions for strings | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/data-transformation-functions/strings.md "Edit this page")

# Strings#

A reference document listing built-in convenience functions to support data transformation in [expressions](../../../../glossary/#expression-n8n) for strings.

JavaScript in expressions

You can use any JavaScript in expressions. Refer to [Expressions](../../../expressions/) for more information.

###  base64Encode(): A base64 encoded string. #

Encode a string as base64. 

* * *

###  base64Decode(): A plain string. #

Convert a base64 encoded string to a normal string. 

* * *

###  extractDomain(): String #

Extracts a domain from a string containing a valid URL. Returns undefined if none is found. 

* * *

###  extractEmail(): String #

Extracts an email from a string. Returns undefined if none is found. 

* * *

###  extractUrl(): String #

Extracts a URL from a string. Returns undefined if none is found. 

* * *

###  extractUrlPath(): String #

Extract the path but not the root domain from a URL. For example, `"https://example.com/orders/1/details".extractUrlPath()` returns `"/orders/1/details/"`. 

* * *

###  hash(algo?: Algorithm): String #

Returns a string hashed with the given algorithm. 

#### Function parameters#

algoOptionalString enum

Which hashing algorithm to use.

Default: `md5`

One of: `md5`, `base64`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`, `sha3`, `ripemd160`

* * *

###  isDomain(): Boolean #

Checks if a string is a domain. 

* * *

###  isEmail(): Boolean #

Checks if a string is an email. 

* * *

###  isEmpty(): Boolean #

Checks if a string is empty. 

* * *

###  isNotEmpty(): Boolean #

Checks if a string has content. 

* * *

###  isNumeric(): Boolean #

Checks if a string only contains digits. 

* * *

###  isUrl(): Boolean #

Checks if a string is a valid URL. 

* * *

###  parseJson(): Object #

Equivalent of `JSON.parse()`. Parses a string as a JSON object. 

* * *

###  quote(mark?: String): String #

Returns a string wrapped in the quotation marks. Default quotation is `"`. 

#### Function parameters#

markOptionalString

Which quote mark style to use.

Default: `" `

* * *

###  removeMarkdown(): String #

Removes Markdown formatting from a string. 

* * *

###  replaceSpecialChars(): String #

Replaces non-ASCII characters in a string with an ASCII representation. 

* * *

###  removeTags(): String #

Remove tags, such as HTML or XML, from a string. 

* * *

###  toBoolean(): Boolean #

Convert a string to a boolean. `"false"`, `"0"`, `""`, and `"no"` convert to `false`. 

* * *

###  toDateTime(): Date #

Converts a string to a [Luxon date object](https://docs.n8n.io/code/cookbook/luxon/). 

* * *

###  toDecimalNumber(): Number #

See toFloat

* * *

###  toFloat(): Number #

Converts a string to a decimal number. 

* * *

###  toInt(): Number #

Converts a string to an integer. 

* * *

###  toSentenceCase(): String #

Formats a string to sentence case. 

* * *

###  toSnakeCase(): String #

Formats a string to snake case. 

* * *

###  toTitleCase(): String #

Formats a string to title case. Will not change already uppercase letters to prevent losing information from acronyms and trademarks such as iPhone or FAANG. 

* * *

###  toWholeNumber(): Number #

Converts a string to a whole number. 

* * *

###  urlDecode(entireString?: Boolean): String #

Decodes a URL-encoded string. It decodes any percent-encoded characters in the input string, and replaces them with their original characters. 

#### Function parameters#

entireStringOptionalBoolean

Whether to decode characters that are part of the URI syntax (true) or not (false).

* * *

###  urlEncode(entireString?: Boolean): String #

Encodes a string to be used/included in a URL. 

#### Function parameters#

entireStringOptionalBoolean

Whether to encode characters that are part of the URI syntax (true) or not (false).

* * *

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top