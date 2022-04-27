set clipboard=unnamedplus
set clipboard+=unnamedplus
set number
" change cursor line when inside insert mode
let &t_si = "\<esc>[6 q"
let &t_sr = "\<esc>[4 q"
let &t_ei = "\<esc>[2 q"
" set leader key
let g:mapleader = "\<Space>"
inoremap ( ()<Left>
" <TAB>: completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"
" Better tabbing
vnoremap < <gv
vnoremap > >gv
inoremap " ""<Left>
inoremap ' ''<Left>
inoremap [ []<Left>
inoremap < <><Left>
inoremap { {}<Left>
inoremap pysh #!/usr/bin/python3
inoremap bsh #!/usr/bin/bash
vnoremap <Leader>C :'<,'>norm 0i#<CR>

