Located at
/data/data/com.termux/files/home/.bashrc

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=9999
HISTFILESIZE=9999

# Prompt and colors

export PS1=' '
export LS_COLORS='no=00:fi=00:di=36:ln=1;40;31:pi=40;33:so=35:bd=40;33;01:cd=40;33;01:or=40;31;01:ex=04;37:*.pdb=37:*.bz2=2;43;91:*.tar=2;43;91:*.tgz=2;43;91:*.arj=2;43;91:*.taz=2;43;91:*.lzh=2;43;91:*.zip=2;43;91:*.z=2;43;91:*.bz2=2;43;91:*.Z=2;43;91:*.gz=2;43;91:*.deb=2;43;91:*.jpg=31:*.gif=31:*.png=31:*.jpeg=31:*.bmp=31:*.ppm=31:*.tga=31:*.xbm=31:*.xpm=31:*.tif=31:*.mpg=31:*.avi=31:*.gl=31:*.dl=31:*.ps=33:*.ps2=33:*.eps=33:*.map=04;35:*.mtz=35:*.pdf=33:*.dvi=33:*.tex=33:*.c=04;32:*.cu=04;32:*.f=04;32:*.phs=04;32:*.h=04;32:*.f77=04;32:'

# ./  is a bit difficult to type
export PATH=.:$PATH

# make cursor underscore
printf '\x1b[\x34 q'

# start chroot and goto pseudo-home directory
if ! pgrep -f "proot" >/dev/null ; then termux-chroot; fi

#echo '\e[2 q' # Change to block
#echo '\e[4 q' # Change to underline
echo '\e[6 q' # Change to bar

source $HOME/.bashrc

source $HOME/.zshrc

source $HOME/functions

clear

source $HOME/aliases
