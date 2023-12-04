import cv2
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

STBAR_doom_path = os.path.join(script_dir, "STBAR_doom.png")
STBAR_input_path = os.path.join(script_dir, "STBAR.png")

if not os.path.isfile(STBAR_doom_path):
    raise FileNotFoundError("The required file STBAR_doom.png not found in the script directory.")

if not os.path.isfile(STBAR_input_path):
    raise FileNotFoundError("The required file STBAR.png not found in the script directory.")

STBAR_doom = cv2.imread(STBAR_doom_path)
STBAR_input = cv2.imread(STBAR_input_path)

STBAR_left = STBAR_doom[:, :83]
STBAR_right = STBAR_doom[:, -83:]
STBAR_centre = STBAR_doom[:, 83:403]

left_colors = set([tuple(c) for c in STBAR_left.reshape(-1, 3).tolist()])
right_colors = set([tuple(c) for c in STBAR_right.reshape(-1, 3).tolist()])

color_to_coords_left = {tuple(STBAR_centre[y, x].tolist()): (x, y)
                         for y in range(STBAR_centre.shape[0])
                         for x in range(STBAR_centre.shape[1])
                         if tuple(STBAR_centre[y, x].tolist()) in left_colors}

color_to_coords_right = {tuple(STBAR_centre[y, x].tolist()): (x, y)
                         for y in range(STBAR_centre.shape[0])
                         for x in range(STBAR_centre.shape[1])
                         if tuple(STBAR_centre[y, x].tolist()) in right_colors}

new_left_extension = np.zeros_like(STBAR_left)
for y in range(STBAR_left.shape[0]):
    for x in range(STBAR_left.shape[1]):
        c = tuple(STBAR_left[y, x].tolist())
        if c in color_to_coords_left:
            new_x, new_y = color_to_coords_left[c]
            new_left_extension[y, x] = STBAR_input[new_y, new_x]

new_right_extension = np.zeros_like(STBAR_right)
for y in range(STBAR_right.shape[0]):
    for x in range(STBAR_right.shape[1]):
        c = tuple(STBAR_right[y, x].tolist())
        if c in color_to_coords_right:
            new_x, new_y = color_to_coords_right[c]
            new_right_extension[y, x] = STBAR_input[new_y, new_x]

new_STBAR = np.hstack([new_left_extension, STBAR_input, new_right_extension])

cv2.imwrite(os.path.join(script_dir, "STBAR_extended.png"), new_STBAR)

print("Extended STBAR made successfully")
print("STBAR_extended.png is output to the directory where this script/binary was ran")
print("\nPress Enter key to exit")
input()