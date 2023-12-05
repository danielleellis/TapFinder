from tkinter import *
from tkinter import ttk
import psycopg2

def query_database(beer_name, location, beer_style):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="tapfinder",
            user="postgres",
            password="callie"
        )

        # cursor object
        cursor = conn.cursor()

        # initialize results
        beers_result = None
        breweries_result = None

        # QUERIES
        if beer_name:
            # beer name
            cursor.execute("""
                SELECT beers.name, beers.id, breweries.name, beers.style, beers.abv, beers.ibu, beers.ounces
                FROM beers
                JOIN breweries ON beers.brewery_id = breweries.id
                WHERE beers.name = %s
            """, (beer_name,))
            beers_result = cursor.fetchall()

        if beer_style:
            #beer style
            cursor.execute("""
                SELECT beers.name, beers.id, breweries.name, beers.style, beers.abv, beers.ibu, beers.ounces
                FROM beers
                JOIN breweries ON beers.brewery_id = breweries.id
                WHERE LOWER(beers.style) = LOWER(%s)
            """, (beer_style,))
            beers_result = cursor.fetchall()

        if location:
            # location (state)
            cursor.execute("""
                SELECT * FROM breweries
                WHERE LOWER(state) = LOWER(%s)
            """, (location,))
            breweries_result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return beers_result, breweries_result

    except psycopg2.Error as e:
        # Handle the exception (print, log, or show an error message)
        print(f"Error: {e}")
        return None, None



def display_results(result_text, beers_result, breweries_result):
    # clear existing content
    result_text.config(state=NORMAL)
    result_text.delete(1.0, END)

    # text widget display
    if beers_result:
        result_text.insert(END, "Beers:\n")
        for row in beers_result:
            result_text.insert(END, f"Name: {row[0]}\nBrewery: {row[2]}\nStyle: {row[3]}\nABV: {row[4]}\nIBU: {row[5]}\nOunces: {row[6]}\n\n")

    if breweries_result:
        result_text.insert(END, "Breweries:\n")
        for row in breweries_result:
            result_text.insert(END, f"Name: {row[0]}\nCity: {row[1]}\nState: {row[2]}\n\n")

    # read-only 
    result_text.config(state=DISABLED)

def myClick():
    # get user input
    beer_name = beerEntry.get()
    location = locationEntry.get()
    beer_style = styleEntry.get()

    # init variables
    beers_result = None
    breweries_result = None

    # clear existing content
    result_text.config(state=NORMAL)
    result_text.delete(1.0, END)

    # query DB
    if beer_name:
        beers_result, breweries_result = query_database(beer_name, location, None)
    elif beer_style:
        beers_result, breweries_result = query_database(None, location, beer_style)
    elif location:
        _, breweries_result = query_database(None, location, None)

    # display results
    if beers_result is not None or breweries_result is not None:
        display_results(result_text, beers_result, breweries_result)


# GUI Implementation

root = Tk()
root.title("Tap Finder")

# custom style
style = ttk.Style()

# config button style
style.configure("TButton", padding=6, relief="flat", background="#4682B4")

# config scrollbar style
style.configure("TScrollbar", troughcolor="#B0C4DE", slidercolor="#4682B4")

result_frame = Frame(root)

result_text = Text(result_frame, wrap=WORD, width=50, height=20)
result_text.grid(row=0, column=0, sticky=NSEW)

scrollbar = Scrollbar(result_frame, command=result_text.yview)
scrollbar.grid(row=0, column=1, sticky=NSEW)
result_text.config(yscrollcommand=scrollbar.set)
result_text.config(state=DISABLED)

beerEntry = Entry(root)
locationEntry = Entry(root)
styleEntry = Entry(root)

p = Label(root, text="                          ")
p1 = Label(root, text="                          ")
title = Label(root, text="Tap Finder", font=("Helvetica", 24), fg="#4682B4")
p2 = Label(root, text="                        ")
p3 = Label(root, text="                        ")
p4 = Label(root, text="                        ")
p5 = Label(root, text="                        ")
p7 = Label(root, text="                        ")

beerHeading = Label(root, text="Beer Name:", fg="#4682B4") 
locationHeading = Label(root, text="Location:", fg="#4682B4")
styleHeading = Label(root, text="Beer Style:", fg="#4682B4")

myButton = Button(root, text="Search", command=myClick, relief=FLAT, cursor="hand2", bg="#4682B4")

p.pack()
p1.pack()
title.pack()
p2.pack()
p3.pack()
p4.pack()
p5.pack()
beerHeading.pack()
beerEntry.pack(pady=10)
locationHeading.pack()
locationEntry.pack(pady=10)
styleHeading.pack()
styleEntry.pack(pady=10)
myButton.pack(pady=10)
p7.pack()

result_frame.pack()

root.mainloop()