import datetime
import pandas as pd
from pandas.plotting import table
import matplotlib.pyplot as plt
from cfg import BASE_DIR, SOAPS_FOLDER

class ExportMatriz():

    def __init__(self, instance):
        self.object = instance
        self.df = pd.DataFrame(instance.matriz)

    def to_image(self):

        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        table(ax,self.df, loc="center")

        m_path = BASE_DIR/SOAPS_FOLDER

        m_path.mkdir(parents=True, exist_ok=True)
        plt.savefig(f"{m_path}/{datetime.datetime.now()}.jpg")




