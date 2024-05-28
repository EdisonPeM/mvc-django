#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

./exec.sh loaddata autores
# ./exec.sh loaddata generos
# ./exec.sh loaddata editoriales
# ./exec.sh loaddata libros