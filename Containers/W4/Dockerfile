FROM alpine:edge

# Update and install necessary packages
RUN apk update && apk upgrade && apk add --no-cache \
    python3 \
    bash \
    curl \
    git \
    tmux \
    neovim \
    starship \
    clang \
    zsh \
    bat \
    eza \
    fzf \
    ripgrep \
    fd \
    bind-tools \
    py3-virtualenv

# Install hashcat from the testing repository
RUN apk add --update --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ hashcat

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

RUN mkdir -p /home/COMP6845/.local/bin
WORKDIR /home/COMP6845/.local/bin
RUN python3 -m venv volatility
RUN ./volatility/bin/pip install --upgrade pip
RUN ./volatility/bin/pip install volatility3

WORKDIR /home/COMP6845
RUN echo "alias 'vol.py'='/home/COMP6845/.local/bin/volatility/bin/vol'" >> .zshrc
CMD ["zsh"]
