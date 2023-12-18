from delete import deleteFolder as df
from verticalExtractor import VerticalPieceExtractor as vpe
from horizontalExtractor import HorizontalPieceExtractor as hpe
from WhiteColFinder import WhiteColumnsFinder as wcf
from WhiteRowFinder import WhiteRowFinder as wrf
from checkParagraph import CheckParagraph
import cv2
import os

class driver_class:
    def __init__(self, pic_arrays):
        self.pic_array = pic_arrays
        self.output_folder = os.path.join(os.path.dirname(self.pic_array[0]), "output") 
        self.paragraph_folder = os.path.join(os.path.dirname(self.pic_array[0]), "paragraph")
        os.makedirs(self.output_folder, exist_ok=True)
        os.makedirs(self.paragraph_folder, exist_ok=True)
        self.df1 = df(self.output_folder)
        self.df2 = df(self.paragraph_folder)
        self.df1.clearExistingFolder()
        self.df2.clearExistingFolder()
        
        
        #Find all the columns 
        for image in range(len(self.pic_array)):
            self.segment_paragraphs_cols(image)  

        # Find all the rows 
        image_files = [os.path.join(self.output_folder, file) for file in os.listdir(self.output_folder) if file.endswith('.png')]
        for i, image_file in enumerate(image_files):

            wrf1 = wrf(image_file)
            wrf1.round_up_or_down()
            wrf1.find_white_rows()
            wrf1.find_white_spaces()
            wrf1.find_gaps_between()

            # Check if the piece is one whole image (threshold here is 80% of the original image width)
            if wrf1.getSeparation() and wrf1.getSeparation()[0] >= 0.8 * cv2.imread(image_file).shape[1]:
                if self.detect_table(image_file, i, len(image_files)):
                    pass
                else:
                    self.segment_paragraphs_row(image_file)
            else:
                hpe1 = hpe(image_file, wrf1.getSeparation(), self.paragraph_folder)
                hpe1.extract_and_save_vertical_pieces()
        
        self.recheck()

    # Find all the cols
    def segment_paragraphs_cols(self, image):
        wcf1 = wcf(self.pic_array[image])
        wcf1.round_up_or_down()
        wcf1.find_white_columns()
        wcf1.find_start_and_end()
        wcf1.enclose_content()

        vpe1 = vpe(self.pic_array[image], wcf1.getSeparation(), self.output_folder)
        vpe1.extract_and_save_vertical_pieces()

    # Find all the rows 
    def segment_paragraphs_row(self, image_path):
        wrf1 = wrf(image_path)
        wrf1.round_up_or_down()
        wrf1.find_white_rows()
        wrf1.find_white_spaces()
        wrf1.find_gaps_between()

    def recheck(self):
        for filename in os.listdir(self.paragraph_folder):
            if filename.endswith(".png"):
                image_path = os.path.join(self.paragraph_folder, filename)
                checker = CheckParagraph(image_path)
                checker.paragraph_only()


