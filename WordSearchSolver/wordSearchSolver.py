####    Author: Po Liu
####    Created: November 14, 2012


from array import *

f = open('temp.txt', 'r')
#print f
text = f.read()
print "Grrrrr! I am a word search crusher"
print "This is what I will search through: "
print "-------------------------------------"
print text
print "-------------------------------------"
print "Let's do this!"

inputText = [ ]
inputLine = []
i = 0

with open('temp.txt', 'r') as f:
    for line in f:
        inputLine = []
        for ch in line.rstrip():
            inputLine.append(ch)

        i = i + 1
        inputText.append(inputLine)
        

#print inputText

interestedWord = raw_input("Please enter the word to search for: ")
sizeX = len(inputLine)
sizeY = len(inputText)
wordSize = len(interestedWord)

#First two loops go over the entire block of text looking for a character match
for i in range(0, sizeY):
    for j in range(0, sizeX):

        #If first letter of word of interest mataches a char, then execute search around algorithm
        if (inputText[i][j] == interestedWord[0]):

            direction = -1

            # These variables become true if the word is found in the direction indicated
            upResults = False
            downResults = False
            leftResults = False
            rightResults = False
            diagULResults = False
            diagURResults = False
            diagDLResults = False
            diagDRResults = False

            continueLoopU = True
            continueLoopD = True
            continueLoopL = True
            continueLoopR = True
            continueLoopUR = True
            continueLoopUL = True
            continueLoopDL = True
            continueLoopDR = True
            u = 0

            upResults = False
            downResults = False
            leftResults = False
            rightResults = False
            diagULResults = False
            diagURResults = False
            diagDLResults = False
            diagDRResults = False

            # Main loop that looks around a matched first character and returns a true boolean if word is found
            while True:
                
                #Looking up
                if (i-u >= 0 and continueLoopU == True):
                    if (inputText[i-u][j] == interestedWord[u] ):

                        upResults = True
                    else:
                        continueLoopU = False
                        upResults = False

                else:
                    continueLoopU = False
                    upResults = False


                #Looking down
                if (i+u < sizeY and continueLoopD == True):
                    if (inputText[i+u][j] == interestedWord[u]):
                        downResults = True
                    else:
                        continueLoopD = False
                        downResults = False

                else:
                    continueLoopD = False
                    downResults = False

                #Looking Left
                if (j-u >= 0 and continueLoopL == True):
                    if (inputText[i][j-u] == interestedWord[u]):
                        leftResults = True
                    else:
                        continueLoopL = False
                        leftResults = False

                else:
                    continueLoopL = False
                    leftResults = False

                #Looking Right
                if (j+u < sizeX and continueLoopR == True):
                    if (inputText[i][j+u] == interestedWord[u]):
                        rightResults = True
                    else:
                        continueLoopR = False
                        rightResults = False
                else:
                    continueLoopR = False
                    rightResults = False


                #Looking UpLeft
                if (i-u >= 0 and j-u >= 0 and continueLoopUL == True):
                    if (inputText[i-u][j-u] == interestedWord[u]):
                        diagULResults = True
                        #print 1

                    else:
                        continueLoopUL = False
                        diagULResults = False
                        #print 2
                else:
                    #print 3
                    continueLoopUL = False
                    diagULResults = False
                
                #Looking UpRight
                if (i-u >= 0  and j+u < sizeX and continueLoopUR == True):
                    if (inputText[i-u][j+u] == interestedWord[u]):

                        diagURResults = True
                    else:
                        continueLoopUR = False
                        diagURResults = False
                else:
                    continueLoopUR = False
                    diagURResults = False

                
                #Looking DownLeft
                if (i-u >= 0 and j-u >= 0  and continueLoopDL == True):
                    if (inputText[i-u][j-u] == interestedWord[u]):
                        diagULResults = True
                    else:
                        continueLoopDL = False
                        diagULResults = False
                else:
                    continueLoopDL = False
                    diagULResults = False

                
                #Looking DownRight
                if (i+u < sizeY  and j+u < sizeX and continueLoopDR == True):
                    if (inputText[i+u][j+u] == interestedWord[u]):
                        diagDRResults = True
                    else:
                        continueLoopDR = False
                        diagDRResults = False
                else:
                    continueLoopDR = False
                    diagDRResults = False


                # Increment the u to move through the length of the word of interst
                u = u + 1
                

                
                #Fail condition for while loop
                if ((continueLoopU == False and continueLoopR == False and continueLoopD == False and continueLoopL == False
                     and continueLoopUL == False and continueLoopUR == False and continueLoopDL == False and continueLoopDR == False)):
                    break
                
                if (u >= wordSize):
                    break
                        
                


            if (upResults):
                direction = 1
            if (downResults):
                direction = 6
            if (leftResults):
                direction = 3
            if (rightResults):
                direction = 4
            if (diagULResults):
                direction = 0
            if (diagURResults):
                direction = 2
            if (diagDLResults):
                direction = 5
            if (diagDRResults):
                direction = 7


            #  If the word was found (no order specified)...
            if (upResults == True or downResults==True or leftResults==True or
                rightResults==True or diagULResults==True or diagDLResults==True or diagURResults==True or diagDRResults==True):

                print "-----------------"
                print "Found word at position"
                print "Row: ", i+1
                print "Col: ", j+1

                if (upResults == True):
                    print "Look up"
                if (downResults == True):
                    print "Look down"
                if (leftResults == True):
                    print "Look left"
                if (rightResults == True):
                    print "Look right"
                if (diagULResults == True):
                    print "Look diagonally up left"
                if (diagURResults == True):
                    print "Look diagonally up right"
                if (diagDLResults == True):
                    print "Look diagonally down left"
                if (diagDRResults == True):
                    print "Look diagonally down right"



raw_input("Press ENTER to close the window...")





	    
