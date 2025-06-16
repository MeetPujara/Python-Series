import json

file_name = '09_error_handling\\youtube.txt'

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    print("\n" + "=" * 50)
    print("📺  YOUTUBE VIDEO LIST".center(50))
    print("=" * 50)
    if not videos:
        print("⚠️  No videos found.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. 🎬 Name: {video['name']} | ⏱️ Duration: {video['time']}")
    print("=" * 50 + "\n")

def add_video(videos):
    name = input("📝 Enter Video Name: ")
    time_duration = input("⏱️ Enter Video Duration: ")
    videos.append({'name': name, 'time': time_duration})
    save_data_helper(videos)
    print(f"✅ '{name}' added successfully!\n")

def update_video(videos):
    list_all_video(videos)
    index = int(input("✏️ Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("📝 New Video Name: ")
        time_duration = input("⏱️ New Duration: ")
        videos[index - 1] = {'name': name, 'time': time_duration}
        save_data_helper(videos)
        print("✅ Video updated successfully!\n")
    else:
        print("❌ Invalid Index Selected")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("🗑️ Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        deleted_video = videos[index - 1]['name']
        del videos[index - 1]
        save_data_helper(videos)
        print(f"✅ '{deleted_video}' deleted successfully!\n")
    else:
        print("❌ Invalid Video Index Selected")

def main():
    videos = load_data()
    while True:
        print("\n" + "=" * 40)
        print("🎬  YOUTUBE VIDEO MANAGER".center(40))
        print("=" * 40)
        print("1️⃣  List all YouTube Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit")

        choice = input("👉 Enter your choice: ")

        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("👋 Exiting YouTube Video Manager. Goodbye!")
                break
            case _:
                print("❗ Invalid Choice. Please select 1-5.")

if __name__ == "__main__":
    main()
