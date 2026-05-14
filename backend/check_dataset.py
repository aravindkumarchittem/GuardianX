import pandas as pd
from utils.text_cleaner import clean_text

data = pd.read_csv("../dataset/social_engineering_messages.csv")

print("Before cleaning:")
print(data.head())

data["message"] = data["message"].apply(clean_text)

print("\nAfter cleaning:")
print(data.head())
