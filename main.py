# Path
from playwright.sync_api import sync_playwright
import random, re, requests, json

# Get Names
names = ["marillia", "marine", "ana", "vitoria", "vivi", "surtada", "marcia", "juju", "karol", "karoline", "coralline", "sophia", "emily", "sofia", "sara", "alice", "jessica", "irelia", "issabella", "leticia", "isadora", "laura", "manu", "manuela", "luisa", "maria", "joselli"]
subnames  = ["silva", "alckerman", "mendonca", "carlo", "uzumaki", "oliveira", "santos", "souza", "ferreira", "alves", "lima", "gomes", "ribeiro", "martins", "carvalho", "aumeida", "lopes", "soares", "fernandes", "vieira", "barbosa", "rocha", "dias", "naicimento", "nunes", "machado", "cardoso", "teixeira"]
def get_new_name():
    def F(list):
        return random.randint(0, len(list)) - 1

    return f"{names[F(names)]} {subnames[F(subnames)]}"
class Names:
    def __init__(self):
        self.get_new_name = get_new_name

# Account Class
class Account:
    def __init__(self):
        self.Username = ""
        self.Email = ""
        self.Name = ""
        self.Password = ""
        self.year = ""

# Get New Email
def GetEmail(page, ac):
    print("\t * getting email")

    page.goto("https://cryptogmail.com/")
    page.wait_for_selector(".field--value")
    email =  page.evaluate("""()=>{
        const email = document.getElementsByClassName("field--value js-email")
        const e = email[0]
        return e.innerText
    }""")
    print(f"\t\t -> email: {email}")
    ac.Email = email

# Get New Code
def GetCode(email):
    print("\t [*] getting code (may take)")
    while True:
        res = requests.get(f"https://cryptogmail.com/api/emails?inbox={email}").text
        if re.search("<!DOCTYPE html>", res):
            pass
        else:
            js = json.loads(res)
            code = js["data"][0]["subject"]
            code = code.replace(" is your Instagram code", "")
            return code

# Instagram
def instagram():
    print("[*] Starting instagram automation")
    
    with sync_playwright() as p:
        print("[log] in actions: {")
        ac = Account()

        printin_url = "https://www.instagram.com/sem/campaign/emailsignup/"

        print("\t opening browser")
        browser = p.chromium.launch(headless=True)

        print("\t opening page")
        page = browser.new_page()

        GetEmail(page, ac)

        print(f"\t Going to: {printin_url}")
        page.goto(printin_url)
        page.goto("https://www.instagram.com/accounts/emailsignup/")

        selctor_email    = "div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_name     = "div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_username = "div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_password = "div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_btn_sub  = "div.bkEs3:nth-child(1) > button:nth-child(1)"
        
        print("\t waiting for page")
        page.wait_for_selector(selctor_email)

        # auto
        def Set_Email():
            page.type(selctor_email, ac.Email)
        
        def Set_Name():
            name = n.get_new_name()    
            page.type(selctor_name, name)
            ac.Name = name

        def Set_Password_and_Name(name):
            pwd = str(random.randint(0, 72) * 2)
            pwd += name+pwd
            pwd = pwd.replace(" "  , f"_{random.randint(0, 6)}_")

            user = pwd.replace("_", "__")
            page.type(selctor_password, pwd)
            page.type(selctor_username, user)

            ac.Password = pwd
            ac.Username = user

        def SelectDate():
            print("\t selecting age")
            page.wait_for_selector("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6")
            page.evaluate("""()=>{
                const Opt = document.getElementsByClassName("h144Z  ")
                Opt[2].options.selectedIndex = 23
            }""")
            page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select")
            page.click("""//*[@id="react-root"]/section/main/div/div/div[1]/div[1]/span""")
            page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button")

        def SelectCode(code):
            print(f"\t\t code: {code}")
            page.type("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(1) > input", code)
            page.click("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(2) > button")
        
        def SaveAcc(ac):
            print("\t account saved in:: ./accs.txt")
            file = open("accs.txt", "a")
            payload = f"""Email: {ac.Email}\nPass: {ac.Password}\nUsername: {ac.Username}\n"""
            file.write(payload)
            file.close()

        Set_Email()
        Set_Name()
        Set_Password_and_Name(ac.Name)
        page.click(selctor_btn_sub)
        
        SelectDate()
        code = GetCode(ac.Email)
        SelectCode(code)
        SaveAcc(ac)
        
        print("}")
        browser.close()

        print(f"# Your account is: \"{ac.Email}\" Pass: \"{ac.Password}\"")

# Main Func
if __name__ == "__main__":
    instagram()        
