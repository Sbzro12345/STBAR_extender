# What does the script do
The script extends huds to 486x32 based off of previously extended huds that look similar, but are just re-colored. Here are some examples of it in action. For this example, I will be using the extended hud **doom_wide.wad** from OpenRift's Google Drive link: https://www.doomworld.com/forum/topic/121385-widescreen-assets-pack-and-appreciation-thread/

![STBAR_doom](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/d40517df-8221-4ff9-8e8f-fdaa5e30a26b)

From this one extended hud, here are some examples of huds that the script can extend:

Haste

![STBAR](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/f02c9d0d-0a2e-4ca2-b350-c3301d28f337)


# Installation
This Python script requires Python to run, download here: https://www.python.org/downloads/

This Python script also requires two external Python libraries - **opencv** and **numpy**.

#### Installing numpy
To install **numpy**, open Command Prompt or PowerShell and run the following command:
If you use macOS or Linux, just run it in Terminal
```pip install numpy```

#### Installing opencv
To install **opencv**, open Command Prompt or PowerShell and run the following command:
If you use macOS or Linux, just run it in Terminal
```pip install opencv-python```

# How to use the script
Once Python and the required libraries are installed, simply run **stbar_converter.py** in Python.
The script requires two files in the same directory as the script:
1. An image named "STBAR.png". Case sensitive, and must be png. Must be 320x32. STBAR.png is the original STBAR from PWADs that is to be extended.
2. An image named "STBAR_doom.png". Case sensitive, and must be png. Must be 486x32. STBAR_doom.png is the extended hud used to extend STBAR.

If everything runs correctly, the script will output the extended STBAR as "STBAR_extended.png" in the same directory as itself after running.
