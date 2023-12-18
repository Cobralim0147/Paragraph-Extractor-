from matplotlib import pyplot as plt
import cv2

class WhiteRowFinder:
    def __init__(self, image_path, white_threshold=253, gap_threshold=30):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path, 0)
        self.nrow, self.ncol = self.image.shape
        self.white_rows = []
        self.separation_row = []
        self.start = [0]
        self.end = []
        self.white_threshold = white_threshold
        self.gap_threshold = gap_threshold

    # Find the white 
    def find_white_rows(self):
        for row in range(self.nrow):
            is_white = all(pixel_value >= self.white_threshold for pixel_value in self.image[row, :])
            if is_white:
                self.white_rows.append(row)

    # Round up and down to 0 or 255 
    def round_up_or_down(self):
        for row in range(self.nrow):
            for col in range(self.ncol):
                pixel_value = self.image[row, col]
                if pixel_value >= self.white_threshold:
                    self.image[row, col] = 255 
                else:
                    self.image[row, col] = 1  

    # find the white rows in the picture 
    def find_white_spaces(self):
        for i in range(1, len(self.white_rows)):
            if (self.white_rows[i] - self.white_rows[i - 1]) != 1:
                self.start.append(self.white_rows[i])
                self.end.append(self.white_rows[i - 1])
        self.end.append(self.nrow)

    #Enclose the paragraphs 
    def find_gaps_between(self):
        for i in range(len(self.end)):
            if (self.end[i] - self.start[i]) > self.gap_threshold:
                self.separation_row.append(self.start[i])
                self.separation_row.append(self.end[i])

        self.separation_row.pop(0)
        self.separation_row.pop(-1)

    #display the image with marking 
    def display_image_with_markings(self):
        plt.imshow(self.image, cmap='gray')

        for row in self.separation_row:
            plt.axhline(y=row, color='black', linewidth=1)

        plt.title("Image with White Rows Marked")
        plt.show()
    
    # getter for the separation array
    def getSeparation(self):
        return self.separation_row


