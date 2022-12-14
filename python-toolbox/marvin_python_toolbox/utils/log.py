#!/usr/bin/env python
# coding=utf-8

# Copyright [2020] [Apache Software Foundation]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom logging module.

This module is responsible to manage log messages and log file.
"""

import os
import os.path
import logging

DEFAULT_LOG_LEVEL = logging.INFO

class Logger(logging.getLoggerClass()):
    """Custom logger class.

    Use this class to customize the logger behavior or to intercept the
    messages.
    """
    # def error(self, msg, *args, **kwargs):
    #     # Add here code to intercept the project error messages
    #     super(Logger, self).error(msg, *args, **kwargs)

    # def critical(self, msg, *args, **kwargs):
    #     # Add here code to intercept the project critical messages
    #     super(Logger, self).critical(msg, *args, **kwargs)


logging.setLoggerClass(Logger)


def get_logger(name, namespace='marvin_ai',
               log_level=DEFAULT_LOG_LEVEL):
    """Build a logger that outputs to a file and to the console,"""

    log_level = (os.getenv('{}_LOG_LEVEL'.format(namespace.upper())) or
                 os.getenv('LOG_LEVEL', log_level))

    logger = logging.getLogger('{}.{}'.format(namespace, name))
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console stream handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger