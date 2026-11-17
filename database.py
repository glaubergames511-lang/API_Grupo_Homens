import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtém as credenciais
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Cria a conexão com o Supabase
supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)