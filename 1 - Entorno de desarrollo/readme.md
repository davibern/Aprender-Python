# Elegir Entorno de Desarrollo

Existen varios entornos de desarrollo para Python, y para cualquier sistema, pero no es mi misión mostrártelos todos.

De entre todos los que hay, te diferencio los siguientes tres:

* [Pycharm] > Es el ide de los chicos de JetBrains, y sus productos son conocidos por su alta calidad. Este cliente está en dos versiones: la de estudiante, que es gratis, y la profesional, que tiene un coste mensual.
* [Visual Studio Code] > El ide más famoso, junto con el primero y completamente gratuito. Para usarlo hace falta configurar un par de cosillas, pero una vez hecho, va como la seda.
* [Vim] > Este se lo dejo a los pros, porque sé que se puede programar en este entorno, pero yo de Vim no tengo ni idea 😵‍💫

[Pycharm]: https://www.jetbrains.com/pycharm/
[Visual Studio Code]: https://code.visualstudio.com/
[Vim]: https://www.vim.org/

# Configurar Visual Studio Code

Yo estoy usando VSCode, por varias razones:

- Es completamente gratuito
- Funciona bastante bien
- Tiene plugins realizados por la comunidad que potencian su uso.

Nos lo descargamos desde la web oficial: [Visual Studio Code] o bien usamos WinGet (si estás en windows)

```winget install vscode```

Si estás en un sistema Debian:

```sudo apt-get install vscode```

Visual Studio Code nos debería de reconocer automáticamente que tenemos Python instalado, por lo que lo siguiente sería instalar el complemento de Python.

El mejor que te recomiendo es [Python Extension Pack], porque esta herramienta contiene:

- El plugin oficial de Python de Microsoft
- Intellisense para Pyhon
- Python indent
- Django
- Etc.

![Python Extension Pack](/99%20-%20Imagenes/python_extension_pack.png)

[Python Extension Pack]: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack

También te recomiendo instalar [Error Lens], porque te ayudará a detectar errores en la síntaxis de tu código.

[Error Lens]: https://marketplace.visualstudio.com/items?itemName=PhilHindle.errorlens

Y con esto deberías de tener todo lo suficiente para empezar a trabajar con Python en tu sistema operativo.

**¡A por ello!** 💪