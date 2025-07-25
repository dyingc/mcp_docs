# CLI commands | n8n Docs

[ ](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/cli-commands.md "Edit this page")

# CLI commands for n8n#

n8n includes a CLI (command line interface), allowing you to perform actions using the CLI rather than the n8n editor. These include starting workflows, and exporting and importing workflows and credentials.

## Running CLI commands#

You can use CLI commands with self-hosted n8n. Depending on how you choose to install n8n, there are differences in how to run the commands:

  * npm: the `n8n` command is directly available. The documentation uses this in the examples below.
  * Docker: the `n8n` command is available within your Docker container:
        
        1

| 
        
        docker exec -u node -it <n8n-container-name> <n8n-cli-command>
          
  
---|---  
  

## Start a workflow#

You can start workflows directly using the CLI.

Execute a saved workflow by its ID:
    
    
    1

| 
    
    
    n8n execute --id <ID>
      
  
---|---  
  
## Change the active status of a workflow#

You can change the active status of a workflow using the CLI.

Restart required

These commands operate on your n8n database. If you execute them while n8n is running, the changes don't take effect until you restart n8n.

Set the active status of a workflow by its ID to false:
    
    
    1

| 
    
    
    n8n update:workflow --id=<ID> --active=false
      
  
---|---  
  
Set the active status of a workflow by its ID to true:
    
    
    1

| 
    
    
    n8n update:workflow --id=<ID> --active=true
      
  
---|---  
  
Set the active status to false for all the workflows:
    
    
    1

| 
    
    
    n8n update:workflow --all --active=false
      
  
---|---  
  
Set the active status to true for all the workflows:
    
    
    1

| 
    
    
    n8n update:workflow --all --active=true
      
  
---|---  
  
## Export workflows and credentials#

You can export your workflows and credentials from n8n using the CLI.

Command flags:

Flag | Description  
---|---  
\--help | Help prompt.  
\--all | Exports all workflows/credentials.  
\--backup | Sets --all --pretty --separate for backups. You can optionally set --output.  
\--id | The ID of the workflow to export.  
\--output | Outputs file name or directory if using separate files.  
\--pretty | Formats the output in an easier to read fashion.  
\--separate | Exports one file per workflow (useful for versioning). Must set a directory using --output.  
\--decrypted | Exports the credentials in a plain text format.  
  
### Workflows#

Export all your workflows to the standard output (terminal):
    
    
    1

| 
    
    
    n8n export:workflow --all
      
  
---|---  
  
Export a workflow by its ID and specify the output file name:
    
    
    1

| 
    
    
    n8n export:workflow --id=<ID> --output=file.json
      
  
---|---  
  
Export all workflows to a specific directory in a single file:
    
    
    1

| 
    
    
    n8n export:workflow --all --output=backups/latest/file.json
      
  
---|---  
  
Export all the workflows to a specific directory using the `--backup` flag (details above):
    
    
    1

| 
    
    
    n8n export:workflow --backup --output=backups/latest/
      
  
---|---  
  
### Credentials#

Export all your credentials to the standard output (terminal):
    
    
    1

| 
    
    
    n8n export:credentials --all
      
  
---|---  
  
Export credentials by their ID and specify the output file name:
    
    
    1

| 
    
    
    n8n export:credentials --id=<ID> --output=file.json
      
  
---|---  
  
Export all credentials to a specific directory in a single file:
    
    
    1

| 
    
    
    n8n export:credentials --all --output=backups/latest/file.json
      
  
---|---  
  
Export all the credentials to a specific directory using the `--backup` flag (details above):
    
    
    1

| 
    
    
    n8n export:credentials --backup --output=backups/latest/
      
  
---|---  
  
Export all the credentials in plain text format. You can use this to migrate from one installation to another that has a different secret key in the configuration file.

Sensitive information

All sensitive information is visible in the files.
    
    
    1

| 
    
    
    n8n export:credentials --all --decrypted --output=backups/decrypted.json
      
  
---|---  
  
## Import workflows and credentials#

You can import your workflows and credentials from n8n using the CLI.

Update the IDs

When exporting workflows and credentials, n8n also exports their IDs. If you have workflows and credentials with the same IDs in your existing database, they will be overwritten. To avoid this, delete or change the IDs before importing.

Available flags:

Flag | Description  
---|---  
\--help | Help prompt.  
\--input | Input file name or directory if you use --separate.  
\--projectId | Import the workflow or credential to the specified project. Can't be used with `--userId`.  
\--separate | Imports `*.json` files from directory provided by --input.  
\--userId | Import the workflow or credential to the specified user. Can't be used with `--projectId`.  
  
Migrating to SQLite

n8n limits workflow and credential names to 128 characters, but SQLite doesn't enforce size limits.

This might result in errors like **Data too long for column name** during the import process.

In this case, you can edit the names from the n8n interface and export again, or edit the JSON file directly before importing.

### Workflows#

Import workflows from a specific file:
    
    
    1

| 
    
    
    n8n import:workflow --input=file.json
      
  
---|---  
  
Import all the workflow files as JSON from the specified directory:
    
    
    1

| 
    
    
    n8n import:workflow --separate --input=backups/latest/
      
  
---|---  
  
### Credentials#

Import credentials from a specific file:
    
    
    1

| 
    
    
    n8n import:credentials --input=file.json
      
  
---|---  
  
Import all the credentials files as JSON from the specified directory:
    
    
    1

| 
    
    
    n8n import:credentials --separate --input=backups/latest/
      
  
---|---  
  
## License#

### Clear#

Clear your existing license from n8n's database and reset n8n to default features:
    
    
    1

| 
    
    
    n8n license:clear
      
  
---|---  
  
If your license includes [floating entitlements](../../glossary/#entitlement-n8n), running this command will also attempt to release them back to the pool, making them available for other instances.

### Info#

Display information about the existing license:
    
    
    1

| 
    
    
    n8n license:info
      
  
---|---  
  
## User management#

You can reset user management using the n8n CLI. This returns user management to its pre-setup state. It removes all user accounts.

Use this if you forget your password, and don't have SMTP set up to do password resets by email.
    
    
    1

| 
    
    
    n8n user-management:reset
      
  
---|---  
  
### Disable MFA for a user#

If a user loses their recovery codes you can disable MFA for a user with this command. The user will then be able to log back in to set up MFA again.
    
    
    1

| 
    
    
    n8n mfa:disable --email=johndoe@example.com
      
  
---|---  
  
### Disable LDAP#

You can reset the LDAP settings using the command below.
    
    
    1

| 
    
    
    n8n ldap:reset
      
  
---|---  
  
## Security audit#

You can run a [security audit](../securing/security-audit/) on your n8n instance, to detect common security issues.
    
    
    1

| 
    
    
    n8n audit
      
  
---|---  
  
Was this page helpful? 

Thanks for your feedback! 

Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs). 

Back to top