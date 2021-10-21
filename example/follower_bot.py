# Logic - creating a simple follower bot with it
# code:
from src.instagram import instagram; insta = instagram()
from instagram_private_api import Client, ClientCompatPatch

Account = insta.NewAccount()
user_name = Account.Email
password = Account.Pass

print(f"Bot - Using: {user_name}, {password}")
api = Client(user_name, password)
instaId = "11873066713"

print(f"Follow {instaId}")
api.friendships_create(instaId) # follow this
