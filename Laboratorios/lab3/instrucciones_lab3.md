# Lineamientos para la Entrega del Laboratorio - Curso Estructuras de Datos

## Instrucciones Generales

Enlace a los enunciados: [`lab3.xml`](https://github.com/IUSH-DS-202502/recursos-clase/blob/main/Laboratorios/lab3/lab3.xml)

1. **Desarrollo del Algoritmo**:
   - Cada laboratorio está compuesto por varios puntos.
   - En cada punto, deberás desarrollar un algoritmo en el lenguaje de programación de tu preferencia.
   - Asegúrate de que tu solución cumpla con lo especificado en el enunciado, no más, no menos.
   - Lea atentamente cada una de las instrucciones, la calificación es automatizada con mínima intervención manual.
   - Para el desarrollo de este laboratorio NO SE PODRÁ HACER USO DE NINGUNA ESTRUCTURA TIPO COLA, PILA o LISTA, ARREGLO o DICCIONARIO (ni variantes) con excepción de aquellas que sean implementadas por usted como parte del laboratorio y que **sea coherente y correspondiente con lo visto en clase**.
     - En síntesis, lo que se espera es que usted haga uso de la clases Árbol, ÁrbolAVL, MinHeap,MaxHeap que USTED implemente con base en lo visto en el curso.

2. **Archivos del Laboratorio**:
   - Para este laboratorio solo está disponible el archivo [`lab3.xml`](https://github.com/IUSH-DS-202502/recursos-clase/blob/main/Laboratorios/lab3/lab3.xml).
   - El archivo contiene los puntos a desarrollar.

3. **Formato de la Solución**:
   - Usted debe entregar la solución en un archivo con el mismo nombre del archivo original y **conservando la estructura del mismo**. 
   - Debe poner las soluciones en las secciones donde se indica.
   - Cada punto tiene unas instrucciones claras de que es lo que se espera, siga las instrucciones detalladamente, especial atención al nombramiento de los métodos y atributos. Si se solicita que se llamen por ejemplo 'mover', no será valido ningun otro nombre, ni 'moverValor', 'moviendo', 'moverA'. La atención al detalle es determinante para aprobar. 
   - Cada punto en el archivo tiene una sección que indica el inicio y el final de la solución de la siguiente forma:
     - `<codigo lenguaje=""></codigo>`
       - Aquí usted deberá insertar el código entre las etiquetas, 
       - Adicionalmente, donde dice lenguaje debe poner el nombre del lenguaje que usó para desarrollar la solución
     - `<pruebas></pruebas>`
       - Entre estas etiquetas debe colocar las líneas de código que evaluen que su código funciona correctamente
     - `<complejidad></complejidad>`
       - Aquí debe poner el orden de magnitud de su solución.
   - Cada punto será evaluado como una solución independiente y aislado de las demás consignadas en el documento, es por esto que la solución a cada punto debe ser completa e independiente de las demás, si se importan bibliotecas externas, estos imports deben formar parte de cada punto que son usados.
     - Para cada punto deberá incluir el código usado para la creación de las clases de los nodos, las Pilas, Colas o HashMap según corresponda.
   - Si usas Python, por favor valida la correcta identación del código antes de entregarlo, de lo contrario se calificará como incorrecto.
   - No modifiques ni elimines ninguna otra parte del archivo.
   - El no seguir las instrucciones anteriores causará la pérdida del entregable de manera irremediable.
   - Si requiere de un ejemplo sobre como se incluye la solución de los laboratorios en la plantilla entregada, por favor refierase al siguiente archivo: [`lab_ejemplo.xml`](https://github.com/IUSH-DS-202502/recursos-clase/blob/main/Laboratorios/lab_ejemplo.xml)

## Envío del Archivo

1. **Formato y Nombre del Archivo**:
   - El archivo debe ser enviado en el mismo formato entregado.
   - Es crucial que **conserves el nombre original** del archivo (`lab3.xml` ).
   - El no seguir estas instrucciones implicará que la entrega es inválida.

2. **Método de Envío**:
   - Debe abrir el chat con el docente en Teams (Christian Delany) y enviar el documento al chat donde estemos únicamente los dos. Favor no enviarlo a ningun chat grupal ni por email.

3. **Verificación del Documento**:
   - Asegúrate de que el archivo enviado esté correctamente y que contenga tu solución dentro del espacio indicado.

4. **Fecha máxima de envío:**:
   - 02 de Noviembre del 2025 a las 23:59:59 PM

## Evaluación

- La evaluación del laboratorio es semiautomatizada.
- La realización y entrega del laboratorio es INDIVIDUAL.
- Cualquier incumplimiento con los lineamientos anteriores resultará en la invalidez de la entrega.
- El código será ejecutado y la sintaxis validada, si no ejecuta, el punto se dará por perdido.
- Para aprobar debes tener al menos la mitad + 1 de los puntos correctos.
- Recuerde que si tiene dudas, el docente está presto a contar con espacios de asesoría presenciales o virtuales, asegurese que los solicita con tiempo para evitar problemas de disponibilidad.

Por favor, asegúrate de seguir todas las instrucciones cuidadosamente para garantizar que tu entrega sea válida y evaluada correctamente.