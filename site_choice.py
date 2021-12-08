def get_choice() -> str:
   choices = {1: "ebay", 2: "amazon"}
   user_choice = int(input("type 1 or 2 "))
   return choices[user_choice]
print(get_choice())
