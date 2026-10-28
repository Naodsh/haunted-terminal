# 👻 Haunted Terminal

A spooky, privacy-first terminal companion powered by a locally running
open-weight language model through Ollama.

## Features

- Three fictional AI personalities: Ghost, Oracle, and Cryptkeeper.
- Local AI inference using Ollama.
- Safe shell-command explanations without automatic command execution.
- Explicitly saved local lore.
- Colorful terminal interface using Rich.
- No cloud AI API key required.

## Requirements

- Ubuntu Linux or another compatible Linux distribution
- Python 3.10+
- Ollama
- A locally installed compatible model, such as `qwen3:0.6b`

## Installation

Install Ollama using its official instructions:
https://ollama.com/download

Download the model:

```bash
ollama pull qwen3:0.6b
```

Create and launch the application:

```bash
git clone YOUR_REPOSITORY_URL
cd haunted-terminal
python3 -m venv .venv
source .venv/bin/activate
pip install rich
python haunted.py
```

If you are already working from a local project directory, skip the
clone command and run the remaining commands from that directory.

## Commands

| Command | Description |
|---|---|
| `summon` | Awaken the current personality |
| `whisper <text>` | Ask the local AI a question |
| `inspect <command>` | Explain a shell command without running it |
| `personality` | List available personalities |
| `personality oracle` | Switch to the Oracle |
| `personality cryptkeeper` | Switch to the Cryptkeeper |
| `lore add <text>` | Save a note locally |
| `lore list` | Read saved lore |
| `lore clear` | Clear saved lore after confirmation |
| `history` | Show this session's conversation |
| `status` | Show local configuration |
| `banish` | Exit |

## Privacy and offline operation

The application sends inference requests to Ollama through the loopback
address `127.0.0.1`. It does not intentionally send prompts to a remote
AI API. Initial software and model downloads require internet access.

After installing the dependencies and model, test operation with the
internet disconnected. Verify that the installed Ollama service and model
are local before relying on offline operation.

Saved lore is stored under:

`~/.local/share/haunted-terminal/lore.json`

Review saved lore before sharing your computer or backing up your home
directory. Never save passwords, access tokens, private keys, or other
secrets as lore.

## Open innovation

Haunted Terminal demonstrates how a developer can run a language model
locally, inspect and modify the application, and retain control of local
data without requiring a hosted AI API. The application license and the
model license are separate; check the selected model's license before
redistributing it.

## Limitations

The AI can produce incorrect explanations. Review commands before running
them yourself. The application does not execute inspected commands.

## License

The application code is licensed under the MIT License. The model and
its associated files remain subject to their own license terms.
