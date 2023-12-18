import os 
import shutil 

class deleteFolder:
    def __init__(self, objectPath):
        self.folderPath= objectPath

    #check for existing folder and delete it 
    def deleteExistingFolder(self):
        if os.path.exists(self.folderPath): 
            shutil.rmtree(self.folderPath)
    
    #clear files in the folder
    def clearExistingFolder(self): 
        if os.path.exists(self.folderPath):
            for file_name in os.listdir(self.folderPath):
                file_path = os.path.join(self.folderPath, file_name)
                if os.path.isfile(file_path):
                    os.remove(file_path)