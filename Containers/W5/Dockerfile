FROM alpine:edge

# Update and install necessary packages
RUN apk update && apk upgrade && apk add --no-cache \
    curl \
    git \
    tmux \
    neovim \
    starship \
    zsh \
    bat \
    eza \
    fzf \
    ripgrep \
    fd \
    bind-tools

# Install hashcat from the testing repository
RUN apk add --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ ettercap

# Add a new user
RUN adduser -D COMP6845

USER COMP6845
WORKDIR /home/COMP6845

# Copy tmux and zsh configuration files
COPY --chown=COMP6845:COMP6845 tmux/ /home/COMP6845/.config/tmux
COPY --chown=COMP6845:COMP6845 .zshrc /home/COMP6845/.zshrc

# Clone necessary repositories
RUN git clone https://github.com/tmux-plugins/tpm /home/COMP6845/.local/share/tmux/plugins/tpm
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /home/COMP6845/.local/share/zsh/zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions /home/COMP6845/.local/share/zsh/zsh-autosuggestions
RUN git clone https://github.com/Aloxaf/fzf-tab /home/COMP6845/.local/share/zsh/fzf-tab

WORKDIR /home/COMP6845
CMD ["zsh"]
