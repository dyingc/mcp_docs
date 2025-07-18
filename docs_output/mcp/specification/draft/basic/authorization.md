# Authorization - Model Context Protocol

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [Ruby SDK](https://github.com/modelcontextprotocol/ruby-sdk)
* [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

##### 2025-03-26 (Latest)

  * [Specification](/specification/2025-03-26)
  * [Key Changes](/specification/2025-03-26/changelog)
  * [Architecture](/specification/2025-03-26/architecture)
  * Base Protocol

  * Client Features

  * Server Features

##### 2024-11-05

  * [Specification](/specification/2024-11-05)
  * [Architecture](/specification/2024-11-05/architecture)
  * Base Protocol

  * Client Features

  * Server Features

##### draft

  * [Specification](/specification/draft)
  * [Key Changes](/specification/draft/changelog)
  * [Architecture](/specification/draft/architecture)
  * Base Protocol

    * [Overview](/specification/draft/basic)
    * [Lifecycle](/specification/draft/basic/lifecycle)
    * [Transports](/specification/draft/basic/transports)
    * [Authorization](/specification/draft/basic/authorization)
    * [Security Best Practices](/specification/draft/basic/security_best_practices)
    * Utilities

  * Client Features

  * Server Features

##### Resources

  * [Versioning](/specification/versioning)
  * [Contributions](/specification/contributing)

[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](/)

Search...

⌘K

Search...

Navigation

Base Protocol

Authorization

[User Guide](/introduction)[Specification](/specification/2025-03-26)

[User Guide](/introduction)[Specification](/specification/2025-03-26)

* [GitHub](https://github.com/modelcontextprotocol)

**Protocol Revision** : draft

## 

​

Introduction

### 

​

Purpose and Scope

The Model Context Protocol provides authorization capabilities at the transport level, enabling MCP clients to make requests to restricted MCP servers on behalf of resource owners. This specification defines the authorization flow for HTTP-based transports.

### 

​

Protocol Requirements

Authorization is **OPTIONAL** for MCP implementations. When supported:

  * Implementations using an HTTP-based transport **SHOULD** conform to this specification.
  * Implementations using an STDIO transport **SHOULD NOT** follow this specification, and instead retrieve credentials from the environment.
  * Implementations using alternative transports **MUST** follow established security best practices for their protocol.

### 

​

Standards Compliance

This authorization mechanism is based on established specifications listed below, but implements a selected subset of their features to ensure security and interoperability while maintaining simplicity:

  * OAuth 2.1 IETF DRAFT ([draft-ietf-oauth-v2-1-12](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12))
  * OAuth 2.0 Authorization Server Metadata ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))
  * OAuth 2.0 Dynamic Client Registration Protocol ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))
  * OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728))

## 

​

Authorization Flow

### 

​

Overview

  1. MCP authorization servers **MUST** implement OAuth 2.1 with appropriate security measures for both confidential and public clients.

  2. MCP authorization servers and MCP clients **SHOULD** support the OAuth 2.0 Dynamic Client Registration Protocol ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591)).

  3. MCP servers **MUST** implement OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)). MCP clients **MUST** use OAuth 2.0 Protected Resource Metadata for authorization server discovery.

  4. MCP authorization servers **MUST** provide OAuth 2.0 Authorization Server Metadata ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414)). MCP clients **MUST** use the OAuth 2.0 Authorization Server Metadata.

### 

​

Roles

A protected MCP server acts as an [OAuth 2.1 resource server](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-12.html#name-roles), capable of accepting and responding to protected resource requests using access tokens.

An MCP client acts as an [OAuth 2.1 client](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-12.html#name-roles), making protected resource requests on behalf of a resource owner.

The authorization server is responsible for interacting with the user (if necessary) and issuing access tokens for use at the MCP server. The implementation details of the authorization server are beyond the scope of this specification. It may be hosted with the resource server or a separate entity. The [Authorization Server Discovery section](/_sites/modelcontextprotocol.io/specification/draft/basic/authorization#authorization-server-discovery) specifies how an MCP server indicates the location of its corresponding authorization server to a client.

### 

​

Authorization Server Discovery

This section describes the mechanisms by which MCP servers advertise their associated authorization servers to MCP clients, as well as the discovery process through which MCP clients can determine authorization server endpoints and supported capabilities.

#### 

​

Authorization Server Location

MCP servers **MUST** implement the OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)) specification to indicate the locations of authorization servers. The Protected Resource Metadata document returned by the MCP server **MUST** include the `authorization_servers` field containing at least one authorization server.

The specific use of `authorization_servers` is beyond the scope of this specification; implementers should consult OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728)) for guidance on implementation details.

Implementors should note that Protected Resource Metadata documents can define multiple authorization servers. The responsibility for selecting which authorization server to use lies with the MCP client, following the guidelines specified in [RFC9728 Section 7.6 “Authorization Servers”](https://datatracker.ietf.org/doc/html/rfc9728#name-authorization-servers).

MCP servers **MUST** use the HTTP header `WWW-Authenticate` when returning a _401 Unauthorized_ to indicate the location of the resource server metadata URL as described in [RFC9728 Section 5.1 “WWW-Authenticate Response”](https://datatracker.ietf.org/doc/html/rfc9728#name-www-authenticate-response).

MCP clients **MUST** be able to parse `WWW-Authenticate` headers and respond appropriately to `HTTP 401 Unauthorized` responses from the MCP server.

#### 

​

Server Metadata Discovery

MCP clients **MUST** follow the OAuth 2.0 Authorization Server Metadata [RFC8414](https://datatracker.ietf.org/doc/html/rfc8414) specification to obtain the information required to interact with the authorization server.

#### 

​

Sequence Diagram

The following diagram outlines an example flow:

### 

​

Dynamic Client Registration

MCP clients and authorization servers **SHOULD** support the OAuth 2.0 Dynamic Client Registration Protocol [RFC7591](https://datatracker.ietf.org/doc/html/rfc7591) to allow MCP clients to obtain OAuth client IDs without user interaction. This provides a standardized way for clients to automatically register with new authorization servers, which is crucial for MCP because:

  * Clients may not know all possible MCP servers and their authorization servers in advance.
  * Manual registration would create friction for users.
  * It enables seamless connection to new MCP servers and their authorization servers.
  * Authorization servers can implement their own registration policies.

Any MCP authorization servers that _do not_ support Dynamic Client Registration need to provide alternative ways to obtain a client ID (and, if applicable, client credentials). For one of these authorization servers, MCP clients will have to either:

  1. Hardcode a client ID (and, if applicable, client credentials) specifically for the MCP client to use when interacting with that authorization server, or
  2. Present a UI to users that allows them to enter these details, after registering an OAuth client themselves (e.g., through a configuration interface hosted by the server).

### 

​

Authorization Flow Steps

The complete Authorization flow proceeds as follows:

### 

​

Access Token Usage

#### 

​

Token Requirements

Access token handling when making requests to MCP servers **MUST** conform to the requirements defined in [OAuth 2.1 Section 5 “Resource Requests”](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5). Specifically:

  1. MCP client **MUST** use the Authorization request header field defined in [OAuth 2.1 Section 5.1.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.1.1):

Copy
    
    
    Authorization: Bearer <access-token>
    

Note that authorization **MUST** be included in every HTTP request from client to server, even if they are part of the same logical session.

  2. Access tokens **MUST NOT** be included in the URI query string

Example request:

Copy
    
    
    GET /v1/contexts HTTP/1.1
    Host: mcp.example.com
    Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
    

#### 

​

Token Handling

MCP servers, acting in their role as an OAuth 2.1 resource server, **MUST** validate access tokens as described in [OAuth 2.1 Section 5.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.2). If validation fails, servers **MUST** respond according to [OAuth 2.1 Section 5.3](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-5.3) error handling requirements. Invalid or expired tokens **MUST** receive a HTTP 401 response.

MCP clients **MUST NOT** send tokens to the MCP server other than ones issued by the MCP server’s authorization server.

MCP authorization servers **MUST** only accept tokens that are valid for use with their own resources.

MCP servers **MUST NOT** accept or transit any other tokens.

### 

​

Error Handling

Servers **MUST** return appropriate HTTP status codes for authorization errors:

Status Code| Description| Usage  
---|---|---  
401| Unauthorized| Authorization required or token invalid  
403| Forbidden| Invalid scopes or insufficient permissions  
400| Bad Request| Malformed authorization request  
  
## 

​

Security Considerations

Implementations **MUST** follow OAuth 2.1 security best practices as laid out in [OAuth 2.1 Section 7. “Security Considerations”](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#name-security-considerations).

### 

​

Token Theft

Attackers who obtain tokens stored by the client, or tokens cached or logged on the server can access protected resources with requests that appear legitimate to resource servers.

Clients and servers **MUST** implement secure token storage and follow OAuth best practices, as outlined in [OAuth 2.1, Section 7.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-7.1).

MCP authorization servers SHOULD issue short-lived access tokens to reduce the impact of leaked tokens. For public clients, MCP authorization servers **MUST** rotate refresh tokens as described in [OAuth 2.1 Section 4.3.1 “Refresh Token Grant”](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-4.3.1).

### 

​

Communication Security

Implementations **MUST** follow [OAuth 2.1 Section 1.5 “Communication Security”](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-1.5).

Specifically:

  1. All authorization server endpoints **MUST** be served over HTTPS.
  2. All redirect URIs **MUST** be either `localhost` or use HTTPS.

### 

​

Authorization Code Protection

An attacker who has gained access to an authorization code contained in an authorization response can try to redeem the authorization code for an access token or otherwise make use of the authorization code. (Further described in [OAuth 2.1 Section 7.5](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-7.5))

To mitigate this, MCP clients **MUST** implement PKCE according to [OAuth 2.1 Section 7.5.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-7.5.2). PKCE helps prevent authorization code interception and injection attacks by requiring clients to create a secret verifier-challenge pair, ensuring that only the original requestor can exchange an authorization code for tokens.

### 

​

Open Redirection

An attacker may craft malicious redirect URIs to direct users to phishing sites.

MCP clients **MUST** have redirect URIs registered with the authorization server.

Authorization servers **MUST** validate exact redirect URIs against pre-registered values to prevent redirection attacks.

MCP clients **SHOULD** use and verify state parameters in the authorization code flow and discard any results that do not include or have a mismatch with the original state.

Authorization servers **MUST** take precautions to prevent redirecting user agents to untrusted URI’s, following suggestions laid out in [OAuth 2.1 Section 7.12.2](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-12#section-7.12.2)

Authorization servers **SHOULD** only automatically redirect the user agent if it trusts the redirection URI. If the URI is not trusted, the authorization server MAY inform the user and rely on the user to make the correct decision.

### 

​

Confused Deputy Problem

Attackers can exploit MCP servers acting as intermediaries to third-party APIs, leading to [confused deputy vulnerabilities](/specification/draft/basic/security_best_practices#confused-deputy-problem). By using stolen authorization codes, they can obtain access tokens without user consent.

MCP proxy servers using static client IDs **MUST** obtain user consent for each dynamically registered client before forwarding to third-party authorization servers (which may require additional consent).

### 

​

Access Token Privilege Restriction

An attacker can gain unauthorized access or otherwise compromise a MCP server if the server accepts tokens issued for other resources.

This vulnerability has two critical dimensions:

  1. **Audience validation failures.** When an MCP server doesn’t verify that tokens were specifically intended for it (for example, via the audience claim, as mentioned in [RFC9068](https://www.rfc-editor.org/rfc/rfc9068.html)), it may accept tokens originally issued for other services. This breaks a fundamental OAuth security boundary, allowing attackers to reuse legitimate tokens across different services than intended.
  2. **Token passthrough.** If the MCP server not only accepts tokens with incorrect audiences but also forwards these unmodified tokens to downstream services, it can potentially cause the [“confused deputy” problem](/_sites/modelcontextprotocol.io/specification/draft/basic/authorization#confused-deputy-problem), where the downstream API may incorrectly trust the token as if it came from the MCP server or assume the token was validated by the upstream API. See the [Token Passthrough section](/specification/draft/basic/security_best_practices#token-passthrough) of the Security Best Practices guide for additional details.

MCP servers **MUST** validate access tokens before processing the request, ensuring the access token is issued specifically for the MCP server, and take all necessary steps to ensure no data is returned to unauthorized parties.

A MCP server **MUST** follow the guidelines in [OAuth 2.1 - Section 5.2](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-12.html#section-5.2) to validate inbound tokens.

MCP servers **MUST** only accept tokens specifically intended for themselves.

If the MCP server makes requests to upstream APIs, it may act as an OAuth client to them. The access token used at the upstream API is a seperate token, issued by the upstream authorization server. The MCP server **MUST NOT** pass through the token it received from the MCP client.

If the authorization server supports the `resource` parameter, it is recommended that implementers follow [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html) to prevent token misuse.

Was this page helpful?

YesNo

[Transports](/specification/draft/basic/transports)[Security Best Practices](/specification/draft/basic/security_best_practices)

On this page

  * Introduction
  * Purpose and Scope
  * Protocol Requirements
  * Standards Compliance
  * Authorization Flow
  * Overview
  * Roles
  * Authorization Server Discovery
  * Authorization Server Location
  * Server Metadata Discovery
  * Sequence Diagram
  * Dynamic Client Registration
  * Authorization Flow Steps
  * Access Token Usage
  * Token Requirements
  * Token Handling
  * Error Handling
  * Security Considerations
  * Token Theft
  * Communication Security
  * Authorization Code Protection
  * Open Redirection
  * Confused Deputy Problem
  * Access Token Privilege Restriction

Assistant

Responses are generated using AI and may contain mistakes.