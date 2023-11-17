set nocompatible
syntax on
set nowrap
set encoding=utf8
source $VIMRUNTIME/vimrc_example.vim

" Use 4 spaces instead of tab
set expandtab
set shiftwidth=4
set softtabstop=4

" Set backup and swap directories
set backupdir=~/.vim/backup/,/tmp//,.
set directory=~/.vim/swap/,/tmp//,.
set undodir=~/.vim/undo/,/tmp//,.
