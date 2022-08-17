# API TWITTER 132

La api realiza varias peticiones a la api de twitter. La funcion principal de este proyecto es obtener los ultimos resultados de tweets con un filtro de cuenta y palabra clave, conectado a una base de datos local que se ejecuta en un docker.

~~~
mkdocs serve -a localhost:8001
pip install -r requirements_docs.txt 
mkdocs serve
make docs-serve # ver makefile - lo abre en un servidor
make docs-build # ver makefile - te genera una carpeta con el html
~~~


For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.