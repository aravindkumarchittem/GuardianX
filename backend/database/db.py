# from pymongo import MongoClient


# client = MongoClient(MONGO_URI)

# db = client["guardianx_db"]

# # ✅ existing
# messages_collection = db["flagged_messages"]

# # ✅ ADD THIS LINE
# users_collection = db["users"]

from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin:admin123@cluster0.ovdjtzu.mongodb.net/guardianx_db?retryWrites=true&w=majority"

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=True,
    serverSelectionTimeoutMS=5000
)

try:
    client.server_info()  # forces connection test
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Failed:", e)

db = client["guardianx_db"]

messages_collection = db["flagged_messages"]
users_collection = db["users"]