import numpy as np
from typing import Dict
from scripts.metadata.base_metadata import BaseMetadata

NC = 1
IMG_SIZE = (3, 64, 64)
N_FACTORS = 5 # after the background colour has been removed

SHAPE = 0
SCALE = 1 
ORIENTATION = 2 
POS_X = 3 
POS_Y = 4

# remove all orientations outside [0, 90) to ensure injective
FACTOR_SIZES = np.array([3, 6, 40, 32, 32]) 
FACTOR_IDX_TO_VALS_MAP = {
                POS_X: np.array([0., 0.03225806, 0.06451613, 0.09677419,
                                       0.12903226, 0.16129032, 0.19354839,
                                       0.22580645, 0.25806452, 0.29032258,

                                       0.32258065, 0.35483871, 0.38709677,
                                       0.41935484, 0.4516129, 0.48387097,
                                       0.51612903, 0.5483871, 0.58064516,
                                       0.61290323, 0.64516129, 0.67741935,
                                       
                                       0.70967742, 0.74193548, 0.77419355,
                                       0.80645161, 0.83870968, 0.87096774,
                                       0.90322581, 0.93548387, 0.96774194, 1.]),
                  POS_Y: np.array([0., 0.03225806, 0.06451613, 0.09677419,
                                    0.12903226, 0.16129032, 0.19354839,
                                    0.22580645, 0.25806452, 0.29032258,
                                    0.32258065, 0.35483871, 0.38709677,
                                    0.41935484, 0.4516129, 0.48387097,
                                    0.51612903, 0.5483871, 0.58064516,
                                    0.61290323, 0.64516129, 0.67741935,
                                    0.70967742, 0.74193548, 0.77419355,
                                    0.70967742, 0.74193548, 0.77419355,
                                    0.80645161, 0.83870968, 0.87096774,
                                    0.90322581, 0.93548387, 0.96774194, 1.]),
                  SCALE: np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.]),
                  ORIENTATION: np.array([0., 0.16110732, 0.32221463, 0.48332195, 0.64442926,
                                         0.80553658, 0.96664389, 1.12775121, 1.28885852,1.44996584, 
                                           1.61107316, 1.77218047,1.93328779, 2.0943951, 2.25550242, 
                                           2.41660973, 2.57771705, 2.73882436, 2.89993168, 3.061039, 
                                           3.22214631,3.38325363, 3.54436094, 3.70546826, 3.86657557, 
                                           4.02768289, 4.1887902, 4.34989752, 4.51100484, 4.67211215, 
                                           4.83321947, 4.99432678, 5.1554341, 5.31654141, 5.47764873, 
                                           5.63875604,5.79986336, 5.96097068, 6.12207799, 6.28318531]),
                  SHAPE: np.array([1., 2., 3.])}

POS_ROLE = 'pos_role'
SCALE_ROLE = 'scale_role'
SHAPE_ROLE = 'shape_role'
ORIENTATION_ROLE = 'orientation_role'

SEMANTIC_CATEGORY_TO_FAC_IDXS = {
    SHAPE_ROLE: (SHAPE,),
    SCALE_ROLE: (SCALE,),
    POS_ROLE: (POS_X, POS_Y),
    ORIENTATION_ROLE: (ORIENTATION,)
}

# sizes 
X_SMALL = 0.5 
SMALL = 0.6
MED_0 = 0.7
MED_1 = 0.8
LARGE = 0.9
X_LARGE = 1

# shapes 
SQUARE = 1
ELLIPSE = 2 
HEART = 3 

# orientation in middle of all seen orientations
CENTER_ORIENTATION = 0.32221463
ORIENTATION_THRESH = 0.64442926

# binned positions (split into a grid 10, 12, 10)
LOWER_START = 0 
LOWER_END = 0.29032258
CENTER_START = 0.32258065
CENTER = 0.48387097
CENTER_END = 0.67741935
UPPER_START = 0.70967742
UPPER_END = 1.


ONE_HOT_PRED_TO_FACTOR = {
    0: 'shape',
    1: 'shape',
    2: 'shape',

    3: 'scale', 
    4: 'scale', 
    5: 'scale', 
    6: 'scale', 
    7: 'scale', 
    8: 'scale', 

    9: 'orientation', 
    10: 'orientation',
    11: 'orientation',
    12: 'orientation',
    13: 'orientation',
    14: 'orientation', 
    15: 'orientation',
    16: 'orientation',
    17: 'orientation',
    18: 'orientation',
    19: 'orientation', 
    20: 'orientation',
    21: 'orientation',
    22: 'orientation',
    23: 'orientation',
    24: 'orientation', 
    25: 'orientation',
    26: 'orientation',
    27: 'orientation',
    28: 'orientation',
    29: 'orientation',
    30: 'orientation',
    31: 'orientation',
    32: 'orientation',
    33: 'orientation',
    34: 'orientation', 
    35: 'orientation',
    36: 'orientation',
    37: 'orientation',
    38: 'orientation',
    39: 'orientation', 
    40: 'orientation',
    41: 'orientation',
    42: 'orientation',
    43: 'orientation',
    44: 'orientation', 
    45: 'orientation',
    46: 'orientation',
    47: 'orientation',
    48: 'orientation', # 49

    49: 'pos_x',
    50: 'pos_x',
    51: 'pos_x',
    52: 'pos_x',
    53: 'pos_x',
    54: 'pos_x',
    55: 'pos_x',
    56: 'pos_x',
    57: 'pos_x',
    58: 'pos_x',
    59: 'pox_x',
    60: 'pox_x',
    61: 'pox_x',
    62: 'pox_x',
    63: 'pox_x',
    64: 'pox_x',
    65: 'pox_x',
    66: 'pox_x',
    67: 'pox_x',
    68: 'pox_x',
    69: 'pox_x',
    70: 'pox_x', 
    71: 'pox_x',
    72: 'pox_x',
    73: 'pox_x',
    74: 'pox_x',
    75: 'pos_x',
    76: 'pos_x',
    77: 'pos_x',
    78: 'pos_x',
    79: 'pos_x',
    80: 'pos_x',

    80: 'pos_y',
    81: 'pox_y',
    82: 'pox_y',
    83: 'pox_y',
    84: 'pox_y',
    85: 'pox_y',
    86: 'pox_y',
    87: 'pox_y',
    88: 'pox_y',
    89: 'pox_y',
    90: 'pox_y',
    91: 'pox_y',
    92: 'pox_y',
    93: 'pox_y',
    94: 'pox_y',
    95: 'pox_y',
    96: 'pox_y',
    97: 'pox_y',
    98: 'pox_y',
    99: 'pox_y',
    100: 'pox_y',
    101: 'pox_y',
    102: 'pox_y',
    103: 'pox_y',
    104: 'pox_y',
    105: 'pox_y',
    106: 'pox_y',
    107: 'pox_y',
    108: 'pox_y',
    109: 'pox_y',
    110: 'pox_y',
    111: 'pos_y',
    112: 'pos_y'

}

ONE_HOT_PRED_TO_SERIALISED = {
    0: 'heart',
    1: 'ellipse', 
    2: 'square',

    3: '0.5',
    4: '0.6',
    5: '0.7',
    6: '0.8',
    7: '0.9',
    8: '1',

    9: '1/40', 
    10: '2/40',
    11: '3/40',
    12: '4/40',
    13: '5/40',
    14: '6/40', 
    15: '7/40',
    16: '8/40',
    17: '9/40',
    18: '10/40',
    19: '11/40', 
    20: '12/40',
    21: '13/40',
    22: '14/40',
    23: '15/40',
    24: '16/40', 
    25: '17/40',
    26: '18/40',
    27: '19/40',
    28: '20/40',
    29: '21/40',
    30: '22/40',
    31: '23/40',
    32: '24/40',
    33: '25/40',
    34: '26/40', 
    35: '27/40',
    36: '28/40',
    37: '29/40',
    38: '30/40',
    39: '31/40', 
    40: '32/40',
    41: '33/40',
    42: '34/40',
    43: '35/40',
    44: '36/40', 
    45: '37/40',
    46: '38/40',
    47: '39/40',
    48: '40/40',

    49: '1/32',
    50: '2/32',
    51: '3/32',
    52: '4/32',
    53: '5/32',
    54: '6/32',
    55: '7/32',
    56: '8/32',
    57: '9/32',
    58: '10/32',
    59: '11/32',
    60: '12/32',
    61: '13/32',
    62: '14/32',
    63: '15/32',
    64: '16/32',
    65: '17/32',
    66: '18/32',
    67: '19/32',
    68: '20/32',
    69: '21/32',
    70: '22/32', 
    71: '23/32',
    72: '24/32',
    73: '25/32',
    74: '26/32',
    75: '27/32',
    76: '28/32',
    77: '29/32',
    78: '30/32',
    79: '31/32',
    80: '32/32',

    81: '1/32',
    82: '2/32',
    83: '3/32',
    84: '4/32',
    85: '5/32',
    86: '6/32',
    87: '7/32',
    88: '8/32',
    89: '9/32',
    90: '10/32',
    91: '11/32',
    92: '12/32',
    93: '13/32',
    94: '14/32',
    95: '15/32',
    96: '16/32',
    97: '17/32',
    98: '18/32',
    99: '19/32',
    100: '20/32',
    101: '21/32',
    102: '22/32',
    103: '23/32',
    104: '24/32',
    105: '25/32',
    106: '26/32',
    107: '27/32',
    108: '28/32',
    109: '29/32',
    110: '30/32',
    111: '31/32',
    112: '32/32'

}
SHAPE_PRED_TO_SERIALISED_MAP = {
    0: 'heart',
    1: 'ellipse', 
    2: 'square',
}
SCALE_PRED_TO_SERIALISED_MAP = {
    0: '0.5',
    1: '0.6',
    2: '0.7',
    3: '0.8',
    4: '0.9',
    5: '1',
}
ORIENTATION_PRED_TO_SERIALISED_MAP = {
    0: '1/40', 
    1: '2/40',
    2: '3/40',
    3: '4/40',
    4: '5/40',
    5: '6/40', 
    6: '7/40',
    7: '8/40',
    8: '9/40',
    9: '10/40',
    10: '11/40', 
    11: '12/40',
    12: '13/40',
    13: '14/40',
    14: '15/40',
    15: '16/40', 
    16: '17/40',
    17: '18/40',
    18: '19/40',
    19: '20/40',
    20: '21/40',
    21: '22/40',
    22: '23/40',
    23: '24/40',
    24: '25/40',
    25: '26/40', 
    26: '27/40',
    27: '28/40',
    28: '29/40',
    29: '30/40',
    30: '31/40', 
    31: '32/40',
    32: '33/40',
    33: '34/40',
    34: '35/40',
    35: '36/40', 
    36: '37/40',
    37: '38/40',
    38: '39/40',
    39: '40/40',
}
POS_X_PRED_TO_SERIALISED_MAP = {
    0: '1/32',
    1: '2/32',
    2: '3/32',
    3: '4/32',
    4: '5/32',
    5: '6/32',
    6: '7/32',
    7: '8/32',
    8: '9/32',
    9: '10/32',
    10: '11/32',
    11: '12/32',
    12: '13/32',
    13: '14/32',
    14: '15/32',
    15: '16/32',
    16: '17/32',
    17: '18/32',
    18: '19/32',
    19: '20/32',
    20: '21/32',
    21: '22/32',
    22: '23/32',
    23: '24/32',
    24: '25/32',
    25: '26/32',
    26: '27/32', 
    27: '28/32',
    28: '29/32',
    29: '30/32',
    30: '31/32',
    31: '32/32',
}

POS_Y_PRED_TO_SERIALISED_MAP = POS_X_PRED_TO_SERIALISED_MAP

FACTOR_IDX_TO_SERIALISED_MAP = {
    POS_X: 'pos_x', 
    POS_Y: 'pos_y',
    SCALE: 'scale',
    SHAPE: 'shape',
    ORIENTATION: 'orientation'
}
IDX_TO_SERIALISED_MAP = {
    SHAPE: SHAPE_PRED_TO_SERIALISED_MAP,
    SCALE: SCALE_PRED_TO_SERIALISED_MAP,
    ORIENTATION: ORIENTATION_PRED_TO_SERIALISED_MAP, 
    POS_X: POS_X_PRED_TO_SERIALISED_MAP,
    POS_Y: POS_Y_PRED_TO_SERIALISED_MAP,
}


def get_role_filler_info(factor_classes: np.array) -> Dict: 
    return BaseMetadata.get_role_filler_info(factors=factor_classes, 
                                             s_category_to_fac_idxs=SEMANTIC_CATEGORY_TO_FAC_IDXS)

def get_n_fillers_per_role(role_filler_info: Dict) -> np.array: 
    return BaseMetadata.get_n_fillers_per_role(role_filler_info)