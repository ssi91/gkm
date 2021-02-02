# git key manager

## Getting started

### Installation

```bash
pip install git-cli
```

### Usage

```bash
gkm.py -i /path/to/your/non-default/ssh-key clone git@github.com:username/repo.git
```

or

```bash
export GIT_SSH_KEY=/path/to/your/non-default/ssh-key
gkm.py clone git@github.com:username/repo.git
```

It's possible to skip the key passing if it's not necessary. In this case all arguments will be passed in `git` command
as if `git` was used directly
