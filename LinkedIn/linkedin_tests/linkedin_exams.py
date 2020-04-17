from selenium import webdriver
import time
import json
import logging
import sys

# TODO: if you doont have3 rtghe answer give user a chance to submit one

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
options = webdriver.ChromeOptions()


driver = webdriver.Chrome('/Volumes/REDTEAM/lottokingkarl/chromedriver') 
username_link   = "karl-machleidt"
my_username     = "machleidtk@gmail.com"
my_password     = "Biggiesmallslives88"
#exam_name       = "After Effects"
loslegen_button = "Loslegen" # have to change dpending on lang -> is button u press to confirm start exam
question_number = 15 #default 
path_to_write_q = "/Users/teamred/Desktop/WebDev/linkedin_tests/"
next_button     = 'Weiter' # this is the button to click next on questions
answer_file     = "some.json"
submit_button_de   = "Ergebnisse"
back_to_profile = "Profil"



def main():
    test = True
    # login and go to exam page

    for x in ['Agile Methoden', 'Android', 'AngularJS', 'Apache Hadoop', 'ArcGIS', 'Autodesk Inventor', 'Bash', 'C', 'C#', 'C++', 'Cascading Style Sheets (CSS)', 'Dreamweaver', 'HTML', 'Java', 'jQuery', 'JSON', 'Keynote', 'Maya', 'Microsoft Access', 'Microsoft Excel', 'Microsoft PowerPoint', 'Microsoft Project', 'MongoDB', 'MySQL', 'NoSQL', 'Objective-C', 'Objektorientierte Programmierung (OOP)', 'PHP', 'Pro Tools', 'QuickBooks', 'R', 'Revit', 'Ruby on Rails', 'Scala', 'SharePoint', 'Spring Framework', 'Transact\xadSQL (T-SQL)', 'Visual Basic for Applications (VBA)', 'Windows Server', 'WordPress', 'XML']:
        exam_name = x
        if test == True:
            login()
            test = False

            # has to run so we get all the tests visible
            get_all_test()

            # pick exam to take - leave blank for all
            pick_and_go(exam_name)

            # handles our exam taking 
            during_the_exam(exam_name)

            # after exam go back to profile
            # maybe we add more here we wanna do after 
            result, score = after_exam()
        else:
            time.sleep(5)
            driver.get("https://www.linkedin.com/in/"+username_link+"/")
            logging.info('we are on the page of ' + username_link)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.get("https://www.linkedin.com/in/"+username_link+"/detail/assessments/assessment-hub/quizzes/")
            logging.info('just clciked on the quizzes link')
            time.sleep(2)

            # has to run so we get all the tests visible
            get_all_test()

            # pick exam to take - leave blank for all
            pick_and_go(exam_name)

            # handles our exam taking 
            during_the_exam(exam_name)

            # after exam go back to profile
            # maybe we add more here we wanna do after 
            result, score = after_exam()






def login():
    try:
        driver.get("https://www.linkedin.com/login")
        logging.info('got to login page')
        time.sleep(3)
    except Exception as e:
        logging.critical("login page could not be loaded " + str(e)) 
        sys.exit()

    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    username.send_keys(my_username)
    password.send_keys(my_password)

    logging.info('entered credentials')
    time.sleep(1)
    driver.find_element_by_css_selector(" main > div > form > div > button").click()
    logging.info('clicked on login')
    time.sleep(5)
    driver.get("https://www.linkedin.com/in/"+username_link+"/")
    logging.info('we are on the page of ' + username_link)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get("https://www.linkedin.com/in/"+username_link+"/detail/assessments/assessment-hub/quizzes/")
    logging.info('just clciked on the quizzes link')
    time.sleep(2)

def get_all_test():
    click_more_test = "var buttons = document.querySelectorAll('button');\
        for (var i = 0; i < buttons.length; i++){if(buttons[i].innerText.includes('Weitere'))\
            {buttons[i].scrollIntoView();buttons[i].click();};};"

    get_more_in_view = "var buttons = document.querySelectorAll('button');\
        for (var i = 0; i < buttons.length; i++){if(buttons[i].innerText.includes('Weitere'))\
            {buttons[i].scrollIntoView();};};"

    for x in range(0,6):
        driver.execute_script(get_more_in_view)
        time.sleep(1)
        driver.execute_script(click_more_test)
        logging.info('getting all the tests and sleepin 2 sec')
        time.sleep(1)
        driver.execute_script(get_more_in_view)

    logging.info('all tests should be present now - returning True')
    return True

def pick_and_go(exam_name):
    if exam_name:
        logging.info('Attempting to take: '+exam_name)
    else:
        logging.warning('Trying to start all exams..DANGERZONE')

    options_list = driver.execute_script('''
        var availableTests = []
        var buttons = document.querySelectorAll('button > span.visually-hidden');
        for (var i = 0; i < buttons.length; i++){
            var btnTxt = buttons[i].innerText.trim();
            var btnArr = btnTxt.split(' ');
            btnArr.shift();
            btnArr.shift();
            var cleanArr = btnArr;
            btnTxt = cleanArr.join(',');
            btnTxt = btnTxt.replace(/,/g, ' ');
            availableTests.push(btnTxt);
        ;}
        return availableTests;
    ''')
    time.sleep(1)
    logging.info('Current Exam Options'+str(options_list))

    if exam_name:
        print(str(options_list))
        if exam_name in options_list:
            driver.execute_script('''
                var availableTests = []
                var buttons = document.querySelectorAll('button > span.visually-hidden');
                for (var i = 0; i < buttons.length; i++){
                    var btnTxt = buttons[i].innerText.trim();
                    var btnArr = btnTxt.split(' ');
                    btnArr.shift();
                    btnArr.shift();
                    var cleanArr = btnArr;
                    btnTxt = cleanArr.join(',');
                    btnTxt = btnTxt.replace(/,/g, ' ');
                    availableTests.push(btnTxt);''' + "if (btnTxt.toLowerCase() === '"+exam_name.lower()+"') {buttons[i].click();};};")

            time.sleep(1)
            logging.info('Selected Exam: '+exam_name)
            
            driver.execute_script(''' 
                (function (el) {
                    var buttons = document.querySelectorAll('button');
                    for (var i = 0; i < buttons.length; i++){
                        var btnTxt = buttons[i].innerText.trim();
                        if (btnTxt.toLowerCase() === el.toLowerCase()) {
                            buttons[i].click()
                        };};}'''+ "('"+loslegen_button+"'));")
            logging.info('Starting Exam: '+exam_name)
        else:
            print("The choice:{0} is not available.".format(exam_name))
            logging.error(exam_name+' is not a valid exam name.')
            print('Here is a list of choices')
            for x in options_list:
                print(str(x) + "\n")
    else:
        logging.warning('Trying all exams, this is an experimental feauture')
        print("Under construction, we have to implement this function")



def during_the_exam(exam_name):

    #"Avid Media Composer: Evaluierung Q7/15"
    # get quest number (standard is 15)
    try:
        time.sleep(3)
        num_quest = str(driver.find_element_by_css_selector('main > section > h3').get_attribute('innerText'))
        num_quest = num_quest.split('/')[-1]
        quest_count = int(num_quest)
    except:
        quest_count = question_number



    save_questions = {}
    have_to_be_answere = {}


    for question in range(quest_count):
        time.sleep(3)
        question_text = driver.find_element_by_css_selector('main > section > p').get_attribute('innerText')
        answer_list   = driver.execute_script('''
            var cleanAnswers = [];
            var allAnswers = document.querySelectorAll("label > p");
            for (var i = 0; i < allAnswers.length; i++){
                var newAnswer = allAnswers[i].innerText;
                cleanAnswers.push(newAnswer)
            }; return cleanAnswers;
        ''')
        exam_detail   = driver.find_element_by_css_selector('main > section > h3').get_attribute('innerText')


        correct_answers = []

        with open("/Users/teamred/Desktop/WebDev/linkedin_tests/"+answer_file) as f:
            questions_from_some_file = json.load(f)

        for match in questions_from_some_file:
            if question_text.lower() == questions_from_some_file[match]['question'].lower():
                correct_answers = questions_from_some_file[match]['answers']

        if len(correct_answers) < 1:
            have_to_be_answere[str(question)] = {
                "question":question_text,
                "answers": answer_list,
            }
            time.sleep(1)
            driver.execute_script('''
                var allAnswers = document.querySelectorAll("label > p");
                for (var i = 0; i < allAnswers.length; i++){
                    allAnswers[i].click()
                };''')
        else:
            driver.execute_script('''
            (function (myAnswers) {
                var allAnswers = document.querySelectorAll("label > p");
                for (var i = 0; i < allAnswers.length; i++){
                    for (var x = 0; x < myAnswers.length; x++){
                        var poss = allAnswers[i].innerText.toLowerCase().trim();
                        if(poss === myAnswers[x].toLowerCase().trim()){
                            allAnswers[i].click()
                        }
                    };
                };
            }''' + "('"+correct_answers+"'));")
            time.sleep(1)

   
        our_answer = driver.execute_script('''
                var ourPick = [];
                var answers = document.querySelectorAll('li');
                for (var i = 0; i < answers.length; i++){
                    if(answers[i].classList.contains('is-selected')){
                        ourPick.push(answers[i]);
                    };
                }; return ourPick;
            ''')

        if len(our_answer) < 1:
            save_questions[str(question)] = {
                    "question":question_text,
                    "answers": answer_list,
                    "exam": exam_detail,
                    "picked": our_answer,
                }
        else:
            save_questions[str(question)] = {
                "question":question_text,
                "answers": answer_list,
                "exam": exam_detail,
                "picked": "nothing",
            }
    
        time.sleep(1)
        driver.execute_script('''
            var buttons = document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++){'''+"if(buttons[i].innerText.includes('"+submit_button_de+"')){buttons[i].click();};};")
        
        # if next button diabled - choose answer first oir try answer again 
        next_button_disabled = driver.execute_script('''
            var isDisabled = "no";
            var buttons = document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++){
                if (buttons[i].disabled) {
                    isDisabled="yes";
                };
            }; return isDisabled;
        ''')

        if str(next_button_disabled) == "no":
            driver.execute_script('''
            var buttons = document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++){
                var btnTxt = buttons[i].innerText.trim();
                if (btnTxt.toLowerCase() ''' + "=== '"+next_button+"'.toLowerCase()) {buttons[i].click()};};")
        else:
            print("next is diabled, wait and picxk answer again, then try agaion ")
            driver.execute_script('''
                var buttons = document.querySelectorAll('button');
                for (var i = 0; i < buttons.length; i++){'''+"if(buttons[i].innerText.includes('"+submit_button_de+"')){buttons[i].click();};};")



    # at the end of the test write as json to file
    with open(path_to_write_q+exam_name+"_qa.json", 'w') as fps:
        fps.write(str(save_questions))

    with open(path_to_write_q+exam_name+"_have_todo.json", 'w') as fps:
        fps.write(str(have_to_be_answere))








def after_exam():
    time.sleep(8)
    # when you actrually pass an exam make this return score
    # we only know the selectors when not passed
    result = driver.execute_script("var result = document.querySelector('section > div > h3').innerText;return result;")
    score = driver.execute_script("var score = document.querySelector('section > div > p').innerText;return score;")

    logging.info('Test is done, going back to profile')
    time.sleep(1)
    driver.execute_script('''
        var buttons = document.querySelectorAll('button');
        for (var i = 0; i < buttons.length; i++){'''+"if(buttons[i].innerText.includes('"+back_to_profile+"')){buttons[i].click();};};")

    print(result)
    print(score)

    return result,score




main()