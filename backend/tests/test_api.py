import requests

url = "http://127.0.0.1:5000/analyze-message"

test_messages = [
    # ✅ Safe
    "Hello, how are you doing today?",
    "Let us meet tomorrow to discuss the project",

    # 🟠 Social engineering
    "Please don’t tell anyone about this, I trust only you",
    "This is urgent, your account will be locked if you don’t respond now",
    "You are very mature for your age, let’s keep this conversation private",

    # 🔴 Dangerous
    "If you do not cooperate, there will be serious consequences",
    "I am from the admin team, verify your details immediately to avoid issues"
]

for msg in test_messages:
    try:
        response = requests.post(url, json={"message": msg})
        result = response.json()

        print("\nMessage:", msg)
        print("Risk:", result.get("risk_level"))
        print("Score:", result.get("final_score"))
        print("Confidence:", result.get("ml_confidence"))
        print("Reasons:", result.get("reasons"))
        print("-" * 60)

    except Exception as e:
        print("Error:", e)




# import requests

# url = "http://127.0.0.1:5000/analyze-message"

# test_messages = [
#     # ✅ Normal / Safe
#     "Hello, how are you doing today?",
#     "Let us meet tomorrow to discuss the project",

#     # 🟠 Social engineering – trust & secrecy
#     "Please don’t tell anyone about this, I trust only you",

#     # 🟠 Social engineering – urgency & authority
#     "This is urgent, your account will be locked if you don’t respond now",

#     # 🟠 Social engineering – grooming style manipulation
#     "You are very mature for your age, let’s keep this conversation private",

#     # 🔴 Explicit threat / coercion
#     "If you do not cooperate, there will be serious consequences",

#     # 🔴 Hybrid case (polite but dangerous)
#     "I am from the admin team, verify your details immediately to avoid issues"
# ]

# for msg in test_messages:
#     response = requests.post(url, json={"message": msg})
#     print("Message:", msg)
#     print("Response:", response.json())
#     print("-" * 50)
