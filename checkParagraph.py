from WhiteRowFinder import WhiteRowFinder as wrf
from WhiteColFinder import WhiteColumnsFinder as wcf
import os

class CheckParagraph:
    def __init__(self, image_file):
        self.image_file = image_file

    # Extract paragraphs only and delete the none paragraphs 
    def paragraph_only(self):
        wrf1 = wrf(self.image_file)
        wrf1.round_up_or_down()
        wrf1.find_white_rows()
        wcf1= wcf(self.image_file)
        wcf1.round_up_or_down()
        wcf1.find_white_columns()

        if (len(wrf1.white_rows) > 2) & (len(wcf1.white_cols) >= 5) :
            pass
        else:
            os.remove((self.image_file))
