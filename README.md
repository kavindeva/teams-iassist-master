# Teams-iAssist

Table of Contents
=================

1. [Project description](#project-description)
2. [Inspired from which](#inspired-from-which)
3. [Files involved](#files-involved)
4. [Package Installation](#Package-Installation)
5. [Configuration steps](#Configuration-steps)
6. [Test and Debug](#Test-and-Debug)
7. [Links to refer](#Links-to-refer)
8. [Note: PYJWT version conflict](#PYJWT-version-conflict)

<a name="projectdesc"></a>

# Project description:
This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how it has been integrated an 
iAssist with Microsoft Teams that accepts input queries from the user in Teams platform and echoes its responses back.

<a name="inspiredfrom"></a>

# Inspired from which?
This repository contains code for the Python version of the [Microsoft Bot Framework SDK](https://github.com/Microsoft/botframework-sdk), 
which is part of the Microsoft Bot Framework-a comprehensive framework for building enterprise-grade conversational AI experiences.

This SDK enables developers to model conversation and build sophisticated bot applications using Python.

Echo bot link inspired from this - [Echo Bot](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/02.echo-bot)

This Microsoft Teams integration with iAssist is inspired from the above echo bot repository. This echo bot and also all
other bot builder samples are built with aiohttp(a python web framework). But to deploy it on IIS this project has been developed using Flask library.

<a name="filesinvolved"></a>

# Files involved:
1. [app.py](https://github.com/kavindevarajan/teams-iassist/blob/master/app.py) - API endpoint file to call a function
2. [config.py](https://github.com/kavindevarajan/teams-iassist/blob/master/config.py) - App ID and password configurations
3. [iAssistbot.py](https://github.com/kavindevarajan/teams-iassist/blob/master/iAssistbot.py) - A module for iAssistbot
4. [etisalatbot.py](https://github.com/kavindevarajan/teams-iassist/blob/master/etisalatbot.py) - A module for etisalat bot
5. [Etisalat_schemes.json](https://github.com/kavindevarajan/teams-iassist/blob/master/Etisalat_schemes.json) - Etisalat schemes data
6. [web.config](https://github.com/kavindevarajan/teams-iassist/blob/master/web.config) - IIS configuration
7. [wfastcgi.py](https://github.com/kavindevarajan/teams-iassist/blob/master/wfastcgi.py) - A flask fastCGI module
8. [msteamsbot.log](https://github.com/kavindevarajan/teams-iassist/blob/master/msteamsbot.log) - All log entries.

This sample **requires** prerequisites in order to run.

<a name="packageinstall"></a>

# Package Installation
To run this repository just install all the required packages mentioned in [requirements.txt]() file using the below command.
To install in virtual environment get into the project working directory and install using below command.
```bash
pip install -r requirements.txt
```

## Running the sample
- Run `python app.py`

<a name="Configurationsteps"></a>

# Configuration steps
1. Register your bot with its endpoint URL here with Azure: [dev.botframework](https://dev.botframework.com/bots/new)
2. Create an App ID and password then set those ID's in [configuration]()
3. Add your app as channel in MS-teams
4. Next expire date: 3/26/2023
5. If you want to create a new username from admin portal among 25 fictional users visit here: [Microsoft admin](https://admin.microsoft.com/#/homepage)
6. username : LeeG@8pklrt.onmicrosoft.com
7. Password: Xud40036
8. If that didn't work use below login credentials:
   1. Username: kavin_d@8pklrt.onmicrosoft.com
   2. Password: Lan@1234
   3. Username: AdeleV@8pklrt.onmicrosoft.com 
   4. Password: Moy17287
## Settings in teams-iassist 
1.	Display name: teams-iassist
2.	Bot handle: teams-iassist
3.	Long description: An AI powered chatbot for support.
4.	Messaging endpoint: 
5.	App type: Multi tenant
6.	Paste app ID: Check credential file
7.	App tenant ID: Check credential file
 
## Settings in Azure App registrations:
1. Login to azure cloud
2. Choose your active directory accordingly
3. Search app refistration in filter service
4. New app registration
5. Choose multitenant [Manual app registration](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart-registration?view=azure-bot-service-4.0&tabs=userassigned#manual-app-registration )
6. Because python Bot SDK framework must work under multi tenant identity
7. Set app name
8. Once created copy the App ID and password

<a name="testdebug"></a>

# Test and Debug

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.14.1 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

## Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:5000/msteams/messages`
- Enter App ID and Password then run
## Pictorial representation
- Step 1: Open Bot Framework Emulator, Enter App ID and Password
  - ![Teams demo image-1](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-1.png)
- Step 2: You must get a welcome message. If not debug the code once again
  - ![Teams demo image-2](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-2.png)
- Step 3: Check responses for respective error messages
  - ![Teams demo image-3](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-3.png)
- Step 4: Open [dev.botframework](https://dev.botframework.com/bots/new) to setup a bot or to do testing with an existing one.
  - ![Teams demo image-4](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-4.png)
- Step 5: Select iAssist-msteams to do deployment testing
  - ![Teams demo image-5](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-5.png)
- Step 6: Click test
  - ![Teams demo image-6](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-6.png)
- Step 7: Check whether you can get a welcome message. If not check the endpoint URL, App ID and password are entered 
properly or not on both Azure side and as well as in code.
  - ![Teams demo image-7](https://github.com/kavindevarajan/teams-iassist/blob/master/images/Teams%20emulator%20picture-7.png)

<a name="linktorefer"></a>

# Links to refer
- Link to install bot builder to build any bot - [Botbuilder python](https://github.com/microsoft/botbuilder-python)
 
- Bot builder samples link - [Bot builder samples](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python)
 
- Echo bot link inspired from this - [Echobot](https://github.com/microsoft/BotBuilder-Samples/tree/main/samples/python/02.echo-bot)
- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)

<a name="Note:PYJWTversionconflict"></a>

# Note: PYJWT version conflict
Both Microsoft bot and twilio are using PYJWT library. But Twilio is using an updated version and microsoft bot framework is 
using older one (1.7.1). If you face this issue uninstall PYJWT and reinstall recommended one in error console.
