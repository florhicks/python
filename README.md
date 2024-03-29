# Python Development Projects

**Welcome, and nice to have you here!**
Explore my collection of Python projects, developed up to the current date and continuously updated with new content. These projects are based on the curriculum from the App Brewery's Python programming course.

## 1. Exercise Tracking (`exercise-tracking-nt`)

- Utilizes Sheety and Nutritionix APIs.
- Transforms natural language exercise entries into structured data.
- Compiles and organizes exercise data into a Google Sheet for easy tracking.

## 2. Flash Cards (`flash-cards`)

- GUI application for language learning.
- Cards flip between English and French.
- Utilizes a CSV file with words, managed using Pandas.

## 3. Flight Deals (`flight-deals`)

- Employs Sheety and Tequila APIs.
- Finds the cheapest flight deals based on stored cities in a Google Sheet for the next 6 months.

## 4. ISS Overhead (`issoverhead`)

- Determines ISS passover based on input latitude and longitude.
- Uses Sunrise-Sunset API and Open Notify API.
- Sends an email alert if ISS is passing and it's nighttime.

## 5. Kanye Quotes (`kanye-quotes`)

- Simple GUI app using the kanye.rest API.
- Generates random Kanye West quotes.

## 6. Movie Web Scraping (`movie_web_scraping`)

- Beautiful Soup used for web scraping.
- Extracts the top 100 movies from an Empire Online page.

## 7. News Web Scraping (`news-web-scraping`)

- Web scrapes `news.ycombinator.com`.
- Gathers titles, links, and upvotes for the top 30 news items.
- Identifies the news with the highest upvotes.

## 8. Password Manager (`password-manager`)

- GUI application for storing and retrieving passwords.
- Saves data in JSON format.

## 9. Quiz App (`quiz-app`)

- GUI quiz application using the OpenTDB API.
- Generates 10 random questions with scoring and correctness feedback.

## 10. Rain Alert (`rain-alert`)

- Predicts rain in the next 12 hours based on input latitude and longitude.
- Sends an SMS alert if rain is predicted, utilizing OpenWeatherMap API.

## 11. Stock News (`stock-news`)

- Combines AlphaAdvantage and NewsAPI.
- Alerts about significant stock changes for TESLA and provides related news via SMS.

## 12. Snake Game (`snake-game`)

- Classic Snake game using the Turtle graphics library.
- Utilizes object-oriented programming principles to structure the game logic.

## 13. Pong Game (`pong-game`)

- Pong game using the Turtle graphics library.
- Utilizes object-oriented programming principles to structure the game logic.

## 14. Spotify Time Machine (`spotify-time-machine`)

- Travel back in time through music!
- Scrapes the top 100 Billboard songs of a specified date.
- Creates a playlist on your Spotify account with the retrieved songs.

## 15. Amazon Price Tracker (`amazon-price-tracker`)

- Monitors the price of a specified Amazon product.
- Sends email notifications if the price drops below a predefined threshold.

## 16. Cookie Clicker Gaming Bot (`cookie-clicker-gaming-bot`)

- Automates various actions in the Cookie Clicker game.
- Auto-click on the big cookie.
- Auto-click on golden cookies.
- Auto-click on upgrades.
- Auto-click on buildings.

Enjoy your automated Cookie Clicker gaming experience on the official [Cookie Clicker website](https://orteil.dashnet.org/cookieclicker/)!

## 17. Personal Web Card (`REMOVED`)

## 18. Blog Templating (`blog-templating`)

- A blog project using Flask and HTML templates to dynamically render API-fetched posts.
- Offers a dynamic user experience with automatically updated content.

## 19. Clean Blog Project (`clean-blog`)

- Enhanced Flask blog with API-driven content.
- Features diverse sections and a functional contact form.
- Tasks include template setup, styling fixes, API integration, and more.

## 20. Coffee and Wifi Project (`coffee-and-wifi`)

- Developed using Flask, Flask-WTF, Flask-Bootstrap, and CSV file manipulation.
- The Coffee and Wifi Project is a web application designed for users to register and showcase cafes they have visited.
- The /cafes route displays a Bootstrap table containing data from cafe-data.csv.
- There is a secret route "/add" leading to the add.html page for adding new cafes.
- Utilizes WTForms to create a quick form on the add.html page with required fields.
- Upon successfully submitting the form on add.html, the data is appended to cafe-data.csv.

## 21. My Library Flask App (`my-library`)

- **Basic** Flask web app for tracking and managing read books.
- Utilizes Flask and SQLAlchemy to register books with title, author, and rating.
- Allows users to modify book ratings and delete entries for a personalized library.

## 22. My Movie List Flask App (`my-movie-list`)

- Flask web application for curating and organizing a personalized movie list.
- Employs Flask, WTForms, SQLite, and SQLAlchemy to facilitate the addition, editing, and deletion of movie entries.
- Integrates The Movie Database API to fetch movie details, including posters, release years, and descriptions.
- Displays a user-friendly interface with movie cards featuring front-end details and options for back-end actions.
- Features a ranking system that dynamically orders movies based on user ratings.

## 23. Cafe RESTful API (`cafe-api`)

- RESTful API built with Flask and SQLAlchemy for management of cafe information.

### Routes:

- `/random` (GET): Returns JSON details about a randomly selected cafe from the database.
- `/all` (GET): Provides JSON information for all stored cafes.
- `/search` (GET): Allows cafe search by location (parameter: `loc`), delivering details in JSON format.
- `/add` (POST): Facilitates the addition of new cafes through a POST request with JSON body.
  - Parameters: `name`, `map_url`, `img_url`, `location`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`.
- `/update-price/<cafe_id>` (PATCH): Updates the coffee price for a specific cafe identified by its ID.
  - Parameters: `new_price`.
- `/reports-closed/<cafe_id>` (DELETE): Deletes cafes from the database, authenticated by an API key provided as a parameter.
  - Parameters: `api-key`.

### Feel free to explore, contribute, or provide feedback. Thanks for visiting! 😊
