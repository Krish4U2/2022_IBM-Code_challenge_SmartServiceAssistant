import clipboard as clipboard
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract









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


def sendSuccess(userID,password):
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
                    waitForResponse()




def waitForResponse():
    count = 0
    while True and count == 0:
        whatsappDefault = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Default.png', confidence=0.7)
        if whatsappDefault:
            pyautogui.moveTo(whatsappDefault[0], whatsappDefault[1])
            pyautogui.click()
            count=1
            clickUser()

def waitForNewMsg():
    count = 0
    whatsappNotification = None
    while True and count == 0:
        whatsappNotification = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Newmsg.png', confidence=0.7)
        if whatsappNotification:
            pyautogui.moveTo(whatsappNotification[0], whatsappNotification[1])
            pyautogui.click()
            time.sleep(2)
            count = 1




def readStringFromUser():
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


def readingUserDetails():
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


def sendMessage(message):
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
                pyautogui.write('2........... ')
                time.sleep(1)
                pyautogui.write('\n')
                time.sleep(1)
                pyautogui.write('3. ........ ')
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
            elif message=='create new account' or message=='1':
                pyautogui.write('Enter your Adhaar Card number :')
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
                userID=name[0:4]+'_'+adhaarNum[0:4]
                pyautogui.write('Your USER ID is :'+userID)
                time.sleep(1)
                pyautogui.write('\n')
                createNewAccount(name,userID,email,password,adhaarNum,rationCardNum,mobileNum)

                print(name)
                print(userID)
                print(email)
                print(password)
                print(adhaarNum)
                print(rationCardNum)
                print(mobileNum)
            else:
                pyautogui.write('Sorry unknown response.How can I help you')
                time.sleep(1)
                pyautogui.write('\n')

            count=1
            waitForResponse()


def readMessage():
    count = 0
    whatsappReadmsg=None
    while True and count == 0:
        whatsappReadmsg = pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Readmsg.png', confidence=0.5
                                                         )
        if whatsappReadmsg:
            pyautogui.moveTo(whatsappReadmsg[0], whatsappReadmsg[1])
            pyautogui.moveRel(0,-100)
            pyautogui.tripleClick()
            pyautogui.hotkey('ctrl', 'c')
            message=clipboard.paste()
            sendMessage(message.lower())
            count = 1

def clickUser():
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




def openWhatsapp():
    count=0
    while True and count==0:
        whatsappIcon=pyautogui.locateCenterOnScreen(r'Photos/Whatsapp_Icon.png', confidence=0.7)
        if whatsappIcon:
            pyautogui.moveTo(whatsappIcon[0],whatsappIcon[1])
            pyautogui.click()
            count=1
            clickUser()

#openWhatsapp()
createNewAccount()

