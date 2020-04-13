# termshare
Share your terminal history on web

## Setup

### 0-Clone this repository

You can clone this repository using the command below(git needs to be installed).

```bash
git clone https://github.com/fdiblen/termshare.git
```

### 1-Bash shell

Add the following lines to your `.bashrc`

```shell
export HISTSIZE=1000000
export HISTFILESIZE=1000000
PROMPT_COMMAND='history -a'
shopt -s histappend
#export HISTFILE=~/.custom_file
```

### 2-Virtual environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
. ./venv/bin/activate
```

### 3-Install dependencies

Install required Python packages:

```bash
pip install --upgrade pip pipenv
```

```bash
pipenv install
```

### 4-Start the server

The following command will start sharing your terminal history on port 80. To start the server, you will need admin rights (sudo).

```bash
sudo python server.py
```