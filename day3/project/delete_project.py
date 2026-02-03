import project
import json
project_config = json.load(open("project/project_config.json"))

def delete_project(user_email, project_title):
    try:
        with open(project_config["projects_data_file"], "r") as file:
            projects = json.load(file)
        
        initial_count = len(projects)
        projects = [proj for proj in projects if not (proj["user_email"] == user_email and proj["title"] == project_title)]
        
        if len(projects) < initial_count:
            with open(project_config["projects_data_file"], "w") as file:
                json.dump(projects, file, indent=4)
            print("Project deleted successfully.")
        else:
            print("Project not found for the given user.")
    except FileNotFoundError:
        print("Project data file not found.")


if __name__ == "__main__":
    delete_project("ibrahim@gmail.com", "Save the Earth")