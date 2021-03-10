import io, json, sys, os
from helper import clean

folderpath = sys.argv[1] # folder path argument comes first
outputname = sys.argv[2] # then it's the output file name (add the prefix, like .txt)

dirs = os.listdir(folderpath)
outputf = io.open(outputname, mode = 'w',  encoding="utf-8") #the output file

for onefile in dirs:
    whole_file = json.load(io.open(folderpath + "/" + onefile, mode="r", encoding="utf-8")) #load that json file

    for message in whole_file["messages"]: #json is a dict now. we only want the things from the "messages" portion
        id = message["author"]["id"]
        name = message["author"]["name"]
        content = message["content"]
        cleanedName = clean(name, author=id) # the cleaning of the name and message needs to be done separately
        cleanedContent = clean(content)
        if (cleanedName != None) and (cleanedContent != None) and (len(cleanedContent.split()) > 10):
            cleanedString = cleanedName + "\t" + cleanedContent + "\n" #but then you have to put it back together anyways
            outputf.write(cleanedString)

outputf.close()