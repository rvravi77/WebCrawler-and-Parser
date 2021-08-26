# WebCrawler and Parser for RottenTomatos.com
### Description
RottenTomatoes is an IMDb like website, where you can find an online database of information related to films, television programs, including cast, production crew, personal biographies, plot summaries, trivia, ratings, critic and fan reviews.
The code reads data from file “rotten tomatoes movie genre link.txt,” which contains URL links for ten different genre-wise top 100 movie lists. 

#### Task 1:
1. Reads each of the URLs, saves the pages in HTML format.
2. Given a user input of any of the ten genres, it should list all the movies in that genre and wait for user input of a particular movie name from the list.
3. Given a movie name as the input, it should download and save the corresponding movie page’s HTML file and save in  "./MOVIE" directory.

#### Task 2 :
After saving movie pages in HTML format, create grammar using the syntax of the HTML file to extract following fields:

1. Movie Name
2. Director
3. Producer
4. Writers
5. Original Language
6. Cast and Crew Members
7. Storyline
8. Box Office Collection
9. Runtime
10. You Might Also Like
11. Where to Watch
For any selected movie, the user can ask for any of the above field to show and our program will display the information after extractng using grammar . For example if user asks for "Movie Name" then user will get movie title,if user asks for "Director" then it will show director name(s) to user and so on.

After completion of above task we need to do two more extra tasks to add some special features with two fields "You Might Also Like" and "Cast and Crew Members" :

##### Sub-Task-2.1: 
When user selects **"You Might Also Like"** option then it will show movie names given in this field,and then it will wait for user input to selects any of the shown movie name,and when user selects any it will download HTML page for that movie and show the above list for selected movie.

##### Sub-Task-2.2:
If user selects **"Cast and Crew Members"** then it will show list of memebers with their role(or responsibility),then wait for user input of any one of the listed cast member, given the input we need to download and save that actor/actress profile and write grammar to extract the below fields:

Highest Rated film
Lowest Rated film
Birthday
His/Her other movies
Then wait for the user to select from any of the above options and show the result as per selection and for the ‘His/Her other movies’ further ask for a year and use it as a filter to show all the movies on or after that year.

