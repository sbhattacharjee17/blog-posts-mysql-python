# 📤 Sample Output – Blog Post Manager CLI

This document showcases how the CLI application behaves during usage.

---

## ▶️ Command to Run the App

```bash
python app.py

🏁 Main Menu Output
--- Blog Post Manager ---
1. Create Post
2. View All Posts
3. Search by Tag
4. Exit
Enter choice:


✏️ 1. Create Post
✅ Input:
Enter title: My First Blog
Enter content: This is a test blog about Python learning.
Enter tags (comma-separated): python, learning
✅ Output:
Post created successfully.


📚 2. View All Posts
✅ Output:
ID: 1
Title: My First Blog
Tags: python, learning
Date: 2025-06-22 15:14:30


🔎 3. Search by Tag
✅ Input:
Enter tag to search: python
✅ Output:
Title: My First Blog
Content: This is a test blog about Python learning....


❌ 3. Search by Tag – No Matches
✅ Input:
Enter tag to search: cooking
✅ Output:
No posts found with that tag.


🚪 4. Exit
✅ Output:
(Program ends)


---

### Save the File as `output.md`

1. Click **File → Save As**
2. Navigate to your folder:  
   👉 `Desktop > python-blog-post-manager-cli`
3. In **File name**, type:

output.md
4. In **Save as type**, choose:


