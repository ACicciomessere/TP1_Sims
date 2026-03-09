#!/bin/bash

# Este script compila el proyecto completo en Java, lo ejecuta pasándole los argumentos
# que le des a este script, y si finaliza correctamente, entonces corre la visualización.

echo ">>> COMPILING JAVA..."
cd java || exit 1
javac -cp . *.java || exit 1

echo ">>> RUNNING CELL INDEX METHOD..."
java -cp . App "$@"
EXIT_CODE=$?

cd ..

if [ $EXIT_CODE -ne 0 ]; then
    echo ">>> EXECUTION FAILED. SKIPPING VISUALIZATION."
    exit 1
fi

echo ">>> RUNNING VISUALIZATION..."
python3 python/visualize.py
