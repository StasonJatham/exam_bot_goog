
from selenium import webdriver
import time
import json


options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/Volumes/REDTEAM/lottokingkarl/chromedriver') 



#done #display_video_first = "https://school4seo.com/display-video-certification-exam/what-is-the-difference-between-programmatic-guaranteed-deals-and-preferred-deals/"
#done #campaign_manager_first = "https://school4seo.com/campaign-manager-certification-exam/counters-and-total-interactions-metrics-are-available-for-which-type-of-creatives/"
#done #search_ads_first = "https://school4seo.com/search-ads-360/what-configuration-setting-eliminates-duplicate-conversions-between-advertisers/"
#done #creative_first = "https://school4seo.com/creative-certification-exam/which-two-options-must-be-true-to-use-open-optimization-select-two/"
ads_search      = "https://school4seo.com/google-ads-search-advertising-exam/leo-is-in-charge-of-advertising-for-the-clothing-lines-of-a-large-manufacturer-he-uses-his-google-ads-recommendations-page-to-help-him-evaluate-his-search-ads-campaigns-which-feature-makes-the-optim/"
#done #ads_measurement = "https://school4seo.com/measurement-certification/you-operate-an-online-retail-website-and-have-google-tag-manager-set-up-to-manage-your-tags-on-your-site-you-now-want-to-set-up-sitewide-conversion-tracking-tags-in-order-to-evaluate-the-effectivenes/"
#done #ads_shopping    = "https://school4seo.com/google-shopping-advertising-exam/local-inventory-ads-are-ideal-for-which-business/"
#done #ads_video       = "https://school4seo.com/google-video-advertising-exam/whats-a-key-benefit-of-bumper-ads/"
#done #ads_display     = "https://school4seo.com/google-display-exam/josephine-is-in-the-process-of-creating-ads-within-her-standard-display-campaign-she-finds-that-there-are-two-main-ad-formats-that-she-can-leverage-what-are-the-two-main-ad-formats-used-in-a-standar/"

# mach im anschluss nochmal von vorne 
#ads_display = "https://school4seo.com/google-display-exam/jakes-been-trying-to-build-brand-awareness-for-his-new-clothing-line-initial-branding-attempts-were-successful-but-he-now-wants-to-scale-things-to-a-larger-degree-jake-can-reach-a-wide-audience-b/"

link = ads_search
# when this is not on page, stop
word = "Google Ads Search"
# click next or previous
direction = 'back'
# ul1 or ul2
site_one = False

# quesstion 7-9 are from ads



scraped_urls = []
counter = 1

driver.get(link)
qa_dict = {}
question = ""
answer = ""
while word in str(driver.find_element_by_css_selector("div > footer > span.cat-links > a").text):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    question =  driver.find_element_by_css_selector("div > header > h1").text
    #answer = driver.find_element_by_css_selector("div > div > ul:nth-child(7)").get_attribute('innerHTML')

    try:
        if "Correct Sequences" in driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML'):
            answer = driver.find_element_by_css_selector("article > div > div > ol").get_attribute('innerHTML')
        else:
            try:
                if site_one:
                    answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(1)").get_attribute('innerHTML')
                    if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')

                else:
                    answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(2)").get_attribute('innerHTML')
                    if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
            except:
                try:
                    answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(3)").get_attribute('innerHTML')
                    if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
                except:
                    try:
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
                    except:
                        try:
                            answer = driver.find_element_by_css_selector("article > div > div > ol").get_attribute('innerHTML')
                        except:
                            answer = "fuck you"
    
    except:

        try:
            if site_one:
                answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(1)").get_attribute('innerHTML')
                if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
            else:
                answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(2)").get_attribute('innerHTML')
                if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
        except:
            try:
                answer = driver.find_element_by_css_selector("article > div > div > ul:nth-child(3)").get_attribute('innerHTML')
                if "Google Ads Certification Exam" in str(answer):
                        answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
            except:
                try:
                    answer = driver.find_element_by_css_selector("article > div > div > p.has-text-color.has-background").get_attribute('innerHTML')
                except:
                    try:
                        answer = driver.find_element_by_css_selector("article > div > div > ol").get_attribute('innerHTML')
                    except:
                        answer = "fuck you"
    
    qa_dict[str(question)] = str(answer)

    print("---question"+str(counter)+"-------")
    print(question)
    if driver.current_url in scraped_urls:
        print("------DUPLICATE", driver.current_url)
    scraped_urls.append(driver.current_url)
    print(answer)
    counter += 1

    # next question 
    #if driver.current_url == "https://school4seo.com/google-video-advertising-exam/whats-the-best-description-of-affinity-audiences-on-youtube/":
    #    driver.get("https://school4seo.com/google-video-advertising-exam/which-value-proposition-do-custom-intent-audiences-offer-advertisers/")
    if direction == 'forward':
        driver.find_element_by_css_selector("#nav-below > div.nav-next > span > a").click()
    else:
        driver.find_element_by_css_selector("#nav-below > div.nav-previous > span > a").click()

    
    time.sleep(2)


link = link
with open("/Users/teamred/Desktop/WebDev/"+str(link.split('/')[3])+ "_qa.json", 'w') as fps:
    json.dump(qa_dict, fps)

"""
// get all links to question on page
document.querySelectorAll('main a')

// next question
document.querySelector("#nav-below > div.nav-previous > span > a").click()

// correct answers
document.querySelector("div > div > ul:nth-child(7)")


document.querySelector("div > header > h1").innerText
// question text
// document.querySelector("#nav-below > div.nav-previous > span > a").innerText

"""

        


















def get_shit():
    # document.querySelector("div > div > ol") works
    ads_search      = "https://school4seo.com/google-ads-search-advertising-exam/google-ads-search-certification-list-of-latest-and-updated-questions/?utm_source=HomePage&utm_medium=HomeBanner&utm_campaign=HomeBannerSearchAds"
    ads_display     = "https://school4seo.com/google-display-exam/google-ads-display-certification-list-of-latest-and-updated-questions/?utm_source=HomePage&utm_medium=HomeBanner&utm_campaign=HomeBannerDisplayAds"
    ads_video       = "https://school4seo.com/google-video-advertising-exam/google-ads-video-certification-list-of-latest-and-updated-questions/?utm_source=HomePage&utm_medium=HomeBanner&utm_campaign=HomeBannerVideoAds"
    ads_measurement = "https://school4seo.com/list-of-questions-and-answers/google-ads-measurement-certification-list-of-latest-and-updated-questions/?utm_source=HomePage&utm_medium=HomeBanner&utm_campaign=HomeBannerMeasurement"
    ads_shopping    = "https://school4seo.com/google-shopping-advertising-exam/google-ads-shopping-certification-list-of-latest-and-updated-questions/?utm_source=HomePage&utm_medium=HomeBanner&utm_campaign=HomeBannerMeasurement"

    easy_questions = [ads_search,ads_display,ads_video,ads_measurement,ads_shopping]


    for link in easy_questions:
        driver.get(link)
        time.sleep(8)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_css_selector("div > div > ol")


        question_dict = {}

        question = ""
        counter = 0
        question_link = ""
        while question != "null":
            counter = counter + 1
            try:
                question = str(driver.find_element_by_css_selector("div > div > ol > li:nth-child("+str(counter)+") > a").text)
                question_link = str(driver.find_element_by_css_selector("div > div > ol > li:nth-child("+str(counter)+") > a").get_attribute("href"))

                question_dict[str(question_link)] = str(question)
            except:
                break


        with open("/Users/teamred/Desktop/WebDev/"+str(link.split('/')[3])+ ".json", 'w') as fp:
            json.dump(question_dict, fp)

        

        qa_dict = {}
        question2 = ""
        for key in question_dict:
            driver.get(key)
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except:
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                question2 = driver.find_element_by_css_selector("div > div > h2").text
            except:
                try:
                    question2 = driver.find_element_by_css_selector("div > header > h1").text
                except:
                    pass

            try:
                answer_text = driver.find_element_by_css_selector("div > div > ul:nth-child(2)").get_attribute('innerHTML')
            except:
                try:
                    answer_text = driver.find_element_by_css_selector("div > div > ul:nth-child(1)").get_attribute('innerHTML')
                except:
                    pass

                
            print("-------------------------")
            print(answer_text)
            
            qa_dict[str(question2)] = str(answer_text)

        with open("/Users/teamred/Desktop/WebDev/"+str(link.split('/')[3])+ "_qa.json", 'w') as fps:
            json.dump(qa_dict, fps)







"""
// get all links to question on page
document.querySelectorAll('main a')

// next question
document.querySelector("#nav-below > div.nav-previous > span > a").click()

// correct answers
document.querySelector("div > div > ul:nth-child(7)")


document.querySelector("div > header > h1").innerText
// question text
// document.querySelector("#nav-below > div.nav-previous > span > a").innerText

"""
