import streamlit as st
from supabase import create_client, Client

st.title('Teste ECMI 2')
st.write("Tabela")

SUPABASE_URL = "https://fdpjesdfiwnuxuabvrdn.supabase.co"
SUPABASE_KEY = st.secrets["supabase"]
connection: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
st.write("Sucesso: Cliente Supabase inicializado!")
resposta = connection.table("django_migrations").select("*").limit(1).execute()
st.write("Dados recebidos:", resposta.data)

# print('xuxu')
# nome = st.input('Digite o seu nome')
#if nome.upper() == 'JOSIR':
#    print(f'{nome} é legal!')
#else:
#    print('Eu não te conheço')
