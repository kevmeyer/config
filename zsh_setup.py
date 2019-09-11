#!/usr/bin/env python3
from utils import call


def install_oh_my_zsh():
    def install_plugins():
        def clone_zsh_plugin(url, path):
            call(f'git clone {url} ${{ZSH_CUSTOM:-~/.oh-my-zsh/custom}}/{path}')

        clone_zsh_plugin("https://github.com/romkatv/powerlevel10k.git", "themes/powerlevel10k")
        clone_zsh_plugin("https://github.com/zsh-users/zsh-autosuggestions.git", "plugins/zsh-autosuggestions")
        clone_zsh_plugin("https://github.com/zsh-users/zsh-syntax-highlighting.git", "plugins/zsh-syntax-highlighting")

    install_plugins()


def install_vim_config():
    call("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
    call("vim +PluginInstall +qall")


def install_tmux_config():
    call("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
    call(
        "tmux start-server && tmux new-session -d && ~/.tmux/plugins/tpm/scripts/install_plugins.sh && tmux kill-server")


def install_fzf():
    call("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    call("~/.fzf/install")


def main():
    # install_zsh()
    # install_oh_my_zsh()
    install_oh_my_zsh()
    install_vim_config()
    install_tmux_config()
    install_fzf()


if __name__ == "__main__":
    main()
