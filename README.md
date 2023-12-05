<b>Tap Finder</b><br>
<br>

<b>OVERVIEW<br></b>
Tap Finder is a simple GUI application built using Tkinter in Python. The purpose of this application is to search for beers and breweries based on user input such as beer name, location (state), and beer style. The application connects to a PostgreSQL database named "tapfinder" and retrieves information about beers and breweries.


<b>PREREQUISITES<br></b>
Before running the application, ensure that you have the following installed:
Python
Tkinter (included in Python standard library)
psycopg2 (Python PostgreSQL adapter)


<b>USAGE<br></b>
Run the script in a Python environment.
python tap_finder.py
The GUI window will appear, allowing you to enter information in the "Beer Name," "Location," and "Beer Style" fields.
Click the "Search" button to query the database based on the provided input.
Results will be displayed in the text area below, showing information about matching beers and breweries.


<b>DATABASE CONNECTION<br></b>
The application connects to a PostgreSQL database with the following credentials:
Host: localhost
Port: 5432
Database: tapfinder
User: postgres
Password: callie


<b>QUERIES<br></b>
The application performs three types of queries based on user input:
Search by Beer Name:
Retrieves information about beers with a matching name, including brewery details.
Search by Beer Style:
Retrieves information about beers with a matching style, including brewery details.
Search by Location (State):
Retrieves information about breweries in the specified state.


<b>ACKNOWLEDGEMENTS<br></b>
The application utilizes the Tkinter library for GUI development.
Special thanks to the psycopg2 library for PostgreSQL database connectivity.
Feel free to explore and enhance the application for your specific needs!
