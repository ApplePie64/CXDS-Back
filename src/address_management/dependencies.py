# Dependencies for address_management
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Load Supabase credentials from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_ANON_KEY")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)