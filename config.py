#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    # PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "165a8f35-3ecb-431d-abd5-9e97eb45bc3a")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "jfF8Q~X6kzK1zNZLTKZW-bWbZRZnrjMwWip_Yc33")
