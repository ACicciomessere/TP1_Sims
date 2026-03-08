# TP1_Sims

## 0. Dependencias

```bash
pip3 install matplotlib
```

## 1. Compilación

```bash
cd java
javac -cp . *.java
```

## 2. Ejecución de la Simulación

El programa puede correr de dos maneras:
**A) Proveyendo archivos de configuración (Recomendado):**
```bash
java -cp . App <StaticPath> <DynamicPath> <M> <rc> <periodic (true/false)> <target_id>
```

Ejemplo:
```bash
java -cp . App ../files/Static100.txt ../files/Dynamic100.txt 13 2.0 true 9
```

**B) Generando partículas aleatorias internamente:**
```bash
java -cp . App <N> <L> <M> <rc> <periodic (true/false)> <target_id>
```

Ejemplo:
```bash
java -cp . App 100 20.0 13 2.0 true 9
```

*(Opcional)* Si necesitas generar un set de archivos aleatorio nuevo:
```bash
java -cp . InputGenerator <N> <L> <OutputPrefix>
```

## 3. Visualización

```bash
cd ..
python3 python/visualize.py
```

## 4. Ejecución con visualización en 1 comando

(Usando archivos):
```bash
cd java && javac -cp . *.java && java -cp . App <StaticPath> <DynamicPath> <M> <rc> <periodic (true/false)> <target_id> && cd .. && python3 python/visualize.py
```

Ejemplo:
```bash
cd java && javac -cp . *.java && java -cp . App ../files/Static100.txt ../files/Dynamic100.txt 13 2.0 true 9 && cd .. && python3 python/visualize.py
```

(Usando generación interna aleatoria):
```bash
cd java && javac -cp . *.java && java -cp . App <N> <L> <M> <rc> <periodic (true/false)> <target_id> && cd .. && python3 python/visualize.py
```

Ejemplo:
```bash
cd java && javac -cp . *.java && java -cp . App 100 20.0 13 2.0 true 9 && cd .. && python3 python/visualize.py
```
