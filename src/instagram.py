# Logic -  useful for build, execution and beautiful , this is the automation that creates the accounts in instagram
# code:
from logging import log


def NewAccount(proxy=False, hide=True, debug=False):
    # imports
    from playwright.sync_api import sync_playwright
    from src.genName import genName; name = genName() # for generate new names with subnames
    from src.makeStorage import Storage as STORAGE; S = STORAGE() # new storage
    from src.tempMail import TempMail as TM; Tm = TM() # for recive emails
    from src.log import Console; console = Console()

    # automation
    with sync_playwright() as p:
        # New storage for accounts
        if debug: console.Log("== DEBUG MODE ==")
        if debug: console.Log("Creating new Storage")

        Storage = S.New()
        
        if debug: console.Log("Starting Browser")
        if proxy == False:
            browser = p.chromium.launch(headless=hide)
        else:
            log(f"Using Proxy -> {proxy['config']}")
            browser = p.chromium.launch(headless=hide, proxy=proxy)
       
        page = browser.new_page()
        
        # Get Email and Name
        if debug: console.Log("Getting email")
        Storage.Email = Tm.NewEmail(page)
        Storage.Name = name.gen()
        
        if debug: console.Log(f"email: {Storage.Email}")

        # To avoid redirect, it will go to instagram twice 
        if debug: console.Log("Going to: https://www.instagram.com/sem/campaign/emailsignup/")
        page.goto("https://www.instagram.com/sem/campaign/emailsignup/")
        page.goto("https://www.instagram.com/accounts/emailsignup/")

        selctor_email    = "div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_name     = "div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_username = "div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_password = "div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)"
        selctor_btn_sub  = "div.bkEs3:nth-child(1) > button:nth-child(1)"
        
        # wait for email
        if debug: console.Log("Waiting for Selector .email")
        page.wait_for_selector(selctor_email)
        # set email
        if debug: console.Log(f"Seting Email: {Storage.Email}")
        page.type(selctor_email, Storage.Email)
        # set name
        if debug: console.Log(f"Seting Name: {Storage.Name}")
        page.type(selctor_name, Storage.Name)

        # creating a password
        pwd = f"$p4sSworD_{Storage.Email}"
        user = f"us3r.{Storage.Name.replace(' ', '.')}.1"
        
        # save
        if debug: console.Log(f"User: {user}, {pwd}")
        Storage.Username = user
        Storage.Pass = pwd

        # set username with pass
        page.type(selctor_password, pwd)
        page.type(selctor_username, user)
        page.click(selctor_btn_sub)

        # selecting age
        if debug: console.Log("selecting age")
        
        page.wait_for_selector("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6")
        page.evaluate("""()=>{
            const Opt = document.getElementsByClassName("h144Z  ")
            Opt[2].options.selectedIndex = 23
        }""")
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select")
        page.click("""//*[@id="react-root"]/section/main/div/div/div[1]/div[1]/span""")
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button")

        # setting code
        if debug: console.Log("wait for code (it'ay take)")
        Storage.code = Tm.GetCode(Storage)
       
        if debug: console.Log(f"code: {Storage.code}")
        page.type("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(1) > input", Storage.code)
        page.click("#react-root > section > main > div > div > div:nth-child(1) > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > form > div > div:nth-child(2) > button")


        # close
        if debug: console.Log("Closing Browser")
        browser.close()
        class Account:
            Email = Storage.Email
            Pass = Storage.Pass
            User = Storage.Username
        
        return Account

class instagram:
    def __init__(self) -> None:
        self.NewAccount = NewAccount
