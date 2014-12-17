# Filename : install.sh
# Author : ihainan
# Created Date : 2014/10/11
# Description : installation script for Ubuntu Desktop

# Update source list
sudo apt-get update

# Development Tools
echo "Installing vim build-essential openssh-server git curl tmux zsh ipython"
sudo apt-get install vim build-essential git curl tmux zsh openssh-server ipython

# oh-my-zsh
echo "Installing oh-my-zsh"
curl -L http://install.ohmyz.sh | sh

# OpenJdk
echo "Installing OpenJdk 6"
sudo apt-get install openjdk-6-jdk

# Pinyin
# echo "Installing fcitx"
# sudo apt-get install fcitx fcitx-sunpinyin
