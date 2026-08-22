def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    
    name = name.strip()
    if not name:
        raise ValueError("Name is empty")

    return name

def validate_age(age):
    if isinstance(age, str):
        if not age.strip():
            raise ValueError("Age is empty")
        
        if not age.isdigit():
            raise ValueError("Age must be a valid whole number")
        age = int(age)

    elif not isinstance(age, int):
        raise ValueError("Age must be a valid whole number")
    
    if age <= 0:
        raise ValueError("Age must be greater than 0")

    return age

def validate_id(record_id):
    if not isinstance(record_id, str):
        raise ValueError("ID must be a string")
    record_id = record_id.strip()
    if not record_id:
        raise ValueError("ID is empty")
    return record_id
