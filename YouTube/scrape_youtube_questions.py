

from selenium import webdriver
import time
import json

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('/Volumes/REDTEAM/lottokingkarl/chromedriver') 


question_urls = ["https://www.gcertificationcourse.com/how-would-you-update-channel-branding-to-support/", 
"https://www.gcertificationcourse.com/how-do-playlists-affect-watch-time-on-a-channel/", 
"https://www.gcertificationcourse.com/whats-something-that-video-cards-can-promote/", 
"https://www.gcertificationcourse.com/what-does-not-describe-a-thumbnail-that-has-been/", 
"https://www.gcertificationcourse.com/what-does-a-channels-search-data-reveal/", 
"https://www.gcertificationcourse.com/how-can-subscribers-boost-engagement-and-thus-discovery/", 
"https://www.gcertificationcourse.com/what-type-of-video-is-designed-to-get-fans-excited/", 
"https://www.gcertificationcourse.com/why-is-behind-the-scenes-footage-from-a-tour-valuable/", 
"https://www.gcertificationcourse.com/what-is-the-most-effective-way-to-promote-a-collaboration/", 
"https://www.gcertificationcourse.com/which-of-the-following-accurately-describes-art-tracks/", 
"https://www.gcertificationcourse.com/how-does-upgrading-to-an-official-artist-channel-affect/", 
"https://www.gcertificationcourse.com/how-does-an-artist-benefit-from-upgrading-to-an-official-artist/", 
"https://www.gcertificationcourse.com/what-is-the-best-way-to-leverage-fan-videos-to-grow/", 
"https://www.gcertificationcourse.com/what-is-the-best-way-to-engage-fans-before-an-album-release/", 
"https://www.gcertificationcourse.com/why-is-it-important-to-keep-uploading-videos/", 
"https://www.gcertificationcourse.com/what-is-the-most-effective-way-to-encourage-subscribers/", 
"https://www.gcertificationcourse.com/why-might-you-want-to-pin-a-fan-comment-on-a-video/", 
"https://www.gcertificationcourse.com/how-can-you-use-community-to-give-fans-an-inside-look/", 
"https://www.gcertificationcourse.com/with-which-youtube-feature-can-you-establish-a-watch/", 
"https://www.gcertificationcourse.com/what-is-one-effective-way-to-use-the-community-tab/", 
"https://www.gcertificationcourse.com/what-can-tell-you-about-the-global-reach-of-a-channel/", 
"https://www.gcertificationcourse.com/what-can-you-do-to-prevent-a-sudden-drop-in-a-videos/", 
"https://www.gcertificationcourse.com/what-should-you-do-when-a-channels-demographics-data/", 
"https://www.gcertificationcourse.com/youtube-analytics-for-artists-provides-data-about-what-type/", 
"https://www.gcertificationcourse.com/what-can-you-learn-from-the-data-in-music-charts-insights/", 
"https://www.gcertificationcourse.com/whats-one-practical-application-for-youtube-analytics/", 
"https://www.gcertificationcourse.com/if-you-wanted-to-learn-in-which-major-city-a-competing-artists/", 
"https://www.gcertificationcourse.com/what-requirement-must-a-video-meet-before-its-eligible/", 
"https://www.gcertificationcourse.com/which-two-parties-most-commonly-enter-into-an-srav/", 
"https://www.gcertificationcourse.com/who-can-monetize-videos-on-youtube/", 
"https://www.gcertificationcourse.com/what-is-the-goal-of-the-ad-serving-model-2/", 
"https://www.gcertificationcourse.com/what-deters-advertisers-from-showing-ads-on-a-video/", 
"https://www.gcertificationcourse.com/why-might-you-want-to-review-the-ratio-of-views-to-ads/", 
"https://www.gcertificationcourse.com/how-can-you-estimate-which-ad-formats-are-earning/", 
"https://www.gcertificationcourse.com/what-low-investment-strategy-could-a-channel-try/", 
"https://www.gcertificationcourse.com/why-might-two-videos-with-similar-monetizable-view/", 
"https://www.gcertificationcourse.com/what-can-generate-additional-revenue-for-an-artist/", 
"https://www.gcertificationcourse.com/can-an-artist-promote-a-paid-product-or-service/", 
"https://www.gcertificationcourse.com/what-can-you-do-to-maximize-an-artists-revenue-potential/", 
"https://www.gcertificationcourse.com/why-should-an-artist-seek-legal-advice-before-uploading/", 
"https://www.gcertificationcourse.com/which-types-of-copyright-apply-most-often-to-music/", 
"https://www.gcertificationcourse.com/what-happens-to-a-channel-when-it-receives-a-copyright/", 
"https://www.gcertificationcourse.com/what-is-subject-to-a-match-in-content-id/", 
"https://www.gcertificationcourse.com/what-is-the-difference-between-copyright-and-content-id/", 
"https://www.gcertificationcourse.com/how-does-content-id-support-the-work-of-music-rights-holders/", 
"https://www.gcertificationcourse.com/why-is-it-important-to-resolve-asset-ownership-conflicts/", 
"https://www.gcertificationcourse.com/which-asset-type-is-always-linked-to-a-sound-recording/", 
"https://www.gcertificationcourse.com/what-may-indicate-that-a-channel-needs-to-clean-up/", 
"https://www.gcertificationcourse.com/what-predefined-match-policy-allows-viewers-to-watch/", 
"https://www.gcertificationcourse.com/where-can-you-see-the-relationship-between-references/"]

qa_dict = {}
counter = 1
for question_link in question_urls:
    driver.get(question_link)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    question_text = driver.find_element_by_css_selector("article > header > h1").get_attribute('innerText')
    answer_ul = driver.find_element_by_css_selector("article > div.entry-content > ul").get_attribute('innerHTML')

    qa_dict[str(question_text)] = str(answer_ul)

    print(qa_dict)
    print("---question"+str(counter)+"-------")
    counter += 1



with open("/Users/teamred/Desktop/WebDev/youtube_answers_qa.json", 'w') as fps:
    json.dump(qa_dict, fps)
