import cv2
import os 

class VerticalPieceExtractor:
    def __init__(self,image_path ,separation_columns, output_folder):
        self.image_path = image_path
        self.image= cv2.imread(image_path)
        self.separation_col= separation_columns
        self.output_folder= output_folder
        

    #to extract the image 
    def extract_and_save_vertical_pieces(self):
        for i in range(0, len(self.separation_col), 2):
            vertical_piece = self.image[:, self.separation_col[i]:self.separation_col[i+1]]
            file_path = os.path.join(self.output_folder, f"{self.image_path[:-4]}_C{round(i/2)}.png")
            cv2.imwrite(file_path, vertical_piece)






