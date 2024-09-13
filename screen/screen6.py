# -*- coding: UTF-8 -*-
from cavd import bv_calculation
import warnings
from pymatgen.io.cif import CifWriter
import pandas as pd

warnings.filterwarnings("ignore")



if __name__ == "__main__":
    """
    calculate BVSE landscape
    :param filename: cif filename
    :param moveion:  move ion
    :param valenceofmoveion: valence of move ion
    :param resolution: resolution for calculating BVSE landsacpe
    :return: migration energy barrier, Pgrid file for saving and visualization BVSE landscape
    """
    predict_df = pd.read_csv('./selected_materials.csv')
    for i in predict_df['id']:
        mp_id = str(i)
        Ea = bv_calculation("./screen-data/" + mp_id + ".cif","Li", 1, 0.1)[0]
        f = open('./Ea.txt', 'a')
        print(Ea, file=f)
        f.close()
