
from validation import validate_date, validate_date_range
import json
project_config = json.load(open("project/project_config.json"))
class project:
    def __init__(self):
        pass

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def user_email(self):
        return self._user_email
    
    @user_email.setter
    def user_email(self, value):
        self._user_email = value

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, value):
        self._details = value

    @property
    def total_target(self):
        return self._total_target   
    
    @total_target.setter
    def total_target(self, value):
        self._total_target = value

    @property
    def start_date(self):
        return self._start_date 
    @start_date.setter
    def start_date(self, value):
        if validate_date(value):
            self._start_date = value
        else:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):      
        if validate_date(value):
            pass
        else:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        if validate_date_range(self.start_date, value):
            self._end_date = value

    def __str__(self):
        return f"Project Title: {self.title}\nDetails: {self.details}\nTotal Target: {self.total_target}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}"
    

    def save_project(self):
        try:
            with open(project_config["projects_data_file"], "r") as file:
                projects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            projects = []

        project_data = {
            "title": self.title,
            "user_email": self.user_email,
            "details": self.details,
            "total_target": self.total_target,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        projects.append(project_data)

        with open(project_config["projects_data_file"], "w") as file:
            json.dump(projects, file, indent=4)

        
        
        
    

if __name__ == "__main__":
    new_project = project()
    new_project.title = "Save the Earth"
    new_project.user_email = "ibrahim@gmail.com"
    new_project.details = "A project to raise funds for environmental conservation."
    new_project.total_target = 500000
    new_project.start_date = "2024-07-01"
    new_project.end_date = "2024-12-31"
    new_project.save_project()