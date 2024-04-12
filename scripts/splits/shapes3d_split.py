import numpy as np 
import math
from typing import Tuple 

import scripts.metadata.shapes3d_metadata as Metadata    
   
    
class Shapes3DSplits(): 
    @staticmethod
    def make_injective(imgs: np.array, factor_vals: np.array, factor_classes: np.array) -> Tuple[np.array, np.array, np.array]: 
        mask = (factor_vals[:, Metadata.ORIENTATION] <= 0)
        return imgs[mask], factor_vals[mask], factor_classes[mask]
    
    @staticmethod 
    def preprocess(imgs: np.array, factor_vals: np.array, factor_classes: np.array) -> Tuple[np.array, np.array, np.array]: 
        return Shapes3DSplits.make_injective(imgs=imgs, factor_vals=factor_vals, factor_classes=factor_classes)

    @staticmethod
    def recomb_to_element_random(factor_vals: np.array, train_frac: float=0.8) -> np.array:
        N = factor_vals.shape[0] 
        mask = np.zeros(shape=N, dtype=int)
        n_train = math.floor(train_frac * N)
        mask[0:n_train] = 1 
        np.random.shuffle(mask) 
        mask = mask.astype(bool)
        return mask
    
     # ORIGINAL SPLITS 3/3 
    @staticmethod 
    def recomb_to_range_oh_wh(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.OBJECT_HUE] >= Metadata.PURPLE) &
                    (factor_vals[:, Metadata.WALL_HUE] <= Metadata.YELLOW))

        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_fh(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.OBLONG) &
                    (factor_vals[:, Metadata.FLOOR_HUE] >= Metadata.AQUA))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_oh(factor_vals: np.array) -> np.array:
        def test_filter(factor_vals: np.array):
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.OBLONG) &
                    (factor_vals[:, Metadata.OBJECT_HUE] >= Metadata.AQUA)) 

        test_mask = test_filter(factor_vals)
        return ~test_mask
    
    # CUSTOM SPLITS 
    @staticmethod 
    def recomb_to_range_osh_osz1(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.SPHERE) & 
                    (factor_vals[:, Metadata.SCALE] >= Metadata.MEDIUM_1))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_osz2(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.SPHERE) & 
                    (factor_vals[:, Metadata.SCALE] >= Metadata.X_SMALL_1))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_oh1(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.CUBE) & 
                    (factor_vals[:, Metadata.OBJECT_HUE] >= Metadata.FLURO_GREEN))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_oh2(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return (((factor_vals[:, Metadata.SHAPE] == Metadata.CUBE) & 
                    (factor_vals[:, Metadata.OBJECT_HUE] >= Metadata.FLURO_GREEN)) | 
                    ((factor_vals[:, Metadata.SHAPE] == Metadata.SPHERE) & 
                     (factor_vals[:, Metadata.OBJECT_HUE] < Metadata.FLURO_GREEN))
                    )
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osz_oh(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return ((factor_vals[:, Metadata.SCALE] <= Metadata.X_SMALL_1) & 
                    (factor_vals[:, Metadata.OBJECT_HUE] <= Metadata.FLURO_GREEN))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def schott_split(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array): 
            return ((factor_vals[:, Metadata.FLOOR_HUE] != Metadata.RED) & 
                    (factor_vals[:, Metadata.WALL_HUE] != Metadata.RED) & 
                     (factor_vals[:, Metadata.OBJECT_HUE] != Metadata.RED) & 
                     (factor_vals[:, Metadata.ORIENTATION] != -30))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
