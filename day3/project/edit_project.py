import project
import json
project_config = json.load(open("project/project_config.json"))

def edit_project(user_email, project_title, new_title=None, new_details=None, new_total_target=None, new_start_date=None, new_end_date=None):
    try:
        with open(project_config["projects_data_file"], "r") as file:
            projects = json.load(file)
        
        project_found = False
        for proj in projects:
            if proj["user_email"] == user_email and proj["title"] == project_title:
                project_found = True
                if new_title:
                    proj["title"] = new_title
                if new_details:
                    proj["details"] = new_details
                if new_total_target:
                    proj["total_target"] = new_total_target
                if new_start_date:
                    proj["start_date"] = new_start_date
                if new_end_date:
                    proj["end_date"] = new_end_date
                break
        
        if project_found:
            with open(project_config["projects_data_file"], "w") as file:
                json.dump(projects, file, indent=4)
            print("Project updated successfully.")
        else:
            print("Project not found for the given user.")
    except FileNotFoundError:
        print("Project data file not found.")

if __name__ == "__main__":
    edit_project("ibrahim@gmail.com", "Save the Earth", new_title="Save the Earth - Updated", new_details="Updated details for the project.", new_total_target=600000)