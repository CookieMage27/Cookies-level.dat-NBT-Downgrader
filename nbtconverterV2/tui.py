import argparse


# # INITIALISER - takes file arguments and processes them
# parser = argparse.ArgumentParser(description="Takes a level.dat input file and asks details on what to do with it, then passes the information on to main.py.")
# parser.add_argument("inputFile", type = str, help = "A Minecraft level.dat file (1.21.11 or older), to be downgraded")
# input=parser.parse_args()

# print(input) #only required for debug - feel free to comment out

testdata = ["1", "y"]
#function definitons 
def queryOptions():
	versionUserInput = input("Which version would you like to convert to?\n12w49a -> 1\nBeta 1.7.3 -> 2\n?) ")
	enchantmentNamespacesUserInput = input("Are you converting from a version that uses enchantment namespaces(1.20.5+)?\ny/n?) ")
	return [str(versionUserInput), enchantmentNamespacesUserInput]

def validateInput(dataInput):
	if type(dataInput) != list:
		print("Invalid data type. If you're seeing this, the code is probably broken. Please open a GitHub issue ASAP.")
		return False
	version = dataInput[0]
	enchantNamespace = dataInput[1]
	if version != "1" and version != "2":
		print("Invalid version. Please try again:")
		queryOptions()
		return False

	if enchantNamespace.lower() != "y" and enchantNamespace.lower() != "n":
		print("Invalid enchantment namespace. Please answer y or n. Try again:")
		queryOptions()
		return False

	else:
		return True


if __name__ == "__main__":
	userInput = queryOptions()
	print(validateInput(userInput))