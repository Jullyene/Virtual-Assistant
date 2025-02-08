import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

# Carregar o arquivo CSV
loader = CSVLoader(file_path="treinamento_ia_programacao_50.csv", encoding="utf-8")
documents = loader.load()

# Criar o banco de dados FAISS com embeddings
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

# Função para buscar informações similares
def retrieve_info(query):
    # Buscar resposta similar
    similar_response = db.similarity_search(query, k=3)
    return similar_response

# Exemplo de consulta
response = retrieve_info("O que é um método em programação?")
st.write(response)

llm = ChatOpenAI(temperature=1, model="gpt-3.5-turbo-16k-0613")

prompt_template = """
Você está ajudando um usuário a entender conceitos de programação a partir de uma tabela de treinamento. A tabela contém perguntas e respostas sobre programação.

Aqui estão as informações de treinamento:

Pergunta: {pergunta}
Categoria: {categoria}

Agora, com base na pergunta fornecida, forneça uma resposta adequada:
"""

# Definir o template com placeholders
template = PromptTemplate(
    input_variables=["pergunta", "categoria"], 
    template=prompt_template
)

# Exemplo de como usar o template com dados
pergunta = "O que é um método em programação?"
categoria = "Conceitos básicos"

# Gerar o prompt com base no template
prompt = template.format(pergunta=pergunta, categoria=categoria)
print(prompt)


chain - LLMChain(llm=llm, prompt=prompt)
def generate_response (message):
    best_response = retrieve_info(message)
    response = chain.run(message=message, best_practice=best_practice)
    return response


generate_response("O que é um retorno de função?")


# Comentários para me ajudar a entender os pensos de criação através do vídeo da Asimov Academy