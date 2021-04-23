# Copyright (c) HelloYeew <me@helloyeew.dev>. Licensed under the MIT Licence.
# See the LICENCE file in the repository root for full licence text.

import logging  # Use for make logs file for dev mode
from logging import handlers
import sys
import time

# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout


def set_log(logfile="logs/main.log", filemode='a', level='notset', gmtime=True):
    """Start import logging system to bot
    """
    logging.info("Bot log setting :")
    log = logging.getLogger('')

    logging.info("Log file location : logs/main.log")

    # Logging level (NOTSET (lowest), DEBUG, INFO, WARNING or CRITICAL (highest))
    level.lower()
    if level == 'notset':
        log.setLevel(logging.NOTSET)
        logging.info("Log level : notset")
    elif level == 'debug':
        log.setLevel(logging.DEBUG)
        logging.info("Log level : debug")
    elif level == 'info':
        log.setLevel(logging.INFO)
        logging.info("Log level : info")
    elif level == 'warning':
        log.setLevel(logging.WARNING)
        logging.info("Log level : warning")
    elif level == 'critical':
        log.setLevel(logging.CRITICAL)
        logging.info("Log level : critical")

    format_log = logging.Formatter(fmt="%(asctime)s [%(name)s]: %(levelname)s - %(message)s", datefmt='%Y-%m-%d %H:%M:%S')

    if filemode == 'w':
        logging.info("File mode : w (open for writing, truncating the file first)")
    elif filemode == 'a':
        logging.info("File mode : a (open for writing, appending to the end of the file if it exists)")
    else:
        logging.exception("File mode can be only 'w' or 'a'. Set filemode to default mode ('a').")

    if gmtime:
        format_log.converter = time.gmtime
        logging.info("Timezone : GMT")
    else:
        logging.info("Timezone : Local")

    # Set logging to print on console
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format_log)
    log.addHandler(ch)

    # Set logging to collect log to file
    fh = handlers.RotatingFileHandler(logfile, mode=filemode)
    fh.setFormatter(format_log)
    log.addHandler(fh)


def write_log(message,level='info'):
    try:
        level.lower()
        if level == 'debug':
            logging.debug(message)
        elif level == 'info':
            logging.info(message)
        elif level == 'warning':
            logging.warning(message)
    except:
        logging.exception('Got exception on main handler')
        raise
