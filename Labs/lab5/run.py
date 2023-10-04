import os
import subprocess

#Nicolas Van der Werf

def runCommands(qNumber,givenName,type,lengths,eth):
    commands = [["python", "name_search.py", "-algorithm", type, "-name", eth, "-length", str(length)] for length in
                lengths]
    results = []
    names = []
    for command in commands:
        results.append(subprocess.run(command, text=True, stdout=subprocess.PIPE))
    for result in results:
        if result.returncode != 0:
            print(f"The command failed with error code {result.returncode}")
            print(result.stderr)
            return "Error on Question: " +str(qNumber) +": " + result.stderr
        else: names.append(result.stdout.strip())

    question = "Question "+str(qNumber)+" "+type+": What is this "+eth+" person's full name?\n"
    if eth == "Mexican":
        question += givenName + " " + names[0] + " " + names[1] + "\n\n"
    elif eth == "Chinese":
        question += names[0] + " " + givenName + "\n\n"
    elif eth == "Arabic":
        question += givenName + " " + names[0] + " " + names[1] + "\n\n"
    return question


with open('result.txt', 'w') as file_handler:

    file_handler.write(runCommands(1,"Andres Manuel","BruteForce",[5,8],"Mexican"))
    file_handler.write(runCommands(2,"Tianyi","BruteForce",[5],"Chinese"))
    file_handler.write(runCommands(3, "Harun", "BruteForce", [7,8], "Arabic"))

    file_handler.write("\n\n")

    file_handler.write(runCommands(1, "Andres Manuel", "Horspool", [5, 8], "Mexican"))
    file_handler.write(runCommands(2, "Tianyi", "Horspool", [5], "Chinese"))
    file_handler.write(runCommands(3, "Harun", "Horspool", [7, 8], "Arabic"))


