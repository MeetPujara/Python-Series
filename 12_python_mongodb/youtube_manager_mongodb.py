import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
client = pymongo.MongoClient(os.getenv("MONGO_URI"))

db = client["youtubemanager"]
video_collection = db["videos"]

def fetch_videos():
    return list(video_collection.find())

def display_videos(videos):
    print("\n" + "-" * 40)
    print("📺 Your YouTube Video List".center(40))
    print("-" * 40)
    if not videos:
        print("🚫 No videos found.")
    for video in videos:
        print(f"🆔 ID: {str(video['_id'])}")
        print(f"🎞️  Name: {video['name']}")
        print(f"⏱️  Duration: {video['time']}")
        print("-" * 40)

def add_video(name, time):
    video_collection.insert_one({'name': name, 'time': time})
    print("✅ Video added successfully!")

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {'$set': {'name': new_name, 'time': new_time}}
        )
        if result.modified_count:
            print("✅ Video updated successfully!")
        else:
            print("⚠️  No video found with that ID or nothing changed.")
    except Exception as e:
        print("❌ Error updating video:", e)

def delete_video(video_id):
    try:
        result = video_collection.delete_one({'_id': ObjectId(video_id)})
        if result.deleted_count:
            print("🗑️ Video deleted successfully!")
        else:
            print("⚠️  No video found with that ID.")
    except Exception as e:
        print("❌ Error deleting video:", e)

def main():
    while True:
        print("\n" + "=" * 40)
        print("🎬  YOUTUBE VIDEO MANAGER (MongoDB)".center(40))
        print("=" * 40)
        print("1️⃣  List all YouTube Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '1':
            videos = fetch_videos()
            display_videos(videos)
            input("🔁 Press Enter to return to the main menu...")
        elif choice == '2':
            name = input("📝 Enter Video Name: ")
            time = input("⏱️ Enter Video Duration: ")
            add_video(name, time)
        elif choice == '3':
            videos = fetch_videos()
            display_videos(videos)
            video_id = input("✏️ Enter Video ID to Update: ")
            new_name = input("📝 New Video Name: ")
            new_time = input("⏱️ New Duration: ")
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            videos = fetch_videos()
            display_videos(videos)
            video_id = input("🗑️ Enter Video ID to Delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting YouTube Video Manager. Goodbye!")
            break
        else:
            print("❗ Invalid Choice. Please select between 1 to 5.")

if __name__ == "__main__":
    main()
