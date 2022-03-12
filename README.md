# natemarks.arole-bash

This role configures a bash environment the way i like it. It's also compatible with a similar zsh config that I'll create at some point.

### shell config organization
$HOME/.bashrc runs $HOME/bashrc.local which sources files in a plugin directory. The plugin directory is convenient and avoids conflicts using a similar pattern for other shells (ex. $HOME/zshrc.local)

### install required packages
 - git
 - tree
 - make
 - wget
 - curl
 - zip
 - unzip
 - fzf
 - ripgrep
 - silversearcher-ag
 - jq
 - fonts-powerline
 - dconf-cli  # for gogh colors
 - uuid-runtime  # for gogh colors

### bash fzf integration
 - [CTRL-T, CTRL-R, ALT-C](https://github.com/junegunn/fzf#key-bindings-for-command-line)
 - [bash autocomplete](https://github.com/junegunn/fzf#fuzzy-completion-for-bash-and-zsh)

## gnome terminal colors
https://mayccoll.github.io/Gogh/
I like Afterglow

### set EDITOR
to vim if it's available, vi otherwise

### $HOME/bin
I use this to install binaries like packer, terraform, terragrunt, makemine, etc. I use install scripts in my [pipeline-scripts](https://github.com/natemarks/pipeline-scripts) project. These scripts generally install like:
bin/terragrunt/0.1.2/terragrunt

```shell
pathinsert $HOME/bin/terraform/1.0.6
pathinsert $HOME/bin/terragrunt/0.31.8
```


### Configure powerline status and powerline-gitstatus

This role manages the config files in ~/.config/powerline. If you run the role again, it'll set the config back, but your changes will be backed up by ansible.
- git
- aws (later)

----------------

```shell
git clone https://github.com/natemarks/arole-bash.git
cd arole-bash
sudo apt install -y curl 
bash -c 'curl "https://raw.githubusercontent.com/natemarks/pipeline-scripts/v0.0.39/scripts/run_playbook.sh" | bash -s --  -p  playbook' 
```
