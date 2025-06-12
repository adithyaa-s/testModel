from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
# from pytube import YouTube
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
# import faiss from "faiss-cpu"
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def getQuestions():
    transcript = """prisma an open source tool that makes it fun and safe to work with your database the relational database is ancient technology that has stood the test of time but writing sql code is not an ideal abstraction for modern app development it provides too much low level control and you'll probably blow your foot off writing it to address this concern orms like sqlize implement object relational mapping to express data with object oriented code like javascript classes prisma is also an orm that addresses similar problems but instead it has its own declarative schema definition language you write a schema to express your data and relationships in a human readable way or the schema can be automatically inferred from any existing database prisma then converts the schema into type definitions allowing you to perform typesafe crud operations with your own database models which means you get ide autocompletion tailored to your own custom schema in addition it handles migrations as your data structure evolves and if you want to visualize your data prisma studio allows you to view and manage all of your tables and rows in the browser to get started you'll need a relational database like mysql or postgres although mongodb is supported as well from a nodejs project run npx prisma init this creates a env file where you can add your database url and a prisma directory to define the schema if the existing database already has data we can run prismadb pool to introspect it and automatically generate the schema from it notice how each table is represented with the model keyword then inside the braces we have column names and their data types as well as optional constraints like for example we might use relation to create a foreign key constraint between a weapon and a human and we can also index the weapon id while we're at it the beauty of this is that the code is significantly more concise than what you would write otherwise in raw sql now if we decide to modify our schema like add an extra timestamp column we'll also need to modify the database structure which can be handled automatically with the prisma migrate command now to interact with the database on the server we tell prisma to generate the client library import the client into a javascript file and notice how it auto-completes the models in the schema if you do something wrong you'll know about it right away now find all the humans with the find menu method to filter the results we can add a where clause as a plain javascript object and if we want to join a related table we can do that by adding the include object prisma already knows how to run the complicated sql code under the hood and returns the data as an array of javascript objects ready to use in your application this has been prisma in 100 seconds if you want to see more short """
    system_template = "Given a video transcript, analyse it and generate me 5 questions from it. Strictly frame the questions only from the transcript and provide the output back as a list of questions. Refer to the data source as 'the video' rather than the transcript. For each question,  generate 4 options labelled alphabetically from 'A' to 'D'."

    prompt_template = ChatPromptTemplate.from_messages(
        [("system",system_template),("user",transcript)]
    )

    messages = prompt_template.format_messages()
    result = llm.invoke(messages)
    return result.content

def askMe(userQuestion: str):
    prompt_template = PromptTemplate.from_template("Please reply to the user input : {question}")
    formatted_prompt = prompt_template.format(question=userQuestion)
    result = llm.invoke(formatted_prompt)
    return result.content
    

# from langchain_community.vectorstores import FAISS
# from langchain_openai import OpenAIEmbeddings
# # from langchain_community.document_loaders import YoutubeLoader

# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain_core.documents import Document
# import os
# from dotenv import load_dotenv
# load_dotenv()

# # embeddings = OpenAIEmbeddings()
# embeddings = OpenAIEmbeddings(
#     openai_api_key=os.getenv("OPENAI_API_KEY"),
#     openai_organization=os.getenv("OPENAI_ORG_ID")
# )


# # video_url = "rLRIB6AF2Dg"
# def create_db() -> FAISS:
#     transcript = """prisma an open source tool that makes it fun and safe to work with your database the relational database is ancient technology that has stood the test of time but writing sql code is not an ideal abstraction for modern app development it provides too much low level control and you'll probably blow your foot off writing it to address this concern orms like sqlize implement object relational mapping to express data with object oriented code like javascript classes prisma is also an orm that addresses similar problems but instead it has its own declarative schema definition language you write a schema to express your data and relationships in a human readable way or the schema can be automatically inferred from any existing database prisma then converts the schema into type definitions allowing you to perform typesafe crud operations with your own database models which means you get ide autocompletion tailored to your own custom schema in addition it handles migrations as your data structure evolves and if you want to visualize your data prisma studio allows you to view and manage all of your tables and rows in the browser to get started you'll need a relational database like mysql or postgres although mongodb is supported as well from a nodejs project run npx prisma init this creates a env file where you can add your database url and a prisma directory to define the schema if the existing database already has data we can run prismadb pool to introspect it and automatically generate the schema from it notice how each table is represented with the model keyword then inside the braces we have column names and their data types as well as optional constraints like for example we might use relation to create a foreign key constraint between a weapon and a human and we can also index the weapon id while we're at it the beauty of this is that the code is significantly more concise than what you would write otherwise in raw sql now if we decide to modify our schema like add an extra timestamp column we'll also need to modify the database structure which can be handled automatically with the prisma migrate command now to interact with the database on the server we tell prisma to generate the client library import the client into a javascript file and notice how it auto-completes the models in the schema if you do something wrong you'll know about it right away now find all the humans with the find menu method to filter the results we can add a where clause as a plain javascript object and if we want to join a related table we can do that by adding the include object prisma already knows how to run the complicated sql code under the hood and returns the data as an array of javascript objects ready to use in your application this has been prisma in 100 seconds if you want to see more short """
#     document = Document(page_content=transcript)
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     docs = text_splitter.split_documents([document])
    
#     db = FAISS.from_documents(docs, embeddings)

#     return db
# db = create_db()
# print(db)