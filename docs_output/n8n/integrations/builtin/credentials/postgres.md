# Postgres credentials | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/credentials/postgres.md "Edit this page")

# Postgres credentials#

You can use these credentials to authenticate the following nodes:

  * [Postgres](../../app-nodes/n8n-nodes-base.postgres/)
  * [Agent](../../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
  * [Postgres Chat Memory](../../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat/)
  * [PGVector Vector Store](../../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector/)

Agent node users

The Agent node doesn't support SSH tunnels.

## Prerequisites#

[Create a user account](https://www.postgresql.org/docs/current/sql-createuser.html) on a Postgres server. 

## Supported authentication methods#

  * Database connection

## Related resources#

Refer to [Postgres's documentation](https://www.postgresql.org/docs/16/index.html) for more information about the service.

## Using database connection#

To configure this credential, you'll need:

  * The **Host** or domain name for the server.
  * The **Database** name.
  * A **User** name.
  * A user **Password**.
  * **Ignore SSL Issues** : Set whether the credential connects if SSL validation fails.
  * **SSL** : Choose whether to use SSL in your connection.
  * The **Port** number to use for the connection.
  * **SSH Tunnel** : Choose if you want to use SSH to encrypt the network connection with the Postgres server.

To set up the database connection:

  1. Enter the **Host** or domain name for the Postgres server. You can either run the `/conninfo` command to confirm the host name or run this query:
         
         1

| 
         
         SELECT inet_server_addr();
           
  
---|---  
  
  2. Enter the **Database** name. Run the `/conninfo` command to confirm the database name.

  3. Enter the **User** name of the user you wish to connect as.
  4. Enter the user's **Password**.
  5. **Ignore SSL Issues** : If you turn this on, the credential will connect even if SSL validation fails.
  6. **SSL** : Choose whether to use SSL in your connection. Refer to Postgres [SSL Support](https://www.postgresql.org/docs/16/libpq-ssl.html) for more information. Options include:
     * **Allow** : Sets the `ssl-mode` parameter to `allow`. First try a non-SSL connection; if that fails, try an SSL connection.
     * **Disable** : Sets the `ssl-mode` parameter to `disable`. Only try a non-SSL connection.
     * **Require** : Sets the `ssl-mode` parameter to `require`. Only try an SSL connection. If a root CA file is present, verify that a trusted certificate authority (CA) issued the server certificate.
  7. Enter the **Port** number to use for the connection. You can either run the `/conninfo` command to confirm the host name or run this query:
         
         1

| 
         
         SELECT inet_server_port();
           
  
---|---  
  
  8. **SSH Tunnel** : Turn this setting on to connect to the database over SSH. Refer to SSH tunnel limitations for some guidance around using SSH. Once turned on, you'll need:

     1. Select **SSH Authenticate with** to set the SSH Tunnel type to build:
        * Select **Password** if you want to connect to SSH using a password.
        * Select **Private Key** if you want to connect to SSH using an identity file (private key) and a passphrase.
     2. Enter the remote bind address you're connecting to as the **SSH Host**.
     3. **SSH Port** : Enter the local port number for the SSH tunnel.
     4. **SSH Postgres Port** : Enter the remote end of the tunnel, the port number the database server is using.
     5. **SSH User** : Enter the username to log in as.
     6. If you selected **Password** for SSH Authenticate with, add the user's **SSH Password**.
     7. If you selected **Private Key** for **SSH Authenticate with** :
        1. Add the contents of the **Private Key** or identity file used for SSH.
        2. If the **Private Key** was created with a passphrase, enter that **Passphrase**. If the **Private Ke** y has no passphrase, leave this field blank.

Refer to [Secure TCP/IP Connections with SSH Tunnels](https://www.postgresql.org/docs/16/ssh-tunnels.html) for more information.

### SSH tunnel limitations#

Only use the **SSH Tunnel** setting if:

  * You're using the credential with the [Postgres](../../app-nodes/n8n-nodes-base.postgres/) node (Agent node doesn't support SSH tunnels).
  * You have an SSH server running on the same machine as the Postgres server.
  * You have a user account that can log in using `ssh`.

Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top