#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "4f5f6d9f-126c-476a-9ce0-35ea8ecd34b1")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "s.NC4cnE.SXIu57f0aqNo6~5.XDdL_JkTp")
