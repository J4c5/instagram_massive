# How to Use
### Simple Example:
```py
from src.instagram import instagram; insta = instagram()

Account = insta.NewAccount()
print(Account)
```
> Response
`{"Email":email@sub.com, "Pass":password, "Username":username}`

### Simple Example with proxy:
```py
from src.instagram import instagram; insta = instagram()

Account = insta.NewAccount(proxy={"server":"u proxy"})
print(Account)
```
> Response
`{"Email":email@sub.com, "Pass":password, "Username":username}`

### Simple Example with debug mode:
```py
from src.instagram import instagram; insta = instagram()

Account = insta.NewAccount(debug=true)
print(Account)
```
#### if you leave debug enabled you will see something like this:
> Response
```py
== DEBUG MODE ==
log - Creating new Storage
log - Starting Browser
log - Getting email
log - email: ************
log - Going to: https://www.instagram.com/sem/campaign/emailsignup/
log - Waiting for Selector .email
log - Seting Email: ************
log - Seting Name: manuela lima
log - User: *****, **********
log - selecting age
log - wait for code (it'ay take)
log - code: 749581
log - Closing Browser
{"Email":email@sub.com, "Pass":password, "Username":username}
```
> Hey, check out how this [project](https://github.com/gh-ninja/instagram_massive) can be useful at: [examples](https://github.com/gh-ninja/instagram_massive/tree/main/example) ! Tank'U ❤️ 
