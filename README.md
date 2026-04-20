### Cookie's level.dat NBT Downgrader

currently downgrades to Minecraft Java versions :
    12w49a
    b1.7.3

keeps-
    enchantments
    
    items
    
    armor
    
    tools
    
    blocks
    
    position
    
    rotation
    
    blocks and item variants from older versions if the versions are close enough
does NOT keep-
    chunks
    
    ender chest items (maybe in the future)
    
    block and item variants from newer versions (will just make them normal versions of themselves red wool into wool)
    
    items that dont exist in older versions

perfect for-
    going to the position of the farlands in newer versions and generating them in b1.7.3
    
    applying any enchantment to any item in 12w49a
    
    thats it, those were the reasons i spent a week making this
    

## instructions

open the main folder in vscode(or your own IDE if you can get it working)

run pip install -r requirements.txt (the libraries for this project)

go to the world you want to downgrade in files

make a copy in case something goes... wrong

delete the level.dat_old

move the level.dat from your world into the input folder

go to options.py and change the values to your specifications

if everything is set properly, running main.py should make a new level.dat in the output folder

drag the outputed level.dat out into your world

play in the version you selected, minecraft should open the world without saying anything about conversion



# troubleshooting
if there are errors about the "Data" key, theres probably something wrong with the installed libraries or the PATH

if theres something wrong with the item parsing, theres probably something wrong with the version you have selected

if there are other errors its probably a variable edge case i didnt account for or a newer version of minecraft with different formatting

open an issue on the github if theres a problem ill maybe check it eventually and try to help idk

if your doing this sort of thing i assume
