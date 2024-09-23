import streamlit as st
import os

# Helper functions to read and write contacts from a file
CONTACTS_FILE = "contacts.txt"

def add_contact(name, phone):
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone}\n")
    st.success(f"Contact {name} added successfully!")

def get_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        contacts = [line.strip().split(",") for line in file.readlines()]
    return contacts

def search_contact(name):
    contacts = get_contacts()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    contacts = get_contacts()
    updated_contacts = [contact for contact in contacts if contact[0].lower() != name.lower()]
    
    with open(CONTACTS_FILE, "w") as file:
        for contact in updated_contacts:
            file.write(f"{contact[0]},{contact[1]}\n")
    
    if len(contacts) != len(updated_contacts):
        st.success(f"Contact {name} deleted successfully!")
    else:
        st.error(f"Contact {name} not found.")

# Streamlit app starts here
st.title("📒 Contact Book by Aneesh")

menu = ["Add Contact", "View All Contacts", "Search Contact", "Delete Contact", "Exit"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Add Contact":
    st.subheader("Add a New Contact")
    name = st.text_input("Enter contact name:")
    phone = st.text_input("Enter phone number:")
    
    if st.button("Add Contact"):
        if name and phone:
            add_contact(name, phone)
        else:
            st.error("Please provide both name and phone number.")

elif choice == "View All Contacts":
    st.subheader("View All Contacts")
    contacts = get_contacts()
    
    if contacts:
        for contact in contacts:
            st.write(f"**Name**: {contact[0]}, **Phone**: {contact[1]}")
    else:
        st.info("No contacts available.")

elif choice == "Search Contact":
    st.subheader("Search for a Contact")
    search_name = st.text_input("Enter the name to search:")
    
    if st.button("Search"):
        contact = search_contact(search_name)
        if contact:
            st.write(f"**Name**: {contact[0]}, **Phone**: {contact[1]}")
        else:
            st.error(f"Contact {search_name} not found.")

elif choice == "Delete Contact":
    st.subheader("Delete a Contact")
    delete_name = st.text_input("Enter the name to delete:")
    
    if st.button("Delete"):
        if delete_name:
            delete_contact(delete_name)
        else:
            st.error("Please provide a contact name to delete.")

elif choice == "Exit":
    st.write("Thank you for using the Contact Book app!")
    st.stop()
