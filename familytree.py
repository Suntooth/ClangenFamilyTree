import json

def findParents(current):
    if current["parent1"]:
        p1 = "m" + current["parent1"] + "\u0009"
    else:
        p1 = ""
    
    if current["parent2"]:
        p2 = "f" + current["parent2"]
    else:
        p2 = ""
    
    return p1, p2


def findDead(current):
    # clan guides don't have the "member" flag for starclan. for some reason
    if "clan_guide" in current["backstory"]:
        return "z1"
    
    standingHistory = current["status"]["standing_history"]
    
    for group in standingHistory:
        if group["group"] == "2" and "member" in group["standing"]:
            return "z1"
        elif group["group"] == "3" and "member" in group["standing"]:
            return "z1"
        elif group["group"] == "4" and "member" in group["standing"]:
            return "z1"
    
    # the only way to get here is if the cat is alive, so just return "no they're not dead"
    return "z0"


def catInfo(current):
    ID = "i" + current["ID"] + "\u0009"
    name = "p" + (current["name_prefix"] + current["name_suffix"]).replace(" ", "") + "\u0009"
    
    parent1, parent2 = findParents(current)
    isDead = findDead(current)
        
    toWrite = ID + name + parent1 + parent2 + "\n"
    treeFile.write(toWrite)


def mateInfo(current):
    if current["mate"]:
        for cMate in current["mate"]:
            toWrite = "p" + current["ID"] + "\u0009" + cMate + "\u0009" + "e1\n"
            treeFile.write(toWrite)
            
    if current["previous_mates"]:
        for pMate in current["previous_mates"]:
            toWrite = "p" + current["ID"] + "\u0009" + pMate + "\u0009" + "e0\n"
            treeFile.write(toWrite)


path = input("Path to your save: ")
filename = path.split("/")[-2] + "_familytree.txt"
path = path + "clan_cats.json"

with open(path, "r") as catsFile:
    catsData = json.load(catsFile)

with open(filename, "w") as treeFile:
    for cat in catsData:
        # adding to the tree
        catInfo(cat)
        
        # adding the mate relationships
        mateInfo(cat)
        
print("Done.")