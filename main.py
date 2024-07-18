import os
from PIL import Image

# 定义文件夹路径
folder_path = r"D:\Users\Ran\Downloads\同步图标png格式"

# 创建一个新的文件夹来保存转换后的ICO文件
output_folder = os.path.join(folder_path, "ico_files")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的所有PNG文件并进行转换
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)
        
        # 打开并转换图像
        with Image.open(file_path) as img:
            # 将图像转换为ICO格式
            img.save(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.ico"), format='ICO')

print("转换完成")
