# The Contact Network
Our Website Name

# IIIT Contact Directory
Our Project is a contact directory for out college, IIIT, which allows users to search, insert, and update data for both students and faculties. This directory is designed to make it easy for anyone to quickly find the contact information they need for students and faculty members at IIIT.


The project involves creating a database to store all the contact information for students and faculties. Users can search the database by entering the name or other details of the person they are looking for, and the system will return the relevant contact information. Users can also insert new data into the database if they need to add a new student or faculty member, and update existing data if any information changes. There are also features to delete or modify data of student and faculty.

The user interface is simple and intuitive, allowing users to easily find the information they need and make any necessary updates.

Overall, the IIIT contact directory project can be a valuable tool for students, faculty members, and staff at IIIT, making it easy to quickly find and update contact information for anyone in the IIIT community.


## Authors

- [@Priet Ukani](https://github.com/priet-ukani) Made the backend part of the project, consisting of database, flask, website connection and collection of data by web scraping, also the javascript part.
- [@Ayush Sahu](https://github.com/AyushxCentury) Made the Home page and About Page. Applied styling and css to all the webpages. Did the final testing and bug fixing of whole project.
- [@Navdha Bansal](https://github.com/Navdha1801) Made the functions HTML pages for Insert, Modify, Search and Delete details. Prepared the README file for the project. 
## Tech Stack
Used python flask and sqlite3 database for the backend part.

Used HTML5 and CSS alongwith javascript for the designing of webpages (frontend part).


## Installation and usage
Run the app.py (contained in the src folder) to start the applicaion.
```bash
  cd src/
  python app.py
```
Navigate to the local IP provided by the flask applicaion from the python program.
By default, it loads the HomePage of the website. Use the navigation bar to go to the other pages. All functions are given in different individual pages.



## Features

- Maintain a student and faculty database.
- Add new student/faculty.
- Delete existing student/faculty.
- Modify the details of existing student/faculty.
- Search the database based on multiple filters.



## Directory Structure

``` 
.
├── README.md
└── src
    ├── app.py
    ├── data.db
    ├── datatest.py
    ├── faculties_setup.py
    ├── setup.py
    ├── static
    │   ├── ayush.jpg
    │   ├── black.jpeg
    │   ├── cool-background1.png
    │   ├── IIITH_Logo.jpeg
    │   ├── IIITHyd.webp
    │   ├── Navdha (1).jpeg
    │   ├── Navdha.jpeg
    │   ├── priet.jpeg
    │   ├── res_style.css
    │   ├── script.js
    │   ├── style_about.css
    │   └── style.css
    └── templates
        ├── about.html
        ├── delete_faculty.html
        ├── delete_result_faculty.html
        ├── delete_result.html
        ├── delete_student.html
        ├── error.html
        ├── faculty_search.html
        ├── index.html
        ├── insert_faculty.html
        ├── insert_student.html
        ├── result_faculty.html
        ├── result.html
        ├── student_search.html
        ├── testhtml.html
        ├── update_faculty.html
        └── update_student.html
```
## Contributing

Contributions are always welcome!
Please adhere to this project's `code of conduct`.
