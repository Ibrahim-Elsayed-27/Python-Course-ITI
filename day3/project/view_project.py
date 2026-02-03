import project
import json
project_config = json.load(open("project/project_config.json"))
def view_project(user_email):
    try:
        with open(project_config["projects_data_file"], "r") as file:
            projects = json.load(file)
            user_projects = [proj for proj in projects if proj["user_email"] == user_email]
            if user_projects:
                for proj in user_projects:
                    print(f"Title: {proj['title']}")
                    print(f"Details: {proj['details']}")
                    print(f"Total Target: {proj['total_target']}")
                    print(f"Start Date: {proj['start_date']}")
                    print(f"End Date: {proj['end_date']}")
                    print("-" * 20)
            else:
                print("No projects found for this user.")
    except FileNotFoundError:
        print("Project data file not found.")


def view_all_projects():
    try:
        with open(project_config["projects_data_file"], "r") as file:
            projects = json.load(file)
            if projects:
                for proj in projects:
                    print(f"Title: {proj['title']}")
                    print(f"Details: {proj['details']}")
                    print(f"Total Target: {proj['total_target']}")
                    print(f"Start Date: {proj['start_date']}")
                    print(f"End Date: {proj['end_date']}")
                    print(f"User Email: {proj['user_email']}")
                    print("-" * 20)
            else:
                print("No projects available.")
    except FileNotFoundError:
        print("Project data file not found.")

if __name__ == "__main__":
    
    view_project("ibrahim@gmail.com")
    print("\nAll Projects:\n")
    view_all_projects()

