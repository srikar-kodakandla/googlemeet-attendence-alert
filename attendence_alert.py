import undetected_chromedriver.v2 as uc
import os
os.system('rm -r /home/ubuntu/meetautomation/profile')
os.system('cp -r /home/ubuntu/meetautomation/backup/profile /home/ubuntu/meetautomation')
from num2words import num2words
from time import sleep
import re
from statistics import *

from time import sleep

import schedule

import telebot

from math import *

directory = os.getcwd()


def alert(msg):
    print(msg)

    bot = telebot.TeleBot("20534332530252:AAG4ytvt7ZS8-OsdfdsGgpSsvmdoz-Es-TSOsdfOYyE", parse_mode=None)   ###add your telegram api id and hash id 

    bot.send_message(chat_id='-77193522975', text=msg)   # add chatid of the channel (you will get message in that channel)
    try:
        os.system('play -q -n synth 0.5 sin 880 || echo -e "\a"') ## beep sound during alert
    except:
        pass

# setting profile

import background
background.n=10
var=0
lin=0
running=True
chatbox=True
attendence_alert=True
limit=True
relogin=False
driver=0
import undetected_chromedriver.v2 as uc
options = uc.ChromeOptions()
# options = uc.ChromeOptions()
options.user_data_dir = directory
# another way to set profile is the below (which takes precedence if both variants are used
options.add_argument(f'--user-data-dir={directory}/meetautomation/profile')
# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)
#@background.task
def meet(link):
    global driver
    global directory
    global lin
    global running
    global attendence_alert
    global limit
    global driver
    global var
    global chatbox
    chatbox=True
    running=True
    attendence_alert=True
    try:
        login()
    except Exception as error:
        print(error)
    try:
        sleep(2)
        print(link)
        global driver
        yyy = driver.get(link)
        while yyy.count('error')>0:
            print(link)
            yyy=driver.get(link)
            sleep(2)
            print(yyy)
        sleep(5)
        driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
        driver.find_element_by_xpath(

            '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
        try:
            present_people = driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]').text

            present_people = present_people.split(' ')
        except:
            pass
        bbb = list(range(11, 99))

        enter = False
        try:
            while not enter:
                sleep(2)
                present_people = driver.find_element_by_xpath(

                    '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]').text

                present_people = present_people.split(' ')

                for nnn in bbb:

                    for mmm in present_people:

                        if str(mmm) == str(nnn):
                            enter = True

                            break

                print(
                    f'Not enough people entered the meet , waiting ... i need atleast {bbb[0]} people waiting in meet to enter meet')

                sleep(5)
                if not running :
                    break
                if not limit:
                    #global limit
                    break
        except Exception as error:
            print(error)
            # break

        try:


            driver.find_element_by_xpath(

                '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

        except Exception as error:
            print(error)
            driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
        sleep(5)
        bbbbb = False

        while not bbbbb:
            try:
                if not running :
                    break
                driver.find_element_by_xpath(

                    '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[3]/div/span/button/span[2]').click()
                bbbbb = True
                break
            except Exception as error:
                print(error)
                sleep(5)
                bbbbb = False
        # driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div[1]/div[2]/div/span[1]/span').text

        sleep(1)

        driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button/i[1]').click()

        alert_list = ['attendence', 'srikar', 'present', 'present sir', 'present mam', 'attendance', 'presence',
                      'absent', 'absence', 'presence', 'presents']  # when ever this words are there in captions then it throws alert 
        doncare=['presence','absent', 'absence', 'presence', 'presents','present']

        # alert_list=['contineous','descrete','signals']

        roll_no_las = list(range(80, 110))

        roll_n = list(range(1, 120))

        roll_no_last = []

        roll_no = []

        for i in roll_no_las:
            roll_no_last.append(i)

            roll_no_last.append(num2words(i))

        for i in roll_n:
            roll_no.append(i)

            roll_no.append(num2words(i))

        called_no = set()

        members = set()

        check1 = ['present', 'present sir', 'present mam']

        check = []

        for yy in check1:
            check.append(yy)

            check.append(yy.upper())
        alert(f'meet login done :{link}')

    except Exception as error:

        print(error)

    while True:
        sleep(0.5)
        if not running:
            try:
                driver.find_elements_by_xpath(
                    '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button')[0].click()
                alert(f'meet left:{link}')
                #driver.close()
                global relogin
                if relogin:   
                    global lin
                    meet(lin)
                else:
                    break
                break    
            except:
                driver.get('https://www.google.com')
                break
        try:
            try:


                messages = driver.find_element_by_css_selector(
                    '#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.R3Gmyc.qwU8Me > div.WUFI9b > div.hWX4r > div > div.z38b6').text.split(
                    '\n')

                # // *[ @ id = "ow3"] / div[1] / div / div[9] / div[3] / div[4] / div[2] / div[2] / div / div[3]

                # messages = \

                # driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[3]/div[2]/div/div[3]')[

                #    0].text.split('\n')

                check_no = 0

                mam = 0

                sir = 0

                for i in messages:

                    for j in check:

                        if i.count(j) > 0:

                            check_no += 1

                            if j.count('sir') > 0:
                                sir += 1

                            if j.count('mam') > 0:
                                mam += 1

                            # print(check_no)

                if check_no > 15:

                    try:

                        mmm = (given_attendence)

                    except:

                        given_attendence = False

                    if not given_attendence and chatbox:

                        if mam > sir:

                            given_attendence_name = '11189A104 present mam'    #message during attendence for mam

                        else:

                            given_attendence_name = '11189A104 present sir'    #message during attendence for sir

                        driver.find_element_by_css_selector(
                            '#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.R3Gmyc.qwU8Me > div.WUFI9b > div.hWX4r > div > div.BC4V9b > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea').send_keys(
                            given_attendence_name)

                        driver.find_elements_by_css_selector(
                            '#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.R3Gmyc.qwU8Me > div.WUFI9b > div.hWX4r > div > div.BC4V9b > span > button > i')[
                            0].click()

                        given_attendence = True

                        alert('given attendence in chatbox : ' + link)

            except Exception as error:
                print(error)
                #print('unable to fetch messages list bro ')

            try:

                ele = driver.find_element_by_xpath(

                    '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[7]/div/div[2]/div').text.lower()

                ele = re.sub(r'[^\w\s]', '', ele)

                print(ele)

            except:

                continue

            # print(ele)

            for j in alert_list:
                if j in doncare:
                    if len(ele.split(' '))<10:
                        # if ele.count(j) > 0:
                        if j in ele.split(' '):
                            print(j)
                            print('alert.......', j)
                            if attendence_alert:

                                alert(str(ele) + ' : ' + link)
                            sleep(15)
                if j not in doncare:
                    # if ele.count(j) > 0:
                    if j in ele.split(' '):
                        print(j)
                        print('alert.......', j)
                        if attendence_alert:

                            alert(str(ele) + ' : ' + link)
                        sleep(15)
                            

            # for k in roll_no:

            #    if ele.count(str(k)) > 0:

            #        called_no.add(k)

            #        print(ele)

            # if len(called_no) > 20:

            #    alert('roll no calling i think ')

            #    for nn in roll_no_last:

            #        if ele.count(str(nn)) > 0:

            #            alert('alert...', nn)

            aa = int(driver.find_elements_by_class_name('uGOf1d')[0].text)

            # driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/div/div')[0].text

            members.add(int(driver.find_elements_by_class_name('uGOf1d')[0].text))

            if max(members) / 2 > aa:
                driver.find_elements_by_xpath(

                    '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button')[0].click()
                alert(f'meet left:{link}')
                #driver.close()
                break

        except Exception as error:
            print(error)
            # login()
            # meet(link)


def login():
    global driver
    try:
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                   'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                   '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('11189A104@kanchiuniv.ac.in')  ## your school account userid 
        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()
        # driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
        loginBox = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        loginBox.send_keys('password') ### your school account password

        # passWordBox = driver.find_element_by_xpath(
        #   '//*[@id ="password"]/div[1]/div / div[1]/input')
        # passWordBox.send_keys(passWord)

        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()

        print('Login Successful...!!')
        sleep(10)
    except:
        print('Login Failed')

import background
#driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[1]')[0].text
@background.task
def telegram():
    import telebot
    global limit
    global attendence_alert
    global chatbox
    bot = telebot.TeleBot("205325223052:AAG4ytvt7dfZS8-OGgpSsvmdoz-Es-TSOOYyE", parse_mode=None)
    @bot.message_handler(commands=['start', 'help','count','link','leave','screenshot','limit_true','limit_false','stop','chatbox_on','chatbox_off'])
    def send(message):
      global limit
      global attendence_alert
      global chatbox
      if message.text=='/count':
          try:
              aa=int(driver.find_elements_by_class_name('uGOf1d')[0].text)
              bot.reply_to(message,f'{aa} no of people are there in the meeting')
          except:
              bot.reply_to(message,'I am not present in any meeting')

      elif message.text=='/start':
          #try:
              #aa = int(driver.find_elements_by_class_name('uGOf1d')[0].text)
              #bot.reply_to(message,f'I am in the currently in this meeting {driver.current_url}')
          attendence_alert=True
          bot.reply_to(message,'OK i will alert you during attendence')
          #except:
          #    bot.reply_to(message,'I am not in any meeting')
      elif message.text=='/help':
          
          jh='''This is a meet automation bot , you will probalby notified for the attendence , this account runs with srikar account (11189A104@kanchiuniv.ac.in) so please do not misuse it 
          because if you misuse it then i will be at risk . if the meet link is wrong then you can modify by some commands but do not change meet link for fun , because it will affect my attendence. 
          help,start,link,leave,screenshot,count are the commands you can use for the bot with the backslash before the command. help means , it will guide about bot , start means , it tells if the bot is in any meeting 
          , link means it says the meeting link currently the bot is logged in , leave means bot will leave the current meeting, do not leave the meeting unless bot is logged in to wrong link because it affects the attendence of mine , screenshot means it takes the screenshot of the current meeting 
          if the meeting link is wrong or if you want to be notified with any meeting attendence then you can type the following command "bot change meet link https....... " type the meet link in that given dots . 
          Do not change the meet link because if the account is already in meeting then it logout from the meeting and enters in to new meeting you enter so it may effect the attendence of that account.limit_true : if you want to wait untill 15 members enter the meet , limit_false if you do not want to wait and want to enter meet immedietly even if no one there in the meet 
          .stop to stop attendence alerts for this meet , chatbox_on for to keep message in chatbox and chatbox_off for to not to keep attendence in chatbox.
          ,start for resume attendence alerts,PLEASE DO NOT TELL OTHERS ABOUT THIS . PLEASE KEEP THIS A SECRET '''
          bot.reply_to(message,f'i am here to help u \n {jh}')
      elif message.text=='/link':
          try:
              aa = int(driver.find_elements_by_class_name('uGOf1d')[0].text)
              bot.reply_to(message,f'I am currently in this meeting : {driver.current_url}')
          except:
              bot.reply_to(message,'I am not there in any meet')

      elif message.text=='/leave':
          global running
          global relogin
          relogin=False
          running=False
          bot.reply_to(message,'OK leaving meet if i joined any meet')
      elif message.text=='/screenshot':
          try:
              import pyautogui
              im1 = pyautogui.screenshot()
              im1.save('u.png')
              bot.send_photo(message.chat.id,photo=open(os.getcwd()+'/u.png','rb'))
          except Exception as error:
              bot.reply_to(message,f'Unable to send screenshot {error}')
      elif message.text=='/limit_true':
          #global limit
          limit=True
          bot.reply_to(message,'limit is true, it only enters if more than 15 members in the meet')
      elif message.text=='/limit_false':
          #global limit
          limit=False
          bot.reply_to(message,'limit is false, it will enter meet even if no one is there in the meet ')
      elif message.text=='/stop':
          attendence_alert=False
          bot.reply_to(message,'OK ,stopped attendence alerts for this class') 
      elif message.text=='/chatbox_off':
          chatbox=False
          bot.reply_to(message,'OK i will not post attendence in chatbox for today class')
      elif message.text=='/chatbox_on':
          chatbox=True
          bot.reply_to(message,'OK i will post attendence in chatbox for today class')           
      else:
          bot.reply_to(message,'not a valid command')
    @bot.message_handler()
    def echo_all(message):
        print(message)
        if 'bot change meet link' in message.text:
            global lin
            lin=list(message.text.split(" "))[4]
            bot.reply_to(message,"ok  "+message.from_user.first_name+" changes meeet link to {}".format(lin))
            global running
            global relogin
            relogin=True
            #global driver
            running=False
            #global lin=var
            print(lin)
            sleep(5)
            #meet(var)
    bot.polling()

telegram()
# driver.find_elements_by_class_name('uGOf1d')[0].text
# meet('https://meet.google.com/vhx-iyks-shv')
# driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/div/div')
#meet('https://meet.google.com/bfu-vkom-fem')
#schedule.every().day.at('09:30').do(login)



################ day ####### time ############ meet link #############################
schedule.every().tuesday.at('13:59').do(meet, 'https://meet.google.com/tuk-vpwt-sbv')  #class sheduling 
schedule.every().monday.at('13:59').do(meet, 'https://meet.google.com/vhx-iyks-shv ')
schedule.every().wednesday.at('09:59').do(meet, 'https://meet.google.com/vhx-iyks-shv')
schedule.every().monday.at('09:59').do(meet, 'https://meet.google.com/tuk-vpwt-sbv')
schedule.every().tuesday.at('09:59').do(meet, 'https://meet.google.com/yzs-dgoa-wdp')
schedule.every().wednesday.at('13:59').do(meet, 'https://meet.google.com/yzs-dgoa-wdp')

# meet('https://meet.google.com/haf-ftqw-eqc')

while True:
    given_attendence = False
    if running==False and relogin==True:
        meet(lin)
    print('waiting for meet link ......')    
    schedule.run_pending()

    sleep(6)

# driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[1]')[0].text





