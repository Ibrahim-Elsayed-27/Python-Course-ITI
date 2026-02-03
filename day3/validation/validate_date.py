def validate_date(date: str) -> bool:
    from datetime import datetime
    date_format = "%Y-%m-%d"
    try:
        datetime.strptime(date, date_format)
        return True 
    except ValueError:
        return False
    

def validate_date_range(start_date: str, end_date: str) -> bool:
    from datetime import datetime
    date_format = "%Y-%m-%d"
    try:
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
        return start < end
    except ValueError:
        return False