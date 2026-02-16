from fastapi import FastAPI, Form
import sqlite3

app =FastAPI()
#Database

con = sqlite3.connect("contact.db",check_same_thread = False)
cursor = con.cursor()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS contacts
              (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT, 
               email TEXT, 
               message TEXT)""")

con.commit()


@app.get("/")

def form():
    return ""

@app.post("/submit")
def submit(name:str = Form(...), email: str = Form(...), message: str = Form(...)):
              #(id INTEGER, name TEXT, EMAIL TEXT, message TEXT)""")
    cursor.execute("INSERT INTO contacts(name, email, message) VALUES (?, ?, ?)",(name, email,message))

    con.commit()
    return {"message" : "saved successfully"}





