# What does the script do
The script extends huds based off of previously extended huds that look similar, but are just re-colored. Here are some examples of it in action. For this example, I will be using the 486x32 extended hud **doom_wide.wad** from OpenRift's Google Drive link: https://www.doomworld.com/forum/topic/121385-widescreen-assets-pack-and-appreciation-thread/

![STBAR_doom](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/d40517df-8221-4ff9-8e8f-fdaa5e30a26b)

### From this one extended hud, here are some examples of huds that the script can extend:

Haste

![STBAR](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/f02c9d0d-0a2e-4ca2-b350-c3301d28f337)

Fallen Leaves

![STBAR_extended](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/3ce2816a-8707-42a1-a75a-eeb0e92579a1)

Not Even Remotely Fair

![STBAR_extended](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/9f3177c4-1706-40f7-8b33-e306886ec952)

Mayan Mishap

![STBAR_extended](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/811c1a23-0bf8-4aee-aa9e-16ec4a47c476)

**NOTE:** This script works well for STBARs that copy a pre-existing STBAR with an extended hud made for it, such as the original DOOM STBAR. However, this is not the only use of this script, nor is this the list of STBARs this script can work on is not exhaustively listed here. The **output quality of the script heavily relies on the quality of the extended hud template (STBAR_doom.wad).** For example, the usage of this different extended HUD for Ultimate DOOM will affect the output of the program: https://github.com/bangstk/doom-wad-autoloads/blob/main/autoload/doom-all/doom-all_bar_uwide21.wad

![STBAR](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/7aadfb89-45d4-4816-a0fc-32dbb15b3c70)

Example of this 576x32 statusbar being used on Mayan Mishap

![STBAR_extended](https://github.com/Sbzro12345/STBAR_extender/assets/72307706/5e596019-7fe3-4bb1-ab88-dc183bfe25ec)

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
2. An image named "STBAR_doom.png". Case sensitive, and must be png. Must be 32 pixels in height and have a width greater than 320 pixels. STBAR_doom.png is the extended hud used to extend STBAR.

If everything runs correctly, the script will output the extended STBAR as "STBAR_extended.png" in the same directory as itself after running.
