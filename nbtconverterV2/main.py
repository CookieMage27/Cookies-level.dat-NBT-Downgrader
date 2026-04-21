import nbtlib
from nbtlib import *
from nbtlib.tag import *
from options import *
from item_list import all_item_list
new_level_dat = nbtlib.load("input/level.dat")




if (set_to_12w49a == True):
    option = "12w49a"
else:
    option = "Beta 1.7.3"


if (item_namespace == False):
    enchant_namespace = False


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


if(enchant_namespace):
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:overworld"):
        dimension = 0
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:nether"):
        dimension = -1
    if(new_level_dat['Data']['Player']['Dimension'] == "minecraft:the_end"):
        dimension = 1
else:
    dimension = int(new_level_dat['Data']['Player']['Dimension'])


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


ec_converted_items = []
ec_enchantment_list = []

for ec_item in range(len(new_level_dat['Data']['Player']['EnderItems'])):
    ec_slot = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Slot'])
    ec_enchantment_list = []
    ec_found_item = 0
    ec_damage = 0
    if(item_namespace):
        for key, value in all_item_list.items():
            #print(key)
            #print(value)
            if new_level_dat['Data']['Player']['EnderItems'][ec_item]['id'] == key:
                ec_found_item = value
                break
            else:
                ec_found_item = 0
    else:
        ec_found_item = new_level_dat['Data']['Player']['EnderItems'][ec_item]['id']

    try:
        ec_count = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Count'])
    except KeyError:
        ec_count = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['count'])
    
    try:
        ec_damage = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['Damage'])
    except KeyError:
        try:
            ec_damage = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:damage'])
        except KeyError:
            pass
    
        

    
    if(option == "12w49a"):
        if ('components' in list(new_level_dat['Data']['Player']['EnderItems'][ec_item].keys()) or 'tag' in list(new_level_dat['Data']['Player']['EnderItems'][ec_item].keys())):


            if(enchant_namespace):
                ##its dificult to do it with items with enchanted namespaces ill add later
                if(ec_found_item == 403):
                    for ec_enchant in range(len(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:stored_enchantments'])):
                        for key, value in all_enchants_list.items():
                            if list(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:stored_enchantments'].keys())[ec_enchant] == key:
                                ec_enchantment_lvl = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:stored_enchantments'][f'{key}'])
                                ec_enchantment_id = value
                                ec_enchantment_list.append({
                                    "lvl": ec_enchantment_lvl,
                                    "id": ec_enchantment_id,
                                })
                                break
                    #this is the item data for an enchanted book thats converted from a namespace
                    ec_converted_items.append({
                        "Count": ec_count,
                        "Slot": ec_slot,
                        "Damage": ec_damage,
                        "id": ec_found_item,
                        "tag": {
                            "StoredEnchantments": ec_enchantment_list
                            #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                        }
                    })
                if(ec_found_item != 403):
                    for ec_enchant in range(len(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:enchantments'])):
                        print("worked")
                        for key, value in all_enchants_list.items():
                            if list(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:enchantments'].keys())[ec_enchant] == key:
                                ec_enchantment_lvl = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:enchantments'][f'{key}'])
                                ec_enchantment_id = value
                                ec_enchantment_list.append({
                                    "lvl": ec_enchantment_lvl,
                                    "id": ec_enchantment_id,
                                })
                                break
                    ec_repaircost = new_level_dat['Data']['Player']['EnderItems'][ec_item]['components']['minecraft:repair_cost']
                    ec_converted_items.append({
                        "Count": ec_count,
                        "Slot": ec_slot,
                        "Damage": ec_damage,
                        "id": ec_found_item,
                        "tag": {
                            "ench": ec_enchantment_list,
                            #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                            "RepairCost": ec_repaircost,
                        }
                    })     
            else: 
                #if the converted version doesnt have enchantment namespaces
                if(ec_found_item == 403):
                    for ec_enchant in range(len(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['StoredEnchantments'])):
                        
                        ec_enchantment_lvl = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['StoredEnchantments'][ec_enchant]['lvl'])
                        ec_enchantment_id = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['StoredEnchantments'][ec_enchant]['id'])
                        ec_enchantment_list.append({
                            "lvl": ec_enchantment_lvl,
                            "id": ec_enchantment_id,
                        })
                    #this is the item data for an enchanted book with the old id system
                    ec_converted_items.append({
                        "Count": ec_count,
                        "Slot": ec_slot,
                        "Damage": ec_damage,
                        "id": ec_found_item,
                        "tag": {
                            "StoredEnchantments": ec_enchantment_list
                            #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                        }
                    })
                if(ec_found_item != 403):
                    for ec_enchant in range(len(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['ench'])):

                        ec_enchantment_lvl = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['ench'][ec_enchant]['lvl'])
                        ec_enchantment_id = int(new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['ench'][ec_enchant]['id'])
                        ec_enchantment_list.append({
                            "lvl": ec_enchantment_lvl,
                            "id": ec_enchantment_id,
                        })
                    ec_repaircost = new_level_dat['Data']['Player']['EnderItems'][ec_item]['tag']['RepairCost']
                    
                    #this is the item data for a random enchanted item with the old id system
                    ec_converted_items.append({
                        "Count": ec_count,
                        "Slot": ec_slot,
                        "Damage": ec_damage,
                        "id": ec_found_item,
                        "tag": {
                            "ench": ec_enchantment_list,
                            #[{"lvl": enchantment_lvl,"id": enchantment_id,}]
                            "RepairCost": ec_repaircost,
                        }
                    }) 
        else:
            #if tag doesnt exist
            ec_converted_items.append({
                "Count": ec_count,
                "Slot": ec_slot,
                "Damage": ec_damage,
                "id": ec_found_item,
            })
    
    else:
        #if isnt 12w49a(same as tag not existing)
        ec_converted_items.append({
            "Count": ec_count,
            "Slot": ec_slot,
            "Damage": ec_damage,
            "id": ec_found_item,
        })












converted_items = []
enchantment_list = []

for item in range(len(new_level_dat['Data']['Player']['Inventory'])):
    slot = int(new_level_dat['Data']['Player']['Inventory'][item]['Slot'])
    enchantment_list = []
    found_item = 0
    damage = 0
    if(item_namespace):
        for key, value in all_item_list.items():
            #print(key)
            #print(value)
            if new_level_dat['Data']['Player']['Inventory'][item]['id'] == key:
                found_item = value
                break
            else:
                found_item = 0
    else:
        found_item = new_level_dat['Data']['Player']['Inventory'][item]['id']

    try:
        count = int(new_level_dat['Data']['Player']['Inventory'][item]['Count'])
    except KeyError:
        count = int(new_level_dat['Data']['Player']['Inventory'][item]['count'])
    
    try:
        damage = int(new_level_dat['Data']['Player']['Inventory'][item]['Damage'])
    except KeyError:
        try:
            damage = int(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:damage'])
        except KeyError:
            pass
    
        

    
    if(option == "12w49a"):
        if ('components' in list(new_level_dat['Data']['Player']['Inventory'][item].keys()) or 'tag' in list(new_level_dat['Data']['Player']['Inventory'][item].keys())):


            if(enchant_namespace):
                ##its dificult to do it with items with enchanted namespaces ill add later
                if(found_item == 403):
                    for enchant in range(len(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:stored_enchantments'])):
                        for key, value in all_enchants_list.items():
                            if list(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:stored_enchantments'].keys())[enchant] == key:
                                enchantment_lvl = int(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:stored_enchantments'][f'{key}'])
                                enchantment_id = value
                                enchantment_list.append({
                                    "lvl": enchantment_lvl,
                                    "id": enchantment_id,
                                })
                                break
                    #this is the item data for an enchanted book thats converted from a namespace
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
                if(found_item != 403):
                    for enchant in range(len(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:enchantments'])):
                        print("worked")
                        for key, value in all_enchants_list.items():
                            if list(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:enchantments'].keys())[enchant] == key:
                                enchantment_lvl = int(new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:enchantments'][f'{key}'])
                                enchantment_id = value
                                enchantment_list.append({
                                    "lvl": enchantment_lvl,
                                    "id": enchantment_id,
                                })
                                break
                    repaircost = new_level_dat['Data']['Player']['Inventory'][item]['components']['minecraft:repair_cost']
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
            else: 
                #if the converted version doesnt have enchantment namespaces
                if(found_item == 403):
                    for enchant in range(len(new_level_dat['Data']['Player']['Inventory'][item]['tag']['StoredEnchantments'])):
                        
                        enchantment_lvl = int(new_level_dat['Data']['Player']['Inventory'][item]['tag']['StoredEnchantments'][enchant]['lvl'])
                        enchantment_id = int(new_level_dat['Data']['Player']['Inventory'][item]['tag']['StoredEnchantments'][enchant]['id'])
                        enchantment_list.append({
                            "lvl": enchantment_lvl,
                            "id": enchantment_id,
                        })
                    #this is the item data for an enchanted book with the old id system
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
                if(found_item != 403):
                    for enchant in range(len(new_level_dat['Data']['Player']['Inventory'][item]['tag']['ench'])):

                        enchantment_lvl = int(new_level_dat['Data']['Player']['Inventory'][item]['tag']['ench'][enchant]['lvl'])
                        enchantment_id = int(new_level_dat['Data']['Player']['Inventory'][item]['tag']['ench'][enchant]['id'])
                        enchantment_list.append({
                            "lvl": enchantment_lvl,
                            "id": enchantment_id,
                        })
                    repaircost = new_level_dat['Data']['Player']['Inventory'][item]['tag']['RepairCost']
                    
                    #this is the item data for a random enchanted item with the old id system
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
            "EnderItems": [],
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
        "GameType": playerGameType,
        "generatorVersion": 1,
        "MapFeatures": 1,
        "version": 19133,
        "generatorOptions": "",
        "LastPlayed": last_played,
        "DayTime": daytime,
        "LevelName": level_name,
        "initialized": 1,
        "allowCommands": 0,
        "SizeOnDisk": sod
    })

root = Compound({
    'Data': converted_data
})

nbt_file = File(root)
nbt_file.save("output/level.dat", gzipped=True)



