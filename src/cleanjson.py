import io, json, sys, os
from helper import clean
import random

folderpath = sys.argv[1] # folder path argument comes first
outputname = sys.argv[2] # then it's the output file name (add the prefix, like .txt)

dirs = os.listdir(folderpath) #this is only the names of the files though. will be accounted for later
outputf = io.open(outputname, mode = 'w',  encoding="utf-8") #the output file
messageArray = []
for onefile in dirs: #cycle through the files
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
                messageArray.append(cleanedString) #put them all into a chonky array
print("Cleaning done.") #because cleaning takes a long time and checking the output file is just giving in to paranoia


random.shuffle(messageArray) #randomization time
print("Shuffling done.")

for i in range(len(messageArray)):
    outputf.write(messageArray[i]) #file writing time
print("Writing done.") #just for the formality
outputf.close()