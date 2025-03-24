from crud_operations import create_table, insert_user, read_users, update_user, delete_user

def main():
    create_table()
    
    while True:
        print("\nCRUD Operations:")
        print("1. Create (Insert User)")
        print("2. Read (Show Users)")
        print("3. Update (Modify User)")
        print("4. Delete (Remove User)")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            insert_user(name, age)
        
        elif choice == "2":
            read_users()
        
        elif choice == "3":
            user_id = int(input("Enter User ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, age)
        
        elif choice == "4":
            user_id = int(input("Enter User ID to delete: "))
            delete_user(user_id)
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()