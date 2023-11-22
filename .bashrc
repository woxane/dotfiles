#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias charge="upower -d | awk 'BEGIN{RS="\n\n"} /model: *M90 pro/' | grep percentage | awk '{print $2}'"
alias change="find ~/Files/Wallpapers/ -type f | shuf -n 1 | xargs -I {} xwallpaper --stretch {} &"
alias config='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME' 
PS1='[\u@\h \W]\$ '

export PATH="/home/woxane/.detaspace/bin:$PATH"
