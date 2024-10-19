import os
import sqlite3
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=load_dotenv("OPENAI_API_KEY"))

def enviar_mensagem(mensagem):
    resposta = client.chat.completions.create(model = "gpt-3.5-turbo", messages = mensagem)
    return resposta.choices[0].message

def save_message(role, content):
    conn = sqlite3.connect('chat_messages.db')

    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (role, content) VALUES (?, ?)', (role, content))
    
    conn.commit()
    conn.close()

def process_request(request):
    response = enviar_mensagem(request)
    
    save_message("user", request)
    save_message("assistant", response['content'])

    return response

def execute_generated_query(query):
    conn = sqlite3.connect('chat_messages.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

