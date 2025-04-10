from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "25678105"))
API_HASH = environ.get("API_HASH", "7a99fee8bf428017b746942a0eb4835c")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7902264957:AAH8d4xqRejxc0Z0b-bGeA3hS8lcDD6SQWw
")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002360684548")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://Kmr:i0LnzrPXkHubOfWh@cluster0.qitptx5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
