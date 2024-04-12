import numpy as np 
from scripts.metadata.base_metadata import BaseMetadata
from typing import Dict

NC = 3 
IMG_SIZE = (3, 64, 64)

N_FACTORS = 7

OBJECT_HUE = 0  # 9 
SHAPE = 1 # 6
SCALE = 2  # 2 
CAMERA_HEIGHT = 3 # camera height
WALL_HUE = 4 
X_AXIS = 5 
Y_AXIS = 6

FACTOR_SIZES = np.array([6, 6, 2, 3, 3, 40, 40])

FACTOR_IDX_TO_CLASS_MAP = {
    0: np.arange(6), 
    1: np.arange(6), 
    2: np.arange(2), 
    3: np.arange(3), 
    4: np.arange(3), 
    5: np.arange(40),
    6: np.arange(40)
}

AXIS_ROLES = (X_AXIS, Y_AXIS)

COLOUR_ROLE = 'colour_role'
DISTANCE_ROLE = 'distance_role'
SCALE_ROLE = 'scale_role'
SHAPE_ROLE = 'shape_role'
PERSPECTIVE_ROLE = 'perspective_role'


FACTOR_IDX_TO_SERIALISED_MAP = {
    OBJECT_HUE: 'object_hue', 
    WALL_HUE: 'wall_hue', 
    X_AXIS: 'x_axis',
    Y_AXIS: 'y_axis',
    CAMERA_HEIGHT: 'camera_height', 
    SCALE: 'scale', 
    SHAPE: 'shape'
}

SEMANTIC_CATEGORY_TO_FAC_IDXS = {
    COLOUR_ROLE: (OBJECT_HUE, WALL_HUE),
    DISTANCE_ROLE: (X_AXIS, Y_AXIS),
    PERSPECTIVE_ROLE: (CAMERA_HEIGHT,),
    SCALE_ROLE: (SCALE,),
    SHAPE_ROLE: (SHAPE,)
}

# object hue colours
WHITE = 0 
GREEN = 1 
RED = 2 
BLUE = 3 
BROWN = 4
OLIVE = 5 

# shapes
CONE = 0 
CUBE = 1
CYLINDER = 2
HEXAGON = 3 
PYRAMID = 4 # pyramid is 4 weird offset problem happening
SPHERE = 5 # FIX OFFSET PROBLEM - make n roles return 6 for the shapes ...

# scale
SMALL = 0 
LARGE = 1 

# camera height 
TOP = 0  # 17
CENTER = 1  # 18
BOTTOM = 2 # 19

# wall hue 
PURPLE = 0 
SEA_GREEN = 1
SALMON = 2 

MID_AXIS = 19

ONE_HOT_PRED_TO_FACTOR = {
    0: 'object_hue',
    1: 'object_hue',
    2: 'object_hue',
    3: 'object_hue', 
    4: 'object_hue', 
    5: 'object_hue', 
    6: 'object_hue', 
    7: 'object_hue', 
    8: 'object_hue',

    9: 'shape', 
    10: 'shape', 
    11: 'shape', 
    12: 'shape', 
    13: 'shape', 
    14: 'shape',

    15: 'scale',
    16: 'scale',

    17: 'camera_height',
    18: 'camera_height',
    19: 'camera_height',

    20: 'wall_hue',
    21: 'wall_hue',
    22: 'wall_hue',
    23: 'wall_hue', 
    24: 'wall_hue', 
    25: 'wall_hue', 
    26: 'wall_hue',
    27: 'wall_hue',
    28: 'wall_hue',

    29: 'x_axis',
    30: 'x_axis',
    31: 'x_axis',
    32: 'x_axis',
    33: 'x_axis',
    34: 'x_axis',
    35: 'x_axis',
    36: 'x_axis',
    37: 'x_axis',
    38: 'x_axis',
    39: 'x_axis',
    40: 'x_axis',
    41: 'x_axis',
    42: 'x_axis',
    43: 'x_axis',
    44: 'x_axis',
    45: 'x_axis',
    46: 'x_axis',
    47: 'x_axis',
    48: 'x_axis',
    49: 'x_axis',
    50: 'x_axis',
    51: 'x_axis',
    52: 'x_axis',
    53: 'x_axis',
    54: 'x_axis',
    55: 'x_axis',
    56: 'x_axis',
    57: 'x_axis', 
    58: 'x_axis',
    59: 'x_axis', 
    60: 'x_axis',
    61: 'x_axis',
    62: 'x_axis',
    63: 'x_axis',
    64: 'x_axis',
    65: 'x_axis',
    66: 'x_axis',
    67: 'x_axis', 
    68: 'x_axis',

    69: 'y_axis',
    70: 'y_axis',
    71: 'y_axis',
    72: 'y_axis',
    73: 'y_axis',
    74: 'y_axis',
    75: 'y_axis',
    76: 'y_axis',
    77: 'y_axis',
    78: 'y_axis',
    79: 'y_axis',
    80: 'y_axis',
    81: 'y_axis',
    82: 'y_axis',
    83: 'y_axis',
    84: 'y_axis',
    85: 'y_axis',
    86: 'y_axis',
    87: 'y_axis',
    88: 'y_axis',
    89: 'y_axis',
    90: 'y_axis',
    91: 'y_axis',
    92: 'y_axis',
    93: 'y_axis',
    94: 'y_axis',
    95: 'y_axis',
    96: 'y_axis',
    97: 'y_axis',
    98: 'y_axis', 
    99: 'y_axis',
    100: 'y_axis', 
    101: 'y_axis', 
    102: 'y_axis', 
    103: 'y_axis',
    104: 'y_axis', 
    105: 'y_axis', 
    106: 'y_axis', 
    107: 'y_axis', 
    108: 'y_axis',
}

ONE_HOT_PRED_TO_SERIALISED = {
    0: 'white',
    1: 'green',
    2: 'red',
    3: 'blue', 
    4: 'brown', 
    5: 'olive', 
    6: 'purple',
    7: 'sea_green',
    8: 'salmon',

    9: 'cone', 
    10: 'cube', 
    11: 'cylinder',
    12: 'hexagon',
    13: 'pyramid', 
    14: 'sphere',

    15: 'small',
    16: 'large',

    17: 'top',
    18: 'center',
    19: 'bottom',

    20: 'purple',
    21: 'sea_green',
    22: 'salmon',
    23: 'white',
    24: 'green',
    25: 'red',
    26: 'blue', 
    27: 'brown', 
    28: 'olive', 

    29: '0/39',
    30: '1/39',
    31: '2/39',
    32: '3/39',
    33: '4/39',
    34: '5/39',
    35: '6/39',
    36: '7/39',
    37: '8/39',
    38: '9/39',
    39: '10/39',
    40: '11/39',
    41: '12/39',
    42: '13/39',
    43: '14/39',
    44: '15/39',
    45: '16/39',
    46: '17/39',
    47: '18/39',
    48: '19/39',
    49: '20/39',
    50: '21/39',
    51: '22/39',
    52: '23/39',
    53: '24/39',
    54: '25/39',
    55: '26/39',
    56: '27/39',
    57: '28/39',
    58: '29/39',
    59: '30/39', 
    60: '31/39',
    61: '32/39', 
    62: '33/39',
    63: '34/39',
    64: '35/39',
    65: '36/39',
    66: '37/39',
    67: '38/39',
    68: '39/39',

    69: '0/39',
    70: '1/39',
    71: '2/39',
    72: '3/39',
    73: '4/39',
    74: '5/39',
    75: '6/39',
    76: '7/39',
    77: '8/39',
    78: '9/39',
    79: '10/39',
    80: '11/39',
    81: '12/39',
    82: '13/39',
    83: '14/39',
    84: '15/39',
    85: '16/39',
    86: '17/39',
    87: '18/39',
    88: '19/39',
    89: '20/39',
    90: '21/39',
    91: '22/39',
    92: '23/39',
    93: '24/39',
    94: '25/39',
    95: '26/39',
    96: '27/39',
    97: '28/39',
    98: '29/39',
    99: '30/39',
    100: '31/39', 
    101: '32/39',
    102: '33/39', 
    103: '34/39', 
    104: '35/39', 
    105: '36/39',
    106: '37/39', 
    107: '38/39', 
    108: '39/39', 
}

def get_role_filler_info(factor_classes: np.array) -> Dict: 
    n_oh_colours = (np.bincount(
        factor_classes[:, OBJECT_HUE].ravel()) != 0).sum() 
    n_wh_colours = (np.bincount(
        factor_classes[:, WALL_HUE].ravel()) != 0).sum() 
    n_axis_distances = (np.bincount(
        factor_classes[:, np.array([X_AXIS, Y_AXIS])].ravel()) != 0).sum() 
    n_camera_perspectives = (np.bincount(
        factor_classes[:, CAMERA_HEIGHT].ravel()) != 0).sum() 
    n_scales = (np.bincount(
        factor_classes[:, SCALE].ravel()) != 0).sum() 

    print(f'n oh colours {n_oh_colours}, n_wh colours {n_wh_colours}')

    m = {SEMANTIC_CATEGORY_TO_FAC_IDXS[COLOUR_ROLE]: n_oh_colours + n_wh_colours, 
            SEMANTIC_CATEGORY_TO_FAC_IDXS[DISTANCE_ROLE]: n_axis_distances,
            SEMANTIC_CATEGORY_TO_FAC_IDXS[PERSPECTIVE_ROLE]: n_camera_perspectives,  
            SEMANTIC_CATEGORY_TO_FAC_IDXS[SCALE_ROLE]: n_scales, 
            SEMANTIC_CATEGORY_TO_FAC_IDXS[SHAPE_ROLE]: 6}
    return dict(sorted(m.items(), key=lambda x: x[0]))


def get_n_fillers_per_role(role_filler_info: Dict) -> np.array: 
    return BaseMetadata.get_n_fillers_per_role(role_filler_info)

# object colour
# Factors	Possible Values
# object_color	white=0, green=1, red=2, blue=3, brown=4, olive=5
# object_shape	cone=0, cube=1, cylinder=2, hexagonal=3, pyramid=4, sphere=5
# object_size	small=0, large=1
# camera_height	top=0, center=1, bottom=2
# background_color	purple=0, sea green=1, salmon=2
# horizontal_axis	0,...,39
# vertical_axis	0,...,39