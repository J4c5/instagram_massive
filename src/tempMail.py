# Logic - a scraper that will go through until the site gets the email, then it will update the inbox to get new emails
# code:
def GetEmail(page): # for get email, we using browser
        page.goto("https://cryptogmail.com/")
        page.wait_for_selector(".field--value")
        email =  page.evaluate("""()=>{
            const email = document.getElementsByClassName("field--value js-email")
            const e = email[0]
            return e.innerText
        }""")
        
        if email == "":
            GetEmail()
        else:
            return email

def GetCode(Storage):
    import requests, re, json
    while True:
        res = requests.get(f"https://cryptogmail.com/api/emails?inbox={Storage.Email}").text
        if re.search("<!DOCTYPE html>", res):
            pass
        else:
            js = json.loads(res)
            code = js["data"][0]["subject"]
            code = code.replace(" is your Instagram code", "")
            return code

class TempMail:
    def __init__(self) -> None:
        self.NewEmail = GetEmail
        self.GetCode  = GetCode