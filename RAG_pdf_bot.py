from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False


if "agent" not in st.session_state:
    st.session_state.agent= None 

if "vector_store" not in st.session_state:
    st.session_state.vector_store= None

if "messages" not in st.session_state:
    st.session_state.messages= []


def process_document(path):
    loader= PyPDFDirectoryLoader(path)
    docs= loader.load()

    splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap= 50 );
    docs= splitter.split_documents(documents=docs)

    embeddings= GoogleGenerativeAIEmbeddings( model="gemini-embedding-001")
    db= InMemoryVectorStore.from_documents(
        documents= docs,
        embedding= embeddings,
    )


    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    @tool
    def retrieve_context(query:str):
        """Retrieve documents relvant to a query from the knowledge base."""
        context=""
        docs= db.similarity_search(query= query, k=3)
        for doc in docs:
            context= doc.page_content +"\n\n"
        return context

    system_prompt="""You are  a helpful assistant that answers questions from the uploaded file. My Knowledge base consist of the details fro the uploaded document.
    Always use `retrieve_context` tool fro questions requiring external knowledge"""

    memory= InMemorySaver()

    agent= create_agent(
        model= llm,
        tools=[retrieve_context],
        system_prompt= system_prompt,
        checkpointer= memory
    )
    st.session_state.agent= agent
    st.session_state.document_uploaded= True

if not st.session_state.document_uploaded:
    uploaded= st.file_uploader(label="Add multiple files", type= ["pdf"], accept_multiple_files= True)
    if uploaded:
        with st.spinner("Processing...."):
            path= "./doc_files/"
            for file in uploaded:
                with open( path + file.name, "wb") as f:
                    f.write(file.getvalue())
            
            process_document(path)
            st.rerun()


if st.session_state.document_uploaded and st.session_state.agent:
    for message in st.session_state.messages:
        role= message.get("role")
        content= message.get("content")
        st.chat_message(role).markdown(content)



    query= st.chat_input("ask anything related to uploaded documents")
    if query:
        st.session_state.messages.append({"role":"user", "content":query})

        st.chat_message("user").markdown(query)
        response= st.session_state.agent.invoke(
            {"messages": [{"role":"user", "content":query}]},
            {"configurable":{"thread_id":1}}
        )
        answer= response["messages"][-1].content
        st.chat_message("ai").markdown(answer)
        st.session_state.messages.append({"role":"AI", "content": answer})
