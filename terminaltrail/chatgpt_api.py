#!/usr/bin/env python3
"""ChatGPT API"""
# Copyright 2023 Ar-Ray-code
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import openai
from terminaltrail.prompt import preprompt, comment_ai, comment_user, praise, solve, summary, tips

JP = 0
EN = 1

PRAISE_MODE = 0
SOLVE_MODE = 1
SUMMARY_MODE = 2
TIPS_MODE = 3

class ChatGPT:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, contents: str, lang: int=JP, mode: int=PRAISE_MODE) -> str:
        messages = [
            {'role': 'user', 'content': preprompt[lang]},
            {'role': 'assistant',  'content': comment_ai[lang]}
        ]
        if mode == PRAISE_MODE:
            messages += [{'role': 'user', 'content': comment_user[lang].replace('<trail_mode>', praise[lang]) + '```bash\n' + contents + '```'}]
        elif mode == SOLVE_MODE:
            messages += [{'role': 'user', 'content': comment_user[lang].replace('<trail_mode>', solve[lang]) + '```bash\n' + contents + '```'}]
        elif mode == SUMMARY_MODE:
            messages += [{'role': 'user', 'content': comment_user[lang].replace('<trail_mode>', summary[lang]) + '```bash\n' + contents + '```'}]
        elif mode == TIPS_MODE:
            messages += [{'role': 'user', 'content': comment_user[lang].replace('<trail_mode>', tips[lang]) + '```bash\n' + contents + '```'}]

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        return result
