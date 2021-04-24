# Copyright (c) HelloYeew <me@helloyeew.dev>. Licensed under the MIT Licence.
# See the LICENCE file in the repository root for full licence text.

import gettext
import os
import glob

# https://phrase.com/blog/posts/translate-python-gnu-gettext/

def new_language(language,directory="locales"):
    # TODO: Make notice is .mo file not found
    language_file = gettext.translation('base', localedir=directory, languages=[language])
    language_file.install()
    language_to_translate = language_file.gettext
    return language_to_translate
