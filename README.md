
# Bob - The AI Code Generator

Bob is an AI-powered code generation tool that helps developers create code repositories with proper structure and organization. It uses OpenAI's models to generate code based on natural language descriptions.

## Features
- Automated repository structure generation
- Docker support for easy deployment
- Built-in testing framework
- Class-based architecture
- Simple and efficient code generation

## Quick Start
```bash
# Build the Docker environment
./scripts/build.sh

# Run the application
./scripts/run.sh
```

## Project Structure
```
bob/
├── bob/
│   ├── __init__.py
│   ├── bob.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_bob.py
├── scripts/
│   ├── build.sh
│   └── run.sh
├── Dockerfile
├── requirements.txt
└── README.md
```
