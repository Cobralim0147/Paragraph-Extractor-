import cv2
import os

class HorizontalPieceExtractor:
    def __init__(self, image_path, separation_rows, paragraph_folder):
        self.counter = 0
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.separation_row = separation_rows 
        self.paragraph_folder = paragraph_folder


    #to extract and save horizontal elements 
    def extract_and_save_vertical_pieces(self):
        for i in range(0, len(self.separation_row), 2):
            horizontal_piece = self.image[self.separation_row[i]:self.separation_row[i+1], :]
            file_path = os.path.join(self.paragraph_folder, f"{os.path.basename(self.image_path[:-7])}_P{self.counter}.png")
            while os.path.exists(file_path):
                self.counter += 1
                file_path = os.path.join(self.paragraph_folder, f"{os.path.basename(self.image_path[:-7])}_P{self.counter}.png")
            cv2.imwrite(file_path, horizontal_piece)


