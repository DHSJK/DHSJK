Para guiarte en la realización de la entrega "Tercer_Encargo_BIY7131", te proporciono un paso a paso basado en la información de los documentos proporcionados y el ejemplo en Google Cloud Platform (GCP).

### Paso 1: Conectar con la Fuente de Datos

1. **API de Servicios de Transporte:**

   - Accede a la API que proporciona todos los recorridos disponibles: [getservicios](https://www.red.cl/restservice_v2/rest/getservicios/all).
   - Utiliza esta API para obtener los códigos de los recorridos.

2. **Detalles del Recorrido:**
   - Para cada código de recorrido obtenido, realiza una consulta a la API [conocerecorrido](https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint=101), reemplazando "101" por el código de cada recorrido.

### Paso 2: Ingesta de Datos en el Data Lake

1. **Creación del Bucket en GCP:**

   - Navega a Google Cloud Console [GCP Console](https://console.cloud.google.com/).
   - Crea un nuevo Bucket en Cloud Storage con un nombre relevante, por ejemplo, "nombre_proyecto-real-time".

2. **Configuración de Pub/Sub:**

   - Asegúrate de que la API de Pub/Sub esté habilitada.
   - Crea un nuevo tema (topic) en Pub/Sub.
   - Crea una suscripción al tema con la opción "Escribir en Cloud Storage" y selecciona el Bucket creado previamente.

3. **Publicar Mensajes Manualmente:**
   - Publica manualmente los mensajes obtenidos de la API `conocerecorrido` en formato JSON en el tema de Pub/Sub.
   - Puedes optar por desarrollar un código en Python para automatizar la publicación (opcional para un punto extra).

### Paso 3: Procesamiento de Datos

1. **Limpieza y Transformación:**
   - Utiliza DataProc, DataFlow o DataPrep para construir procesos de limpieza y transformación de los datos.
   - Asegúrate de manejar duplicidad, datos nulos y datos incorrectos o no esperados.

### Paso 4: Construcción de Reportes

1. **Consultas SQL en BigQuery:**

   - Realiza tres consultas SQL en BigQuery para extraer la información relevante.
   - Por ejemplo:
     - Consulta 1: Resumen de recorridos y horarios.
     - Consulta 2: Paradas más frecuentadas.
     - Consulta 3: Duración promedio de los trayectos.

2. **Visualizaciones en Looker Studio:**
   - Utiliza los resultados de las consultas para generar tres reportes visuales en Looker Studio.
   - Cada reporte debe ser claro y relevante para la toma de decisiones en el negocio de transporte público.

### Elaboración del Informe

1. **Estructura del Informe:**

   - **Portada:** Título del proyecto, nombres de los integrantes, fecha y nombre del profesor.
   - **Tabla de Contenidos:** Índice con las secciones del informe.
   - **Desarrollo:** Detallar cada paso realizado en GCP con capturas de pantalla y explicaciones detalladas de cada línea de código si aplica.
   - **Conclusiones:** Resumen de los hallazgos y su relevancia.
   - **Referencias:** Fuentes y recursos utilizados.

2. **Diagramas y Capturas:**
   - Incluye un diagrama de la arquitectura que considere las herramientas y canalizaciones utilizadas.
   - Asegúrate de que todas las capturas de pantalla sean claras y estén bien etiquetadas.

### Evaluación (Seguir Rubrica)

1. **Conexión y Control de Errores:**

   - Implementa los procesos de carga y asegúrate de manejar los errores y logs adecuadamente.

2. **Transformación de Datos:**

   - Realiza todas las transformaciones necesarias para que los datos estén en un formato adecuado para el consumo.

3. **Remediación de Datos:**

   - Asegúrate de que los datos estén limpios y sin duplicidades o errores.

4. **Informe y Presentación:**

   - Asegúrate de que el informe tenga todos los apartados solicitados y que estén en el orden adecuado.

5. **Presentación:**

   - Justifica el contenido del informe y responde correctamente a las preguntas planteadas.

6. **Comunicación Efectiva:**
   - Utiliza un lenguaje técnico adecuado y comunícalo efectivamente.

### Ejemplo de GCP

Referente al ejemplo proporcionado en el archivo "Ejemplo_GCP_entregable3 (1).docx", sigue los pasos indicados allí para la configuración en GCP, asegurándote de realizar todas las configuraciones correctamente, y utiliza las capturas de pantalla como referencia visual.

### Entrega

- **Fecha de Entrega:** lunes 24 de junio.
- **Forma de Entrega:** Correo electrónico.
- **Formato de Entrega:** Carpeta comprimida con el informe en Word y cualquier código fuente desarrollado.

Si necesitas más detalles específicos o asistencia adicional en algún paso, no dudes en preguntar. ¡Buena suerte con tu entrega!
