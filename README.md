# Generador de memes
La aplicación genera memes a partir de las imágenes provistas y los textos incluir.

#### (Proyecto utilizado para la demo de documentación con sphinx)


## Entorno de desarrollo

1. Creamos el entorno virtual y lo activamos
```
python -m venv env

source env/bin/activate
```

2. Instalamos las dependencias
```
pip install -r src/requirements.txt
```

## Configuración inicial del directorio de documentación
1. Creamos el directorio
```
mkdir docs
```

2. inicializamos la estructura de archivos de sphinx
```
cd docs
sphinx-quickstart
```

Para este ejemplo la configuración fue la siguiente:
```
> Separar directorios fuente y compilado (y/n) [n]: y
> Nombre de proyecto: Meme Generator
> Autor(es): Fernando D. Gómez
> Liberación del proyecto []: 0.0.1
> Lenguaje del proyecto [en]: es
```

Para compilar nuestra documentación:

```
> make html
```

y Para previsualizar nuestra documentación, desde la raíz de nuestro proyecto:

```
python -m http.server 8080 -d docs/build/html
```
