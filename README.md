
# Weather Alert

This program sends you a SMS directly to your number to let you know today is going to rain and suggests you take an umbrella with you.

## Description

#### **How to work with Twilio**

->First, Create a trial account

->After that, it goes through few checkbox questions to know the purpose of the user.

->After all the setup completed, going through this link will take you to the site were we can sent messages 

```bash
  https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms
```

-> Get the virtual ph number and modify the code in preferred programming language. Copy and paste the code in our program.

#### **PythonAnywhere**

->This program can be executed every day using "python everywhere"

->First create an account

->Add program files in files tab and folder(same name as in program "letter_templates") in directories

->Create new bash console in "console" tab

->run cmd "python3 main.py" to run our program

->If "smtpAuthenticationError" occurs the copy the link at the end of the message and search it

->Once page loaded, under step 2, click the link "DisplayUnlockCaptcha" and hit "continue"

->run cmd "python3 main.py" again and nothing if displayed, the code executed successfully

->To run this program daily, go to "task" tab

->Type cmd "python3 main.py" in the input field and utc time

->Click "create", CONGRATS!!! this program will run daily at specified utc time.

#### **NOTE :** If you're trying to use Twilio on a PythonAnywhere free account, you're likely to run into an error. To fix that, go through the link in acknowledgement.


## API Reference

#### Open Weather
```http
  https://api.openweathermap.org/data/2.5/forecast
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |



| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `lat`      | `num` | **Required**. Your latitude |
| `lon`      | `num` | **Required**. Your longitude |
| `appid`      | `string` | **Required**. API key |
| `cnt`      | `num` | **Optional**. Number of time stamps  |

#### Twilio
```http
  https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `auth_token` | `string` | **Required**. Your API key |
| `account_sid`      | `string` | **Required**. Your acc ID


Need to create free account in order to get api key from both sites.

5 Day / 3 Hour Forecast api from Open Weather api is used.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OW_API_KEY`

`account_sid`

`auth_token`

`from_`

`to`


## Acknowledgements

 - [Twilio to work on Free accounts with the proxy](https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/)


