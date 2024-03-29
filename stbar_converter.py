import cv2
import numpy as np
import os

copyright = "DOOM STBAR Extender Script\nCopyright (C) 2023  Sbzro12345\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see <https://www.gnu.org/licenses/>."

script_dir = os.path.dirname(os.path.abspath(__file__))

STBAR_doom_path = os.path.join(script_dir, "STBAR_doom.png")
STBAR_input_path = os.path.join(script_dir, "STBAR.png")
missing_flag = 0

print(copyright)
print("====================================================================")
print("\n\n\n\n\n")

if not os.path.isfile(STBAR_doom_path):
    missing_flag = 1
    print("The required file STBAR_doom.png not found in the script directory.")

if not os.path.isfile(STBAR_input_path):
    missing_flag = 1
    print("The required file STBAR.png not found in the script directory.")

if(missing_flag == 1):
    print("\nPress Enter key to exit")
    input()
    raise FileNotFoundError("One or more files were not found in script directory")

STBAR_doom = cv2.imread(STBAR_doom_path)
STBAR_input = cv2.imread(STBAR_input_path)

STBAR_doom_width = STBAR_doom.shape[1]
STBAR_width = STBAR_input.shape[1]
STBAR_slice_width = int( (STBAR_doom_width - STBAR_width) / 2 )

STBAR_left = STBAR_doom[:, :STBAR_slice_width]
STBAR_right = STBAR_doom[:, -STBAR_slice_width:]
STBAR_centre = STBAR_doom[:, STBAR_slice_width:(STBAR_doom_width - STBAR_slice_width)]

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

cv2.imwrite(os.path.join(script_dir, "STBAR.png"), new_STBAR)

print("Extended STBAR made successfully.")
print("STBAR.png in directory where this script was ran has been successfully overwritten with the extended STBAR.")
print("\nPress Enter key to exit")
input()
