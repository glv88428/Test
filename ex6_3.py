import json
import tkinter as tk
from tkinter import Canvas
import zipfile

def read_keypoints_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['people']

def is_confident(keypoints, joint_index, confidence_threshold=0):
    return keypoints[joint_index * 3 + 2]>confidence_threshold

def draw_skeleton(canvas, keypoints, color, confidence_threshold=0):
    skeleton_lines = [
        (0, 1), (1, 2), (2, 3),  # 上半身
        (1, 5), (5, 6), (6, 7),  # 左腕
        (1, 8),  # 腰
        (8, 9), (9, 10), (10, 11),  # 右腿
        (8, 12),  # 腰
        (12, 13), (13, 14)  # 左腿
    ]

    for line in skeleton_lines:
        start_joint, end_joint=line

        if is_confident(keypoints, start_joint, confidence_threshold) and \
           is_confident(keypoints, end_joint, confidence_threshold):
            start_point = (int(keypoints[start_joint * 3])/2, int(keypoints[start_joint * 3 + 1])/2)
            end_point = (int(keypoints[end_joint * 3])/2, int(keypoints[end_joint * 3 + 1])/2)

            canvas.create_line(start_point, end_point, fill=color, width=2)

def update_frame(frame):
    json_file_path = f"kabeposter/kabeposter_000000000{frame:03d}_keypoints.json"
    with zip_f.open(json_file_path, "r") as file:
        data = json.load(file)
    people_data = data["people"]
    canvas.delete("all") 
    draw_skeleton(canvas, people_data[0]["pose_keypoints_2d"], "red")
    draw_skeleton(canvas, people_data[1]["pose_keypoints_2d"], "blue")
    root.update()
zip_f = zipfile.ZipFile('kabeposter.zip')
root = tk.Tk()
root.title("Skeleton Animation")

canvas = Canvas(root, width=4000, height=6000)
canvas.pack()

for frame in range(100):
    update_frame(frame)
    root.update()

root.mainloop()