from tkinter import *
import json

def read_contacts():
    with open('./contact.json', 'r') as f:
        contacts = json.load(f)
        return contacts


def write_contacts(contacts):
    with open('./contact.json', 'w') as f:
        json.dump(contacts, f, indent=4)


def display_contacts():
    global contact_list
    contacts = read_contacts()

    for contact in contacts:
        contact_list.insert(END, f"{contact['name'].upper()} = {contact['phone']}")


def add_contact():
    global contact_list
    new_name = name_entry.get()
    new_phone = phone_entry.get()
    contact = {"name": new_name, "phone": new_phone}
    contacts = read_contacts()
    contacts.append(contact)
    write_contacts(contacts)
    contact_list.delete(0, END)
    display_contacts()
    name_entry.delete(0, END)
    phone_entry.delete(0, END)


def delete_contact():
    global contact_list
    index = contact_list.curselection()[0]
    contacts = read_contacts()
    del contacts[index]
    write_contacts(contacts)
    contact_list.delete(0, END)
    display_contacts()


root = Tk()
root.title("Contact List")


contact_list = Listbox(root, width=50, height=8)
contact_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
display_contacts()


name_label = Label(root, text="Name")
name_label.grid(row=2, column=0, padx=0, pady=0)
name_entry = Entry(root, width=25)
name_entry.grid(row=2, column=0, columnspan=3, pady=10)

phone_label = Label(root, text="Phone")
phone_label.grid(row=3, column=0, padx=0, pady=0)
phone_entry = Entry(root, width=25)
phone_entry.grid(row=3, column=0, columnspan=3, pady=10)


add_button = Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=0, pady=10)

delete_button = Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=1, padx=0, pady=10)

quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.grid(row=4, column=2, padx=0, pady=10)

root.mainloop()