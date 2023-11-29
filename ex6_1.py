import json
import zipfile

zip_f = zipfile.ZipFile('kabeposter.zip')
json_file_path = "kabeposter/kabeposter_000000000000_keypoints.json"

with zip_f.open(json_file_path, "r") as file:
    data = json.load(file)

people_data = data["people"]

nose1 = people_data[0]["pose_keypoints_2d"][:3]
neck1 = people_data[0]["pose_keypoints_2d"][3:6]

nose2 = people_data[1]["pose_keypoints_2d"][:3]
neck2 = people_data[1]["pose_keypoints_2d"][3:6]

print("Person 1 - Nose:")
print("X座標:", nose1[0])
print("Y座標:", nose1[1])
print("信頼度:", nose1[2])

print("\nPerson 1 - Neck:")
print("X座標:", neck1[0])
print("Y座標:", neck1[1])
print("信頼度:", neck1[2])

print("\nPerson 2 - Nose:")
print("X座標:", nose2[0])
print("Y座標:", nose2[1])
print("信頼度:", nose2[2])

print("\nPerson 2 - Neck:")
print("X座標:", neck2[0])
print("Y座標:", neck2[1])
print("信頼度:", neck2[2])
