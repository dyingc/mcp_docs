# GitHub - radareorg/r2ai: local language model for radare2

[ radareorg ](/radareorg) / **[r2ai](/radareorg/r2ai) ** Public

  * ###  Uh oh! 

There was an error while loading. [Please reload this page]().

  * [ Notifications ](/login?return_to=%2Fradareorg%2Fr2ai) You must be signed in to change notification settings
  * [ Fork 35 ](/login?return_to=%2Fradareorg%2Fr2ai)
  * [ Star  282 ](/login?return_to=%2Fradareorg%2Fr2ai)

local language model for radare2 

[www.radare.org](https://www.radare.org "https://www.radare.org")

### License

[ MIT license ](/radareorg/r2ai/blob/master/LICENSE)

[ 282 stars ](/radareorg/r2ai/stargazers) [ 35 forks ](/radareorg/r2ai/forks) [ Branches ](/radareorg/r2ai/branches) [ Tags ](/radareorg/r2ai/tags) [ Activity ](/radareorg/r2ai/activity)

[ Star  ](/login?return_to=%2Fradareorg%2Fr2ai)

[ Notifications ](/login?return_to=%2Fradareorg%2Fr2ai) You must be signed in to change notification settings

# radareorg/r2ai

master

[Branches](/radareorg/r2ai/branches)[Tags](/radareorg/r2ai/tags)

[](/radareorg/r2ai/branches)[](/radareorg/r2ai/tags)

Go to file

Code

Open more actions menu

## Folders and files

Name| Name| Last commit message| Last commit date  
---|---|---|---  
  
## Latest commit

## History

[774 Commits](/radareorg/r2ai/commits/master/)[](/radareorg/r2ai/commits/master/)  
[.github/workflows](/radareorg/r2ai/tree/master/.github/workflows "This path skips through empty directories")| [.github/workflows](/radareorg/r2ai/tree/master/.github/workflows "This path skips through empty directories")|  |   
[Attic](/radareorg/r2ai/tree/master/Attic "Attic")| [Attic](/radareorg/r2ai/tree/master/Attic "Attic")|  |   
[decai](/radareorg/r2ai/tree/master/decai "decai")| [decai](/radareorg/r2ai/tree/master/decai "decai")|  |   
[dist/docker](/radareorg/r2ai/tree/master/dist/docker "This path skips through empty directories")| [dist/docker](/radareorg/r2ai/tree/master/dist/docker "This path skips through empty directories")|  |   
[doc](/radareorg/r2ai/tree/master/doc "doc")| [doc](/radareorg/r2ai/tree/master/doc "doc")|  |   
[examples](/radareorg/r2ai/tree/master/examples "examples")| [examples](/radareorg/r2ai/tree/master/examples "examples")|  |   
[openapiproxy](/radareorg/r2ai/tree/master/openapiproxy "openapiproxy")| [openapiproxy](/radareorg/r2ai/tree/master/openapiproxy "openapiproxy")|  |   
[py](/radareorg/r2ai/tree/master/py "py")| [py](/radareorg/r2ai/tree/master/py "py")|  |   
[server](/radareorg/r2ai/tree/master/server "server")| [server](/radareorg/r2ai/tree/master/server "server")|  |   
[src](/radareorg/r2ai/tree/master/src "src")| [src](/radareorg/r2ai/tree/master/src "src")|  |   
[.gitignore](/radareorg/r2ai/blob/master/.gitignore ".gitignore")| [.gitignore](/radareorg/r2ai/blob/master/.gitignore ".gitignore")|  |   
[LICENSE](/radareorg/r2ai/blob/master/LICENSE "LICENSE")| [LICENSE](/radareorg/r2ai/blob/master/LICENSE "LICENSE")|  |   
[MANIFEST.in](/radareorg/r2ai/blob/master/MANIFEST.in "MANIFEST.in")| [MANIFEST.in](/radareorg/r2ai/blob/master/MANIFEST.in "MANIFEST.in")|  |   
[Makefile](/radareorg/r2ai/blob/master/Makefile "Makefile")| [Makefile](/radareorg/r2ai/blob/master/Makefile "Makefile")|  |   
[README.md](/radareorg/r2ai/blob/master/README.md "README.md")| [README.md](/radareorg/r2ai/blob/master/README.md "README.md")|  |   
[make.bat](/radareorg/r2ai/blob/master/make.bat "make.bat")| [make.bat](/radareorg/r2ai/blob/master/make.bat "make.bat")|  |   
View all files  
  
## Repository files navigation
    
    
    ,______  .______ .______  ,___
    : __   \ \____  |:      \ : __|
    |  \____|/  ____||  _,_  || : |
    |   :  \ \   .  ||   :   ||   |
    |   |___\ \__:__||___|   ||   |
    |___|        :       |___||___|
                 *
    

[![ci](https://github.com/radareorg/r2ai/actions/workflows/ci.yml/badge.svg)](https://github.com/radareorg/r2ai/actions/workflows/ci.yml)

Run a language model to entertain you or help answering questions about radare2 or reverse engineering in general. The language model may be local (running without Internet on your host) or remote (e.g if you have an API key). Note that models used by r2ai are pulled from external sources which may behave different or respond unreliable information. That's why there's an ongoing effort into improving the post-finetuning using memgpt-like techniques which can't get better without your help!

[![](/radareorg/r2ai/raw/master/doc/images/r2clippy.jpg)](/radareorg/r2ai/blob/master/doc/images/r2clippy.jpg)

## Components

R2AI repository contains four different projects:

Recommended plugins:

  * **r2ai-plugin** (`src/` directory) 
    * Native plugin written in C
    * adds r2ai command inside r2
  * **decai** (r2js plugin focus on decompilation) 
    * adds 'decai' command to the r2 shell
    * talks to local or remote services with curl
    * focus on decompilation

Deprecated implementations:

  * **r2ai-python** cli tool (`py/` directory) 
    * r2-like repl using r2pipe to comunicate with r2
    * supports auto solving mode
    * client and server openapi protocol
    * download and manage models from huggingface
  * **r2ai-server**
    * favour _ollama_ instead
    * list and select models downloaded from r2ai
    * simple cli tool to start local openapi webservers
    * supports llamafile, llamacpp, r2ai-w and kobaldcpp

## Features

  * Support Auto mode to solve tasks using function calling
  * Use local and remote language models (llama, ollama, openai, anthropic, ..)
  * Support OpenAI, Anthropic, Bedrock
  * Index large codebases or markdown books using a vector database
  * Slurp file and perform actions on that
  * Embed the output of an r2 command and resolve questions on the given data
  * Define different system-level assistant role
  * Set environment variables to provide context to the language model
  * Live with repl and batch mode from cli or r2 prompt
  * Scriptable via r2pipe
  * Use different models, dynamically adjust query template
  * Load multiple models and make them talk between them

## Installation

### Radare2 Package Manager

The recommended way to install any of the r2ai components is via r2pm:

You can find all the packages with `r2pm -s r2ai`:
    
    
    $ r2pm -s r2ai
    r2ai-py             run a local language model integrated with radare2
    r2ai-py-plugin      r2ai plugin for radare2
    r2ai-plugin         r2ai plugin rewritten in plain C
    r2ai-server         start a language model webserver in local
    decai               r2ai r2js subproject with focus on LLM decompilation for radare2
    $

### From sources

Running `make` on the root directory will instruct you where the sub-projects are, just run the `install`/`user-install` targets in there.
    
    
    $ make
    Usage: Run 'make' in the following subdirectories instead
    src/    - Modern C rewrite in form of a native r2 plugin
    py/     - The old Python cli and r2 plugin
    decai/  - r2js plugin with focus on decompiling
    server/ - shellscript to easily run llamacpp and other
    $

## Running r2ai

### Launch r2ai

  * The r2ai-plugin adds the **r2ai** command to the radare2 shell: `r2 -qc r2ai-r`
  * If you installed via r2pm, you can execute it like this: `r2pm -r r2ai`
  * Otherwise, `./r2ai.sh [/absolute/path/to/binary]`

If you have an **API key** , put it in the adequate file:

AI | API key  
---|---  
OpenAI | `$HOME/.r2ai.openai-key`  
Gemini | `$HOME/.r2ai.gemini-key`  
Anthropic | `$HOME/.r2ai.anthropic-key`  
Mistral | `$HOME/.r2ai.mistral-key`  
... |   
  
Example using an Anthropic API key:
    
    
    $ cat ~/.r2ai.anthropic-key 
    sk-ant-api03-CENSORED
    

## Videos

  * <https://infosec.exchange/@radareorg/111946255058894583>

## About

local language model for radare2 

[www.radare.org](https://www.radare.org "https://www.radare.org")

### Topics

[ ai ](/topics/ai "Topic: ai") [ radare2 ](/topics/radare2 "Topic: radare2") [ radare2-plugin ](/topics/radare2-plugin "Topic: radare2-plugin") [ llm ](/topics/llm "Topic: llm")

### Resources

Readme 

### License

MIT license 

###  Uh oh! 

There was an error while loading. [Please reload this page]().

[ Activity](/radareorg/r2ai/activity)

[ Custom properties](/radareorg/r2ai/custom-properties)

### Stars

[ **282** stars](/radareorg/r2ai/stargazers)

### Watchers

[ **6** watching](/radareorg/r2ai/watchers)

### Forks

[ **35** forks](/radareorg/r2ai/forks)

[ Report repository ](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fradareorg%2Fr2ai&report=radareorg+%28user%29)

##  [Releases 14](/radareorg/r2ai/releases)

[ 0.9.6 Latest  May 13, 2025 ](/radareorg/r2ai/releases/tag/0.9.6)

[\+ 13 releases](/radareorg/r2ai/releases)

## Sponsor this project

###  Uh oh! 

There was an error while loading. [Please reload this page]().

  * ![open_collective](https://github.githubassets.com/assets/open_collective-0a706523753d.svg) [opencollective.com/**radareorg**](https://opencollective.com/radareorg)

##  [Packages 0](/orgs/radareorg/packages?repo_name=r2ai)

No packages published   

###  Uh oh! 

There was an error while loading. [Please reload this page]().

##  [Contributors 15](/radareorg/r2ai/graphs/contributors)

  * [ ![@radare](https://avatars.githubusercontent.com/u/917142?s=64&v=4) ](https://github.com/radare)
  * [ ![@dnakov](https://avatars.githubusercontent.com/u/3777433?s=64&v=4) ](https://github.com/dnakov)
  * [ ![@nitanmarcel](https://avatars.githubusercontent.com/u/41646249?s=64&v=4) ](https://github.com/nitanmarcel)
  * [ ![@trufae](https://avatars.githubusercontent.com/u/6431515?s=64&v=4) ](https://github.com/trufae)
  * [ ![@cryptax](https://avatars.githubusercontent.com/u/2493690?s=64&v=4) ](https://github.com/cryptax)
  * [ ![@riptl](https://avatars.githubusercontent.com/u/21371810?s=64&v=4) ](https://github.com/riptl)
  * [ ![@prodrigestivill](https://avatars.githubusercontent.com/u/1381592?s=64&v=4) ](https://github.com/prodrigestivill)
  * [ ![@FernandoDoming](https://avatars.githubusercontent.com/u/6620286?s=64&v=4) ](https://github.com/FernandoDoming)
  * [ ![@brainstorm](https://avatars.githubusercontent.com/u/175587?s=64&v=4) ](https://github.com/brainstorm)
  * [ ![@sha0coder](https://avatars.githubusercontent.com/u/1431618?s=64&v=4) ](https://github.com/sha0coder)
  * [ ![@emilius3m](https://avatars.githubusercontent.com/u/8901201?s=64&v=4) ](https://github.com/emilius3m)
  * [ ![@stevenengland](https://avatars.githubusercontent.com/u/11787949?s=64&v=4) ](https://github.com/stevenengland)
  * [ ![@AdamBromiley](https://avatars.githubusercontent.com/u/40538037?s=64&v=4) ](https://github.com/AdamBromiley)
  * [ ![@Xplo8E](https://avatars.githubusercontent.com/u/55936553?s=64&v=4) ](https://github.com/Xplo8E)

## Languages

  * [ Python 50.9% ](/radareorg/r2ai/search?l=python)
  * [ C 32.6% ](/radareorg/r2ai/search?l=c)
  * [ JavaScript 10.3% ](/radareorg/r2ai/search?l=javascript)
  * [ TypeScript 2.3% ](/radareorg/r2ai/search?l=typescript)
  * [ Swift 1.8% ](/radareorg/r2ai/search?l=swift)
  * [ Makefile 1.1% ](/radareorg/r2ai/search?l=makefile)
  * Other 1.0%