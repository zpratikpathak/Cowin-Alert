## Requirements
- Python 3.8.x
- Chrome Browser 92.0.x.x
## Installation
Install Dependecies using command 👇

`pip install -r requirements.txt`

Create a `.env` file in the root directory and add the following credentials

```
PINCODES=
gmail = 
gmailPassword = 
receiverEmail = 
```

- Add pincodes separated by Space eg. `PINCODES=12345 12343 12343`
- Add gmail Username
- Add gmail Password
- Add `receiverEmail` on which you want to receive email notification.

### Note:
+ If you get error `Wrong Username and password` then turn ON "Less Secure" option of your google account by visiting here https://myaccount.google.com/lesssecureapps
+ If you still get error go to https://g.co/allowaccess and autheticate yourself then try again
## How to run?
Use command

```python tracker .py```


## HEADLESS/GUI
You can turn ON/OFF Headless/GUI mode of chrome by commenting/uncommenting `line 10` of `tracker.py`

## TO DO
- Add various deployment Compatability
