#!/usr/bin/env python3
import os
import subprocess

from utils import home_path, call


def main():
    pass
    # install_zsh()
    # install_oh_my_zsh()
    # install plugins:
    # git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
    # git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    # git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    # apt: powerline

    # Vim
    # git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
    # vim +PluginInstall +qall

    # tmux
    # git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

    # tmux start-server
    # # create a new session but don't attach to it either
    # tmux new-session -d
    # # install the plugins
    # ~/.tmux/plugins/tpm/scripts/install_plugins.sh
    # # killing the server is not required, I guess
    # tmux kill-server

    # fzf
    # git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    # ~/.fzf/install



if __name__ == "__main__":
    main()
