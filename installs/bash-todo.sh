#!/data/data/com.termux/files/usr/bin/sh

echo "Bash To Do Install"

cd

if [[ ! -d /data/data/com.termux/files/home/bin ]]; then
    mkdir -p /data/data/com.termux/files/home/bin/;
fi

if [[ -e /data/data/com.termux/files/home/bin/TODO.sh ]]; then
    echo "/data/data/com.termux/files/home/bin/TODO.sh already exists, overwrite? [Y/n]" >&2;
    read -sn1 choice;

    if [[ $choice = *n* || $choice = *N* ]]; then
        echo "Aborting." >&2;
        exit 1;
    fi
fi

curl -s https://raw.githubusercontent.com/dom111/bash-todo/master/TODO.sh > /data/data/com.termux/files/home/bin/TODO.sh;
chmod +x /data/data/com.termux/files/home/bin/TODO.sh;

echo "Add to /data/data/com.termux/files/home/.bashrc? [Y/n]";
read -sn1 choice;

if [[ $choice = *n* || $choice = *N* ]]; then
    echo 'Run the following to activate:

alias TODO=/data/data/com.termux/files/home/bin/TODO.sh;

if [[ -n $PROMPT_COMMAND ]]; then
    if [[ $PROMPT_COMMAND = *";" || $PROMPT_COMMAND = *"; " ]]; then
        PROMPT_COMMAND="$PROMPT_COMMAND /data/data/com.termux/files/home/bin/TODO.sh";
    else
        PROMPT_COMMAND="$PROMPT_COMMAND; /data/data/com.termux/files/home/bin/TODO.sh";
    fi
else
    PROMPT_COMMAND="/data/data/com.termux/files/home/bin/TODO.sh";
fi';
else
    if ! grep 'alias TODO=/data/data/com.termux/files/home/bin/TODO.sh' /data/data/com.termux/files/home/.bashrc > /dev/null; then
        echo >> /data/data/com.termux/files/home/.bashrc;
        echo 'alias TODO=/data/data/com.termux/files/home/bin/TODO.sh;' >> /data/data/com.termux/files/home/.bashrc;
    fi

    if ! grep 'PROMPT_COMMAND="/data/data/com.termux/files/home/bin/TODO.sh";' /data/data/com.termux/files/home/.bashrc > /dev/null; then
        echo >> /data/data/com.termux/files/home/.bashrc;
        echo 'if [[ -n $PROMPT_COMMAND ]]; then
    if [[ $PROMPT_COMMAND = *";" || $PROMPT_COMMAND = *"; " ]]; then
        PROMPT_COMMAND="$PROMPT_COMMAND /data/data/com.termux/files/home/bin/TODO.sh";
    else
        PROMPT_COMMAND="$PROMPT_COMMAND; /data/data/com.termux/files/home/bin/TODO.sh";
    fi
else
    PROMPT_COMMAND="/data/data/com.termux/files/home/bin/TODO.sh";
fi
' >> /data/data/com.termux/files/home/.bashrc;
    fi

    exec bash;
fi
