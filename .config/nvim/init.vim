set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
source ~/.vimrc
"map vertical split terminal to Space T
noremap <Leader>t :vsplit term://zsh<CR>
"map <Esc> to exit terminal-mode
tnoremap <Esc> <C-\><C-n>
let g:neovide_transparency=0.5
