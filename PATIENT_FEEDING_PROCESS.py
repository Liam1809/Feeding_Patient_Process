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
    
