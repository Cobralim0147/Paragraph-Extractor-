from matplotlib import pyplot as plt
import cv2
import numpy as np

class WhiteColumnsFinder:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, 0)
        self.nrow, self.ncol = self.image.shape
        self.white_cols = []
        self.separation_col = []
        self.start = [0]
        self.end = []
        self.white_rows = []  

    # Round the pixel value to 0 or 255 
    def round_up_or_down(self):
        _, thresholded = cv2.threshold(self.image, 253, 255, cv2.THRESH_BINARY)
        self.image = thresholded

    # find the white columns in the picture using histogram projection
    def find_white_columns(self):
        vertical_projection = np.sum(self.image, axis=0)
        peak_threshold = 0.9 * np.max(vertical_projection)
        peaks = np.where(vertical_projection > peak_threshold)[0]
        self.white_cols.extend(peaks)

    #find the start and end of the white lines
    def find_start_and_end(self):
        for i in range(1, len(self.white_cols)):
            if (self.white_cols[i] - self.white_cols[i - 1]) != 1:
                self.start.append(self.white_cols[i])
                self.end.append(self.white_cols[i - 1])
        self.end.append(self.nrow)

    #using the start and end enclose the paragraphs 
    def enclose_content(self):
        for i in range(len(self.end)):
            if (self.end[i] - self.start[i]) > 15:
                self.separation_col.append(self.start[i])
                self.separation_col.append(self.end[i])
    
        self.separation_col.pop(0)
        self.separation_col.pop(-1)

        new_separation_col = []
        for i in range(0, len(self.separation_col), 2):
            piece_width = self.separation_col[i + 1] - self.separation_col[i]
            if piece_width > 50:
                new_separation_col.extend(self.separation_col[i:i + 2])
            else:
                new_separation_col.extend(self.separation_col[i:i + 2])  
        self.separation_col = new_separation_col


    #display the image with marking 
    def display_image_with_markings(self):
        plt.imshow(self.image, cmap='gray')
        for col in self.separation_col:
            plt.axhline(y=col, color='black', linewidth=1)
        plt.title("Image with White Cols Marked")
        plt.show()
    
    # getter for the separation array
    def getSeparation(self):
        return self.separation_col

    # getter for the white rows array
    def getWhiteRows(self):
        return self.white_rows



