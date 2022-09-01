#tracking program to keep information used by insurance companies when you file a claim
from tkinter import *
import sqlite3

root = Tk()
root.title("Insurance Helper")
root.geometry("400x400")


#create a database or connect to one
conn =sqlite3.connect("address1_stuff.db")
c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE Stuff(
    item_name text,
    model_number text,
    store_purchase text,
    purchase_price integer,
    date_purchased text,
    item_type text,
    location_stored text 
    )""")
'''


#create function to delete a record
def delete():
    conn =sqlite3.connect("address1_stuff.db")
    c = conn.cursor()
   #delete a record
    c.execute("DELETE from stuff WHERE oid= " + delete_box.get)
    conn.commit()
    conn.close()

    
#create an update function to update a record    
def update():
    conn =sqlite3.connect("address1_stuff.db")
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE stuff SET
        item_name = :item_name,
        model_number = :model_number,
        store_purchase = :store_purchase,
        purchase_price = :purchase_price,
        date_purchased = :date_purchased,
        item_type=  :item_type,
        location_stored=  :location_stored

        WHERE oid = :oid""",
        {
        'item_name': item_name_editor.get(), 
        'model_number': model_number_editor.get(),
        'store_purchase': store_purchase_editor.get(),
        'purchase_price': purchase_price_editor.get(),
        'date_purchased': date_purchased_editor.get(),
        'item_type': item_type_editor.get(),
        'location_stored': location_stored_editor.get(),
        'oid': record_id
        })
    
    conn.commit()
    conn.close()
    editor.destroy()

#create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("400x400")
    conn =sqlite3.connect("address1_stuff.db")
    c = conn.cursor()
    record_id = delete_box.get()
    #query the database
    c.execute("""SELECT * FROM stuff WHERE oid = """ + record_id)
    records = c.fetchall()

   #create Global Variables for text box names
    global item_name_editor
    global model_number_editor
    global store_purchase_editor
    global purchase_price_editor
    global date_purchased_editor
    global item_type_editor
    global location_stored_editor
    
    #text boxes
    item_name_editor = Entry(editor, width = 25)
    item_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    model_number_editor = Entry(editor, width = 25)
    model_number_editor.grid(row=1, column=1, padx=20)
    store_purchase_editor = Entry(editor, width = 25)
    store_purchase_editor.grid(row=2, column=1, padx=20)
    purchase_price_editor = Entry(editor, width = 25)
    purchase_price_editor.grid(row=3, column=1, padx=20)
    date_purchased_editor = Entry(editor, width = 25)
    date_purchased_editor.grid(row=4, column=1, padx=20)
    item_type_editor = Entry(editor, width = 25)
    item_type_editor.grid(row=5, column=1, padx=20)
    location_stored_editor = Entry(editor, width = 25)
    location_stored_editor.grid(row=6, column=1, padx=20)


    #create text box labels
    item_name_label = Label(editor, text ='Item Name')
    item_name_label.grid(row=0, column=0, pady=(10,0))
    model_number_label = Label(editor, text= 'Model Number')
    model_number_label.grid(row=1, column=0)
    store_purchase_label = Label(editor, text= 'Store Purchased From')
    store_purchase_label.grid(row=2, column=0)
    purchase_price_label = Label(editor, text= 'Purchase Price')
    purchase_price_label.grid(row=3, column=0)
    date_purchased_label = Label(editor, text= 'Date Purchased')
    date_purchased_label.grid(row=4, column=0)
    item_type_label = Label(editor, text= 'Item Type')
    item_type_label.grid(row=5, column=0)
    location_stored_label = Label(editor, text= 'Location Stored')
    location_stored_label.grid(row=6, column=0)

    #loop through results
    for record in records:
        item_name_editor.insert(0,record[0])
        model_number_editor.insert(0,record[1])
        store_purchase_editor.insert(0,record[2])
        purchase_price_editor.insert(0,record[3])
        date_purchased_editor.insert(0,record[4])
        item_type_editor.insert(0,record[5])
        location_stored_editor.insert(0,record[6])
        
    #create a save button to save edited record
    upd_btn = Button(editor, text= "Save Record", command=update)
    upd_btn.grid(row =7, column=0, columnspan=2, pady=10, padx=10, ipadx=135 )


    
#create submit function database
def submit():
    conn =sqlite3.connect("address1_stuff.db")
    c = conn.cursor()
    #insert into table
    c.execute("INSERT INTO stuff VALUES (:item_name, :model_number, :store_purchase,:purchase_price, :date_purchased, :item_type, :location_stored)",
        {
            'item_name': item_name.get(),
            'model_number': model_number.get(),
            'store_purchase': store_purchase.get(),
            'purchase_price': purchase_price.get(),
            'date_purchased': date_purchased.get(),
            'item_type': item_type.get(),
            'location_stored': location_stored.get()
            })
    conn.commit()
    conn.close()


    
    #clear the text boxes
    item_name.delete(0,END)
    model_number.delete(0,END)
    store_purchase.delete(0,END)
    purchase_price.delete(0,END)
    date_purchased.delete(0,END)
    item_type.delete(0,END)
    location_stored.delete(0,END)

#create query function
def query():
    conn =sqlite3.connect("address1_stuff.db")
    c = conn.cursor()
    #query the database
    c.execute("SELECT *, oid FROM stuff")
    records = c.fetchall()
    #print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " +  str(record[2]) + " " +  str(record[3]) + " " +  str(record[4]) + " " +  str(record[5])+ " " +  str(record[6]) + " " + "\t"  + str(record[7])+ "\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row = 13, column = 0, columnspan = 2)
    conn.commit()
    conn.close()

#text boxes
item_name = Entry(root, width = 25)
item_name.grid(row=0, column=1, padx=20, pady=(10,0))
model_number = Entry(root, width = 25)
model_number.grid(row=1, column=1, padx=20)
store_purchase = Entry(root, width = 25)
store_purchase.grid(row=2, column=1, padx=20)
purchase_price = Entry(root, width = 25)
purchase_price.grid(row=3, column=1, padx=20)
date_purchased = Entry(root, width = 25)
date_purchased.grid(row=4, column=1, padx=20)
item_type = Entry(root, width = 25)
item_type.grid(row=5, column=1, padx=20)
location_stored = Entry(root, width = 25)
location_stored.grid(row=6, column=1, padx=20)

delete_box = Entry(root, width = 25)
delete_box.grid(row=10, column=1, pady=5)

#create text box labels
item_name_label = Label(root, text ='Item Name')
item_name_label.grid(row=0, column=0, pady=(10,0))
model_number_label = Label(root, text= 'Model Number')
model_number_label.grid(row=1, column=0)
store_purchase_label = Label(root, text= 'Store Purchased From')
store_purchase_label.grid(row=2, column=0)
purchase_price_label = Label(root, text= 'Purchase Price')
purchase_price_label.grid(row=3, column=0)
date_purchased_label = Label(root, text= 'Date Purchased')
date_purchased_label.grid(row=4, column=0)
item_type_label = Label(root, text= 'Item Type')
item_type_label.grid(row=5, column=0)
location_stored_label = Label(root, text= 'Location Stored')
location_stored_label.grid(row=6, column=0)

delete_box_label=Label(root, text = 'Select ID')
delete_box_label.grid(row =10, column=0, pady=5)

#create submit button
submit_btn =Button(root, text = 'Add Item', command = submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139)

#create a query button
query_btn = Button(root, text= "Show Stuff", command=query)
query_btn.grid(row =8, column=0, columnspan=2, pady=10, padx=10, ipadx=137 )

#create a Delete button
delete_btn = Button(root, text= "Delete Record", command=delete)
delete_btn.grid(row =9, column=0, columnspan=2, pady=10, padx=10, ipadx=128 )

#create an update button
upd_btn = Button(root, text= "Edit Record", command=edit)
upd_btn.grid(row =12, column=0, columnspan=2, pady=10, padx=10, ipadx=135 )

conn.commit()
conn.close()



root.mainloop()
