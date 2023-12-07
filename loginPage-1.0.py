import json
import ttkbootstrap as ttk


def create_account():
    location = 'C:\\Users\\abir\\Desktop\\data.json'
    name = createnameEntry.get()
    password = createpassEntry.get()
    confirmpassword = createconfirmpassEntry.get()
    try:
        with open(location, "r") as json_file:
            accounts = json.load(json_file)
    except FileNotFoundError:
        accounts = {}
    if password == confirmpassword:
        if name not in accounts and password:
            accounts[name] = password
            signinerrormessageLabel.config(text="Account Created", foreground="green")
        else:
            signinerrormessageLabel.config(text="Account Exists", foreground="green")
    else:
        signinerrormessageLabel.config(text="Passwords must match", foreground="green")
    with open(location, "w") as json_file:
        json.dump(accounts, json_file)


def login():
    location = 'C:\\Users\\abir\\Desktop\\data.json'
    try:
        with open(location, "r") as json_file:
            accounts = json.load(json_file)
    except FileNotFoundError:
        loginerrormessageLabel.config(text="Account Doesnt Exist", foreground="green")
    name = loginnameEntry.get()
    password = loginpassEntry.get()
    if name in accounts and accounts[name] == password:
        loginerrormessageLabel.config(text="Login Successful", foreground="green")
        mainwindowpage()
    else:
        loginerrormessageLabel.config(text="Invalid Credentials", foreground="green")


def loginpage():
    signinerrormessageLabel.config(text="")
    createAccountframe.pack_forget()
    loginframe.pack(expand=True)


def creationpage():
    loginerrormessageLabel.config(text="")
    loginframe.pack_forget()
    createAccountframe.pack(expand=True)


window = ttk.Window(themename="journal")
window.title("Software")
window.resizable(False, False)
loginframe = ttk.Frame(window, height=450, width=350)
loginframe.pack(expand=True)
loginframe.propagate(False)
loginSubframe = ttk.Frame(loginframe)
loginLabel = ttk.Label(loginSubframe, text="LOGIN", font=("Hevletica", 15, "bold"))
loginnameLabel = ttk.Label(loginSubframe, text="Username", font=("Hevletica", 11))
loginnameEntry = ttk.Entry(loginSubframe, width=25, font=("Hevletica", 11))
loginpassLabel = ttk.Label(loginSubframe, text="Password", font=("Hevletica", 11))
loginpassEntry = ttk.Entry(loginSubframe, width=25, font=("Hevletica", 11), show="*")
loginButton = ttk.Button(loginSubframe, text="Login", command=login)
loginerrormessageLabel = ttk.Label(loginSubframe)
createAccountLabel = ttk.Label(loginSubframe, text="Don't have a account?")
createAccountButton = ttk.Button(loginSubframe, text="Sign up now", command=creationpage)
loginSubframe.pack(pady=30)
loginLabel.pack(pady=20)
loginnameLabel.pack(anchor="w", pady=5)
loginnameEntry.pack()
loginpassLabel.pack(anchor="w", pady=5)
loginpassEntry.pack()
loginButton.pack(pady=20, fill="x")
loginerrormessageLabel.pack(pady=5)
createAccountLabel.pack()
createAccountButton.pack(pady=5)

# account creation page
createAccountframe = ttk.Frame(window, height=500, width=350)
createAccountframe.propagate(False)
createAccountSubframe = ttk.Frame(createAccountframe)
createAccountLabel = ttk.Label(createAccountSubframe, text="SIGN UP", font=("Hevletica", 15, "bold"))
createnameLabel = ttk.Label(createAccountSubframe, text="Username", font=("Hevletica", 11))
createnameEntry = ttk.Entry(createAccountSubframe, width=25, font=("Hevletica", 11))
createpassLabel = ttk.Label(createAccountSubframe, text="Password", font=("Hevletica", 11))
createpassEntry = ttk.Entry(createAccountSubframe, width=25, font=("Hevletica", 11), show="*")
createconfirmpassLabel = ttk.Label(createAccountSubframe, text="Confirm Password", font=("Hevletica", 11))
createconfirmpassEntry = ttk.Entry(createAccountSubframe, width=25, font=("Hevletica", 11), show="*")
createAccountButton = ttk.Button(createAccountSubframe, text="Submit", command=create_account)
signinerrormessageLabel = ttk.Label(createAccountSubframe)
loginAccountLabel = ttk.Label(createAccountSubframe, text="Already have a account?")
loginAccountButton = ttk.Button(createAccountSubframe, text="Sign in now", command=loginpage)
createAccountSubframe.pack(pady=30)
createAccountLabel.pack(pady=20)
createnameLabel.pack(anchor="w", pady=5)
createnameEntry.pack()
createpassLabel.pack(anchor="w", pady=5)
createpassEntry.pack()
createconfirmpassLabel.pack(anchor="w", pady=5)
createconfirmpassEntry.pack()
createAccountButton.pack(pady=20, fill="x")
signinerrormessageLabel.pack(pady=5)
loginAccountLabel.pack()
loginAccountButton.pack(pady=5)

#mainwindow
def mainwindowpage():
    loginframe.pack_forget()
    mainwindow.pack(expand=True,fill="both")
mainwindow = ttk.Frame(window)
WelcomeLabel = ttk.Label(mainwindow, text="Welcome")
WelcomeLabel.pack()
window.mainloop()
