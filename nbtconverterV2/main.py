import nbtlib
from nbtlib import *
from nbtlib.tag import *
from options import *

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

all_item_list = {
    "minecraft:stone": 1, 
    "minecraft:grass": 2, 
    "minecraft:dirt": 3, 
    "minecraft:cobblestone": 4,
    "minecraft:planks": 5,
    "minecraft:sapling": 6,
    "minecraft:bedrock": 7,
    "minecraft:sand": 12,
    "minecraft:gravel": 13,
    "minecraft:gold_ore": 14,
    "minecraft:iron_ore": 15,
    "minecraft:coal_ore": 16,
    "minecraft:log": 17,
    "minecraft:leaves": 18,
    "minecraft:sponge": 19,
    "minecraft:glass": 20,
    "minecraft:lapis_ore": 21,
    "minecraft:lapis_block": 22,
    "minecraft:dispenser": 23,
    "minecraft:sandstone": 24,
    "minecraft:noteblock": 25,
    "minecraft:powered_rail": 27,
    "minecraft:detector": 28,
    "minecraft:sticky_piston": 29,
    "minecraft:web": 30,
    "minecraft:tallgrass": 31,
    "minecraft:deadbush": 32,
    "minecraft:piston": 33,
    "minecraft:wool": 35,
    "minecraft:yellow_flower": 37,
    "minecraft:red_flower": 38,
    "minecraft:brown_mushroom": 39,
    "minecraft:red_mushroom": 40,
    "minecraft:gold_block": 41,
    "minecraft:iron_block": 42,
    "minecraft:stone_slab": 44,
    "minecraft:bricks": 45,
    "minecraft:tnt": 46,
    "minecraft:bookshelf": 47,
    "minecraft:mossy_cobblestone": 48,
    "minecraft:obsidian": 49,
    "minecraft:torch": 50,
    "minecraft:fire": 51,
    "minecraft:mob_spawner": 52,
    "minecraft:oak_stairs": 53,
    "minecraft:chest": 54,
    "minecraft:redstone_dust": 55,
    "minecraft:diamond_ore": 56,
    "minecraft:diamond_block": 57,
    "minecraft:crafting_table": 58,
    "minecraft:crops": 59,
    "minecraft:farmland": 60,
    "minecraft:furnace": 61,
    "minecraft:lit_furnace": 62,
    "minecraft:standing_sign": 63,
    "minecraft:ladder": 65,
    "minecraft:rail": 66,
    "minecraft:stone_stairs": 67,
    "minecraft:lever": 69,
    "minecraft:stone_pressure_plate": 70,
    "minecraft:wooden_pressure_plate": 72,
    "minecraft:redstone_ore": 73,
    "minecraft:redstone_torch": 76,
    "minecraft:stone_button": 77,
    "minecraft:snow_layer": 78,
    "minecraft:ice": 79,
    "minecraft:snow": 80,
    "minecraft:cactus": 81,
    "minecraft:clay": 82,
    "minecraft:jukebox": 84,
    "minecraft:fence": 85,
    "minecraft:pumpkin": 86,
    "minecraft:netherrack": 87,
    "minecraft:soul_sand": 88,
    "minecraft:glowstone": 89,
    "minecraft:portal": 90,
    "minecraft:trapdoor": 96,
    "minecraft:infested_stone": 97,
    "minecraft:stone_bricks": 98,
    "minecraft:mossy_stone_bricks": 98,
    "minecraft:cracked_stone_bricks": 98,
    "minecraft:chisled_stone_bricks": 98,
    "minecraft:brown_mushroom_block": 99,
    "minecraft:red_mushroom_block": 99,
    "minecraft:mushroom_stem": 100,
    "minecraft:iron_bars": 101,
    "minecraft:glass_pane": 102,
    "minecraft:melon": 103,
    "minecraft:vine": 106,
    "minecraft:fence_gate": 107,
    "minecraft:brick_stairs": 108,
    "minecraft:stone_brick_stairs": 109,
    "minecraft:mycelium": 110,
    "minecraft:lily_pad": 111,
    "minecraft:nether_bricks": 112,
    "minecraft:nether_brick_fence": 113,
    "minecraft:nether_brick_stairs": 114,
    "minecraft:enchantment_table": 116,
    "minecraft:end_portal": 119,
    "minecraft:end_portal_frame": 120,
    "minecraft:end_stone": 121,
    "minecraft:redstone_lamp": 122,
    "minecraft:oak_wood_slab": 126,
    "minecraft:sandstone_stairs": 128,
    "minecraft:emerald_ore": 129,
    "minecraft:ender_chest": 130,
    "minecraft:tripwire_hook": 131,
    "minecraft:emerald_block": 133,
    "minecraft:spruce_wood_stairs": 134,
    "minecraft:birch_wood_stairs": 135,
    "minecraft:jungle_wood_stairs": 136,
    "minecraft:command_block": 137,
    "minecraft:beacon": 138,
    "minecraft:cobblestone_wall": 139,
    "minecraft:mossy_cobblestone_wall": 139,
    "minecraft:button": 143,
    "minecraft:oak_button": 143,
    "minecraft:anvil": 145,
    "minecraft:iron_shovel": 256,
    "minecraft:iron_pickaxe": 257,
    "minecraft:iron_axe": 258,
    "minecraft:flint_and_steel": 259,
    "minecraft:apple": 260,
    "minecraft:bow": 261,
    "minecraft:arrow": 262,
    "minecraft:coal": 263,
    "minecraft:diamond": 264,
    "minecraft:iron_ingot": 265,
    "minecraft:gold_ingot": 266,
    "minecraft:iron_sword": 267,
    "minecraft:wooden_sword": 268,
    "minecraft:wooden_shovel": 269,
    "minecraft:wooden_pickaxe": 270,
    "minecraft:wooden_axe": 271,
    "minecraft:stone_sword": 272,
    "minecraft:stone_shovel": 273,
    "minecraft:stone_pickaxe": 274,
    "minecraft:stone_axe": 275,
    "minecraft:diamond_sword": 276,
    "minecraft:diamond_shovel": 277,
    "minecraft:diamond_pickaxe": 278,
    "minecraft:diamond_axe": 279,
    "minecraft:netherite_sword": 276,
    "minecraft:netherite_shovel": 277,
    "minecraft:netherite_pickaxe": 278,
    "minecraft:netherite_axe": 279,
    "minecraft:stick": 280,
    "minecraft:bowl": 281,
    "minecraft:mushroom_stew": 282,
    "minecraft:golden_sword": 283,
    "minecraft:golden_shovel": 284,
    "minecraft:golden_pickaxe": 285,
    "minecraft:golden_axe": 286,
    "minecraft:string": 287,
    "minecraft:feather": 288,
    "minecraft:gunpowder": 289,
    "minecraft:wooden_hoe": 290,
    "minecraft:stone_hoe": 291,
    "minecraft:iron_hoe": 292,
    "minecraft:diamond_hoe": 293,
    "minecraft:netherite_hoe": 293,
    "minecraft:golden_hoe": 294,
    "minecraft:wheat_seeds": 295,
    "minecraft:wheat": 296,
    "minecraft:bread": 297,
    "minecraft:leather_helmet": 298,
    "minecraft:leather_chestplate": 299,
    "minecraft:leather_leggings": 300,
    "minecraft:leather_boots": 301,
    "minecraft:chainmail_helmet": 302,
    "minecraft:chainmail_chestplate": 303,
    "minecraft:chainmail_leggings": 304,
    "minecraft:chainmail_boots": 305,
    "minecraft:iron_helmet": 306,
    "minecraft:iron_chestplate": 307,
    "minecraft:iron_leggings": 308,
    "minecraft:iron_boots": 309,
    "minecraft:diamond_helmet": 310,
    "minecraft:diamond_chestplate": 311,
    "minecraft:diamond_leggings": 312,
    "minecraft:diamond_boots": 313,
    "minecraft:netherite_helmet": 310,
    "minecraft:netherite_chestplate": 311,
    "minecraft:netherite_leggings": 312,
    "minecraft:netherite_boots": 313,
    "minecraft:netherite_helmet": 314,
    "minecraft:golden_chestplate": 315,
    "minecraft:golden_leggings": 316,
    "minecraft:golden_boots": 317,
    "minecraft:flint": 318,
    "minecraft:porkchop": 319,
    "minecraft:cooked_porkchop": 320,
    "minecraft:painting": 321,
    "minecraft:golden_apple": 322,
    "minecraft:sign": 323,
    "minecraft:wooden_door": 324,
    "minecraft:bucket": 325,
    "minecraft:water_bucket": 326,
    "minecraft:lava_bucket": 327,
    "minecraft:minecart": 328,
    "minecraft:saddle": 329,
    "minecraft:iron_door": 330,
    "minecraft:redstone": 331,
    "minecraft:snownball": 332,
    "minecraft:boat": 333,
    "minecraft:leather": 334,
    "minecraft:milk_bucket": 335,
    "minecraft:brick": 336,
    "minecraft:clay_ball": 337,
    "minecraft:reeds": 338,
    "minecraft:paper": 339,
    "minecraft:book": 340,
    "minecraft:slime_ball": 341,
    "minecraft:chest_minecart": 342,
    "minecraft:furnace_minecart": 343,
    "minecraft:egg": 344,
    "minecraft:compass": 345,
    "minecraft:fishing_rod": 346,
    "minecraft:clock": 347,
    "minecraft:glowstone_dust": 348,
    "minecraft:fish": 349,
    "minecraft:cooked_fish": 350,
    "minecraft:dye": 351,
    "minecraft:bone": 352,
    "minecraft:sugar": 353,
    "minecraft:cake": 354,
    "minecraft:bed": 355,
    "minecraft:repeater": 356,
    "minecraft:cookie": 356,
    "minecraft:filled_map": 358,
    "minecraft:shears": 359,
    "minecraft:melon_slice": 360,
    "minecraft:pumpkin_seeds": 361,
    "minecraft:melon_seeds": 362,
    "minecraft:raw_beef": 363,
    "minecraft:cooked_beef": 364,
    "minecraft:raw_chicken": 365,
    "minecraft:cooked_chicken": 366,
    "minecraft:rotten_flesh": 367,
    "minecraft:ender_pearl": 368,
    "minecraft:blaze_rod": 369,
    "minecraft:ghast_tear": 370,
    "minecraft:gold_nugget": 371,
    "minecraft:nether_wart": 372,
    "minecraft:potion": 373,
    "minecraft:splash_potion": 373,
    "minecraft:glass_bottle": 374,
    "minecraft:spider_eye": 375,
    "minecraft:fermented_spider_eye": 376,
    "minecraft:blaze_powder": 377,
    "minecraft:magma_cream": 378,
    "minecraft:brewing_stand": 379,
    "minecraft:cauldron": 380,
    "minecraft:eye_of_ender": 381,
    "minecraft:glistering_melon": 382,
    "minecraft:spawn_egg": 383,
    "minecraft:experience_bottle": 384,
    "minecraft:fire_charge": 385,
    "minecraft:writable_book": 386,
    "minecraft:written_book": 387,
    "minecraft:emerald": 388,
    "minecraft:item_frame": 389,
    "minecraft:flower_pot": 390,
    "minecraft:carrot": 391,
    "minecraft:potato": 392,
    "minecraft:baked_potato": 393,
    "minecraft:poisonous_potato": 394,
    "minecraft:map": 395,
    "minecraft:golden_carrot": 396,
    "minecraft:skull": 397,
    "minecraft:carrot_on_a_stick": 398,
    "minecraft:nether_star": 399,
    "minecraft:pumpkin_pie": 400,
    "minecraft:firework_rocket": 401,
    "minecraft:firework_charge": 402,
    "minecraft:enchanted_book": 403,
    "minecraft:record_13": 2256,
    "minecraft:record_cat": 2257,
    "minecraft:record_blocks": 2258,
    "minecraft:record_chirp": 2259,
    "minecraft:record_far": 2260,
    "minecraft:record_mall": 2261,
    "minecraft:record_mellohi": 2262,
    "minecraft:record_stal": 2263,
    "minecraft:record_strad": 2264,
    "minecraft:record_ward": 2265,
    "minecraft:record_11": 2266,
    "minecraft:record_wait": 2267,
    "minecraft:music_disc_13": 2256,
    "minecraft:music_disc_cat": 2257,
    "minecraft:music_disc_blocks": 2258,
    "minecraft:music_disc_chirp": 2259,
    "minecraft:music_disc_far": 2260,
    "minecraft:music_disc_mall": 2261,
    "minecraft:music_disc_mellohi": 2262,
    "minecraft:music_disc_stal": 2263,
    "minecraft:music_disc_strad": 2264,
    "minecraft:music_disc_ward": 2265,
    "minecraft:music_disc_11": 2266,
    "minecraft:music_disc_wait": 2267,
    }

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
    
}



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



