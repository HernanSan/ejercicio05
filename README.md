Actividad en clase - no calificada

Generar un scrip de python (un archivo llamada ejercicio05.py) y realizar lo siguiente

1. Instalar la librería de Python: requests
2. Leer la información del archivo frases.csv
3. Determinar el tipo de frase: positiva o negativa; para cada línea del archivo
4. Usar para el efecto el servicio dado en la aplicación flask; que deberá está ejecutandose en http://127.0.0.1:8080/prediccion
4.1 Para usar el servicio puede revisar el siguiente ejemplo:
 
import requests
r = requests.get("http://127.0.0.1:8080/prediccion/'%s'" % "Happy")
r.json()

4.2 Puede probar el ejemplo; a través de la librería ipython
5. Cuando se ejecute el ejecute el script de python, se debera ver como respuesta, listada la frase con su categorización.
