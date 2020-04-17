# You can pass the Google Nalaytics Exam with this 

Source of Questions and Answers
- https://www.certificationanswers.com/en/home/

Link to the Exam
- https://analytics.google.com/analytics/academy/

 ```javascript
 var links = document.querySelectorAll("article > header > h1");
 var links_array = [];
 [].forEach.call(
   links, 
   function(elem){
     links_array.push(elem.getAttribute("href"));
  }
); copy(links_array);
// with copy it copies array to cliboard without truncation
 ```
