import json
import cv2
import numpy as np
import zipfile

zip_f = zipfile.ZipFile('kabeposter.zip')
json_file_path = "kabeposter/kabeposter_000000000000_keypoints.json"

with zip_f.open(json_file_path, "r") as file:
    data = json.load(file)


people_data = data["people"]

shoulder1 = (
    (int(people_data[0]["pose_keypoints_2d"][2]), int(people_data[0]["pose_keypoints_2d"][3])),
    (int(people_data[0]["pose_keypoints_2d"][5]), int(people_data[0]["pose_keypoints_2d"][6]))
)

shoulder2 = (
    (int(people_data[1]["pose_keypoints_2d"][2]), int(people_data[1]["pose_keypoints_2d"][3])),
    (int(people_data[1]["pose_keypoints_2d"][5]), int(people_data[1]["pose_keypoints_2d"][6]))
)
width = 2000
height = 2000

image = np.zeros((height, width, 3), dtype=np.uint8)

cv2.line(image, shoulder1[0], shoulder1[1], (0, 255, 0), 2)
cv2.line(image, shoulder2[0], shoulder2[1], (0, 255, 0), 2)

cv2.imshow("Shoulder Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
