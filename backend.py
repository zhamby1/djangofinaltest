import sqlite3
from bookPOS.models import Book
from datetime import datetime
from django.db import models
from django.utils import timezone


#check name and how database is structured
#This opens and connects to the data base
def connect():
    conn =sqlite3.connect("book.db") #not sure how this name works
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title, author, publisher, pub_date, price) ")
    conn.commit()
    conn.close()


def insert(title, author, publisher, pub_date, price):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (title,author,publisher,pub_date, price))
    conn.commit()
    conn.close()

def view():
    conn =sqlite3.connect("book.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM book")
    rows =cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", publisher="", pub_date="", price=""):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR publisher=? OR pub_date=? OR price=?",(title,author,publisher,pub_date, price))
    rows =cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title,author,publisher,pub_date, price ):
    conn =sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("UPDATE book SET title=? OR author=? OR publisher=? OR pub_date=? OR price=? WHERE id=?",(title,author,publisher,pub_date, price, id))
    conn.commit()
    conn.close()

connect()