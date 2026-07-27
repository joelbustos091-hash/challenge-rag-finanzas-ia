# 🤖 FinNova AI Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue)

![LangChain](https://img.shields.io/badge/LangChain-1.3-green)

![Gemini](https://img.shields.io/badge/Google-Gemini-orange)

![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-red)

![Google Colab](https://img.shields.io/badge/Google-Colab-yellow)

Sistema inteligente basado en arquitectura **RAG (Retrieval-Augmented Generation)** desarrollado como proyecto final del **Challenge Alura – Agentes de IA**.

El asistente permite consultar documentación corporativa mediante lenguaje natural utilizando **Google Gemini**, **LangChain**, **FAISS** y **Embeddings**, entregando respuestas fundamentadas únicamente en la información contenida en los documentos de la empresa.

---

# 📖 Descripción

FinNova AI Knowledge Assistant fue desarrollado para resolver un problema habitual dentro de las organizaciones: la dificultad para encontrar información relevante entre manuales, políticas internas y documentación corporativa.

El sistema procesa documentos PDF, genera una base de conocimiento mediante embeddings y responde preguntas utilizando búsqueda semántica sobre la documentación disponible.

La solución implementa una arquitectura **RAG**, permitiendo generar respuestas más precisas, transparentes y fundamentadas.

---

# 🎯 Objetivos del Proyecto

- Automatizar la consulta de documentación corporativa.
- Reducir los tiempos de búsqueda de información.
- Implementar una arquitectura RAG utilizando LangChain.
- Construir una base vectorial mediante FAISS.
- Utilizar Google Gemini como modelo de lenguaje.
- Demostrar un flujo completo desde la carga de documentos hasta la generación de respuestas.

---

# 📂 Documentación utilizada

El asistente consulta la siguiente documentación:

- 📘 Manual Financiero Corporativo
- 📙 Manual SAP Business One para Finanzas
- 📗 Términos y Condiciones de Uso de FinNova AI

---

# ⚙️ Tecnologías utilizadas

- Python
- Google Colab
- LangChain
- Google Gemini 3.6 Flash
- Gemini Embedding 001
- FAISS
- PyPDF
- Git
- GitHub
---

# 🏗️ Arquitectura de la Solución

El proyecto implementa una arquitectura **Retrieval-Augmented Generation (RAG)** para consultar documentación corporativa.

El flujo de procesamiento es el siguiente:

```text
                    Documentos PDF
        ┌──────────────┬──────────────┬──────────────┐
        │              │              │
        ▼              ▼              ▼
 Manual Financiero   Manual SAP B1   Términos y Condiciones
        │              │              │
        └──────────────┴──────────────┘
                       │
                       ▼
                 PyPDFLoader
                       │
                       ▼
              División en Chunks
                       │
                       ▼
           Gemini Embedding-001
                       │
                       ▼
             Base Vectorial FAISS
                       │
                       ▼
             Retriever (LangChain)
                       │
                       ▼
          Google Gemini 3.6 Flash
                       │
                       ▼
      FinNova AI Knowledge Assistant
                       │
                       ▼
                    Usuario
```

Esta arquitectura permite recuperar únicamente los fragmentos más relevantes de la documentación antes de generar una respuesta con el modelo de lenguaje, reduciendo respuestas incorrectas y mejorando la precisión del sistema.
---

# 🔄 Flujo del Sistema

1. El usuario realiza una pregunta en lenguaje natural.
2. LangChain consulta la base vectorial FAISS.
3. El Retriever recupera los fragmentos más relevantes.
4. Google Gemini recibe únicamente ese contexto.
5. El modelo genera una respuesta basada en la documentación.
6. El sistema informa el documento consultado y el tiempo de respuesta.

---

# 💬 Ejemplos de Consultas

A continuación se presentan algunos ejemplos de consultas realizadas al asistente utilizando la documentación cargada.

| Pregunta | Documento consultado |
|----------|----------------------|
| ¿Cuál es el flujo de aprobación de pagos? | Manual Financiero Corporativo |
| ¿Qué es un Socio de Negocio? | Manual SAP Business One para Finanzas |
| ¿Quién puede acceder a FinNova AI? | Términos y Condiciones de Uso |

El agente identifica automáticamente el documento más relevante antes de generar la respuesta, permitiendo obtener información precisa sin necesidad de revisar manualmente cada archivo.
---

# 📈 Resultados

Durante las pruebas realizadas, el asistente fue capaz de:

- Consultar correctamente múltiples documentos PDF.
- Recuperar información mediante búsqueda semántica.
- Identificar el documento utilizado para responder.
- Mostrar el tiempo de respuesta de cada consulta.
- Evitar generar respuestas cuando la información no estaba disponible en la documentación.

# 📸 Evidencias de Ejecución y Pipeline RAG

A continuación se muestra el funcionamiento paso a paso registrado durante las pruebas en Google Colab:

### 1. Generación de Chunks y Modelo de Embeddings
Se procesaron los documentos PDF generando 36 fragmentos (chunks) e inicializando el modelo de embeddings de Google.

<img width="1101" height="559" alt="Fragmentacion y Embeddings" src="https://github.com/user-attachments/assets/fa511352-cbf9-4dab-afad-d6979b96256c" />

---

### 2. Creación y Almacenamiento del Índice FAISS
Construcción de la base vectorial con los embeddings generados y guardado local del índice `finnova_vector_db`.

<img width="1113" height="640" alt="Base Vectorial-FFAISS" src="https://github.com/user-attachments/assets/edae9626-ec7b-4d0c-9fc1-22e0da6695e4" />

---

### 3. Respuesta Final del Asistente (Inferencia)
Consulta en tiempo real sobre el flujo de aprobación de pagos, demostrando recuperación precisa del contexto, identificación del documento fuente y tiempo de ejecución.

<img width="1035" height="675" alt="Evidencia- Ejecucion" src="https://github.com/user-attachments/assets/3f9c38d8-79c6-4d98-bf8a-f1500bb76161" />


Estas validaciones demuestran el correcto funcionamiento de la arquitectura RAG implementada.
---

# 🚀 Mejoras Futuras

- Incorporar nuevos documentos automáticamente.
- Implementar una interfaz web con Streamlit.
- Integrar autenticación de usuarios.
- Agregar memoria conversacional.
- Permitir carga dinámica de documentos por parte del usuario.
- Incorporar historial de consultas.
---

# 👨‍💻 Autor

Proyecto desarrollado por **Joel Bustos** como parte del **Challenge Alura – Agentes de IA**, aplicando técnicas de Inteligencia Artificial Generativa, Recuperación Aumentada por Generación (RAG) y búsqueda semántica sobre documentación corporativa.

Tecnologías principales:

- Google Gemini
- LangChain
- FAISS
- Python
- Google Colab
- GitHub
---

# 💻 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/JoelBustos/FinNova-AI-Knowledge-Assistant.git
```

## 2. Acceder al proyecto

```bash
cd challenge-rag-finanzas-ia
```

## 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 4. Configurar la API Key de Google Gemini

Crear un secreto en Google Colab llamado:

```
GOOGLE_API_KEY
```

y asociar la API Key obtenida desde Google AI Studio.

## 5. Ejecutar el Notebook

Abrir el notebook en Google Colab y ejecutar las celdas en el siguiente orden:

- Instalación de librerías
- Configuración de Gemini
- Carga de documentos
- División en Chunks
- Embeddings
- FAISS
- Retriever
- Agente RAG
- Pruebas del sistema
---

# 📂 Estructura del Proyecto

```text
FinNova-AI-Knowledge-Assistant/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── notebooks/
│   └── Challenge_Alura_FinNova_AI.ipynb
│
├── data/
│   ├── Manual_Financiero_Corporativo.pdf
│   ├── Manual_SAP_Business_One_Finanzas.pdf
│   └── Terminos_y_Condiciones_FinNova_AI.pdf
│
└── images/
    ├── arquitectura.png
    └── demo.png
```
---

# 📚 Aprendizajes Obtenidos

Durante el desarrollo de este proyecto se aplicaron conceptos fundamentales de Inteligencia Artificial Generativa y Recuperación Aumentada por Generación (RAG), entre ellos:

- Procesamiento de documentos PDF.
- División de texto mediante Chunking.
- Generación de Embeddings.
- Construcción de bases vectoriales con FAISS.
- Recuperación semántica mediante LangChain Retriever.
- Integración de modelos Google Gemini.
- Ingeniería de Prompts.
- Desarrollo de asistentes documentales basados en IA.

Este proyecto permitió comprender el flujo completo necesario para construir un asistente inteligente capaz de consultar documentación empresarial utilizando lenguaje natural.
---

> *"La Inteligencia Artificial no reemplaza el conocimiento de una organización; lo hace más accesible."*

**FinNova AI Knowledge Assistant**
---
