import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20562331")

API_HASH = os.environ.get("API_HASH", "9e3e4148e73756a85b95fc69980b678d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7654333888:AAEZK_d0dWCK7u4gZjjOHcEF29q0LyvZj_g") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002245201063") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://deepchutia:deepchutia@123@cluster0.eqcc3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2107586423').split()]

PORT = os.environ.get("PORT", "8080")
