import numpy as np
from typing import Dict
from scripts.metadata.base_metadata import BaseMetadata

NC = 3
IMG_SIZE = (3, 64, 64)
N_FACTORS = 6
FLOOR_HUE = 0
WALL_HUE = 1 
OBJECT_HUE = 2 
SCALE = 3 
SHAPE = 4 
ORIENTATION = 5
FACTOR_SIZES = np.array([10, 10, 10, 8, 4, 15])
FACTOR_IDX_TO_VALS_MAP = {
                0: np.array([0., 0.1, 0.2, 0.3, 0.4,
                            0.5, 0.6, 0.7, 0.8, 0.9]),
                1: np.array([0., 0.1, 0.2, 0.3, 0.4,
                            0.5, 0.6, 0.7, 0.8, 0.9]),
                2: np.array([0., 0.1, 0.2, 0.3, 0.4,
                            0.5, 0.6, 0.7, 0.8, 0.9]),
                3: np.array([0.75, 0.82142857, 0.89285714, 0.96428571,
                            1.03571429, 1.10714286, 1.17857143, 1.25]),
                4: np.array([0, 1, 2, 3]),
                5: np.array([-30., -25.71428571, -21.42857143,
                            -17.14285714, -12.85714286, -8.57142857,
                            -4.28571429, 0., 4.28571429, 8.57142857,
                            12.85714286, 17.14285714, 21.42857143,
                            25.71428571,  30.])}
COLOUR_ROLE = 'colour_role'
SCALE_ROLE = 'scale_role'
SHAPE_ROLE = 'shape_role'
ORIENTATION_ROLE = 'orientation_role'

SEMANTIC_CATEGORY_TO_FAC_IDXS = {
    COLOUR_ROLE: (FLOOR_HUE, WALL_HUE, OBJECT_HUE),
    SCALE_ROLE: (SCALE,),
    SHAPE_ROLE: (SHAPE,),
    ORIENTATION_ROLE: (ORIENTATION,)
}
# small 
X_SMALL_0 = 0.75 # xsmall
X_SMALL_1 = 0.82142857
SMALL = 0.89285714
# medium 
MEDIUM_1 = 0.96428571
MEDIUM_2 = 1.03571429
# large
LARGE = 1.10714286
X_LARGE_0 = 1.17857143
X_LARGE_1 = 1.25 # xlarge 
# colours
RED = 0 
ORANGE = 0.1
YELLOW = 0.2 
FLURO_GREEN = 0.3 
TEAL_GREEN = 0.4
AQUA = 0.5 
BLUE = 0.6
DARK_BLUE = 0.7
PURPLE = 0.8
MAGENTA = 0.9
# shapes 
CUBE = 0
CYLINDER = 1
SPHERE = 2
OBLONG = 3

ONE_HOT_PRED_TO_FACTOR = {
    0: 'floor_hue',
    1: 'floor_hue',
    2: 'floor_hue',
    3: 'floor_hue', 
    4: 'floor_hue', 
    5: 'floor_hue', 
    6: 'floor_hue', 
    7: 'floor_hue', 
    8: 'floor_hue', 
    9: 'floor_hue', 
    
    10: 'wall_hue',
    11: 'wall_hue',
    12: 'wall_hue',
    13: 'wall_hue',
    14: 'wall_hue',
    15: 'wall_hue',
    16: 'wall_hue',
    17: 'wall_hue',
    18: 'wall_hue',
    19: 'wall_hue',
    20: 'object_hue',
    21: 'object_hue',
    22: 'object_hue',
    23: 'object_hue',
    24: 'object_hue',
    25: 'object_hue',
    26: 'object_hue',
    27: 'object_hue',
    28: 'object_hue',
    29: 'object_hue',
    30: 'scale',
    31: 'scale',
    32: 'scale',
    33: 'scale',
    34: 'scale',
    35: 'scale',
    36: 'scale',
    37: 'scale',
    38: 'shape',
    39: 'shape',
    40: 'shape', 
    41: 'shape',
    42: 'orientation',
    43: 'orientation',
    44: 'orientation',
    45: 'orientation',
    46: 'orientation',
    47: 'orientation',
    48: 'orientation',
    49: 'orientation',
    50: 'orientation',
    51: 'orientation',
    52: 'orientation',
    53: 'orientation',
    54: 'orientation',
    55: 'orientation',
    56: 'orientation',
}
ONE_HOT_PRED_TO_SERIALISED = {
    0: 'red',
    1: 'orange', 
    2: 'yellow', 
    3: 'fluro_green',
    4: 'teal_green',
    5: 'aqua',
    6: 'blue',
    7: 'dark_blue',
    8: 'purple',
    9: 'magenta',
    
    10: 'red',
    11: 'orange', 
    12: 'yellow', 
    13: 'fluro_green',
    14: 'teal_green',
    15: 'aqua',
    16: 'blue',
    17: 'dark_blue',
    18: 'purple',
    19: 'magenta',
    20: 'red',
    21: 'orange', 
    22: 'yellow', 
    23: 'fluro_green',
    24: 'teal_green',
    25: 'aqua',
    26: 'blue',
    27: 'dark_blue',
    28: 'purple',
    29: 'magenta',
    30: '0-7',
    31: '1-7',
    32: '2-7',
    33: '3-7',
    34: '4-7',
    35: '5-7',
    36: '6-7',
    37: '7-7',
    38: 'cube', 
    39: 'cylinder',
    40: 'sphere', 
    41: 'oblong',
    42: '0-14',
    43: '1-14',
    44: '2-14',
    45: '3-14',
    46: '4-14',
    47: '5-14',
    48: '6-14',
    49: '7-14',
    50: '8-14',
    51: '9-14',
    52: '10-14',
    53: '11-14',
    54: '12-14',
    55: '13-14',
    56: '14-14',
}
COLOUR_PRED_TO_SERIALISED_MAP = {
    0: 'red',
    1: 'orange', 
    2: 'yellow', 
    3: 'fluro_green',
    4: 'teal_green',
    5: 'aqua',
    6: 'blue',
    7: 'dark_blue',
    8: 'purple',
    9: 'magenta'
}
SHAPE_PRED_TO_SERIALISED_MAP = {
    0: 'cube', 
    1: 'cylinder',
    2: 'sphere', 
    3: 'oblong'
}
SCALE_PRED_TO_SERIALISED_MAP = {
    0: '0-7',
    1: '1-7',
    2: '2-7',
    3: '3-7',
    4: '4-7',
    5: '5-7',
    6: '6-7',
    7: '7-7'
}
ORIENTATION_PRED_TO_SERIALISED_MAP = {
    0: '0-14',
    1: '1-14',
    2: '2-14',
    3: '3-14',
    4: '4-14',
    5: '5-14',
    6: '6-14',
    7: '7-14',
    8: '8-14',
    9: '9-14',
    10: '10-14',
    11: '11-14',
    12: '12-14',
    13: '13-14',
    14: '14-14',
}
FACTOR_IDX_TO_SERIALISED_MAP = {
    FLOOR_HUE: 'floor_hue',
    WALL_HUE: 'wall_hue',
    OBJECT_HUE: 'object_hue',
    SCALE: 'scale',
    SHAPE: 'shape',
    ORIENTATION: 'orientation'
}
IDX_TO_SERIALISED_MAP = {
    FLOOR_HUE: COLOUR_PRED_TO_SERIALISED_MAP,
    WALL_HUE: COLOUR_PRED_TO_SERIALISED_MAP,
    OBJECT_HUE: COLOUR_PRED_TO_SERIALISED_MAP, 
    SHAPE: SHAPE_PRED_TO_SERIALISED_MAP,
    SCALE: SCALE_PRED_TO_SERIALISED_MAP,
    ORIENTATION: ORIENTATION_PRED_TO_SERIALISED_MAP
}


def get_role_filler_info(factor_classes: np.array) -> Dict: 
    return BaseMetadata.get_role_filler_info(factors=factor_classes, 
                                             s_category_to_fac_idxs=SEMANTIC_CATEGORY_TO_FAC_IDXS)

def get_n_fillers_per_role(role_filler_info: Dict) -> np.array: 
    return BaseMetadata.get_n_fillers_per_role(role_filler_info)

# rotation 
# cylinder, sphere, oblong are all invariant wrt rotation (should not try predict rotation)
# rotation is only predictable from background wall angle (a bit difficult)
