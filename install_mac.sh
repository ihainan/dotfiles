# Filename : install_mac.sh
# Author : ihainan
# Created Date : 2014/12/17
# Description : installation script for OS X

# homebrew
echo "Installing homebrew"
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# oh-my-zsh
echo "Installing oh-my-zsh"
curl -L http://install.ohmyz.sh | sh

# tmux
brew install tmux

# pip
sudo easy_install pip

# ipython
sudo pip install ipython
