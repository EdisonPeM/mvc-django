#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

./exec.sh python manage.py loaddata autores
# ./exec.sh python manage.py loaddata generos
# ./exec.sh python manage.py loaddata editoriales
# ./exec.sh python manage.py loaddata libros