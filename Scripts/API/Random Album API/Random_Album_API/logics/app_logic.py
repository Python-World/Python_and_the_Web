import random

import pandas as pd


class GetRandomAlbum:
    """Class to get random album from dataset"""

    def __init__(self, context):
        """ """
        self.context = context
        self.__out = []
        self.dataset = None

    def load_dataset(self):
        """loading the dataset into pandas"""
        self.dataset = pd.read_csv(
            "Random_Album_API/dataset/albumlist.csv", engine="python"
        )

    def get_random_album(self):
        """Get a random album from dataset"""
        self.__out = self.dataset.iloc[[random.randint(0, 499)]].to_dict(
            "record"
        )

    def get_all_album(self):
        """In case if you want all the records"""
        self.__out = self.dataset.to_dict("record")

    def driver_method(self):
        """A method for all methods"""
        self.load_dataset()
        if self.context == "random":
            self.get_random_album()
        else:
            self.get_all_album()
        return self.__out
