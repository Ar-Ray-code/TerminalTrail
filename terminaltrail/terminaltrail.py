#!/usr/bin/env python3
"""TerminalTrail✨"""
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

import argparse
from terminaltrail import chatgpt_api
from terminaltrail.prompt import text
import os


def get_bash_history(text_path: str, max_depth: int = 100) -> str:
    bash_history_path = os.path.expanduser(os.path.expandvars(text_path))
    history = ''
    with open(bash_history_path, 'r') as f:
        length = len(f.readlines())
        if length > max_depth:
            f.seek(0)
            for i, line in enumerate(f):
                if i >= length - max_depth:
                    history += line
    return history


def main():
    parser = argparse.ArgumentParser(
        description='TerminalTrail✨ - A tool to generate a summary of your bash history using ChatGPT API.')
    parser.add_argument('--api_key', help='API key for OpenAI (Default: use OPENAI_API_KEY environment)',
                        default=os.environ.get('OPENAI_API_KEY'))

    parser.add_argument(
        '--mode', help='Conversation mode using number: praise (0), solve (1), gen summary (2), tips (3) default: 2', type=int, default=2)
    parser.add_argument(
        '--max_depth', help='Maximum depth to traverse bash history', default=20, type=int)
    parser.add_argument(
        '--lang', help='Language to use: Japanese (0), English (1) default: 0', type=int, default=0)
    parser.add_argument(
        '--text_path', help='Path to bash history', default='~/.bash_history')
    args = parser.parse_args()

    if args.api_key is None:
        print('Please set API key for OpenAI')
        exit(1)

    chat = chatgpt_api.ChatGPT(args.api_key)

    print('------- TerminalTrail✨ Summary -------')
    if (args.mode == 0):
        print('Mode: {}'.format(text.praise[args.lang]))
    elif (args.mode == 1):
        print('Mode: {}'.format(text.solve[args.lang]))
    elif (args.mode == 2):
        print('Mode: {}'.format(text.summary[args.lang]))
    elif (args.mode == 3):
        print('Mode: {}'.format(text.tips[args.lang]))

    print('Language: {}'.format(text.lang[args.lang]))
    print('History path: {}'.format(args.text_path))
    print('History max depth: {}'.format(args.max_depth))
    print('')
    print('Waiting for response... (This may take a while)')
    print('-------------------------------------')
    print('')

    history = get_bash_history(
        text_path=args.text_path, max_depth=args.max_depth)

    print(text.comment_prefix[args.lang])
    response = chat.generate_text(history, lang=args.lang, mode=args.mode,
                                  prompt=text.preprompt[args.lang] + text.praise[args.lang] + text.comment_ai[args.lang])

    print(response)


if __name__ == '__main__':
    main()
