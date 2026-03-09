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

**A) Proveyendo archivos de configuración (Recomendado):**
```bash
java -cp . App <StaticPath> <DynamicPath> <M> <rc> <periodic (true/false)>
```

Ejemplo:
```bash
java -cp . App ../files/Static100.txt ../files/Dynamic100.txt 13 2.0 true 9
```

**B) Generando partículas aleatorias internamente:**
```bash
java -cp . App <N> <L> <M> <rc> <periodic (true/false)>
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

Llame a `target.sh`, que invoca el script Python; éste solicitará el id de la partícula y leerá la información de `output.txt` para colorear sus vecinos. Tenga en cuenta que si no corre run.sh previamente no existira 

```bash
python3 python/visualize.py
```

## 4. Scripts auxiliares

* `run.sh` – compila el código Java y genera `particles.txt` / `output.txt`. No realiza ninguna visualización.
  1. `cd java && javac -cp . *.java`
  2. Ejecuta `App` con los argumentos proporcionados.

* `target.sh` – verifica que `particles.txt` y `output.txt` existen y lanza el script de visualización interactiva `python3 python/visualize.py`, que pedirá el id de la partícula objetivo y pintará sus vecinos.

**Uso típico:**
```bash
# generar datos (usar archivos o valores aleatorios, omitir target_id)
./run.sh ../files/Static100.txt ../files/Dynamic100.txt 13 2.0 true
# luego iniciar la visualización interactiva
./target.sh
# el script pedirá el ID y mostrará la gráfica correspondiente
```
