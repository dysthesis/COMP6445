FROM alpine:edge

# Update and install necessary packages
RUN apk update && apk upgrade && apk add --no-cache \
    python3 \
    7zip \
    shadow \
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
    py3-virtualenv \
    termshark \
    traceroute \
    neomutt

# Add a new user
RUN adduser -D COMP6845
RUN usermod -aG wireshark COMP6845
RUN chsh -s /bin/zsh COMP6845

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

# Set up volatility
RUN mkdir -p /home/COMP6845/.local/bin
WORKDIR /home/COMP6845/.local/bin
RUN python3 -m venv volatility
RUN ./volatility/bin/pip install --upgrade pip
RUN ./volatility/bin/pip install volatility3

WORKDIR /home/COMP6845
RUN echo "alias 'vol.py'='/home/COMP6845/.local/bin/volatility/bin/vol'" >> .zshrc

# Create Mail directory and copy mbox files
RUN mkdir -p /home/COMP6845/Mail
COPY --chown=COMP6845:COMP6845 Emails/Harris/all.mbox /home/COMP6845/Mail/harris.mbox
COPY --chown=COMP6845:COMP6845 Emails/Hamilton/all.mbox /home/COMP6845/Mail/hamilton.mbox

# Configure NeoMutt
RUN echo 'set mbox_type=mbox' >> /home/COMP6845/.neomuttrc
RUN echo 'set folder=~/Mail' >> /home/COMP6845/.neomuttrc
RUN echo 'mailboxes ~/Mail/hamilton.mbox ~/Mail/harris.mbox' >> /home/COMP6845/.neomuttrc
RUN echo 'set spoolfile=~/Mail/hamilton.mbox' >> /home/COMP6845/.neomuttrc

CMD ["zsh"]
