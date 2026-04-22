import nbtlib
from nbtlib import *
from nbtlib.tag import *
from item_list import all_item_list
import argparse
import pathlib
import platform


#brings in args from being executed by tui.py
argParser = argparse.ArgumentParser(description="Brings arguments from tui.py")
argParser.add_argument("leveldatPath", type = str)
argParser.add_argument("--versionChoice", type = str)
parsedArgs = argParser.parse_args()

leveldatPath = parsedArgs.leveldatPath
versionChoice = parsedArgs.versionChoice



try:
    new_level_dat = nbtlib.load(leveldatPath)
except:
    print("unable to load file. check the path and that it's a real level.dat file")
    exit()




if versionChoice == "1":
    option = "12w49a"
else:
    option = "Beta 1.7.3"



Beta173 = schema("Beta 1.7.3", {

    "RandomSeed": Long,
    
    "Player": schema("Player", {
        "Motion": List[Double],
        "Health": Short,
        "Air": Short,
        "OnGround": Byte,
        "Dimension": Int,
        "Rotation": List[Float],
        "SleepTimer": Short,
        "FallDistance": Float,
        "Score": Int,
        "Sleeping": Byte,
        "Pos": List[Double],
        "DeathTime": Short,
        "Fire": Short,
        "HurtTime": Short,
        "AttackTime": Short,
        "Inventory": List[schema("Item", {
            "Count": Byte,
            "Damage": Short,
            "Slot": Byte,
            "id": Short
        })],
    }),
    "SpawnY": Int,
    "rainTime": Int,
    "thunderTime": Int,
    "SpawnZ": Int,
    "SpawnX": Int,
    "raining": Byte,
    "Time": Long,
    "thundering": Byte,
    "version": Int,
    "LastPlayed": Long,
    "LevelName": String,
    "SizeOnDisk": Long,
})

TwelveWFourtyNineA = schema("12w49a", {

    "RandomSeed": Long,
    "generatorName": String,
    "GameRules": schema("GameRules", {
        "doTileDrops": String,
        "doFireTick": String,
        "mobGriefing": String,
        "commandBlockOutput": String,
        "doMobSpawning": String,
        "doMobLoot": String,
        "keepInventory": String,
    }),
    "Player": schema("Player", {
        "SleepTimer": Short,
        "Invulnerable": Byte,
        "PortalCooldown": Int,
        "abilities": schema("abilities", {
            "invulnerable": Byte,
            "mayfly": Byte,
            "instabuild": Byte,
            "walkSpeed": Float,
            "mayBuild": Byte,
            "flying": Byte,
            "flySpeed": Float,
        }),
        "FallDistance": Float,
        "DeathTime": Short,
        "DropChances": List[Float],
        "PersistenceRequired": Byte,
        "XpTotal": Int,
        "playerGameType": Int,
        "Motion": List[Double],
        "Health": Short,
        "foodSaturationLevel": Float,
        "Air": Short,
        "OnGround": Byte,
        "Dimension": Int,
        "Rotation": List[Float],
        "XpLevel": Int,
        "Score": Int,
        "Equipment": List[schema("equipment", {}) ],
        "Sleeping": Byte,
        "Pos": List[Double],
        "Fire": Short,
        "CanPickUpLoot": Byte,
        "XpP": Float,
        "EnderItems": List[schema("EnderItems", {
            "Count": Byte,
            "Damage": Short,
            "Slot": Byte,
            "id": Short,
            "tag": schema("Enchantments", {
                "StoredEnchantments": List[schema("StoredEnchantments", {
                    "lvl": Short,
                    "id": Short,
                })],
                "ench": List[schema("ench", {
                    "lvl": Short,
                    "id": Short,
                })],
                "RepairCost": Int,
            }),
        })],
        "foodLevel": Int,
        "foodExhaustionLevel": Float,
        "HurtTime": Short,
        "SelectedItemSlot": Int,
        "AttackTime": Short,
        "Inventory": List[schema("Item", {
            "Count": Byte,
            "Damage": Short,
            "Slot": Byte,
            "id": Short,
            "tag": schema("Enchantments", {
                "StoredEnchantments": List[schema("StoredEnchantments", {
                    "lvl": Short,
                    "id": Short,
                })],
                "ench": List[schema("ench", {
                    "lvl": Short,
                    "id": Short,
                })],
                "RepairCost": Int,
            }),
        })],
        "foodTickTimer": Int,
    }),
    "SpawnY": Int,
    "rainTime": Int,
    "thunderTime": Int,
    "SpawnZ": Int,
    "hardcore": Byte,
    "SpawnX": Int,
    "raining": Byte,
    "Time": Long,
    "thundering": Byte,
    "GameType": Int,
    "generatorVersion": Int,
    "MapFeatures": Byte,
    "version": Int,
    "generatorOptions": String,
    "LastPlayed": Long,
    "DayTime": Long,
    "LevelName": String,
    "initialized": Byte,
    "allowCommands": Byte,
    "SizeOnDisk": Long,
})

last_played = int(new_level_dat['Data']['LastPlayed'])
level_name = str(new_level_dat['Data']['LevelName'])
health = int(new_level_dat['Data']['Player']['Health'])
score = int(new_level_dat['Data']['Player']['Score'])


try:
    dimension = int(new_level_dat['Data']['Player']['Dimension'])
except:
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:overworld"):
        dimension = 0
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:nether"):
        dimension = -1
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:the_end"):
        dimension = 1


try:
    if(option=="12w49a"):
        doTileDrops = str(new_level_dat['Data']['GameRule']['doTileDrops'])
        doFireTick = str(new_level_dat['Data']['GameRule']['doFireTick'])
        mobGriefing = str(new_level_dat['Data']['GameRule']['mobGriefing'])
        commandBlockOutput = str(new_level_dat['Data']['GameRule']['commandBlockOutput'])
        doMobSpawning = str(new_level_dat['Data']['GameRule']['doMobSpawning'])
        doMobLoot = str(new_level_dat['Data']['GameRule']['doMobLoot'])
        keepInventory = str(new_level_dat['Data']['GameRule']['keepInventory'])
except:
    doTileDrops = "true"
    doFireTick = "true"
    mobGriefing = "true"
    commandBlockOutput = "true"
    doMobSpawning = "true"
    doMobLoot = "true"
    keepInventory = "false"
    

    
try:
    Invulnerable = int(new_level_dat['Data']['Player']['Invulnerable'])
except:
    Invulnerable = 0


try:
    seed = int(new_level_dat['Data']['RandomSeed'])
except KeyError:
    seed = int(new_level_dat['Data']['WorldGenSettings']['seed'])

try:
    xptotal = int(new_level_dat['Data']['Player']['XpTotal'])
except KeyError:
    xptotal = 0

try:
    xplevel = int(new_level_dat['Data']['Player']['XpLevel'])
except KeyError:
    xplevel = 0

try:
    playerGameType = int(new_level_dat['Data']['Player']['playerGameType'])
except KeyError:
    playerGameType = 0

try:
    GameType = int(new_level_dat['Data']['GameType'])
except KeyError:
    GameType = 0

try:
    allowCommands = int(new_level_dat['Data']['allowCommands'])
except KeyError:
    allowCommands = 0

try:
    satu = float(new_level_dat['Data']['Player']['foodSaturationLevel'])
except KeyError:
    satu = 0

try:
    foode = float(new_level_dat['Data']['Player']['foodExhaustionLevel'])
except KeyError:
    foode = 0

try:
    daytime = int(new_level_dat['Data']['Player']['DayTime'])
except:
    daytime = int(new_level_dat['Data']['DayTime'])

try:
    hardcore = int(new_level_dat['Data']['Player']['hardcore'])
except:
    hardcore = 0



sod = 0

try:
    sx = int(new_level_dat['Data']['SpawnX'])
    sy = int(new_level_dat['Data']['SpawnY'])
    sz = int(new_level_dat['Data']['SpawnZ'])
except KeyError:
    sx = int(new_level_dat['Data']['spawn']['pos'][0])
    sy = int(new_level_dat['Data']['spawn']['pos'][1])
    sz = int(new_level_dat['Data']['spawn']['pos'][2])

x = float(new_level_dat['Data']['Player']['Pos'][0])
y = float(new_level_dat['Data']['Player']['Pos'][1])
z = float(new_level_dat['Data']['Player']['Pos'][2])

motx = float(new_level_dat['Data']['Player']['Motion'][0])
moty = float(new_level_dat['Data']['Player']['Motion'][1])
motz = float(new_level_dat['Data']['Player']['Motion'][2])

rotx = float(new_level_dat['Data']['Player']['Rotation'][0])
roty = float(new_level_dat['Data']['Player']['Rotation'][1])

time = int(new_level_dat['Data']['Time'])

all_enchants_list = {
    "minecraft:protection": 0,
    "minecraft:fire_protection": 1,
    "minecraft:feather_falling": 2,
    "minecraft:blast_protection": 3,
    "minecraft:projectile_protection": 4,
    "minecraft:respiration": 5,
    "minecraft:aqua_affinity": 6,
    "minecraft:thorns": 7,
    "minecraft:sharpness": 16,
    "minecraft:smite": 17,
    "minecraft:bane_of_arthropods": 18,
    "minecraft:knockback": 19,
    "minecraft:fire_aspect": 20,
    "minecraft:looting": 21,
    "minecraft:efficiency": 32,
    "minecraft:silk_touch": 33,
    "minecraft:unbreaking": 34,
    "minecraft:fortune": 35,
    "minecraft:power": 48,
    "minecraft:punch": 49,
    "minecraft:flame": 50,
    "minecraft:infinity": 51,
}




def itemEnchantmentParser(storage, item, tag, container, is_book, ender, repair='RepairCost'):
    #print(item)
    enchantment_list = []
    if (new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'].get('Damage') != None and new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'].get(f'{container}') == None): 
        damage = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}']['Damage'])
        converted_items.append({
            "Count": count,
            "Slot": slot,
            "Damage": damage,
            "id": found_item,
        })
        print("damage Thingy")
        return
        
    for enchant in range(len(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'])):
        
        try:
            enchantment_lvl = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'][enchant].get('lvl'))
            enchantment_id  = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'][enchant].get('id'))
            print(enchantment_id, enchantment_lvl)
            enchantment_list.append({
                "lvl": enchantment_lvl,
                "id": enchantment_id,
            })
        except:
            for key, value in all_enchants_list.items():
                try:
                    if new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'][enchant]['id'] == key:
                        enchantment_id = value
                        enchantment_lvl = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'][enchant]['lvl'])
                        enchantment_list.append({
                            "lvl": enchantment_lvl,
                            "id": enchantment_id,
                        })
                        break
                except:
                    
                    try:
                        if list(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'].keys())[enchant] == key:
                            #print("got in")
                            enchantment_id = value
                            #print(enchantment_id," id")
                            enchantment_lvl = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{container}'][f'{key}'])
                            #print(enchantment_lvl," lvl")
                            enchantment_list.append({
                                "lvl": enchantment_lvl,
                                "id": enchantment_id,
                            })
                            #print(enchantment_list)
                    except:
                        pass
    try:
        damage = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}']['Damage'])
    except:
        try:
            damage = int(new_level_dat['Data']['Player'][f'{storage}'][item]['Damage'])
        except:
            try:
                damage = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}']['minecraft:damage'])
            except:
                damage = 0
    if(ender):
        if(is_book == True):
        
            ec_converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
                "tag": {
                    "StoredEnchantments": enchantment_list
                    #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                }
            })
        else:
            
            repaircost = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{repair}'])
            ec_converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
                "tag": {
                    "ench": enchantment_list,
                    #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                    "RepairCost": repaircost,
                }
            })
    else:
        if(is_book == True):
            
            converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
                "tag": {
                    "StoredEnchantments": enchantment_list
                    #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                }
            })
        else:
            
            repaircost = int(new_level_dat['Data']['Player'][f'{storage}'][item][f'{tag}'][f'{repair}'])
            converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
                "tag": {
                    "ench": enchantment_list,
                    #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                    "RepairCost": repaircost,
                }
            })



#############
#ENDER CHEST#
#############

ec_converted_items = []
ec_enchantment_list = []

for ec_item in range(len(new_level_dat['Data']['Player']['EnderItems'])):
    slot = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Slot'])
    ec_enchantment_list = []
    found_item = 0
    

    try:
        if type(str(new_level_dat['Data']['Player']['EnderItems'][ec_item].get('int'))) == str:
        
            for key, value in all_item_list.items():
                #print(key)
                #print(value)
                if new_level_dat['Data']['Player']['EnderItems'][ec_item]['id'] == key:
                    found_item = value
                    break
                else:
                    found_item = 0
    except:
        try:
            if type(int(new_level_dat['Data']['Player']['EnderItems'][ec_item].get('int'))) == int:
                found_item = new_level_dat['Data']['Player']['EnderItems'][ec_item]['id']
        except:
            found_item = 0

    try:
        count = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Count'])
    except:
        count = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['count'])
    
    try:
        damage = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Damage'])
    except:
        try:
            damage = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['Damage'])
        except:
            try:
                damage = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:damage'])
            except:
                damage = 0
    
        

    
    if(option == "12w49a"):
        if ('components' in list(new_level_dat['Data']['Player']['EnderItems'][ec_item].keys())): 
            
                
            
            if(found_item == 403):
                print(ec_item)
                itemEnchantmentParser('EnderItems', ec_item, 'components', 'minecraft:stored_enchantments', True, True)
                
            if(found_item != 403):
                itemEnchantmentParser('EnderItems', ec_item, 'components', 'minecraft:enchantments', False, True, 'minecraft:repair_cost')
                
        
        elif('tag' in list(new_level_dat['Data']['Player']['EnderItems'][ec_item].keys())):
        
            if(found_item == 403):
                itemEnchantmentParser('EnderItems', ec_item, 'tag', 'StoredEnchantments', True, True)
                
            if(found_item != 403):
                try:
                    itemEnchantmentParser('EnderItems', ec_item, 'tag', 'Enchantments', False, True)
                except:
                    itemEnchantmentParser('EnderItems', ec_item, 'tag', 'ench', False, True)
            
        else:
            #if tag doesnt exist
            ec_converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
            })
    
    else:
        #if isnt 12w49a(same as tag not existing)
        ec_converted_items.append({
            "Count": count,
            "Slot": slot,
            "Damage": damage,
            "id": found_item,
        })





###########
#INVENTORY#
###########

converted_items = []
enchantment_list = []

for item in range(len(new_level_dat['Data']['Player']['Inventory'])):
    slot = int(new_level_dat['Data']['Player']['Inventory'][item]['Slot'])
    enchantment_list = []
    found_item = 0
    
    try:
        if type(str(new_level_dat['Data']['Player']['Inventory'][item].get('int'))) == str:
        
            for key, value in all_item_list.items():
                #print(key)
                #print(value)
                if new_level_dat['Data']['Player']['Inventory'][item]['id'] == key:
                    found_item = value
                    break
                else:
                    found_item = 0
    except:
        try:
            if type(int(new_level_dat['Data']['Player']['Inventory'][item].get('int'))) == int:
                found_item = new_level_dat['Data']['Player']['Inventory'][item]['id']
        except:
            found_item = 0

    try:
        count = int(new_level_dat['Data']['Player']['Inventory'][item]['Count'])
    except:
        count = int(new_level_dat['Data']['Player']['Inventory'][item]['count'])
    
    try:
        damage = int(new_level_dat['Data']['Player']['Inventory'][item]['Damage'])
    except:
        try:
            damage = int(new_level_dat['Data']['Player']['Inventory'][item]['tag']['Damage'])
        except:
            try:
                damage = int(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:damage'])
            except:
                damage = 0
    
        

    
    if(option == "12w49a"):
        if ('components' in list(new_level_dat['Data']['Player']['Inventory'][item].keys())): 
        
            if(found_item == 403):
                itemEnchantmentParser('Inventory', item, 'components', 'minecraft:stored_enchantments', True, False)
                
            if(found_item != 403):
                itemEnchantmentParser('Inventory', item, 'components', 'minecraft:enchantments', False, False, 'minecraft:repair_cost')
                
                
        elif('tag' in list(new_level_dat['Data']['Player']['Inventory'][item].keys())):

            if(found_item == 403):
                itemEnchantmentParser('Inventory', item, 'tag', 'StoredEnchantments', True, False)
                
            if(found_item != 403):
                try:
                    itemEnchantmentParser('Inventory', item, 'tag', 'Enchantments', False, False)
                except:
                    itemEnchantmentParser('Inventory', item, 'tag', 'ench', False, False)
                

        else:
            #if tag doesnt exist
            converted_items.append({
                "Count": count,
                "Slot": slot,
                "Damage": damage,
                "id": found_item,
            })
    
    else:
        #if isnt 12w49a(same as tag not existing)
        converted_items.append({
            "Count": count,
            "Slot": slot,
            "Damage": damage,
            "id": found_item,
        })

#print(converted_items)
if (option == "Beta 1.7.3"):
    converted_data = Beta173({
        "RandomSeed": seed,
        "Player": {
            "Motion": [
                motx,
                moty,
                motz
            ],
            "SleepTimer": 0,
            "Health": health,
            "Air": 300,
            "OnGround": 1,
            "Dimension": 0,
            "Rotation": [
                rotx,
                roty,
            ],
            "FallDistance": 0,
            "Score": score,
            "Sleeping": 0,
            "Pos": [
                x,
                y,
                z
            ],
            "DeathTime": 0,
            "Fire": -20,
            "HurtTime": 0,
            "AttackTime": 0,
            "Inventory": converted_items,
        },
        "SpawnY": sy,
        "rainTime": 0,
        "thunderTime": 0,
        "SpawnZ": sz,
        "SpawnX": sx,
        "raining": 0,
        "Time": time,
        "thundering": 0,
        "version": 19132,
        "LastPlayed": last_played,
        "LevelName": level_name,
        "SizeOnDisk": sod,
        })
elif(option == "12w49a"):
    #definitely need to add this, itll be useless without it to have 12w49a
    converted_data = TwelveWFourtyNineA({
        "RandomSeed": seed,
        "generatorName": "default",
        "GameRules": {
            "doTileDrops": doTileDrops,
            "doFireTick": doFireTick,
            "mobGriefing": mobGriefing,
            "commandBlockOutput": commandBlockOutput,
            "doMobSpawning": doMobSpawning,
            "doMobLoot": doMobLoot,
            "keepInventory": keepInventory,
        },
        "Player":{
            "SleepTimer": 0,
            "Invulnerable": Invulnerable,
            "PortalCooldown": 0,
            "abilities": {
                "invulnerable": 0,
                "mayfly": 0,
                "instabuild": 0,
                "walkSpeed": 0.10000000149011612,
                "mayBuild": 1,
                "flying": 0,
                "flySpeed": 0.05000000074505806,
            },
            "FallDistance": 0,
            "DeathTime": 0,
            "DropChances": [
                0.05000000074505806,
                0.05000000074505806,
                0.05000000074505806,
                0.05000000074505806,
                0.05000000074505806
            ],
            "PersistenceRequired": 0,
            "XpTotal": xptotal,
            "playerGameType": playerGameType,
            "Motion": [
                motx,
                moty,
                motx
            ],
            "Health": health,
            "foodSaturationLevel": satu,
            "Air": 300,
            "OnGround": 1,
            "Dimension": dimension,
            "Rotation": [
                rotx,
                roty,
            ],
            "XpLevel": xplevel,
            "Score": score,
            "Equipment": [ {}, {}, {}, {}, {},],
            "Sleeping": 0,
            "Pos": [
                x,
                y,
                z,
            ],
            "Fire": -20,
            "CanPickUpLoot": 0,
            "XpP": 0.5,
            "EnderItems": ec_converted_items,
            "foodLevel": 20,
            "foodExhaustionLevel": foode,
            "HurtTime": 0,
            "SelectedItemSlot": 0,
            "AttackTime": 0,
            "Inventory": converted_items,
            "foodTickTimer": 0,
        },
        "SpawnY": sy,
        "rainTime": 0,
        "thunderTime": 0,
        "SpawnZ": sz,
        "hardcore": hardcore,
        "SpawnX": sx,
        "raining": 0,
        "Time": time,
        "thundering": 0,
        "GameType": GameType,
        "generatorVersion": 1,
        "MapFeatures": 1,
        "version": 19133,
        "generatorOptions": "",
        "LastPlayed": last_played,
        "DayTime": daytime,
        "LevelName": level_name,
        "initialized": 1,
        "allowCommands": allowCommands,
        "SizeOnDisk": sod
    })

root = Compound({
    'Data': converted_data
})

nbt_file = File(root)

#checks if output folder exists, makes one if it doesn't
outputFolder = pathlib.Path("output")
if not outputFolder.exists():
    print("output folder not found... creating one")
    outputFolder.mkdir()

# tries to save to the output folder, prints a help message if unsuccessfull
try:
    nbt_file.save("output/level.dat", gzipped=True)
    print("Saved in output!")
except FileNotFoundError:
    nbt_file.save("nbtconverterV2/output/level.dat", gzipped=True)
except Exception:
    print("Error saving file.... check output folder permissions and try again\n")
    if platform.system() == "Linux" or platform.system() == "Darwin":
        print("On Linux/MacOS systems, try 'chmod 777 output' while in the nbtconverterv2 directory")
    elif platform.system() == "Windows":
        print("On Windows systems, right-click on the output folder, then ")
    else:
        print("On Windows systems, right-click on the output folder, then ")
        print("On Linux/MacOS systems, try 'chmod 777 output' while in the nbtconverterv2 directory")




