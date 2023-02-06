class Login_Locators:
    url_login = 'https://api.demoblaze.com/login'
    Error_message = 'Please fill out Username and Password.'
    valid_UserName_and_password = {"Username:": "zzzzz", "password:": "12345"}
    Invalid_password = {"Username:": "zzzzz", "password:": "2023"}
    Invalid_UserName = {"Username:": "wwwwww", "password:": "123456"}
    Invalid_password_and_UserName = {"Username:": "wwwww", "password:": "2023"}
