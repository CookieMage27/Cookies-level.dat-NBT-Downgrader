# Cookie's level.dat NBT Downgrader

---
### currently downgrades to Minecraft Java versions

12w49a

b1.7.3

### keeps:

-enchantments

-items

-armor

-tools

-blocks

-position

-rotation

-blocks and item variants from older versions if the versions are close enough

### does NOT keep:

-chunks

-ender chest items (maybe in the future)

-block and item variants from newer versions (will just make them normal versions of themselves red wool into wool)

-items that dont exist in older versions

### perfect for:

-going to the position of the farlands in newer versions and generating them in b1.7.3

-applying any enchantment to any item in 12w49a

-thats it, those were the reasons i spent a week making this


## Instructions

open the main folder in vscode (or your own IDE if you can get it working)

1. Run `pip install -r requirements.txt` (the libraries for this project)

2. Go to the world you want to downgrade in files

3. Make a copy in case something goes... wrong

4. Delete the level.dat_old

5. Move the level.dat from your world into the input folder

6. Go to options.py and change the values to your specifications

7. If everything is set properly, running main.py should make a new level.dat in the output folder

8. Drag the outputed level.dat out into your world

play in the version you selected, minecraft should open the world without saying anything about conversion

---

## Extra Steps for Linux Users
Installing packages directly with `pip` on linux, particularly arch-based distros, has been known to break things, as the OS relies heavily on python pacakges to operate. If you're using arch or an arch-based distro, or you get `error: externally-managed-environment × This environment is externally managed`, it is recomended to follow these steps.

1. `cd` into your cloned code directory

2. Create a python virtual environment (venv): `python3 -m venv [venvname]` (replace [venvname] with a name of your choice - just venv is perfectly fine)

3. Staying in the same directory, run `[venvname]/bin/activate`. Any python or pip related commands you run now will use any libraries install in the virtual environment

4. Follow the steps as above; all libraries will install into your environment

5. When you're done, run `deactivate` to exit the environment. You'll have to use the venv again if you want to run this script

6. repeat steps 3-5 whenever you wish to use this script.

---

## Troubleshooting
- If there are errors about the "Data" key, theres probably something wrong with the installed libraries or the PATH

- If theres something wrong with the item parsing, theres probably something wrong with the version you have selected

- If there are other errors its probably a variable edge case i didnt account for or a newer version of minecraft with different formatting

**open an issue on the github if theres a problem ill maybe check it eventually and try to help idk**

if your doing this sort of thing i assume you know how it works
