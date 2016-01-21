set nocompatible

" Pathogen load
filetype off

call pathogen#infect()
call pathogen#helptags()

filetype plugin indent on
syntax on

filetype off

" VIM Bunble Manager. Get BundleList wit :BundleList
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'

" The bundles you install will be listed here
Bundle 'tpope/vim-fugitive'
Bundle 'klen/python-mode'
Bundle 'davidhalter/jedi-vim'

let g:pymode = 1
" Python-mode
" Activate rope
" Keys:
" K             Show python docs
" <Ctrl-Space>  Rope autocomplete
" <Ctrl-c>g     Rope goto definition
" <Ctrl-c>d     Rope show documentation
" <Ctrl-c>f     Rope find occurrences
" <Leader>b     Set, unset breakpoint (g:pymode_breakpoint enabled)
" [[            Jump on previous class or function (normal, visual, operator modes)
" ]]            Jump on next class or function (normal, visual, operator modes)
" [M            Jump on previous class or method (normal, visual, operator modes)
" ]M            Jump on next class or method (normal, visual, operator modes)
let g:pymode_rope = 0
" Documentation
let g:pymode_doc = 1
let g:pymode_doc_key = 'K'

"Linting
let g:pymode_lint = 1
let g:pymode_lint_checker = "pyflakes,pep8"
" Auto check on save
let g:pymode_lint_write = 1

" Support virtualenv
let g:pymode_virtualenv = 1

" Enable breakpoints plugin
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_bind = '<leader>b'

" syntax highlighting
let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all

" Don't autofold code
let g:pymode_folding = 0
" let g:pymode_rope = 1
" let g:pymode_rope_completion = 1
" let g:pymode_rope_goto_definition_bind = '<C-c>g'
let g:pymode_run_bind = ',r'


filetype plugin indent on


" set nocompatible	" Use Vim defaults (much better!)
set bs=indent,eol,start		" allow backspacing over everything in insert mode
set ai			" always set autoindenting on
"set backup		" keep a backup file
set viminfo='20,\"50	" read/write a .viminfo file, don't store more
			" than 50 lines of registers
set history=50		" keep 50 lines of command line history
set ruler		" show the cursor position all the time
syntax on
set hlsearch
set spelllang=de
"filetype plugin on

"filetype plugin indent on

" oberhalb und unterhalb der aktuellen Zeile immer 7 Zeilen platz
" Um die Zeile auf dem Bildschirm zu zentrieren: zz
set scrolloff=7

"meine neuen Befehle
nnoremap s :exec "normal i".nr2char(getchar())."\e"<CR>
nnoremap S :exec "normal a".nr2char(getchar())."\e"<CR>
"Zeilen nummerierung
set number 
"k auf visual k
nnoremap k gk
"j auf visual j
nnoremap j gj
"jk auf esc
inoremap öö <esc>
"jj auf esc 
inoremap jj <esc>
"F12 als make Prohaupt.pdf
map <F12> :w<CR>:!make<CR><CR>
inoremap <F12> <esc>:w<CR>:!make<CR><CR>

"set background=dark
