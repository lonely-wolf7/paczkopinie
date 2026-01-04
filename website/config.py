import os

def get_admin_email() -> str:
    #uzyskiwanie maila agministratora do configu
    env: str = None
    try:
        if os.environ.get("ENVIRONMENT") == "DEV":
            env = "DEV"
    finally:
        env = "Local" if env is None else "DEV"

    if env == "DEV":
        return os.environ.get("ADMIN_EMAIL")
    return "282163@student.pwr.edu.pl"

# mail administratora
ADMIN_EMAIL = get_admin_email()

def is_admin(user) -> bool:
    # sprawdzanie czy użytkownik jest administratorem
    return user is not None and user.email == ADMIN_EMAIL
