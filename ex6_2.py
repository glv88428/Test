import json
import tkinter as tk
from tkinter import Canvas
import zipfile

def read_keypoints_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['people']

def draw_shoulder_line(canvas, shoulder):
    canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill="red", width=2)
    
def draw_shoulder_line2(canvas, shoulder):
    canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill="green", width=2)    
    

zip_f = zipfile.ZipFile('kabeposter.zip')
json_file_path = "kabeposter/kabeposter_000000000000_keypoints.json"

with zip_f.open(json_file_path, "r") as file:
    data = json.load(file)

people_data = data["people"]



shoulder1 = [
    int(people_data[0]["pose_keypoints_2d"][6]), int(people_data[0]["pose_keypoints_2d"][7]),
    int(people_data[0]["pose_keypoints_2d"][3]), int(people_data[0]["pose_keypoints_2d"][4])
]

shoulder2 = [
    int(people_data[0]["pose_keypoints_2d"][3]), int(people_data[0]["pose_keypoints_2d"][4]),
    int(people_data[0]["pose_keypoints_2d"][15]), int(people_data[0]["pose_keypoints_2d"][16])
]
shoulder3 = [
    int(people_data[1]["pose_keypoints_2d"][6]), int(people_data[1]["pose_keypoints_2d"][7]),
    int(people_data[1]["pose_keypoints_2d"][3]), int(people_data[1]["pose_keypoints_2d"][4])
]

shoulder4 = [
    int(people_data[1]["pose_keypoints_2d"][3]), int(people_data[1]["pose_keypoints_2d"][4]),
    int(people_data[1]["pose_keypoints_2d"][15]), int(people_data[1]["pose_keypoints_2d"][16])
]



root = tk.Tk()
root.title("Shoulder Lines")

canvas = Canvas(root, width=2000, height=1000)
canvas.pack()

draw_shoulder_line(canvas, shoulder1)
draw_shoulder_line2(canvas, shoulder2)
draw_shoulder_line(canvas, shoulder3)
draw_shoulder_line2(canvas, shoulder4)

# イベントループの開始
root.mainloop()
