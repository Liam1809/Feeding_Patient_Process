import csv
# list of patients
Patient_list = list()
# patient number
Patient_Number = ["A1", "A2", "A3", "B1", "B2", "B3", "B4", "B5", "B6", "B7"]

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Class PATIENT for each patient object
class PATIENT:
    # declare global variables
    global Name, Type, GRV_Patient, Weight, score
    # __init__ method that allows each patient to have a Feeding, GRV, Issue, FIVEDAYS tables
    def __init__(self):
        self.Feeding = [[0] * 24 for i in range(6)]
        self.GRV = [[0] * 24 for i in range(6)]
        self.Issue = [[0] * 24 for i in range(6)]
        self.FIVEDAYS = [[0] * 24 for i in range(6)]
    # get/set for patient's score  
    def getscore(self):
        return self.rankscore
    def setscore(self, value):
        self.rankscore = value
    # get/set for FIVEDAYS table with specific day 
    def getDAYS(self, day):
        return self.FIVEDAYS[day] 
    def setDAYS(self, day, value):
        self.FIVEDAYS[day] = value
    # get/set for patient's name  
    def getName(self):
        return self.Name
    def setName(self, value):
        self.Name = value
    # get/set for patient's weight    
    def getWeight(self):
        return self.Weight
    def setWeight(self, value):
        self.Weight = value
    # get/set for patient's status (HR/LR)
    def getPatientStatus(self):
        return self.Type
    def setPatientStatus(self, value):
        self.Type = value
    # get/set for patient's Normal GRV  
    def getPatientGRV(self):
        return self.GRV_Patient
    def setPatientGRV(self, value):
        self.GRV_Patient = value
    # get/set for Feeding table with specific day and hour
    def getFeedingStatus(self, day, hour):
        return self.Feeding[day][hour]
    def setFeedingStatus(self, day, hour, value):
        self.Feeding[day][hour] = value
    # get/set for GRV table with specific day and hour
    def getGRVStatus(self, day, hour):
        return self.GRV[day][hour]
    def setGRVStatus(self, day, hour, value):
        self.GRV[day][hour] = value
    # get/set for Issue table with specific day and hour
    def getIssueStatus(self,day,hour):
        return self.Issue[day][hour]
    def setIssueStatus(self,day,hour,value):
        self.Issue[day][hour] = value
# TASK A
# each object of PATIENT class hold 4 lists (Feeding, GRV, Issue, FIVEDAYS)
# Acess_data method to save/mangage data for each patient      
def Access_data():
    # loop through Patient_Number list to pass Patient Number
    for i in range(len(Patient_Number)):
        # open csv file data to read as file, storing all the data from csv to each patient object
        with open('PATIENT DATA - PATIENT ' + Patient_Number[i] + '.csv', 'r') as file:
            # create a reader from reader that is able to read from file, separated by the delimiter ','
             reader = csv.reader(file, delimiter = ",")
             # initialise object named patient of PATIENT class
             patient = PATIENT()
             # save patient's name 
             patient.setName(Patient_Number[i])
             # declare some counters
             day = 0
             countrow = 0 #countrow is used to count each row
             countdayrow = 3 # countdayrow is used to count each day
            # using for loop to read each row into reader
             for row in reader:
                 # if counterow at the first row of csv file
                 if countrow == 0:
                     # save patient's Status ( HR or LR) to object patient at row[1]
                     patient.setPatientStatus(row[1])
                     # get patient's weight 
                     temp = row[4]
                     Weight = float(temp[7] + temp[8] + temp[9])
                     # save patient's weight 
                     patient.setWeight(Weight)
                     # patient's weight < 40
                     if patient.getWeight() < 40: # if Patient's weight is less than 40 kg
                         patient.setPatientGRV(patient.getWeight() * 5) # weight * 5ml
                     # patient's weight > 40
                     else:
                         patient.setPatientGRV(250) # 250ml
                 if countrow == countdayrow: # countrow at the 3rd row
                     hour = 0 # initialise hour = 0
                     countdayrow += 24 # countdayrow at the next day
                     # if row at index 0 not equals to nothing
                     if row[0] != "": 
                         day = int(row[0]) # get the string day and parse it into integer
                 if countrow >= 3: # if countrow is greater than or equal to row at 3 in csv file
                     # save each patient's feeding
                     patient.setFeedingStatus(day, hour, row[2])
                     # if row at index 3 not equals to nothing
                     if row[3] != "":
                         # save patient's GRV Status at int(row[3])
                        patient.setGRVStatus(day, hour, int(row[3]))
                     else:
                         # save patient's GRV Status at row[3]
                         patient.setGRVStatus(day, hour, row[3])
                    # save patient's Issue Status at row[4]
                     patient.setIssueStatus(day, hour, row[4])
                     hour += 1 # increase hour by 1
                 countrow += 1 # increase countrow by 1
                 # to skip the last two empty rows at the end of day 5 after 24 hours
                 if day == 5 and hour == 24:
                     break # break out of loop
             # add each patient object to Patient_list
             Patient_list.append(patient)   
# Task A + B                   
def Feeding_Process():
    # declare some amount of feeding 
    Feeding_Amount_1 = "5ML /2 HRS" 
    Feeding_Amount_2 = "10ML /2 HRS" 
    Feeding_Amount_3 = "20ML /2 HRS"
    Feeding_Amount_4 = "30ML /2 HRS"
    # declare some issues
    Issue_1 = "NONE"
    Issue_2 = "FEEDING STOPPED"
    Issue_3 = "REFER TO DIETICIAN"
    # looping through Patient_list
    for i in range(len(Patient_list)):
        # assign each object in Patient_list at index i to patient variable
        patient = Patient_list[i]
        # get patient's normal GRV and assign it to GRV_Patient
        GRV_Patient = patient.getPatientGRV()
        # declare counter for HR and LR patients
        counter1 = 0
        counter2 = 0
        # declare get_days = 0
        get_Days = 0
    
        #HR patient
        # get patient's Status if equals to "HR"
        if patient.getPatientStatus() == "HR":
            # looping from day 1 to day 5
            for day in range(1, 6):
                # looping from 0 hour to 23 hour
                for hour in range(24):
                    # day equals to 1
                     if day == 1:
                          # set patient's Feeding Status with 1ML /1 HR 
                         patient.setFeedingStatus(day,hour,patient.getFeedingStatus(1,0))
                    # day 4 and hour < 3
                     elif day == 4 and hour < 3:
                         # set patient's Issue Status with NONE
                         patient.setIssueStatus(day, hour, Issue_1)
                         # hour 0 or hour 2
                         if hour == 0 or hour == 2:
                              # set patient's Feeding Status with 5ML /2 HRS 
                             patient.setFeedingStatus(day, hour, Feeding_Amount_1)
                    # if GRV_Status equals to nothing
                     else:
                         # get patient's GRV status which is stored in GRV table and assign it to GRV_Status
                         GRV_Status = patient.getGRVStatus(day, hour)                   
                         # if GRV_Status not equals to nothing
                         if GRV_Status != "":
                             # if GRV_Status less than or equal to GRV_Patient
                             if GRV_Status <= GRV_Patient:
                                  # set patient's Feeding Status with 10ML /2 HRS 
                                  patient.setFeedingStatus(day, hour, Feeding_Amount_2)
                                  # set patient's Issue Status with NONE
                                  patient.setIssueStatus(day, hour, Issue_1) 
                             # if GRV_Status greater than GRV_Patient
                             elif GRV_Status > GRV_Patient:
                                 # set patient's Feeding Status with NO FEEDING
                                  patient.setFeedingStatus(day, hour, "NO FEEDING")
                                  # For every 2 FEEDING STOPPED we get 1 REFER TO DIETICIAN                             
                                  if counter1 < 2:
                                         # set patient's Issue Status with FEEDING STOPPED
                                         patient.setIssueStatus(day, hour, Issue_2)
                                         counter1 += 1 # add counter1 by 1
                                  # if counter2 > 2 we only get REFER TO DIETICIAN
                                  else:  
                                         # set patient's Issue Status with REFER TO DIETICIAN
                                         patient.setIssueStatus(day, hour, Issue_3)
                     # get patient's IssueStatus if equals to NONE                   
                     if patient.getIssueStatus(day, hour) == "NONE":
                        counter1 = 0 # reset counter1
                    # save patient's Issue at the end of each day for TASK B + C
                     # get patient's IssueStatus if not equals to ""
                     if patient.getIssueStatus(day, hour) != "":
                          # get patient's Issue then assign to get_Days
                          get_Days = patient.getIssueStatus(day,hour)
                # save patient's Issue at the end of each day for TASK B + C
                patient.setDAYS(day,get_Days)           
                counter1 = 0 # reset counter1   
                get_Days = 0 # reset get_Days  
                               
        # LR patient
        # get patient's Status if equals to "LR"
        if patient.getPatientStatus() == "LR":
            # looping from day 1 to day 5
            for day in range(1, 6):
                # looping from 0 hour to 23 hour
                for hour in range(24):
                    # day == 1 and hour less than 4 and that hour is even ( Patient's Issues are NONE at 4 hours on day 1)
                     if day == 1 and hour < 4 and hour % 2 == 0:
                         # set patient's Issue Status with NONE
                         patient.setIssueStatus(day, hour, Issue_1)
                     else:
                         # get patient's GRV status which is stored in GRV table and assign it to GRV_Status
                         GRV_Status = patient.getGRVStatus(day, hour)
                         # if GRV_Status equals to something
                         if GRV_Status != "":
                                 # if GRV_Status less than or equal to GRV_Patient
                                 if GRV_Status <= GRV_Patient:
                                      # set patient's Issue Status with NONE
                                      patient.setIssueStatus(day, hour, Issue_1)
                                      # patient's weight < 40
                                      if patient.getWeight() < 40:
                                          # set patient's Feeding Status with 10ML /2 HRS 
                                          patient.setFeedingStatus(day, hour, Feeding_Amount_2)  
                                      # patient's weight > 40  
                                      else:
                                          # patient's weight > 40 but has 5ML /2 HRS on day 1 at hour 4
                                          if patient.getFeedingStatus(1,0) == Feeding_Amount_1 and day == 1 and hour == 4:
                                              # set patient's Feeding Status with 10ML /2 HRS
                                              patient.setFeedingStatus(day, hour, Feeding_Amount_2)
                                          else:
                                              # set patient's Feeding Status with 30ML /2 HRS
                                              patient.setFeedingStatus(day, hour, Feeding_Amount_4)
                                 # if GRV_Status greater than GRV_Patient
                                 elif GRV_Status > GRV_Patient:
                                       # set patient's Feeding Status with NO FEEDING
                                       patient.setFeedingStatus(day, hour, "NO FEEDING")
                                       # hour equals to 0
                                       if hour == 0:
                                          # set patient's Issue Status with REFER TO DIETICIAN
                                          patient.setIssueStatus(day, hour, Issue_3)
                                        # For every 2 FEEDING STOPPED we get 1 REFER TO DIETICIAN
                                       elif counter2 < 2:
                                          # set patient's Issue Status with FEEDING STOPPED
                                          patient.setIssueStatus(day, hour, Issue_2)
                                          counter2 += 1 # add counter2 by 1
                                        # if counter2 > 2 we only get REFER TO DIETICIAN
                                       else:
                                          # set patient's Issue Status with REFER TO DIETICIAN
                                          patient.setIssueStatus(day, hour, Issue_3)
                         # if GRV_Status equals to nothing
                         else:  
                                 # get patient's name if equals to B1
                                 if patient.getName() == "B1":
                                     # if hour is even and less than 20
                                     if hour % 2 == 0 and hour < 20:
                                         # if day is less than 5 and hour is less than 16
                                         if day < 5 and hour < 16:
                                             # set patient's Issue status with NONE
                                             patient.setIssueStatus(day, hour, Issue_1)
                                # if hour is even and hour < 20
                                 elif hour % 2 == 0 and hour < 20:
                                     # set patient's Issue Status with NONE
                                    patient.setIssueStatus(day, hour, Issue_1)
                                    # patient's weight < 40
                                    if patient.getWeight() < 40:
                                        # set patient's Feeding Status with 10ML /2 HRS
                                        patient.setFeedingStatus(day, hour, Feeding_Amount_2)
                                    # patient's weight > 40
                                    else:
                                        # patient's weight > 40 but has 5ML /2 HRS on day 1 at hour 6
                                        if patient.getFeedingStatus(1,0) == Feeding_Amount_1 and day == 1 and hour == 6:
                                           # set patient's Feeding Status with 20ML /2 HRS
                                           patient.setFeedingStatus(day, hour,Feeding_Amount_3)
                                        else:
                                          # set patient's Feeding Status with 30ML /2 HRS
                                          patient.setFeedingStatus(day, hour, Feeding_Amount_4)
                     # save patient's Issue at the end of each day for TASK B + C
                     # get patient's Issue Status if not equals to ""
                     if patient.getIssueStatus(day, hour) != "":
                          # get patient's Issue then assign to get_Days
                          get_Days = patient.getIssueStatus(day,hour)
                # save patient's Issue at the end of each day for TASK B + C     
                patient.setDAYS(day,get_Days)
                # if patient's name equals to B1 and day equals to 5
                if patient.getName() == "B1" and day == 5:
                         # save patient's Issue at day 5 with ""
                         patient.setDAYS(day, "")       
                counter2 = 0 # reset counter2
                get_Days = 0 # reset get_Day       

# Task C                              
# method to score patient in Patient_list based on their rate improvement through 5 days cycle
# the idea is to score them based on their Feeding Status at the end of each day
# Patient with higher NONE gets higher score and decrease with times of FEEDING STOPPED AND REFER TO DIETICIAN
# There is also a score classification betwen FS and FS/RD or RD and FS/RD                  
def Ranking():
    # looping through Patient_list
    for i in range(len(Patient_list)):
        # assign each object in Patient_list at index i to patient variable
        patient = Patient_list[i]
        # declare score
        score = 0
        # declare initial score of 20, the highest score a patient can reach is 100( for 5 days)
        initscore = 20
        # declare FEEDING STOPPED with 1 point and REFER TO DIETICIAN with 2 points
        No = 1 # No for "" Issue
        FS = 2
        RD = 3
        # declare distance1, distance2 for FS and RD 
        distance1 = 0
        distance2 = 0
        # declare flag1, flag2 for FS and RD
        flag1 = False
        flag2 = False
        # looping from day 1 to day 5
        for day in range(1,6):
            if patient.getDAYS(day) == "":
                score += initscore - No 
            # if getDAYS at specific day of patient object equals to NONE
            if patient.getDAYS(day) == "NONE" :
                 # add initscore to score
                 score += initscore      
            # if getDAYS at specific day of patient object equals to FEEDING STOPPED
            if patient.getDAYS(day)  == "FEEDING STOPPED":
                  # add initscore and misnus FS to score
                  score += initscore - FS 
                  # looping from (day + 1) to day 5 
                  for i in range(day + 1,6):
                         # if we get FS in the next day and distance1 == 0
                         if patient.getDAYS(i) == "FEEDING STOPPED": 
                             flag1 = True # set flag1 to True
                             break # break out of loop
                         # if we get RD in the next day and distance1 == 0
                         elif patient.getDAYS(i) == "REFER TO DIETICIAN": 
                             flag2 = True # set flag2 to True
                             break # break out of loop
                         # if we get NONE in the next day
                         elif patient.getDAYS(i) == "NONE":
                             distance1 += 1 # add distance1 by 1
                  # if flag1 equals to True     
                  if flag1 == True:
                      # score minus FS
                      score -= FS
                      # set flag1 back to False
                      flag1 = False
                  # if flag2 equals to True
                  if flag2 == True:
                      # score minus RD
                      score -= RD
                      # set flag2 back to False
                      flag2 = False
            # if getDAYS at specific day of patient object equals to REFER TO DIETICIAN
            if patient.getDAYS(day) == "REFER TO DIETICIAN":
                  # add initscore and minus RD to score
                  score += initscore - RD 
                  # looping from (day + 1) to day 5 
                  for i in range(day + 1,6):
                      # if we get FS in the next day and distance2 == 0
                      if patient.getDAYS(i) == "FEEDING STOPPED": 
                         flag1 = True # set flag1 to True
                         break # break out of loop
                      # if we get RD in the next day and distance2 == 0
                      elif patient.getDAYS(i) == "REFER TO DIETICIAN":
                         flag2 = True # set flag2 to True
                         break # break out of loop
                      elif patient.getDAYS(i) == "NONE":
                         distance2 += 1 # add distance2 by 1                        
                  # if flag1 equals to True     
                  if flag1 == True:
                      # score minus FS
                      score -= FS
                      # set flag1 back to False
                      flag1 = False
                  # if flag2 equals to True
                  if flag2 == True:
                      # score minus RD
                      score -= RD
                      # set flag2 back to False
                      flag2 = False
            # save each patient's score
            patient.setscore(score)
        # No NONE between
        if distance2 == 0 or distance1 == 0:
            score -= 4
        # 1 NONE between
        elif distance2 == 1 or distance1 == 0:
            score -= 3
        # 2 NONE between
        elif distance2 == 2 or distance1 == 0:
            score -= 2
        # 3 NONE between
        elif distance2 == 3 or distance1 == 0:
            score -= 1
            
