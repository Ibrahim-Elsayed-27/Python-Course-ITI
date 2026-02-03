from user import *
from project import *

def login_page():
    user_data = user_login()
    if user_data:
        print(f"Welcome, {user_data['name']}!")
        while(True):
            print("1. Create Project")
            print("2. View My Projects")
            print("3. View All Projects")
            print("4. delete Project")
            print("5. Update Project")
            print("6. search Project by Date")
            print("7. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                project_title = input("Enter project title: ")
                details = input("Enter project details: ")
                total_target = float(input("Enter total target amount: "))
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                create_project(
                    user_email=user_data["email"],
                    project_title=project_title,
                    details=details,
                    total_target=total_target,
                    start_date=start_date,
                    end_date=end_date
                )
            elif choice == "2":
                view_project(user_email=user_data["email"])
            elif choice == "3":
                view_all_projects()
            elif choice == "4":
                view_project(user_email=user_data["email"])
                title = input("Enter the title of the project to delete: ")
                delete_project(user_email=user_data["email"], title=title)
            elif choice == "5":
                view_project(user_email=user_data["email"])
                title = input("Enter the title of the project to update: ")
                new_title = input("Enter new title (leave blank to keep unchanged): ")
                new_details = input("Enter new details (leave blank to keep unchanged): ")  
                new_total_target = input("Enter new total target (leave blank to keep unchanged): ")
                new_start_date = input("Enter new start date (YYYY-MM-DD) (leave blank to keep unchanged): ")
                new_end_date = input("Enter new end date (YYYY-MM-DD) (leave blank to keep unchanged): ")
                if new_total_target:
                    new_total_target = float(new_total_target)
                edit_project(user_email=user_data["email"], project_title=title, new_title=new_title, new_details=new_details, new_total_target=new_total_target, new_start_date=new_start_date, new_end_date=new_end_date)
            elif choice == "6":
                date = input("Enter the date to search projects (YYYY-MM-DD): ")
                search_projects_by_date(target_date=date)
            elif choice == "7":
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please try again.")