#!/bin/bash

# Zsh Syntax highlighting Install

cd $HOME
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
echo "\nIf `git` is not installed, download and extract a snapshot of the latest
  development tree from:\n https://github.com/zsh-users/zsh-syntax-highlighting/archive/master.tar.gz\n"
echo "\nNote the `source` command must be **at the end** of `~/.zshrc`.\n"


### With a plugin manager

Note that `zsh-syntax-highlighting` must be the last plugin sourced.

The zsh-syntax-highlighting authors recommend manual installation over the use
of a framework or plugin manager.

This list is incomplete as there are too many
[frameworks / plugin managers][framework-list] to list them all here.

[framework-list]: https://github.com/unixorn/awesome-zsh-plugins#frameworks

#### [Antigen](https://github.com/zsh-users/antigen)

Add `antigen bundle zsh-users/zsh-syntax-highlighting` as the last bundle in
your `.zshrc`.

#### [Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

1. Clone this repository in oh-my-zsh's plugins directory:

    ```zsh
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```

2. Activate the plugin in `~/.zshrc`:

    ```zsh
    plugins=( [plugins...] zsh-syntax-highlighting)
    ```

3. Restart zsh (such as by opening a new instance of your terminal emulator).

#### [Prezto](https://github.com/sorin-ionescu/prezto)

Zsh-syntax-highlighting is included with Prezto. See the
[Prezto documentation][prezto-docs] to enable and configure highlighters.

[prezto-docs]: https://github.com/sorin-ionescu/prezto/tree/master/modules/syntax-highlighting

#### [zgen](https://github.com/tarjoilija/zgen)

Add `zgen load zsh-users/zsh-syntax-highlighting` to the end of your `.zshrc`.

#### [zplug](https://github.com/zplug/zplug)

Add `zplug "zsh-users/zsh-syntax-highlighting", defer:2` to your `.zshrc`.

#### [zplugin](https://github.com/psprint/zplugin)

Add `zplugin load zsh-users/zsh-syntax-highlighting` to the end of your
`.zshrc`.


### System-wide installation

Any of the above methods is suitable for a single-user installation,
which requires no special privileges.  If, however, you desire to install
zsh-syntax-highlighting system-wide, you may do so by running

```zsh
make install
```

and directing your users to add

```zsh
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

to their `.zshrc`s.
