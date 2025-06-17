import requests

def fetch_video_comments():
    url = "https://api.freeapi.app/api/v1/public/youtube/comments/cv-6bAeYsOY"
    response = requests.get(url)
    json_data = response.json()
    
    if json_data['success'] and 'data' in json_data:
        user_data = json_data['data']
        comment = user_data[2]['snippet']['topLevelComment']['snippet']['textDisplay']
        comment_author = user_data[2]['snippet']['topLevelComment']['snippet']['authorDisplayName']
        return comment,comment_author
        
def main():
    try:
        comment,comment_author = fetch_video_comments()
        print(f"Comment is: {comment}")
        print(f"Comment's Author is: {comment_author}")
        
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()