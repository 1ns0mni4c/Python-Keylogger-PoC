# Python Keylogger Proof of Concept

⚠️ **DISCLAIMER: This project is for educational and research purposes only. Use only on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.**

## Overview

This is a proof-of-concept (PoC) demonstration of a basic keylogger implementation in Python. The project consists of two components:
- **Client**: A keylogger that captures keystrokes and sends them to a remote server
- **Server**: A Flask-based server that receives and logs the captured keystrokes

## Features

### Client
- Captures keystrokes on Windows systems
- Maintains persistence through Windows registry modification
- Basic file obfuscation using Windows attributes (`+s +h`)
- Sends logged keystrokes to a remote server

### Server
- Lightweight Flask server
- Receives keystroke data from clients
- Logs received data to text files
