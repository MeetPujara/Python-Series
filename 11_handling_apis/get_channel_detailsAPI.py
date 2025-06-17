import requests

def fetch_channel_details():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    respone = requests.get(url)
    json_data = respone.json()
    
    if json_data['success'] and "data" in json_data:
        user_data = json_data["data"]
        title = user_data["info"]["snippet"]["title"]
        description = user_data["info"]["snippet"]["description"]
        subscriberCount = user_data["info"]["statistics"]["subscriberCount"] 
        return title,description,subscriberCount
    else:
        raise Exception("Failed To Fetch")
    
    
def main():
    try:
        title,description,subscriberCount = fetch_channel_details()
        print(f"Title of the channel is {title}")
        print(f"Description of the channel is {description}")
        print(f"The Subscriber Count of {title} is {subscriberCount}")
    except Exception as e:
        print(str(e))
    
if __name__ == "__main__":
    main()