import os

# 获取当前目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 列出目录中的所有文件和子目录
print("\n目录内容:")
for item in os.listdir(current_dir):
    item_path = os.path.join(current_dir, item)
    item_type = "目录" if os.path.isdir(item_path) else "文件"
    print(f"{item} - {item_type}")

# 检查background1.jpg是否存在
background_path = os.path.join(current_dir, "background1.jpg")
if os.path.exists(background_path):
    print(f"\nbackground1.jpg 存在于: {background_path}")
    print(f"文件大小: {os.path.getsize(background_path)} 字节")
else:
    print("\n错误: background1.jpg 不存在于当前目录")

# 检查index.html是否存在
index_path = os.path.join(current_dir, "index.html")
if os.path.exists(index_path):
    print(f"\nindex.html 存在于: {index_path}")
    print(f"文件大小: {os.path.getsize(index_path)} 字节")
else:
    print("\n错误: index.html 不存在于当前目录")