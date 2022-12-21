# This work done by group 1:
# Sulaiman A. Alomar, 202155890 , 100%. 
# Naif Alenizi, 202154090 , 100%. 


##starting the program##



def main(): #The main() function forms the base of this program since it gathers all the functions in the code and distributes them evenly.
    outputBox() #OutputBox() produces the table format for the students
    studentsData() #Prints out the all students data gathered from the 'data.txt' file
    flag = menuTable() #Boolean "flag" is assigned to menutable() function as a part of Input Validation
    if flag == 1: 
        addStudent() #addStudent() function is called by the user
        outputBox() #Table format for the students
        studentsData() #Prints out the final data of the students
    elif flag == 2:
        value1 = removeStudent() #removeStudent() function is called by the user
        if value1 == 100:  #dummy value to return from removeStudent() for quitting the program 'its value has no meaning for the program except to quit'
            print('Quitting the program')
        else:
            outputBox() #if the user did not exit the program, the table format and the students data will be printed
            studentsData()
    elif flag == 3:
        value2 = modifyStudentInfo() #assigning value to modifyStudentInfo() function as for future changes and quitting the program
        if value2 == 100:
            print('Quitting the program')
    elif flag == 4: 
        value3 = top10Students() #assigning value to top10Students() function as for future changes and quitting the program
    elif flag == 5:
        value4 = largestAbsences() #assigning value to largestAbsences() function as for future changes and quitting the program
    elif flag == 100:
        print('Quitting the program')
    else:
        print('Wrong input!')
        
    
    

def outputBox():  # the first function to create the front end and the format of how the data will be presented
    print('-' * 104)
    print('Current enrolled students')
    print('-' * 104)
    print('%5s %16s %22s %20s %18s %18s' % ('ID','NAME','ABSENCES','EXAM 1 GRADE','EXAM 2 GRADE','TOTAL MARKS'))
    print('-' * 104)
    
    
    
def menuTable(): # second function to give the user the choice of operations 
#first the function will print the munetable  
    print('-' * 104) 
    print('%25s' % '**User Menu**')   
    print('1 - Adding Students to the class') 
    print('2 - Removing students from the class')    
    print('3 - Modifying student information') 
    print('4 - Show the top 10 students')
    print('5 - Show the student with the largest absence')
    print()
#second the user will inter the number of the operation 
    userInput = input('Type the number that correspond to your desired operation or press ENTER KEY to quit: ')
    print('-' * 104) 
#third the function will return the number of the opreation based on the choice of the user
    if userInput == '':
        return 100
    elif userInput == '1':
        return 1
    elif userInput == '2':
        return 2
    elif userInput == '3':
        return 3
    elif userInput == '4':
        return 4
    elif userInput == '5':
        return 5
    else:
        return 1000
    

    
def studentsData(): #third function is used to read all data from the file
    infile = open('data.txt','r') #open the file to read 'Note that the data in the file are spreated by "," '
    readFile = infile.readline() #read the first line of the file
    while readFile != '': #create a loop in odrder to print all the data in the file
        readFile = readFile.rstrip() #first the loop will delet the last '\ln' in each line
        ID = readFile.split(',')[0] #split the data and store it in a list,second the loop will put ID equil to a fisrt argumnet of the list 
        name = readFile.split(',')[1]#split the data and store it in a list,second the loop will put ID equil to a zero argumnet of the list 
        absence = readFile.split(',')[2]#split the data and store it in a list,second the loop will put ID equil to a second argumnet of the list 
        exam1 = readFile.split(',')[3]#split the data and store it in a list,second the loop will put ID equil to a third argumnet of the list 
        exam2 = readFile.split(',')[4]#split the data and store it in a list,second the loop will put ID equil to a fourth argumnet of the list 
        total = readFile.split(',')[5]#split the data and store it in a list,second the loop will put ID equil to a fifth argumnet of the list 
        print('%5s %20s %10s %18s %18s %18s' % (ID,name,absence,exam1,exam2,total) ,end='\n') #print the data that was stored in a spicific arraged
        readFile = infile.readline() #read the second line and enter the loop again unless the line is empity


def addStudent(): # function to add a student to the data
    infile = open('data.txt','r') #first open the file to read
    outfile = open('data.txt','a') #second open the file to write but becase its 'a' then the writing will be in the end of the file 
    readFile = infile.readline() #read the first line 
    checkID =[] #cater a list to store all the IDs that are already in the file to not enter a double ID
    while readFile != '': # the loop to read each line untill the line is empity
        ID = readFile.split(',')[0]
        checkID.append(ID) # add all the IDs in the list
        readFile = infile.readline() # read the next line
    infolist = [] # create a lits to store the information of the new student
    while True : #loop to make sure that the ID is corecct
        addID = input('Enter the ID of the student :') # the new id
        if (len(addID) == 9) and (addID not in checkID) : #to check th id 
            infolist.append(addID) # to add the id to the list
            break #to get out of the loop 
        else: #in case if the user enter a worng id or duplicated one 
            print("You entered a wrong id or a duplicated id! please try again") #tell the user to try again 
    addName = input("Enter the name of the student: ") # to add the name of the student      
    infolist.append(addName) #to add the name in the list
    while True :#loop for checking the absences of the new student
        addAbsence = input('Enter the number of absences: ') #the number of absences
        if addAbsence.isdigit(): #in case of the student did not enter a number
            if int(addAbsence) > 36 : # becase the maximum hours is 36 so if the student get above that 
                print('You exceeded the course maximum hours! please try again')
            elif int(addAbsence) < 0: #absences cannot be negative
                print('You cannot have negative absences! please try again')
            else :
                if int(addAbsence) >= 0 and int(addAbsence) <= 36: #to check the validtiy of the number of absences 
                    infolist.append(addAbsence) # add the valid number of absences to the list 
                    break # to get out the loop 
        else: # in case the student did not enter a number or 
            print('Your input is invalid! please try again')
    while True: # loop to enter the degrre of the two exmas
        addExam1 = input("Enter the grade of the first exam (out of 50): ")  #the degree of the first exma
        if addExam1.isdigit(): # check if the dgree is a number
            if int(addExam1) > 50 or int(addExam1) < 0: #check if the degree is out of range
                print('Your input grade is out of range! please try again') #tell the user to try again 
            else: #if the dgeree is correct enter the else
                infolist.append(addExam1) #add the degree to the list
                break #get out of the loop 
        else: # if the degree was not a number enter the else
            print('You did not enter a valid grade! please try again')
    while True: # the same thing in the second degree
        addExam2 = input("Enter the grade of the second exam (out of 50): ") #the degree of the second exma
        if addExam2.isdigit() : #check if the dgree is a number
            if int(addExam2) > 50 or int(addExam2) < 0: #check if the degree is out of range
                print('Your input grade is out of range! please try again')
            else:
                infolist.append(addExam2) #add the degree to the list
                break #get out of the loop  
    
    addExam1 = int(addExam1) #make the degree as intger to add it to the second and find the total
    addExam2 = int(addExam2)          
    total = str(addExam1 + addExam2) #add the both to find the total 
    infolist.append(total) #add the total to the list
     
    i = 0   #number of iteration 
    outfile.write('\n') #write a new line 
    Final_List = '' #varble to add all argumnets in the list in 
    while i <= 5: # loop to add all arguments in the list in the varble
        Final_List = Final_List + infolist[i]+','
        i = i + 1
    outfile.write(Final_List[:len(Final_List)-1]) #write the varalbe in the file with out the last component which is , 
        
        
                
def removeStudent(): # function to remove the student
    inFile = open('data.txt','r') #read the data from the file
    line = inFile.readlines() #read the first line 
    listOfID = [] #list to store the the ids in the file
    position = ''  #empity varble to store the removed student in 
    updatedList = [] #list to save each line in it
    listofName = [] # list to save each name in it 
    listofshow = [] # list to save each name in it 
    listofirst = [] # list to save each name in it 
    stringnames = '' #varable to put all the names in it 
    emptyVariable = '' #to assign the id to it and then add it to the list
    finalString = '' #to puts the final data in 
    finalRecord = '' # to print the recored of the chosen 
    for i in line: # loop to read each line
        emptyVariable = i[:9] #assing the id to the varable
        listOfID.append(emptyVariable)        #add the id as a string in the list 
    for i in line : # loop to read each line 
        listofsplit = i.split(',') # assing a new varable as a list by spearating the data in the file 
        listofName.append(listofsplit[1])    #add the names to the list
    print('Remove the student by:\n1- ID\n2- Name')#print the opreation to the user 
    while True: #loop to give the user the chance to remove againg
        userInput = input('Type the number that correspond to your desired operation or press ENTER KEY to QUIT: ') #opreation number
        if userInput == '': #if press Enter 
            print('Quitting the program') 
            break #get out o the loop
        elif userInput == '1': # by pressing 1 the user will remove student by name
            userID = input('Please enter the student ID that you wish to remove: ') # enter the id
            if userID.isdigit() : # check if the id is a number
                if userID in listOfID: #check if the id is in the data
                        for i in line: # loop to put the data for each student in one argument of the list
                            updatedList.append(i)  
                        inFile.close()#close the file to avoid any crash         
                        for i in updatedList:#read each data sapreatly
                            if i[0:9] == userID: #if the id in the argemnt is the id enter
                                position = i # assign the varlbe to the whole information of the student
                                finalRecord = i.replace(',','             ') # repalce the , by spaces to arrange the format
                        print('Student record:')# print the table
                        print('-' * 120)
                        print('%5s %22s %25s %17s %15s %15s' % ('ID','NAME','ABSENCES','EXAM 1 GRADE','EXAM 2 GRADE','TOTAL MARKS'))
                        print('-' * 120)
                        print(finalRecord)# print the data of the student 
                        userInput=input('\nDo you wish to continue? (ENTER YES OR PRESS ENTER KEY TO QUIT):  ') #check if the uesr want to continue
                        if userInput.lower() == 'yes': #if yes enter
                            updatedList.remove(position)# to remove the data of the chosen student from the list of data 
                            print('STUDENT removed successfuly') 
                            for i in updatedList: #loop to wirte the new data 
                                finalString = finalString + i#puts the data in a string varable
                            modifiedData = open('data.txt','w') #to write the new list
                            modifiedData.write(finalString.rstrip('\n')) #delet the new line to avoid any errors
                            modifiedData.close() #close the file 
                            break #get out of the loop 
                        elif userInput == '':  #if user enter empity then print and then get out the loop
                            print('Quitting the program')
                            break
                        else: #if the input is wrong enter
                            print('Wrong input!')
                else: #if the id is not in the data enter
                    print('The given ID is not enrolled in the course! please try again')
            else: #if the id id wrong enter
                print('You did not enter a valid ID! please try again')  
                
                
                
                
        elif userInput == '2': # if opreating 2 enter
            print('\n')
            print('Before moving on, the instructor has the option to delete all students who have the same first name. If the instructor does not wish to remove all students who share the same first name, he can provide the student entire name, and it will be removed.')
            userInput1 = input('If you wish to proceed, Enter: Yes , or PRESS ENTER KEY TO QUIT: ') #to assure the user if wnat to proceed
            if userInput1 == '': #if blank entered then get out of the loop
                print('Quitting the operation')
                break
            elif userInput1.lower() == 'yes': # if yse enter get indaed
                userInput = input('Please enter the name that you wish to remove:  ') #ask for the fisrt name of the student
                for i in listofName : #to go around all names
                    stringnames = stringnames + i # assign the varalbe to all names added 
                if userInput in stringnames : #to check if the name entered in the data or not
                    for i in line : # to access each line
                        i.rstrip('\n') #delet the last line
                        updatedList.append(i) #add the data in the list
                    inFile.close()    #close the file
                    for i in updatedList : # go around the data
                        if userInput in i.split(',')[1]: #check if the id in the data list
                            listofshow.append(i) # then add it to a list to show it later
                    print('Student record:')
                    print('-' * 120)
                    print('%5s %22s %25s %17s %15s %15s' % ('ID','NAME','ABSENCES','EXAM 1 GRADE','EXAM 2 GRADE','TOTAL MARKS'))
                    print('-' * 120) # print the table to show the record of the student
                    for i in listofshow: 
                        finalRecord = i.replace(',','             ')
                        print(finalRecord) #print the record
                    userInput2=input('\nDo you wish to continue? (ENTER YES OR PRESS ENTER KEY TO QUIT) ') #check if he want to remove
                    if userInput2.lower() == 'yes': 
                        print('Any student with the given name has been removed successfuly')  
                        if userInput in i.split(',')[1]: #to make sure all names deleted
                                updatedList.remove(i)
                        for i in updatedList:
                            if userInput in i.split(',')[1]:
                                updatedList.remove(i) #to remove the data of the student from the list
                               
                        string = ''
                        for i in updatedList: #loop to assing the string varable to the data left
                            string = string + i   
                        outfile=open('data.txt','w') #open to write
                        outfile.write(string.rstrip('\n')) #write all the data
                        outfile.close()#close file           
                    elif userInput2=='' :
                        print('Quitting the program') #if enter press the program ends
                        break
                    else :
                        print('Wrong input!') 
                    
                else :
                    print('The given name is not enrolled in the course! please try again')
            else:
                print('Wrong input!')
                
                
                
                
                    
def modifyStudentInfo(): #function to modify the students data
    inFile = open('data.txt','r') # open to read the file
    line = inFile.readlines() #read each line 
    listOfID = [] #empity list to store the ides in 
    newID = '' #empty var to chacnge the new id 
    position = '' 
    updatedList = [] #list to store the data in 
    emptyVariable = '' #emptiy var to store the id in 
    studentName = ''
    finalString = ''
    for i in line: #loop the add all the id in the list
        emptyVariable = i[:9]
        listOfID.append(emptyVariable)  
    while True: 
        userInput = input('Enter the student ID or press ENTER KEY to quit: ') # users id
        if userInput == '': # if press enter get out of the function
            print('Quitting the program')
            break
        elif userInput.isdigit(): #if user input is valid enter
            if userInput in listOfID: # if the user input in the list of ides enter
                for i in line: #loop to store the data in a list
                    updatedList.append(i)  
                inFile.close()     #to avoid any crash   
                for i in listOfID: #loop to access all the ids
                    if i[:9] == userInput:
                        position = listOfID.index(i) #save index of the ids in a varble 
                for i in updatedList:  #loop to get the record of the student
                    if i[:9] == userInput:
                        finalRecord = i.replace(',','             ')
                studentName = line[position] # assign a varable to index in each line in the file
                print('Student record:') # print the table
                print('-' * 120)
                print('%5s %22s %25s %17s %15s %15s' % ('ID','NAME','ABSENCES','EXAM 1 GRADE','EXAM 2 GRADE','TOTAL MARKS'))
                print('-' * 120)
                print(finalRecord) #print the recored of the chosen student
                print('\nChoose which data do you want to update for the student')
                print('1-ID\n2-NAME\n3-ABSENCES\n4-EXAM1\n5-EXAM2') # to choose the type of opreation
                userInput = input(': ')
                if userInput == '1': #if the user chose 1 then the if statment will ask for a new id 
                    newID = input('Please enter the new ID: ')
                    if len(newID) == 9 and newID.isdigit() and newID not in listOfID: #check the new id
                        line[position] = newID + studentName[9:] #change the past id to the new
                        print('ID UPDATED SUCCESSFULY')
                        for i in line: #loop to write the data with the new id
                            finalString = finalString + i
                            modifiedData = open('data.txt','w') #open file to write
                            modifiedData.write(finalString.rstrip('\n')) 
                            modifiedData.close() #close file
                    else:
                        print('This ID is already assigned to another student!')
                elif userInput == '2': #if the user enter 2 then the if will change the name
                    newName = input('Please enter the new NAME: ') 
                    if newName.replace(' ','').isalpha(): #check if the name is all alpha bet
                        #chaneg the name by addign the same data but not adding the past name just the new name 
                        line[position] = studentName[:9] + ',' + newName + ',' + studentName.split(',')[2] + ',' + studentName.split(',')[3] + ',' + studentName.split(',')[4] + ',' + studentName.split(',')[5]
                        print('NAME UPDATED SUCCESSFULY')
                        for i in line: #loop to write the new data inside the file
                            finalString = finalString + i
                            modifiedData = open('data.txt','w')
                            modifiedData.write(finalString.rstrip('\n'))
                            modifiedData.close()
                elif userInput == '3': # if statment to change the absences 
                    newAbsence = input('Please enter the new ABSENCES: ')
                    if newAbsence.isdigit() == True and int(newAbsence) >=0 and int(newAbsence) <= 36: #check if the new absences is valid
                    #add the new absences to the same old data 
                        line[position] = studentName[:9] + ',' + studentName.split(',')[1] + ',' + newAbsence + ',' + studentName.split(',')[3] + ',' + studentName.split(',')[4] + ',' + studentName.split(',')[5]
                        print('ABSENCE UPDATED SUCCESSFULY')
                        for i in line: #loop to write the new data 
                            finalString = finalString + i
                            modifiedData = open('data.txt','w')
                            modifiedData.write(finalString.rstrip('\n'))
                            modifiedData.close() 
                    else: #will wnter if new absences not correct
                        print('Incorrect number of absences!')
                elif userInput == '4': #if statment to cahnge the fisrt exam degree
                    newEXAM1 = input('Please enter the new EXAM1: ') #new degree
                    if newEXAM1.isdigit() == True and int(newEXAM1) >=0 and int(newEXAM1) <=50: #check if the new degree is right
                        #make the line as the same as the old but remove the old degree and add the new
                        line[position] = studentName[:9] + ',' + studentName.split(',')[1] + ',' + studentName.split(',')[2] + ',' + newEXAM1 + ',' + studentName.split(',')[4] + ',' + str(int(newEXAM1) + int(studentName.split(',')[4]))
                        print('EXAM1 UPDATED SUCCESSFULY')
                        for i in line: #loop to write the new data
                            finalString = finalString + i
                            modifiedData = open('data.txt','w')
                            modifiedData.write(finalString.rstrip('\n'))
                            modifiedData.close() 
                    else:
                        print('The given grade is out of range! please try again') 
                elif userInput == '5': #if statment to the second degree 
                    newEXAM2 = input('Please enter the new EXAM2: ')#new degree 
                    if newEXAM2.isdigit() == True and int(newEXAM2) >=0 and int(newEXAM2) <=50: #check if the new degree is right
                        #make the line as the same as the old but remove the old degree and add the new
                        line[position] = studentName[:9] + ',' + studentName.split(',')[1] + ',' + studentName.split(',')[2] +',' + studentName.split(',')[3] +','+newEXAM2 + ',' + str(int(newEXAM2) + int(studentName.split(',')[3]))
                        print('EXAM2 UPDATED SUCCESSFULY')
                        for i in line: #loop to write the new data
                            finalString = finalString + i
                            modifiedData = open('data.txt','w')
                            modifiedData.write(finalString.rstrip('\n'))
                            modifiedData.close() 
                    else:
                        print('The given grade is out of range! please try again')
                else:
                    print('Wrong input!')
            else:
                    print('The given ID is not enrolled in the course! please try again')
        else:
            print('You did not enter a valid ID! please try again')
        
        
def top10Students(): #function to show the top 10 student
    inFile = open('data.txt','r') #read the file
    line = inFile.readlines() #read each line
    listOfTotalMark = [] #list to store all the total marks of the student
    listOfString = [] #list to convert the total matks to string
    updatedList = [] #list to store the data
    lastVersionList = [] # list to put the data as top 10 
    finalString = '' #emptiy varble
    for i in line: #loop to store the names and the total marks only in the list
        toSplit = i.split(',')
        toAdd= toSplit[1]+' '+toSplit[5] 
        toDelete = toAdd.rstrip('\n')
        updatedList.append(toDelete) 
    for i in updatedList: #loop to store the total marks only as an inter in the list
        i = i.split(' ')
        INTEGER = int(i[2])
        listOfTotalMark.append(INTEGER)
    
    listOfTotalMark.sort(reverse=True)   #to sort the list form bigger to lower 
    for i in listOfTotalMark: # loop to add the sorted list as an string in a new list
        listOfString.append(str(i))
    print('-'*45) #print a table
    print('%14s %30s' % ('Name','Total Mark'))
    print('-'*45)
    for i in updatedList: # loop to arrange the names and the total marks in a shape to aplly to the table
        listOfSpace = i.split(' ')
        finalString = '%20s %20s' % (listOfSpace[0] + ' ' + listOfSpace[1],listOfSpace[2])
        lastVersionList.append(finalString)
    stop = 0
    for i in listOfString: #loop print the names and the marks based on the top to the least
        if stop == 11:
            break # when reach to the 11 student get out 
        for n in lastVersionList:
            if i in n :
                print(n)
                lastVersionList.remove(n)
        stop = stop + 1    
                
def largestAbsences(): #function to show the lagest absences 
    inFile = open('data.txt','r') #open the file to read
    line = inFile.readlines() #read each line
    updatedlist=[] #list to store the data in
    listofabs = [] #list to store the abseneces in 
    listofstring = [] #list to store the absences as string
    for i in line : #loop to store all lines in the list
        i = i.rstrip() #to delet the lats line
        updatedlist.append(i)
    for i in updatedlist: #loop the store all the absences in a list
        i = i.split(',')
        i = int(i[2])
        listofabs.append(i)
    listofabs.sort(reverse=True) #sort the absences
    for i in listofabs: #loop to convert the absences to srting
        i = str(i)
        listofstring.append(i)
    print('-' * 120) #table
    print('%5s %22s %25s %17s %17s %19s' % ('ID','NAME','ABSENCES','EXAM 1 GRADE','EXAM 2 GRADE','TOTAL MARKS'))
    print('-' * 120)    
    for n in updatedlist: #loop to pring the recored of the students who has the large abscenes
        absences = n.split(',')
        if listofstring[0] in absences[2]:
            finalRecord = n.replace(',','             ')
            print(finalRecord)
                    

            
            
                    
                
            
main() #call the main
    
    

