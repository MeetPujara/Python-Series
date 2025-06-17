import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    json_data = response.json()
    
    if json_data["success"] and "data" in json_data:
        user_data = json_data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed To Fetch")
    
def main():
    try:
        username,country = fetch_random_user()
        print(f"Username is {username} and Country is {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()