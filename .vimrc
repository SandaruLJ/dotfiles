source $VIMRUNTIME/vimrc_example.vim

syntax on

set number
set relativenumber
set nocompatible
set nowrap
set encoding=utf8

" Use 4 spaces instead of tab
set expandtab
set shiftwidth=4
set softtabstop=4

" Set backup and swap directories
set backupdir=~/.vim/backup/,/tmp//,.
set directory=~/.vim/swap/,/tmp//,.
set undodir=~/.vim/undo/,/tmp//,.

