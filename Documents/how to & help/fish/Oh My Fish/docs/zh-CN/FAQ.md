<img src="https://cdn.rawgit.com/oh-my-fish/oh-my-fish/e4f1c2e0219a17e2c748b824004c8d0b38055c16/docs/logo.svg" align="left" width="128px" height="128px"/>
<img align="left" width="0" height="128px"/>

# FAQ

> Oh My Fish Documentation&nbsp;&bull;&nbsp;Also in
> <a href="../en-US/FAQ.md">ðºð¸</a>
> <a href="../ru-RU/FAQ.md">ð·ðº</a>
> <a href="../uk-UA/FAQ.md">ðºð¦</a>
> <a href="../pt-BR/FAQ.md">ð§ð·</a>
<br>

æè°¢æ¨è±ä¸äºæ¶é´æ¥éè¯» FAQãå¦ææ²¡æä»ä¸é¢æ¾å°ä½ æ³é®çé®é¢æ¬¢è¿ç»æä»¬æäº¤æ°çé®é¢(Issue)ã


## ä»ä¹æ¯ Oh My Fishï¼æä¸ºä»ä¹ä¼ä½¿ç¨å®ï¼

Oh My Fish æ¯åºäº [Fishshell](http://fishshell.com/) å°è£çé«çº§ _æ¡æ¶_ãå®å¯ä»¥å¸®ä½ ç®¡çä½ çéç½®ï¼ä¸»é¢åæä»¶ã


## ä½¿ç¨ Oh My Fish æéè¦æ³¨æä»ä¹ï¼

_ä»ä¹é½ä¸éè¦æ³¨æ_ãå®è£ Oh My Fish å¹¶æ³å¹³æ¶ä½¿ç¨ Fish Shell ä¸æ ·ãå½ä½ éè¦è·åæ´å¤å¸®å©ä»éè¦æ§è¡ `omf help`ã


## ä»ä¹æ¯ Oh My Fish åï¼Packagesï¼ï¼

Oh My Fish åæ¯ä½¿ç¨ fish ç¼åçä¸ç³»åä¸»é¢åæä»¶ç¨äºæ©å± Shell çæ ¸å¿åè½ï¼æ¯å¦åå§åæ¶æ§è¡èªå®ä¹ä»£ç ï¼æ·»å èªå¨è¡¥å¨ç­ã


## Oh My Fish åå¤§æ¦åå«åªäºç±»å?

ç®åç²ç¥åç±»å¯ä»¥å®ä¹ 3 ä¸­ç±»åï¼

1. éç½®å¢å¼ºãæ¯å¦ [`pkg-pyenv`](https://github.com/oh-my-fish/pkg-pyenv) æ£æµ `pyenv` æ¯å¦å®è£å¹¶è¿è¡ `(pyenv init - | psub)`ã

2. ä¸»é¢. æ¥çæä»¬ç[ä¸»é¢ç®å½](https://github.com/oh-my-fish).

3. ç³»ç»å¢å¼ºãæ¯å¦ [`pkg-copy`](https://github.com/oh-my-fish/pkg-copy)ï¼å¯åæ¶æ¯æ Linux å Mac OS X çåªåå·¥å·ã


## Oh My Fish ä¸»è¦é½å¹²äºä»ä¹?

+ å¦æå­å¨ `$OMF_CONFIG/before.init.fish`ã

+ èªå¨å è½½ `$OMF_PATH/` ç®å½ä¸å·²å®è£çæä»¶åä¸»é¢ã

+ èªå¨å è½½ä½ çéç½®ãé»è®¤è·¯å¾ `~/.config/omf`ï¼é¤éä½ èªå®ä¹äº `$OMF_CONFIG` åéã

+ èªå¨å è½½ `$OMF_PATH` å `$OMF_CONFIG` ç®å½ä¸é¢çææç `functions`

+ å¦æå­å¨å è½½ `$OMF_CONFIG/init.fish`ã


## å¦ä½åçº§ä¹åå·²å®è£ç Oh My Fish?

> :warning: å¡å¿åå¤ä»½ä½ ç dotfiles åå¶ä»èªå®ä¹çæ°æ®ã

```
curl -L github.com/oh-my-fish/oh-my-fish/raw/master/bin/install | sh
```

ç°å¨ä½ å¯ä»¥å®å¨çç§»é¤ `$fish_path`.

```fish
rm -rf "$fish_path"
```


## å¦ä½æ fish è®¾ç½®ä¸ºæé»è®¤ç shell?

æ·»å  Fish å°  `/etc/shells`:

```sh
echo "/usr/local/bin/fish" | sudo tee -a /etc/shells
```

åæ¢å¹¶ä¿å­é»è®¤ shell:

```sh
chsh -s /usr/local/bin/fish
```

åæ¢ä¹åç shell:
> ä¸è¬æ¥è¯´æ¯ `/bin/bash`ã`/bin/tcsh` æè `/bin/zsh`.

```sh
chsh -s /bin/bash
```
