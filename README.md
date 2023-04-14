# TerminalTrail
Keep Track of Your Terminal Journey with AI !

## Requirements

- openai (with API-Key)
- Ubuntu22

<br>

## Installation


```bash
python3 -m pip install git+https://github.com/Ar-Ray-code/TerminalTrail.git@main
```

<br>

## Usage

```bash
TerminalTrail
```

### Options

| arg | description |
| --- | --- |
| --api_key API_KEY | API key for OpenAI (Default: use OPENAI_API_KEY environment) |
| --mode | Conversation mode using number /0:praise/1:solve/2:gen summary/3:tips (default: 2) |
| --max_depth | Maximum depth to traverse bash history |
| --lang | Language to use: Japanese (0), English (1) (default: 0) |
| --text_path | Path to bash history |

