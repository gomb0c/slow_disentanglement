import numpy as np 
import scripts.metadata.dsprites_metadata as Metadata    
import math

class DSpritesSplits(): 
    @staticmethod
    def recomb_to_element_random(factor_vals: np.array, train_frac: float=0.8) -> np.array:
        N = factor_vals.shape[0] 
        mask = np.zeros(shape=N, dtype=int)
        n_train = math.floor(train_frac * N)
        mask[0:n_train] = 1 
        np.random.shuffle(mask) 
        mask = mask.astype(bool)
        return mask
    
    # make injective as in Schott et al by only retaining 
    # images where the orientation is in [0, 90)
    @staticmethod 
    def make_injective(factor_vals: np.array) -> np.array: 
        return (factor_vals[:, Metadata.ORIENTATION] <= Metadata.ORIENTATION_THRESH)
    
    # preprocess as in Montero et al
    @staticmethod 
    def preprocess(imgs: np.array, factor_vals: np.array, 
                   factor_classes: np.array) -> np.array: 
        mask = DSpritesSplits.make_injective(factor_vals=factor_vals) # TODO: note that montero et al remove cones and hexagons
        # as these 2 shapes are very similar to the pyramid and cylinder, but removing these mean
        # we must change MPI3DMetadata, as pyramid is offset by 4 (and we add the offset to 4)
        return imgs[mask], factor_vals[mask], factor_classes[mask]
    
    # splits from Montero et al 
    @staticmethod 
    def recomb_to_range_sh_sq_pos_x(factor_vals: np.array) -> np.array: 
        def train_filter(factor_vals: np.array) -> np.array: 
            return ( (factor_vals[:, Metadata.SHAPE] != Metadata.SQUARE) | 
            (factor_vals[:, Metadata.POS_X] < 0.5))
        train_mask = train_filter(factor_vals)
        return train_mask  
    
    @staticmethod 
    def recomb_to_range_sh_el_pos_x(factor_vals: np.array) -> np.array: 
        def train_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] != Metadata.ELLIPSE) | 
            (factor_vals[:, Metadata.POS_X] < 0.5))
        train_mask = train_filter(factor_vals)
        return train_mask  

    @staticmethod 
    def recomb_to_range_sh_sq_scale(factor_vals: np.array) -> np.array: 
        def train_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] != Metadata.SQUARE) | 
                    (factor_vals[:, Metadata.SCALE] <= Metadata.MED_1))
        train_mask = train_filter(factor_vals)
        return train_mask 
    
    @staticmethod 
    def recomb_to_range_sh_sq_pos_x_centered(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.SQUARE) & 
                    (factor_vals[:, Metadata.POS_X] > 0.25) & 
                    (factor_vals[:, Metadata.POS_X] > 0.75))
        test_mask = test_filter(factor_vals)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_sh_sq_pos_x_flanked(factor_vals: np.array) -> np.array: 
        def train_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] != Metadata.SQUARE) |
                    (factor_vals[:, Metadata.POS_X] < 0.25) |
                    (factor_vals[:, Metadata.POS_X] > 0.75))
        train_mask = train_filter(factor_vals)
        return train_mask 

    @staticmethod 
    def recomb_to_range_sh_sq_pos_x_rshift(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] == Metadata.SQUARE) &
                    (factor_vals[:, Metadata.POS_X] > 0.40) &
                    (factor_vals[:, Metadata.POS_X] < 0.90))
        test_mask = test_filter(factor_vals)
        return ~test_mask 

    @staticmethod 
    def recomb_to_range_sh_sq_pos_x_lshift(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return ((factor_vals[:, Metadata.SHAPE] != Metadata.ELLIPSE) |
                    (factor_vals[:, Metadata.POS_X] > 0.10) &
                    (factor_vals[:, Metadata.POS_X] < 0.60))
        test_mask = test_filter(factor_vals)
        return ~test_mask 

    @staticmethod
    def schott_split(factor_vals: np.array) -> np.array: 
        def test_filter(factor_vals: np.array) -> np.array: 
            return (
                (factor_vals[:, Metadata.ORIENTATION] >= 0.64442926) & 
                (factor_vals[:, Metadata.POS_X] > 0.09677419) & 
                (factor_vals[:, Metadata.POS_Y] > 0.09677419)
            )
        test_mask = test_filter(factor_vals)
        return ~test_mask 