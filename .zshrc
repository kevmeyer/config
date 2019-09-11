# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="${HOME}/.oh-my-zsh"
export EDITOR="vim"
export VISUAL="vim"

POWERLEVEL9K_STATUS_CROSS=true
POWERLEVEL9K_STATUS_OK=false

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs status)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()

# POWERLEVEL9K_MODE='awesome-fontconfig'
# POWERLEVEL9K_MODE='nerdfont-complete'

ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(tmux colored-man-pages zsh-syntax-highlighting zsh-autosuggestions)
#git gitfast

source $ZSH/oh-my-zsh.sh
# source $HOME/.bash_aliases

# autoload -U compinit && compinit
# zmodload -i zsh/complist

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
