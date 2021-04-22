# Copyright (c) HelloYeew <me@helloyeew.dev>. Licensed under the MIT Licence.
# See the LICENCE file in the repository root for full licence text.

from kasumiframework.bot import *

set_presence("BanKongPor")
set_log(logfile="logs/main.log", filemode='a', level='info', gmtime=True)
start_bot(token="",log=True, presence=True)


# # localization
#
# https://phrase.com/blog/posts/translate-python-gnu-gettext/

# en = gettext.translation('base', localedir='locales', languages=['en'])
# en.install()
# en_lang = en.gettext
#
# # Discord integration part
#
# intents = discord.Intents.default()
# intents.members = True
#


#
# # TODO: Add licenseheader command


