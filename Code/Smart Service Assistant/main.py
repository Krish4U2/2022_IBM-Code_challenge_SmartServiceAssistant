import clipboard as clipboard
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract

import matplotlib.pyplot as plt
import cv2
import easyocr
import json
from pylab import rcParams
from IPython.display import Image
import requests
rcParams['figure.figsize'] = 8, 16

#Internal storage to store new details as well as a dummy data to check with initial test Cases.

listOfNames={
    '9188890350': 'R Abhiramya'
}
listUserID={
    '9188890350': 'Abhu_1399'
}
listRationCard={
    '9188890350': '1422055492'
}
listPassword={
    '9188890350': 'Abhiramya@1'
}
listMobile=['9188890350']
listEmail={
    '9188890350':'abhiramyaramesh@gmail.com'
}
listAdhaar={
    '9188890350' : '829197161833'
}
listGender={}


def assignData(adhaarNum,rationCardNum,mobileNum,name,email,password,gender): # Function to store real time data to an internal database as well as online API call as JSON
    listMobile.append(mobileNum)
    listAdhaar[mobileNum]=adhaarNum
    listPassword[mobileNum]=password
    listOfNames[mobileNum]=name
    listRationCard[mobileNum]=rationCardNum
    listEmail[mobileNum]=email
    listGender[mobileNum]=gender

    url = "https://getpantry.cloud/apiv1/pantry/aa1efbb9-4072-484e-a02d-7b8b664877f8/basket/SmartServiceAssistant"

    payload = json.dumps({
        "Name": name,
        "Mobile": mobileNum,
        "RationCard": rationCardNum,
        "Email": email,
        "Gender": gender,
        "Aadhar Number": adhaarNum
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

#Function to create new account in Kerala Civil Supplies Online citizen Login portal

def createNewAccount(name='Abhiramya',userID='Prad_1969',email='abhiramya@gmail.com',password='Abhiramya@1',adhaarNum='829197161833',rationCardNum='1422055492',mobileNum='9074568912'):
    driver = webdriver.Chrome()     #Creating object instance from Selenium Chrome driver which is a browser automation tool.
    driver.maximize_window()        #Maximize window
    driver.get(r'https://ecitizen.civilsupplieskerala.gov.in/index.php/c_registration')
    count = 0
    while True and count == 0:
        pointer = None
        pointer = pyautogui.locateOnScreen(r'Photos/ConfirmCreateAccount.png')
        if pointer:
            driver.find_element(By.XPATH, '//*[@id="uid"]').send_keys(adhaarNum)
            driver.find_element(By.XPATH, '//*[@id="rcTest"]').send_keys(rationCardNum)
            driver.find_element(By.XPATH, '//*[@id="auth_chk"]').click()
            driver.find_element(By.XPATH, '//*[@id="bCodeValidate"]').click()
            while True and count == 0:
                invalid = None
                time.sleep(2)
                invalid = pyautogui.locateOnScreen(r'Photos/InvalidAdhaar.png')
                if invalid:
                    print("Invalid adhaar number. Not matched with ration card Number")
                else:
                    driver.find_element(By.XPATH, '//*[@id="rUserLogin"]').send_keys(userID)
                    driver.find_element(By.XPATH, '//*[@id="rPass"]').send_keys(password)
                    driver.find_element(By.XPATH, '//*[@id="rCpass"]').send_keys(password)
                    driver.find_element(By.XPATH, '//*[@id="uEmail"]').send_keys(email)
                    driver.find_element(By.XPATH, '//*[@id="rMob"]').send_keys(mobileNum)
                    driver.find_element(By.XPATH, '//*[@id="cap_img"]').click()
                    while True and count==0:
                        pointer=None
                        pointer=pyautogui.locateCenterOnScreen(r'Photos/CaptchaSave.png',confidence=0.5)
                        if pointer:
                            pyautogui.moveTo(pointer[0],pointer[1])
                            pyautogui.moveRel(-100,0)
                            pyautogui.rightClick()
                            pyautogui.press('down')
                            pyautogui.press('down')
                            pyautogui.press('enter')
                            while True and count==0:
                                pointer=pyautogui.locateOnScreen(r'Photos/SaveAs.png')
                                if pointer:
                                    pyautogui.moveTo(pointer[0],pointer[1])
                                    pyautogui.moveRel(-10,10)
                                    pyautogui.click()
                                    pyautogui.write(r'C:\Users\Asus\Desktop\Project\Smart Service Assistant\Captcha')
                                    pyautogui.press('enter')
                                    while True and count==0:
                                        pointer=None
                                        pointer=pyautogui.locateOnScreen(r'Photos/ConfirmLocation.png',confidence=0.8)
                                        if pointer:
                                            pyautogui.moveTo(pointer[0],pointer[1])
                                            pyautogui.moveRel(-100,0)
                                            pyautogui.doubleClick()
                                            pointer=None
                                            count=0
                                            while True and count==0:
                                                pointer=pyautogui.locateCenterOnScreen(r'Photos/Yes.png')
                                                if pointer:
                                                    pyautogui.moveTo(pointer[0],pointer[1])
                                                    pyautogui.click()
                                                    time.sleep(2)
                                                    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # importing pytesseract. User should install this on the PC
                                                    captcha = pytesseract.image_to_string(r'Captcha/Captcha.jpg')
                                                    finecap = []
                                                    for i in range(len(captcha)):
                                                        if captcha[i].isnumeric():
                                                            finecap.append(captcha[i])
                                                    if len(finecap) == 6:
                                                        captcha=''.join(finecap)
                                                        driver.find_element(By.XPATH, '//*[@id="txtcaptcha"]').send_keys(captcha)
                                                        sendSuccess(userID,password)

                                                    else:
                                                        driver.close()
                                                        createNewAccount()

                                                    count=1

                    time.sleep(10)
                    count = 1
                    time.sleep(10)


def sendSuccess(userID,password):   #Successful account creation message to the USER
    count = 0
    while True and count == 0:
        whatsappIcon = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Icon.png', confidence=0.7)
        if whatsappIcon:
            pyautogui.moveTo(whatsappIcon[0], whatsappIcon[1])
            pyautogui.click()
            count = 0
            while True and count == 0:
                whatsappSendmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Sendmsg.png', confidence=0.7)
                if whatsappSendmsg:
                    pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                    pyautogui.click()
                    pyautogui.write("Successfully Created Account for you..!")
                    time.sleep(2)
                    pyautogui.write("\n")
                    time.sleep(2)
                    pyautogui.write('User ID: '+userID+'and Password :'+password)
                    time.sleep(2)
                    pyautogui.write("\n")
                    time.sleep(2)
                    waitForResponse()

def sendSuccessLogin(): #Sending status of succesfull logging to the portal
    count = 0
    while True and count == 0:
        whatsappIcon = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Icon.png', confidence=0.7)
        if whatsappIcon:
            pyautogui.moveTo(whatsappIcon[0], whatsappIcon[1])
            pyautogui.click()
            count = 0
            while True and count == 0:
                whatsappSendmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Sendmsg.png', confidence=0.7)
                if whatsappSendmsg:
                    pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                    pyautogui.click()
                    pyautogui.write("Successfully Logged into your account..!")
                    time.sleep(2)
                    pyautogui.write("\n")
                    time.sleep(2)
                    pyautogui.write('Services Offered by Your SMART ASSISTANT; 1.Change Address  2.Change NRK Status   3.Add or Remove a member    4.Other Services')
                    time.sleep(2)
                    pyautogui.write("\n")
                    time.sleep(2)
                    waitForResponse()


def waitForResponse():  #Function to wait on another chathead to receive new notification in whatsapp from USER
    count = 0
    while True and count == 0:
        whatsappDefault = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Default.png', confidence=0.7)
        if whatsappDefault:
            pyautogui.moveTo(whatsappDefault[0], whatsappDefault[1])
            pyautogui.click()
            count=1
            clickUser()

def waitForNewMsg():    #Function to click on new message when new user is send new messages
    count = 0
    whatsappNotification = None
    while True and count == 0:
        whatsappNotification = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Newmsg.png', confidence=0.7)
        if whatsappNotification:
            pyautogui.moveTo(whatsappNotification[0], whatsappNotification[1])
            pyautogui.click()
            time.sleep(2)
            count = 1




def readStringFromUser():  # Raw string reading from the USER whatsapp message.
    count = 0
    while True and count == 0:
        whatsappDefault = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Default.png', confidence=0.7)
        if whatsappDefault:
            pyautogui.moveTo(whatsappDefault[0], whatsappDefault[1])
            pyautogui.click()
            waitForNewMsg()
            count3 = 0
            whatsappReadmsg = None
            while True and count3 == 0:
                whatsappReadmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Readmsg.png', confidence=0.5)
                if whatsappReadmsg:
                    pyautogui.moveTo(whatsappReadmsg[0], whatsappReadmsg[1])
                    pyautogui.moveRel(0, -100)
                    pyautogui.tripleClick()
                    pyautogui.hotkey('ctrl', 'c')
                    message = clipboard.paste()
                    return message


def readingUserDetails():       #Function to read the User details which should be numeric.
    count = 0
    while True and count == 0:
        whatsappDefault = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Default.png', confidence=0.7)
        if whatsappDefault:
            pyautogui.moveTo(whatsappDefault[0], whatsappDefault[1])
            pyautogui.click()
            waitForNewMsg()
            count3 = 0
            whatsappReadmsg = None
            while True and count3 == 0:
                whatsappReadmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Readmsg.png', confidence=0.5
                                                                 )
                if whatsappReadmsg:
                    pyautogui.moveTo(whatsappReadmsg[0], whatsappReadmsg[1])
                    pyautogui.moveRel(0, -100)
                    pyautogui.tripleClick()
                    pyautogui.hotkey('ctrl', 'c')
                    message = clipboard.paste()
                    if message.isnumeric():
                        count3 = 1
                        return message
                    else:
                        count2=0
                        while count2==0:
                            whatsappSendmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Sendmsg.png',confidence=0.7)
                            if whatsappSendmsg:
                                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                                pyautogui.click()
                                pyautogui.write('Please re-enter your Details')
                                time.sleep(1)
                                pyautogui.write('\n')
                                time.sleep(1)
                                message=readingUserDetails()
                                return message



            if count3==1:
                count = 1
def loginToPortal(userID='username',password='password',mobileNum=9443355647): #Function to login to PDS portal
    driver = webdriver.Chrome()  # Creating object instance from Selenium Chrome driver which is a browser automation tool.
    driver.maximize_window()  # Maximize window
    driver.get(r'https://ecitizen.civilsupplieskerala.gov.in/index.php/c_login')
    while True:
        pointer=None
        pointer=pyautogui.locateOnScreen(r'Photos/CitizenLogin.png')
        if pointer:
            driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(userID)
            driver.find_element(By.XPATH,'//*[@id="hiddenpass"]').send_keys(password)
            count=0
            while True and count == 0:
                pointer = None
                pointer = pyautogui.locateCenterOnScreen(r'Photos/CaptchaLoginSave.png', confidence=0.5)
                if pointer:
                    pyautogui.moveTo(pointer[0], pointer[1])
                    pyautogui.moveRel(-100, 0)
                    pyautogui.rightClick()
                    pyautogui.press('down')
                    pyautogui.press('down')
                    pyautogui.press('enter')
                    while True and count == 0:
                        pointer = pyautogui.locateOnScreen(r'Photos/SaveAs.png')
                        if pointer:
                            pyautogui.moveTo(pointer[0], pointer[1])
                            pyautogui.moveRel(-10, 10)
                            pyautogui.click()
                            pyautogui.write(r'C:\Users\Asus\Desktop\Project\Smart Service Assistant\Captcha')
                            pyautogui.press('enter')
                            while True and count == 0:
                                pointer = None
                                pointer = pyautogui.locateOnScreen(r'Photos/ConfirmLocation.png', confidence=0.8)
                                if pointer:
                                    pyautogui.moveTo(pointer[0], pointer[1])
                                    pyautogui.moveRel(-100, 0)
                                    pyautogui.doubleClick()
                                    pointer = None
                                    count = 0
                                    while True and count == 0:
                                        pointer = pyautogui.locateCenterOnScreen(r'Photos/Yes.png')
                                        if pointer:
                                            pyautogui.moveTo(pointer[0], pointer[1])
                                            pyautogui.click()
                                            time.sleep(2)
                                            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # importing pytesseract. User should install this on the PC
                                            captcha = pytesseract.image_to_string(r'Captcha/Captcha.jpg')
                                            finecap = []
                                            for i in range(len(captcha)):
                                                if captcha[i].isnumeric():
                                                    finecap.append(captcha[i])
                                            print(''.join(finecap))
                                            if len(finecap) == 6:
                                                captcha = ''.join(finecap)
                                                driver.find_element(By.XPATH,'//*[@id="txtcaptcha"]' ).send_keys(captcha)
                                                time.sleep(2)
                                                sendSuccessLogin()
                                                count=1

                                            else:
                                                driver.close()
                                                time.sleep(2)
                                                loginToPortal(userID, password, mobileNum)

def detectDetailsFromAdhaar(whatsappSendmsg,mobileNum):  # Optical Character Recognition from an image and extract the informations from an image and stored on the database and cloud
    Image("test2.png")
    reader = easyocr.Reader(['en'])
    output = reader.readtext('test2.png')
    name = output[4][-2]
    dob = output[6][-2][19:]
    gender = output[8][-2][6:]
    adhaarNo = output[13][-2]
    nadhaar = []
    for i in adhaarNo:
        if (i.isnumeric() == True):
            nadhaar.append(i)
    adhaarstr = ''.join(nadhaar)
    thisdict = {
        "Name": name,
        "DoB": dob,
        "Gender": gender,
        "Adhaar No": adhaarstr
    }
    print(thisdict)
    json_object = json.dumps(thisdict, indent=0)
    print(json_object)
    pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
    pyautogui.click()
    time.sleep(1)
    pyautogui.write('Your Name:'+thisdict['Name']+'   Your DoB:'+thisdict['DoB']+'   Your Gender :'+thisdict['Gender'])
    time.sleep(3)
    pyautogui.write('\n')
    pyautogui.write('\n')
    listMobile.append(mobileNum)
    listOfNames[mobileNum]=thisdict['Name']
    listGender[mobileNum]=thisdict['Gender']
    listAdhaar[mobileNum]=thisdict['Adhaar No']



def sendMessage(message): # Function to reply Accordingly to the messages send by the User
    count=0
    while True and count == 0:
        whatsappSendmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Sendmsg.png', confidence=0.7)
        if whatsappSendmsg:
            pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
            pyautogui.click()
            if message=='hello' or message=='hai':
                pyautogui.write('Hi,Welcome to Smart Service Assistant. Currently I can help you with following services :')
                time.sleep(1)
                pyautogui.write('\n ')
                time.sleep(1)
                pyautogui.write('1. Kerala Civil Supplies Services ')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('2. Aadhar Updation')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('3. National Voters Service ')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('4. Enter details by message ')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('5. Enter details by Adhaar ')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('Please select your required service. ')
                time.sleep(1)
                pyautogui.write('\n')
            elif message=='kerala civil supplies services' or message=='1':
                pyautogui.write('Welcome to Kerala Civil Supplies Services under Govt. of KERALA')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('1. Create a new account')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('2.Login to existing account')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('Please select your choice.')
                time.sleep(1)
                pyautogui.write('\n')
            elif message=='enter details by message' or message=='4':
                pyautogui.write('Enter your Aadhar Card number :')
                time.sleep(1)
                pyautogui.write('\n')
                adhaarNum=readingUserDetails()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('Enter your Ration Card number :')
                time.sleep(1)
                pyautogui.write('\n')
                rationCardNum = readingUserDetails()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('Enter your Mobile number :')
                time.sleep(1)
                pyautogui.write('\n')
                mobileNum=readingUserDetails()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                pyautogui.write('Enter Your name :')
                time.sleep(1)
                pyautogui.write('\n')
                name=readStringFromUser()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                pyautogui.write('Enter Your Gender (Male/Female/Transgender) :')
                time.sleep(1)
                pyautogui.write('\n')
                gender = readStringFromUser()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                pyautogui.write('Enter Your Mail-ID :')
                time.sleep(1)
                pyautogui.write('\n')
                email = readStringFromUser()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                pyautogui.write('Enter desired password for your account. The password should contain atleast 1 Uppercase,1 Lowercase,1 Number,1 Special Character character,')
                time.sleep(1)
                pyautogui.write('\n')
                password=readStringFromUser()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                if mobileNum not in listMobile:
                    pyautogui.write('Your details successfully saved to your database')
                    time.sleep(1)
                    pyautogui.write('\n')
                    assignData(adhaarNum,rationCardNum,mobileNum,name,email,password,gender)
                    waitForResponse()
                else:
                    pyautogui.write('Already existing user..!')
                    time.sleep(1)
                    pyautogui.write('\n')
                    waitForResponse()
            elif message=='enter details by adhaar' or message=='5':
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('Enter your Mobile number :')
                time.sleep(1)
                pyautogui.write('\n')
                mobileNum = readingUserDetails()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('Please send us the  photo of your adhaar card')
                time.sleep(1)
                pyautogui.write('\n')
                detectDetailsFromAdhaar(whatsappSendmsg,mobileNum)
            elif message=='create new account':
                pyautogui.write('Please let me know your Mobile Number...')
                time.sleep(1)
                pyautogui.write('\n')
                mobileNum = readingUserDetails()
                if mobileNum in listMobile:
                    userID=listOfNames[mobileNum][0:4]+'_'+listAdhaar[mobileNum][4:8]
                    listUserID[mobileNum]=userID
                    createNewAccount(listOfNames[mobileNum],userID,listEmail[mobileNum],listPassword[mobileNum],listAdhaar[mobileNum],listRationCard[mobileNum],mobileNum)

            elif message=='2' or message=='log in':
                pyautogui.write('Please let me know your Mobile Number...')
                time.sleep(1)
                pyautogui.write('\n')
                mobileNum = readingUserDetails()
                pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                pyautogui.click()
                if mobileNum in listMobile:
                    userID=listUserID[mobileNum]
                    password=listPassword[mobileNum]
                else:
                    pyautogui.write('Your data not found in Data Base. Enter your User ID :')
                    time.sleep(1)
                    pyautogui.write('\n')
                    userID = readStringFromUser()
                    pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                    pyautogui.click()
                    pyautogui.write('Enter your Password')
                    time.sleep(1)
                    pyautogui.write('\n')
                    password = readStringFromUser()
                    pyautogui.moveTo(whatsappSendmsg[0], whatsappSendmsg[1])
                    pyautogui.click()
                loginToPortal(userID,password,mobileNum)
                count=1

            else:
                pyautogui.write('Sorry unknown response.How can I help you')
                time.sleep(1)
                pyautogui.write('\n')

            count=1
            waitForResponse()


def readMessage(): #Function that reads the message send by the USER and passed to the sendmesssage( message ) function
    count = 0
    whatsappReadmsg=None
    while True and count == 0:
        whatsappReadmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Readmsg.png', confidence=0.5
                                                         )
        if whatsappReadmsg:
            pyautogui.moveTo(whatsappReadmsg[0], whatsappReadmsg[1])
            pyautogui.moveRel(-35,-100)
            pyautogui.tripleClick()
            pyautogui.hotkey('ctrl', 'c')
            message=clipboard.paste()
            sendMessage(message.lower())
            count = 1

def clickUser():  # Function to click on the authorized USER chat head.
    count=0
    whatsappNotification=None
    while True and count == 0:
        whatsappNotification=pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Newmsg.png',confidence=0.7)
        if whatsappNotification:
            pyautogui.moveTo(whatsappNotification[0],whatsappNotification[1])
            pyautogui.click()
            time.sleep(2)
            count=1
            readMessage()




def openWhatsapp(): # Function to open whatsapp beta application
    count=0
    while True and count==0:
        whatsappIcon=pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Icon.png', confidence=0.7)
        if whatsappIcon:
            pyautogui.moveTo(whatsappIcon[0],whatsappIcon[1])
            pyautogui.click()
            count=1
            clickUser()

openWhatsapp() # Beginning of the Project to open Whatsapp from UI

