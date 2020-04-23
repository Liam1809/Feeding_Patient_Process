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
