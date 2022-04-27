source ~/.config/nvim/settings.vim
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'joshdick/onedark.vim'
Plugin 'neoclide/coc.nvim', {'branch': 'release'}
Plugin 'vim-python/python-syntax'
Plugin 'itchyny/lightline.vim' "lightline stausbar
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
source ~/.config/nvim/plugin_conf.vim

