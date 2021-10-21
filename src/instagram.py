# Logic -  useful for build, execution and beautiful , this is the automation that creates the accounts in instagram
# code:
def NewAccount(proxy=False, hide=True):
    # imports
    from playwright.sync_api import sync_playwright
    from src.genName import genName; name = genName() # for generate new names with subnames
    from src.makeStorage import Storage as STORAGE; S = STORAGE() # new storage
    from src.tempMail import TempMail as TM; Tm = TM() # for recive emails

    # automation
    with sync_playwright() as p:
        # New storage for accounts
        Storage = S.New()
        browser = p.chromium.launch(headless=hide, proxy=proxy)
        page = browser.new_page()
        
        # Get Email and Name
        Storage.Email = Tm.NewEmail(page)
        Storage.Name = name.gen()
        
        
        # To avoid redirect, it will go to instagram twice 
        page.goto("https://www.instagram.com/sem/campaign/emailsignup/")
        page.goto("https://www.instagram.com/accounts/emailsignup/")

        selctor_email    = "div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_name     = "div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_username = "div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_password = "div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_btn_sub  = "div.bkEs3:nth-child(1) > button:nth-child(1)"
        
        # wait for email 
        page.wait_for_selector(selctor_email)
        # set email
        page.type(selctor_email, Storage.Email)
        # set name
        page.type(selctor_name, Storage.Name)

        # creating a password
        pwd = f"$p4sSworD_{Storage.Email}"
        user = f"us3r.{Storage.Name.replace(' ', '.')}.1"
        
        # save
        Storage.Username = user
        Storage.Pass = pwd

        # set username with pass
        page.type(selctor_password, pwd)
        page.type(selctor_username, user)
        page.click(selctor_btn_sub)

        # selecting age
        page.wait_for_selector("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6")
        page.evaluate("""()=>{
            const Opt = document.getElementsByClassName("h144Z  ")
            Opt[2].options.selectedIndex = 23
        }""")
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select")
        page.click("""//*[@id="react-root"]/section/main/div/div/div[1]/div[1]/span""")
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button")

        # setting code
        Storage.code = Tm.GetCode(Storage)
        page.type("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(1) > input", Storage.code)
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(2) > button")

        # close
        browser.close()
        return {"Email":Storage.Email, "Pass":Storage.Pass, "Username":Storage.Username}

class instagram:
    def __init__(self) -> None:
        self.NewAccount = NewAccount
