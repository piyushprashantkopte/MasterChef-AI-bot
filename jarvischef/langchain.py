from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from decouple import config


def askJarvisChef(recipe_message):
    SECRET_KEY=config('GROQ_API_KEY')
    chat = ChatGroq(temperature=0, groq_api_key=SECRET_KEY, model_name="deepseek-r1-distill-llama-70b")

    system = "Your name is Jarvis. You are a master chef so First Introduce yourself as Jarivs The Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries. If You don't know the answer then tell I don't know the answer."
    human = "{asked_recipe}"

    chatPrompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])


    chain = chatPrompt | chat
    #print (formattedChatPtompt, chatPrompt)
    response = chain.invoke({"asked_recipe": recipe_message})
    return response.content