🔧 Step-by-Step Setup Instructions:



🐍 Step 1: Install Required Python Package:
Install the MySQL connector for Python:

pip install mysql-connector-python


🗄️ Step 2: Set Up the MySQL Database
1. Open Command Prompt
2. Log in to MySQL:

mysql -u root -p


3. Enter your MySQL password
4. Paste and run the contents of schema.sql:

CREATE DATABASE IF NOT EXISTS blog_app;

USE blog_app;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    tags VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



🔐 Step 3: Update Your MySQL Credentials in app.py
Open app.py and update this part:

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # ← Replace with your actual MySQL password
        database="blog_app"
    )



📂 Step 4: Navigate to Your Project Folder
Open Command Prompt and run:

cd Desktop\python-blog-post-manager-cli


▶️ Step 5: Run the App
Run the app from your terminal:

python app.py

You’ll see:
--- Blog Post Manager ---
1. Create Post
2. View All Posts
3. Search by Tag
4. Exit
Enter choice:


💻 Sample Usage:

➕ Option 1: Create a Post
Enter title: My First Blog
Enter content: Hello world, this is my blog.
Enter tags (comma-separated): python, intro
Post created successfully.

📚 Option 2: View Posts
ID: 1
Title: My First Blog
Tags: python, intro
Date: 2025-06-22 19:00:00

🔎 Option 3: Search by Tag
Enter tag to search: python
Title: My First Blog
Content: Hello world, this is my blog.

❌ Option 4: Exit
(Program ends)


🛠️ Troubleshooting:

| Error                    | Cause                | Fix                                      |
| ------------------------ | -------------------- | ---------------------------------------- |
| `Access denied`          | Wrong MySQL password | Update password in `app.py`              |
| `Can't connect to MySQL` | MySQL not running    | Start MySQL service                      |
| `Unknown database`       | Database not created | Run the SQL from `schema.sql`            |
| `ModuleNotFoundError`    | Missing connector    | Run `pip install mysql-connector-python` |

👨‍💻 Author
Souvik Bhattacharjee

