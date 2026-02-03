import project
import json
project_config = json.load(open("project/project_config.json"))


def create_project(user_email, project_title, details, total_target, start_date, end_date):
    project_instance = project.project()
    project_instance.user_email = user_email
    project_instance.title = project_title
    project_instance.details = details
    project_instance.total_target = total_target
    project_instance.start_date = start_date
    project_instance.end_date = end_date
    project_instance.save_project()

    print("Project created successfully.")


if __name__ == "__main__":
    create_project(
        user_email="ibrahim@gmail.com",
        project_title="New Project",    
        details="This is a new project.",
        total_target=10000,
        start_date="2024-07-01",
        end_date="2024-12-31"
    )