import numpy as np 
import scripts.metadata.mpi3d_metadata as Metadata    
import math

class MPI3DSplits(): 
    @staticmethod
    def recomb_to_element_random(factor_vals: np.array, train_frac: float=0.8) -> np.array:
        N = factor_vals.shape[0] 
        mask = np.zeros(shape=N, dtype=int)
        n_train = math.floor(train_frac * N)
        mask[0:n_train] = 1 
        np.random.shuffle(mask) 
        mask = mask.astype(bool)
        return mask
    
    # Montero et al. remove cones and hexagons as these 2 shapes are very similar to the pyramid
    # and cylinder respectively 
    @staticmethod 
    def remove_ambiguous_shapes(factor_cls: np.array) -> np.array: 
        return ~np.isin(factor_cls[:, Metadata.SHAPE], np.array([Metadata.CONE, Metadata.HEXAGON]))
    
    # they also fix x-axis displacement to 0 with the justification that rotation of both axes 
    # make it difficult to find completely unseen combinations due to the dual effect of rotating both axes
    @staticmethod 
    def fix_x_axis(factor_cls: np.array) -> np.array: 
        return factor_cls[:, Metadata.X_AXIS] == 0
    
    # preprocess as in Montero et al
    @staticmethod 
    def preprocess(imgs: np.array, factor_vals: np.array, 
                   factor_classes: np.array) -> np.array: 
        mask = MPI3DSplits.fix_x_axis(factor_classes) # TODO: note that montero et al remove cones and hexagons
        # as these 2 shapes are very similar to the pyramid and cylinder, but removing these mean
        # we must change MPI3DMetadata, as pyramid is offset by 4 (and we add the offset to 4)
        return imgs[mask], factor_vals[mask], factor_classes[mask]
    
    # use the split given by Montero et al: remove [shape=cylinder, vertical axis > 0.5] from training set
    # this split is used for testing in Lost in Latent Space 
    @staticmethod
    def recomb_to_range_osh_yaxis(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.SHAPE] == Metadata.CYLINDER) & 
                    (factor_cls[:, Metadata.Y_AXIS] <= Metadata.MID_AXIS))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    # other splits in Montero et al. cylinder_to_background 1
    @staticmethod
    def recomb_to_range_osh_wh1(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.SHAPE] == Metadata.CYLINDER) & 
                    (factor_cls[:, Metadata.WALL_HUE] > Metadata.PURPLE)) # test wall hue is sea green, or salmon
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    # other split in Montero et al. object shape to background 2
    @staticmethod
    def recomb_to_range_osh_wh2(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.SHAPE] >= Metadata.PYRAMID) & 
                    (factor_cls[:, Metadata.WALL_HUE] == Metadata.SALMON))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    # other split in Montero et al 
    @staticmethod
    def recomb_to_range_oh_wh(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.WALL_HUE] == Metadata.SALMON) & 
                    (factor_cls[:, Metadata.OBJECT_HUE] > Metadata.RED))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    

    # customised splits 
    @staticmethod 
    def recomb_to_range_osh_osz1(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.SHAPE] == Metadata.PYRAMID) & 
                    (factor_cls[:, Metadata.SCALE] == Metadata.LARGE))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_osh_osz2(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.SHAPE] <= Metadata.CYLINDER) &  # shape cylinder or cube 
                    (factor_cls[:, Metadata.SCALE] == Metadata.SMALL))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_ch_osh1(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.CAMERA_HEIGHT] == Metadata.TOP) & 
                    (factor_cls[:, Metadata.SHAPE] == Metadata.CUBE))
        test_mask = test_filter(factor_cls)
        return ~test_mask 

    @staticmethod 
    def recomb_to_range_ch_osh2(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.CAMERA_HEIGHT] >= Metadata.CENTER) & 
                    (factor_cls[:, Metadata.SHAPE] >= Metadata.PYRAMID)) # pyramid or sphere
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_ch_yaxis1(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.Y_AXIS] >= Metadata.MID_AXIS) & 
                    (factor_cls[:, Metadata.CAMERA_HEIGHT] == Metadata.BOTTOM))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    @staticmethod 
    def recomb_to_range_ch_yaxis2(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.Y_AXIS] <= Metadata.MID_AXIS) & 
                    (factor_cls[:, Metadata.CAMERA_HEIGHT] <= Metadata.CENTER))
        test_mask = test_filter(factor_cls)
        return ~test_mask 
    
    @staticmethod 
    def schott_split(factor_cls: np.array) -> np.array: 
        def test_filter(factor_cls: np.array) -> np.array: 
            return ((factor_cls[:, Metadata.Y_AXIS] > 5) & 
                    (factor_cls[:, Metadata.X_AXIS] > 5))
        test_mask = test_filter(factor_cls)
        return ~test_mask 