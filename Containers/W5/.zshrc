# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/COMP3141/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

alias vim=nvim
alias v=nvim

alias cat=bat

alias ls='eza --icons'
alias ll='eza --icons -l'
alias la='eza --icons -la'

# Plugins
source ~/.local/share/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.local/share/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.local/share/zsh/fzf-tab/fzf-tab.plugin.zsh

# Start starship
# ~/.zshrc
eval "$(starship init zsh)"
