import io, json, sys, os, random
from helper import clean
from helper import extract_fields
from tqdm import tqdm

folderpath = sys.argv[1] # folder path argument comes first
outputname = sys.argv[2] # then it's the output file name (add the prefix, like .txt)

dirs = os.listdir(folderpath) #this is only the names of the files though. will be accounted for later
outputf = io.open(outputname, mode = 'w',  encoding="utf-8") #the output file
messageArray = []
newLine = []
for onefile in tqdm(dirs, desc= "Cleaning"): #cycle through the files
    whole_file = json.load(io.open(folderpath + "/" + onefile, mode="r", encoding="utf-8")) #load that json file (directory kinda hardcoded accounted for)

    for message in whole_file["messages"]: #json is a dict now. we only want the things from the "messages" portion
        if message["author"]["isBot"] == False: #gotta get rid of those bots
            id = message["author"]["id"]
            name = message["author"]["name"]
            #print(name)
            content = message["content"]
            cleanedName = clean(name, author=id) # the cleaning of the name and message needs to be done separately
            #print(cleanedName)
            cleanedContent = clean(content)
            if (cleanedName != None) and (cleanedContent != None) and (len(cleanedContent.split()) > 10):
                cleanedString = cleanedName + "\t" + cleanedContent + "\n" #but then you have to put it back together anyways
                #outputf.write(cleanedString)
                #print(cleanedString)
                messageArray.append(cleanedString) #put them all into a chonky array


for i in tqdm(range(len(messageArray)), desc="Extracting fields"):
    newString = messageArray[i].replace('\\n','\n')
    for val in (extract_fields(newString)):
        outputf.write(val)
    '''
messageArray.extend(newLine) #a Heckin' Chonker of an array

random.shuffle(messageArray) #randomization time
print("Shuffling done.")

for i in tqdm(range(len(messageArray)), desc="Writing"):
    outputf.write(messageArray[i]) #file writing time
outputf.close()
'''