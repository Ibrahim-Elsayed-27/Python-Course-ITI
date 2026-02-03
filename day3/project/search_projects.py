import project
import json
project_config = json.load(open("project/project_config.json"))


def search_projects_by_date(target_date):
    try:
        with open(project_config["projects_data_file"], "r") as file:
            projects = json.load(file)
            matched_projects = [proj for proj in projects if proj["start_date"] <= target_date <= proj["end_date"]]
            if matched_projects:
                for proj in matched_projects:
                    print(f"Title: {proj['title']}")
                    print(f"Details: {proj['details']}")
                    print(f"Total Target: {proj['total_target']}")
                    print(f"Start Date: {proj['start_date']}")
                    print(f"End Date: {proj['end_date']}")
                    print(f"User Email: {proj['user_email']}")
                    print("-" * 20)
            else:
                print("No projects found for the given date.")
    except FileNotFoundError:
        print("Project data file not found.")

if __name__ == "__main__":
    search_date = "2022-08-01"
    print(f"Projects active on {search_date}:\n")
    search_projects_by_date(search_date)