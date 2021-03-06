<img src="https://cdn.rawgit.com/oh-my-fish/oh-my-fish/e4f1c2e0219a17e2c748b824004c8d0b38055c16/docs/logo.svg" align="left" width="192px" height="192px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> El _framework_ de <a href="http://fishshell.com">Fishshell</a> 

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE) [![Fish Shell Version](https://img.shields.io/badge/fish-鈮2.2.0-007EC7.svg?style=flat-square)](http://fishshell.com) [![Travis Build Status](http://img.shields.io/travis/oh-my-fish/oh-my-fish.svg?style=flat-square)](https://travis-ci.org/oh-my-fish/oh-my-fish) [![Slack Status](https://oh-my-fish-slack.herokuapp.com/badge.svg)](https://oh-my-fish-slack.herokuapp.com)


Oh My Fish ofrece la infraestructura b谩sica para permitirle instalar paquetes que extiendan o modifiquen el aspecto de su _shell_. Es r谩pido, extensible y
sencillo de utilizar.

> Tambi茅n disponible en&nbsp;
> <a href="../en-US/FAQ.md">馃嚭馃嚫</a>
> <a href="docs/ru-RU/README.md">馃嚪馃嚭</a>
> <a href="docs/zh-CN/README.md">馃嚚馃嚦</a>
> <a href="docs/uk-UA/README.md">馃嚭馃嚘</a>
> <a href="docs/pt-BR/README.md">馃嚙馃嚪</a>

<br>

## 脥ndice de contenidos
* [Instalaci贸n](#instalaci贸n)
* [Comenzando (descripciones de los comandos)](#comenzando)
* [Avanzado](#avanzado)
  * [Inicio](#inicio)
  * [Archivos de configuraci贸n (Dotfiles)](#dotfiles)
* [Creando paquetes](#creando-paquetes)

## Instalaci贸n 

Puede comenzar de inmediato con la configuraci贸n predeterminada ejecutando lo siguiente en su terminal:

```fish
curl -L https://get.oh-my.fish | fish
```

Esto descargar谩 el script instalador y comenzar谩 la instalaci贸n. De manera alternativa, puede descargar el instalador y personalizar su instalaci贸n:

```fish
curl -L https://get.oh-my.fish > install
fish install --path=~/.local/share/omf --config=~/.config/omf
```

Puede verificar la integridad del instalador descargado comprobando el script con esta [suma de verificaci贸n](bin/install.sha256):

```
434264c56e3a7bb74733d9b293d72403c404e0a0bded3e632433d391d302504e  install
```

Tambi茅n puede insatalar Oh My Fish mediante Git o con un archivo tarball descargado desde la [p谩gina de publicaciones][releases]:

```fish
# with git
$ git clone https://github.com/oh-my-fish/oh-my-fish
$ cd oh-my-fish
$ bin/install --offline
# with a tarball
$ curl -L https://get.oh-my.fish > install
$ fish install --offline=omf.tar.gz
```

Ejecute `install --help` para obtener una lista completa de opciones de instalaci贸n que puede personalizar.

#### Requisitos

- **fish** shell, versi贸n 2.2 o posterior
- **git**, versi贸n 1.9.5 o posterior 

#### Problemas conocidos

- Debido a un error de regresi贸n en fish 2.6 con algunos emuladores de terminal, los prompts a la derecha hacen que la shell no se pueda utilizar.
  El tema OMF's `default` ofrece un prompt a la derecha, as铆 que es necesario utilizar un tema alternativo hasta que se publique una soluci贸n.
  (ver [#541](https://github.com/oh-my-fish/oh-my-fish/issues/541))


## Comenzando 

Oh My Fish incluye una peque帽a utilidad `omf` para extraer e instalar nuevos paquetes y temas.

#### `omf update` _`[omf]`_ _`[<paquete>...]`_

Actualiza Oh My Fish, todos los paquetes de los repositorios y todos los paquetes instalados.

- Cuando es llamado sin argumentos, actualiza el n煤cleo y todos los paquetes instalados.
- Puede escoger actualizar s贸lo el n煤cleo, ejecutando `omf update omf`.
- Para una actualizaci贸n selectiva de paquetes, escriba solo los paquetes que desea actualizar. Deber铆a incluir "omf" en la lista para actualizar tambi茅n el
  n煤cleo.

#### `omf install` _`[<nombre>|<url>]`_

Instala uno _o m谩s_ paquetes.

- Puede instalar paquetes directamente con la URL mediante `omf install URL`
- Cuando es ejecutado sin argumentos, instala paquetes faltantes desde [bundle](#dotfiles).

#### `omf repositories` _`[list|add|remove]`_

Gestiona los paquetes de los repositorios instalados por el usuario. Los paquetes de los repositorios son de donde los paquetes provienen utilizando
comandos como `omf install`. De manera predeterminada el [repositorio oficial](https://github.com/oh-my-fish/packages-main) est谩 siempre instalado y
disponible.

#### `omf list`

Lista los paquetes instalados.

#### `omf theme` _`<tema>`_

Aplica un tema. Para listar los temas disponibles, escriba `omf theme`. Tambi茅n puede [previsualizar los temas disponibles](../Themes.md) antes de
instalarlos.

#### `omf remove` _`<nombre>`_

Elimina un tema o paquete.

> Los paquetes pueden utilizar _hooks_ al desinstalarlos, as铆 que una limpieza de recursos personalizado puede ejecutarse cuando se desinstalen. Ver
> [Desinstalar](/docs/es-ES/Packages.md#uninstall) para m谩s informaci贸n.

#### `omf reload`

Vuelve a cargar Oh My Fish y todos los complementos utilizando `exec` para reemplazar el proceso shell actual con uno nuevo.

> Este comando intenta ser lo m谩s seguro posible, mitigando efectos colaterales cauados por `exec` y prevenir la recarga en el caso de procesos en segundo
> plano.

#### `omf new plugin | theme` _`<nombre>`_

Crea un esqueleto para un nuevo complemento o tema.

> Esto crea un nuevo directorio en `$OMF_CONFIG/{pkg | themes}/` con una plantilla.

#### `omf search` _`-t|--theme / -p|--package`_ _`<nombre>`_

Busca en la base de datos de Oh My Fish un paquete en concreto, tema o ambos. Tambi茅n soporta una b煤squeda menos expl铆cita, as铆 que si no est谩 seguro del
nombre simplemente ejecute `omf search simple`.

#### `omf channel`

Obtiene o cambia el canal de actualizaci贸n.

De manera predeterminada existen dos canales: el canal `stable` ofrece actualizaciones estables con las versi贸n m谩s recientes de Oh My Fish, y `dev` que
ofrece los 煤ltimos cambios en desarrollo. El canal de actualizaci贸n actual determina a qu茅 versi贸n de `omf update` se actualizar谩.

#### `omf doctor`

Utilizar para diagnosticar un error antes de [abrir un _issue_][omf-issues-new].

#### `omf destroy`

Desinstala Oh My Fish.

## Avanzado 

El instalador de Oh My Fish a帽ade un fragmento a los archivos de configuraci贸n de fish del usuario (`~/.config/fish/conf.d/`) que llama al c贸digo de
arranque de OMF.

Tenga en cuenta que los scripts en ese directorio se ofrecen en el orden en el que el sistema de archivos los ve, y quiz谩s puede ser necesario a帽adir un
prefijo a su script con n煤meros para ordenarlos.

Por ejemplo: `a_script.fish` tendr谩 preferencia sobre el fragmento `omf.fish`.
As铆 que si `a_script.fish` depende de complementos gestionados por OMF, considere renombrar el archivo del script a `xx_a_script.fish`.

De manera similar, para asegurarse que un script se ejecuta antes de `omf.fish`, deber铆a a帽adirle el prefijo `00_`.
De manera alternativa tambi茅n se puede utilizar `~/.config/omf/before.init.fish`.

### Inicio 

Cada vez que abre una nueva shell, el c贸digo de inicio inicializa la ruta de instalaci贸n y la ruta de configuraci贸n de Oh My Fish (`~/.config/omf` de manera
predeterminada), ejecutando el script [`init.fish`](init.fish) posteriormente, que carga de manera autom谩tica los paquetes, temas y sus ficheros
personalizados de inicio.

Para m谩s informaci贸n puede consultar la secci贸n de preguntas frecuentes [FAQ](FAQ.md#qu茅-hace-oh-my-fish-exactamente).

### Archivos de configuraci贸n (Dotfiles)

El directorio `$OMF_CONFIG` representa el estado del usuario de Oh My Fish. Es el perfecto candidato para ser a帽adido a sus archivos de configuraci贸n o
_dotfiles_ y/o a帽adirlo a un control de versiones como puede ser Git. All铆 se pueden encontrar tres archivos importantes:

- __`theme`__ - El tema actual
- __`bundle`__ - Lista de los temas/paquetes actualmente instalados
- __`channel`__ - El canal desde el cual OMF descarga las actualizaciones (estable / dev)

Y puede crear o personalizar esos archivos especiales:

- __`init.fish`__ - Script personalizado que se ejecuta despu茅s del arranque de la shell
- __`before.init.fish`__ - Script personalizado que se ejecuta antes del arranque de la shell
- __`key_bindings.fish`__ - Atajos de teclado personalizados donde puede utilizar el comando `bind` de manera libre

#### Configurando variables en `init.fish`

Uno de los usos m谩s comunes utilizados en `init.fish` es la definici贸n de variables. Seguramente, para variables que necesitan estar disponible en cualquier
sesi贸n de la shell. Para conseguir esto, es necesario definirlas de manera global. Por ejemplo:

```fish
# Los desarrolladore de Golang quiz谩s necesitan esto
set -xg GOPATH $HOME/gocode

# En cambio los desarrolladores de Python 
set -xg PYTHONDONTWRITEBYTECODE 1
```

#### Acerca de bundle

Cada vez que un paquete/tema es instalado o eliminado, el archivo `bundle` es actualizado. Tambi茅n puedes editarlo manualmente y despu茅s ejecutar `omf
install` para tomar en cuenta los cambios realizados. Por favor tenga en cuenta que mientras que los paquetes/temas a帽adidos a _bundle_ son 
instalados autom谩ticamente, un paquete/tema eliminado de _bundle_ no es eliminado de la instalaci贸n del usuario.

#### Versiones antiguas de fish

En fish 2.2, no existe el directorio `conf.d`, as铆 que el c贸digo de inicio tiene que ser ubicado en el archivo de configuraci贸n de fish (`~/.config/fish/config.fish`).

Es altamente recomendado que los comandos personalizados de inicio est茅n en el archivo `init.fish` en vez de en `~/.config/fish/config.fish`, ya que esto le
permite mantener todo el directorio `$OMF_CONFIG` bajo un servicio de control de versiones.

Si necesita ejecutar comandos de inicio que sean ejecutados *antes* de que Oh My Fish comience a cargar complementos, ubiquelos en `before.init.fish`. Si no
est谩 seguro, normalmente es mejor poner las cosas en `init.fish`.

## Creando paquetes

Oh My Fish utiliza una avanzada y bien definida arquitectura de desarrollo de complementos, incluyendo _hooks_ de inicializaci贸n/instalaci贸n, carga
autom谩tica de funciones. [Ver la documentaci贸n de paquetes](Packages.md) para m谩s detalles.


[fishshell]: http://fishshell.com
[colaboradores]: https://github.com/oh-my-fish/oh-my-fish/graphs/contributors
[omf-pulls-link]: https://github.com/oh-my-fish/oh-my-fish/pulls
[omf-issues-new]: https://github.com/oh-my-fish/oh-my-fish/issues/new
[publicaciones]: https://github.com/oh-my-fish/oh-my-fish/releases
