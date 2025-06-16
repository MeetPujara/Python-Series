import sqlite3

conn = sqlite3.connect('10_database_sqlite3\\youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def fetch_videos():
    cursor.execute("SELECT * FROM videos")
    return cursor.fetchall()

def display_videos(videos):
    print("\n" + "=" * 50)
    print("📺  CURRENT YOUTUBE VIDEO LIST".center(50))
    print("=" * 50)
    if not videos:
        print("⚠️  No videos found.")
    for row in videos:
        print(f"{row[0]}. 🎬 Name: {row[1]} | ⏱️ Duration: {row[2]}")
    print(f"\n📊 Total Videos: {len(videos)}")
    print("=" * 50 + "\n")

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"✅ '{name}' added successfully!")
    display_videos(fetch_videos())

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("🔄 Video updated successfully!")
    display_videos(fetch_videos())

def delete_video(video_id):
    cursor.execute("SELECT name FROM videos WHERE id = ?", (video_id,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()
        print(f"🗑️ '{row[0]}' deleted successfully!")
    else:
        print("❌ Video ID not found.")
    display_videos(fetch_videos())

def main():
    while True:
        print("\n" + "=" * 40)
        print("🎬  YOUTUBE VIDEO MANAGER (SQLite)".center(40))
        print("=" * 40)
        print("1️⃣  List all YouTube Videos")
        print("2️⃣  Add a YouTube Video")
        print("3️⃣  Update a YouTube Video")
        print("4️⃣  Delete a YouTube Video")
        print("5️⃣  Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '1':
            display_videos(fetch_videos())
            input("🔁 Press Enter to return to the main menu...")
        elif choice == '2':
            name = input("📝 Enter Video Name: ")
            time = input("⏱️ Enter Video Duration: ")
            add_video(name, time)
        elif choice == '3':
            display_videos(fetch_videos())
            video_id = input("✏️ Enter Video ID to Update: ")
            name = input("📝 New Video Name: ")
            time = input("⏱️ New Duration: ")
            update_video(video_id, name, time)
        elif choice == '4':
            display_videos(fetch_videos())
            video_id = input("🗑️ Enter Video ID to Delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("👋 Exiting YouTube Video Manager. Goodbye!")
            break
        else:
            print("❗ Invalid Choice. Please select between 1 to 5.")

    conn.close()

if __name__ == "__main__":
    main()
