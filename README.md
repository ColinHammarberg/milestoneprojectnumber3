 inslaskll # LOVE THERAPY
 
### The Love Therapy application was created for the clients of the Love Therapy center, which is being run by DR. Edward. The application helps the clients to get a better structure on their bookings, meetings, keeping contact with Dr. Edward and being able to search up different content stored in the database.


# UX
 
* As an everyday client I want to experience a User Friendly application that is easy to understand and take usage of.
* The visitor is the individual who is a client of LOVE THERAPY. The application helps the client to get a better structure. 
* They will experience an ordinary, but different kind of application page. Not too much focus on the design, but more focus on the actual data and functions.

<br>
<a href="" target="_blank"><img src="/documentation/Desktop.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Ipad.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Mobile.png" alt="Book Bites mobile Screen"></a>

# REASONS FOR DEVELOPMENT

### I (Colin Hammarberg) am developing/building this application for the therapist and the society circulating around it. Currently therapist and psychotrists centers usually offer a very limited and difficult structure for their clients. Especially in the smaller cities all around the world. I am one of those people who feel that the structure could improve a lot with the therapists and psychotrists. All communication, booking, feedback and content are today handled through email and a piece of physical paper. This application will help the clients of "Improvement Therapy & Psychiatrist Centre" to receive a better and functional structure. At least I will be using it with my therapist instead of emailing back and fourth all the time. 

# TECHNOLOGIES USED 
 
### HTML
* The project uses HTML to get the content visual. The developer has been using HTML in all visual pages.
 
### CSS
* The project uses CSS to design all pages. I have put a lot of energy on the design and still am. I prefer to use external CSS, instead of internal CSS to achive a "better" code.

### JavaScript
* The project uses Javascript.

### jQuery 
* The project uses jQuery.

### PYTHON
* The project uses Python to build the actual application and its functionalities.
 
### FRAMEWORK
* The project uses MaterializeCSS, to achive a very well functioning framework, responsiveness and helpful tools/classes/grids. 

### FLASK
* The project uses Flask framework.

### MONGODB
* The project uses Mongo Database to store data and also display data to the users/clients.
 
### LANGUAGES
* The project uses English as its standard language and an Lang=”en” attribute has also been implemented.

# WIREFRAMES

# FEATURES

### All of the pages have been created with a mix of HTML, CSS, Javascript, jQuery and Python etc. This is shown very clearly, due to that it is a flask and python application. Clients to Improvement Therapy & Psychiatrist Centre are able to book meetings, add comments to what they would like to talk about on the next meeting, visualize a schedule with a drop-down menu which shows their next meetings, contact the centre, search up important information about mental illness etc. 

## Existing Features

### Navigation bar 
<a href="" target="_blank"><img src="/documentation/Navigation-bar-1.png" alt="Book Bites mobile Screen"></a>
<a href="" target="_blank"><img src="/documentation/Navigation-bar-2.png" alt="Book Bites mobile Screen"></a>

- The navigation bar is featured on all pages, but in different ways. If a user has not yet created an account and is currently logged into his/hers account, some of the application's features are not visible. The navigation bar is responsive and includes links to the "Love Therapy" logo, Home/Landing page, Contact page, My Account page, Schedule Meetings page, View Meetings page, Diary page and Log Out function (which directly logs out the user). It is identical in each page to allow for smooth navigation throughout the whole application.
- This nav bar will allow the user to easily find him or herself all around the application. As does the mobile navigation slide out (which comes out from the right side when the user activates it by clicking the hamburger icon).

### Landing Page

- The landing page contains a navigation bar, a Gif with some cool effects, and about us section in between the Gifs and a footer section which contains more information about the application and its therapy centre/application.
- The landing page also contains a footer section in the bottom of the page. 

### Register Page

- The register page contains a registration form with a function which registeres and ads the users deatils into mongodb.
- The register page also contains a footer section in the bottom of the page. 

### Log-in Page

- The log-in page contains a log-in form which contains a function that finds out if the username, password and email address exists in the databse. If the user exists and matches with the one in the database, the user will get logged in to his/hers account.
- The Log-In page also contains a footer section in the bottom of the page. 

### About Us Page

### Contact Page

- The contact page contains a contact form which contains a function that sends the details which the user added into the databse as well. 
- The Contact page also contains a footer section in the bottom of the page. 

### Schedule Meetings

- The Schedule Meetings page contains a form which allows the user/client to send in a requested meetings. The request gets register in the database and the client support executive can then later contact the user from there.
- The Scedhule Meetings page also contains a footer section in the bottom of the page. 

### View Meetings

- The View Meetings page contains drop down menu contains a function, which finds all of the meetings requested by the logged in user. The user/client then receives a structured calendar for his/her requested bookings. 
- The View Meetings page also contains a footer section in the bottom of the page. 



### Edit Meetings

- The View Meetings page contains a form, which contains the meeting's inputs that the user has requested. The Edit Meetings drop down selection menu has a function, which lets the user edit the meeting that they have created. When updating the details in the form, the details with the same ID will be updated in the database as well.
- The Edit Meetings page also contains a footer section in the bottom of the page. 


### Journal

- The Journal page contains a documentation form which allows the user/client to write and documentate about her/his day. It contains a function which registeres everything which has been posted in the database. This is something Therapists & Psychiatrist are using a lot when they are working with clients, and to digitize the procedure makes it a lot easier or both the user/client and the Therapist/Psychiatrist. 
- The Journal page also contains a footer section in the bottom of the page. 

### View Journal

- The View Journal page contains a drop down menu selector which lets the user/client to view the journal posts him/her have done. It also lets the Therpist/Psychiatrist to read what him/her have been writing. It gives a big benefit in the sessions between the client & the Therapist/Psychiatrist, because they both will be aware of where they should begin the conversation. 
- The View Journal page also contains a footer section in the bottom of the page. 

### Footer

- The footer contains information about the company and the company behind the application. It also states very clearly, that the company does not have any social media.

### Features left to implement

* In the future I would like to integrate SPCE (Digital meeting platform) onto the application and that the client automatically receives an account when creating an account on Love Therapy. It would be easier for the client to have digital meetings then.
* I would also like to implement a direct booking system which shows when there are available slots and that triggers an automatic text message and email which should be sent to the client when completing a booking. 

# MEDIA & CONTENT

<br>
<br>

# TESTING

### I have been conducting tests on the deveoped application. The tests that I have been conducting are the following.

#### Landing Page (Macbook Air M1 + External Screen)
* The landing page has two different shades. One where the user has not been logged in and I have made sure that only the pages visible then are (Home, Contact, Register & Log-in). This is made because the user7client has not yet registered and is not allowed access to any other pages at that time. 
* In the second shade of the landing page, the user has logged in and the home/landing page is still visible. But in the second shade, the user/client are able to go to the following pages (Home, Contact, My Account, Schedule Meetings, View Meetings, Journal and the Logout function.)
* There is also a button which works just fine on the landing/home page, which brings the user/client to an external website (https://www.spce.com). 

#### Contact Page (Macbook Air M1 + External Screen)
* The contact page has been tested and works fine too. I decided not to use EmailJS as previous Milestone Projects. Instead, I used mongodb. The user/client enters his/her contact information and message, and that is later on registered into the database folder "emails". 
* I have been testing this carefully as the other functions, where I have filled up the form and then pressed the button. Then I have checked so that the information is published in my databse, in the correct folder & structure.
* Even here, I have ben testing the navigation bar to see that everything works fine. 

#### My Account Page (Macbook Air M1 + External Screen)
* The My Account page includes more options for the user/client. There is a button for making Bookings, Viewing the right journal & for the user/client to delete his/her account. 
* The Booking button on the My Account page works fine and is bringing the user/client to the correct meeting page. 
* The View Journal button brings the user/client to the page where all of their journal posts are visible in order. This has also been tested mutiple times, and has been working fine every time.
* The Delete My Account button has been tested multiple times to. It automatically triggers the delete_user function and I have also made sure that the user/client no longer exists in the database by looking in my database when the function is triggered. I have also tried to log-in with the same user information multiple times after deleting the user, and it doesn't work to log in again and the correct flash message is being displayed.
* Even here, I have ben testing the navigation bar to see that everything works fine. 

#### Scedule Meetings Page (Macbook Air M1 + External Screen)
* The Schedule Meetings page is where the user/client requests a booking. This function inserts the information provided by the user into the database (in the folder named appointments).
* This functionality and form has been tested multiple times too and has been working fine. I have tried to make different variations of bookings, just to see that it inserts the right information provided by the user/client. 
* Even here, I have ben testing the navigation bar to see that everything works fine.

#### View Meetings Page (Macbook Air M1 + External Screen)
* The View Meetings page is where the user/client is able to view all of the requested bookings he/she has made. The function is finding and displaying all of the meetings booked by the logged in user/client.
* I have made sure that the viewing functionality displays all the accurate data. 
* The viewing page also has a few buttons which lets the user/client to make different options. The user/client is able to delete the booking, update the booking and contact the centre. 
* I have made sure that all buttons are working and are bringing the user/client to the accurate pages. The delete meeting function has been tested and I have made sure that the meeting is removed from the database and also not visible on the viewing meetings page.
* Even here, I have ben testing the navigation bar to see that everything works fine.

#### Update Meetings Page (Macbook Air M1 + External Screen)
* The Update Meetings page is only visble if the user/client presses the button on the View Meetings page, named "Update". 
* The page gives the user/client the accurate input they have registered at first when they created the meeting. I have made sure that the accurate data is being displayed right from the beginning on the Update Meetings page. 
* 








### Landing page (https://cdn.dribbble.com/users/388048/screenshots/2303293/therapist.gif)







