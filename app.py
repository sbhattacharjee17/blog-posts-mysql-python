import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with your actual password
        database="blog_app"
    )

def create_post():
    title = input("Enter title: ")
    content = input("Enter content: ")
    tags = input("Enter tags (comma-separated): ")

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO posts (title, content, tags) VALUES (%s, %s, %s)", (title, content, tags))
    db.commit()
    print("Post created successfully.")
    cursor.close()
    db.close()

def view_posts():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, title, tags, created_at FROM posts ORDER BY created_at DESC")
    for (id, title, tags, created_at) in cursor.fetchall():
        print(f"\nID: {id}\nTitle: {title}\nTags: {tags}\nDate: {created_at}\n")
    cursor.close()
    db.close()

def search_by_tag():
    tag = input("Enter tag to search: ")
    db = connect_db()
    cursor = db.cursor()
    query = f"SELECT title, content FROM posts WHERE tags LIKE '%{tag}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        for title, content in results:
            print(f"\nTitle: {title}\nContent: {content[:100]}...\n")
    else:
        print("No posts found with that tag.")
    cursor.close()
    db.close()

def main():
    while True:
        print("\n--- Blog Post Manager ---")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search by Tag")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_by_tag()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
