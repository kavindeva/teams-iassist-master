# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import logging
import traceback
from datetime import datetime
from flask import Flask, jsonify, request, Response

# from aiohttp import web
# from aiohttp.web import Response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
# from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes

from iAssistbot import MyBot
from config import DefaultConfig

CONFIG = DefaultConfig()

app = Flask(__name__)

#Data-logging
logger = logging.getLogger(__name__)
app.logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('msteamsbot.log')
file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)

# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error

# Create the Bot
BOT = MyBot()


@app.route('/msteams')
def home():
    app.logger.debug("/msteams route")
    return "Welcome to iAssist Microsoft Teams integration portal"


# Listen for incoming requests on /api/messages
@app.route('/msteams/messages', methods=["POST"])
async def messages():
    app.logger.debug("/msteams/messages route")
    # Main bot message handler.
    if "application/json" in request.headers["Content-Type"]:
        body = request.get_json()
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return jsonify(data=response.body, status=response.status)
    return Response(status=201)


# APP = web.Application(middlewares=[aiohttp_error_middleware])
# APP.router.add_post("/api/teams", messages)

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        raise error
