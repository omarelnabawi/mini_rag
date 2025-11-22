# mini_rag
This is a minimal implementation of the RAG model for question answering

## Requirments

- Python 3.8 or later
##### Install Python using MiniConda

1) Download and install Miniconda from [here](https://www.anaconda.com/download)
2) Create a new environment using the following command:
```bash
$ conda create -n mini_rag_env python=3.8
```
3) Activate the environment:
```bash 
$ conda activate mini_rag_env
```
### (Optional) Setup your commend line interface for better readability

```bash
export PS1="\[033[01;32m\]\u@\h:\w\n\[\033[00m\]\$"
```
## Installation

### Install the required packages

```bash
$ pip install -r requirments.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

set your evironmet variables in the `.env` file. Link `OPENAI_API_KEY` value.

#### Run the Fastapi server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
- This will help you if you make changes in your work will automatically upload and anyone can access in it.

 
