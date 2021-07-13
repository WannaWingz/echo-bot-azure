#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "cc5c0436-ac1e-4ea5-bb34-67412395a19c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "7i~4f_af_~BTk4U9j~3TXbcO.64DA7ecU7")
