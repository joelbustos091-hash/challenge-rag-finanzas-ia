import streamlit as st
import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="FinNova AI Knowledge Assistant", page_icon="🤖", layout="wide")

st.title("🤖 FinNova AI Knowledge Assistant")
st.write("Bienvenido al asistente virtual corporativo de FinNova Consulting SpA. Consulta la documentación interna en lenguaje natural.")

# Configurar API Key
api_key = st.sidebar.text_input("Ingrese su Google API Key:", type="password")

if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

    @st.cache_resource
    def inicializar_rag():
        # Cargar documentos de la carpeta data
        loader = PyPDFDirectoryLoader("data/")
        documentos = loader.load()
        
        # Splitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documentos)
        
        # Embeddings & FAISS
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
        vectorstore = FAISS.from_documents(chunks, embeddings)
        return vectorstore

    with st.spinner("Cargando la base de conocimiento..."):
        try:
            vectorstore = inicializar_rag()
            retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
            
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
            
            prompt_template = """
            Eres un asistente de Inteligencia Artificial para FinNova Consulting SpA.
            Responde a la pregunta basándote ÚNICAMENTE en el siguiente contexto:
            
            {context}
            
            Pregunta: {question}
            
            Si la información no se encuentra en el contexto, responde educadamente que no dispones de esa información en la documentación corporativa.
            """
            prompt = ChatPromptTemplate.from_template(prompt_template)
            
            chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )
            
            st.success("Base de conocimiento lista.")
            
            pregunta = st.text_input("Haz una pregunta sobre los manuales de FinNova:")
            if pregunta:
                with st.spinner("Procesando consulta..."):
                    respuesta = chain.invoke(pregunta)
                    st.markdown("### 🤖 Respuesta del Asistente:")
                    st.write(respuesta)
                    
        except Exception as e:
            st.error(f"Error al inicializar el sistema: {e}")
else:
    st.info("👈 Por favor, ingresa tu API Key de Google Gemini en la barra lateral para comenzar.")
