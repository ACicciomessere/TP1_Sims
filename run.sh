#!/bin/bash

# Este script compila el proyecto completo en Java, lo ejecuta pasándole los argumentos
# que le des a este script, y si finaliza correctamente, entonces corre la visualización.

echo ">>> COMPILING JAVA..."
cd java || exit 1
javac -cp . *.java || exit 1

echo ">>> RUNNING CELL INDEX METHOD..."
# Pass all parameters to App; target_id is optional and simply ignored if present
java -cp . App "$@"
EXIT_CODE=$?

cd ..

if [ $EXIT_CODE -ne 0 ]; then
    echo ">>> EXECUTION FAILED."
    exit 1
fi

# run.sh solely generates the particle and neighbor files
# visualization is handled separately by target.sh or direct call
echo ">>> DATA GENERATION COMPLETED. Use target.sh to visualize a particle."
