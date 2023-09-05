'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Nicolas Van der Werf, Taeden Anderson]
Worked with Taeden in Class but my code is unique

'''

import sys
import csv
from collections import Counter

#CA:
#VT:
#WA:
#NY:

#Alex: WA
#Barbara: NY
#Charlie: CA
#Doris: VT

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]]


        # print(self.unmatchedHospitals)
        # print(self.unmatchedResidents)
        # print(self.residentsMappings)
        # print(self.hospitalsMappings)
        # print(self.matches)
    
            
    # print out the stable match
    def reportMatches(self):
        print("\n\nFinal Matches:   " + str(self.matches))
            
    # follow the chart described in the lab to find the stable match
    def runMatch(self):
        for res in self.unmatchedResidents:
            self.matches[res] = self.residentsMappings[res][0]
            conflicts = len(self.checkConflicts()) > 0
            while conflicts:
                conflicting = self.checkConflicts()
                res1,res2 = conflicting[0], conflicting[1]
                hospital = self.matches[res1]
                if self.hospitalsMappings[hospital].index(res1) > self.hospitalsMappings[hospital].index(res2):
                    self.residentsMappings[res1].pop(0)
                    self.matches[res1] = self.residentsMappings[res1][0]
                else:
                    self.residentsMappings[res2].pop(0)
                    self.matches[res2] = self.residentsMappings[res2][0]
                conflicts = len(self.checkConflicts()) > 0


    def checkConflicts(self):
        count_dict = Counter(self.matches.values())
        if count_dict[None]: count_dict[None] = 0
        result = [key for key, value in self.matches.items()
                  if count_dict[value] > 1]
        return result

#Alex: WA
#Barbara: NY
#Charlie: CA
#Doris: VT

if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



