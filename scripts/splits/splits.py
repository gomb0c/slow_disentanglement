# SPLITS - ALL 
R2E_RANDOM = 'recomb_to_element_random'
SCHOTT_SPLIT = 'schott_split'

# DSPRITES SPLITS 
DSPRITES_R2R_SH_SQ_POS_X = 'recomb_to_range_sh_sq_pos_x'
DSPRITES_R2R_SH_EL_POS_X = 'recomb_to_range_sh_el_pos_x'
DSPRITES_R2R_SH_SQ_SCALE = 'recomb_to_range_sh_sq_scale'
DSPRITES_R2R_SH_SQ_POS_X_CENTERED = 'recomb_to_range_sh_sq_pos_x_centered'
DSPRITES_R2R_SH_SQ_POS_X_FLANKED = 'recomb_to_range_sh_sq_pos_x_flanked'
DSPRITES_R2R_SH_SQ_POS_X_RSHIFT = 'recomb_to_range_sh_sq_pos_x_rshift'
DSPRITES_R2R_SH_SQ_POS_X_LSHIFT = 'recomb_to_range_sh_sq_pos_x_lshift'

# SHAPES3D SPLITS 
SHAPES3D_R2R_OH_WH = 'recomb_to_range_oh_wh' # original Montero 0.06 unseen
SHAPES3D_R2R_OSH_FH = 'recomb_to_range_osh_fh' # orig 0.125 unseen 
SHAPES3D_R2R_OSH_OH = 'recomb_to_range_osh_oh' # orig 0.125 unseen

SHAPES3D_R2R_OSH_OSZ1 = 'recomb_to_range_osh_osz1' # custom 0.15625 unseen 
SHAPES3D_R2R_OSH_OSZ2 = 'recomb_to_range_osh_osz2'# custom 0.21875 unseen 
SHAPES3D_R2R_OSH_OH1 = 'recomb_to_range_osh_oh1'# custom
SHAPES3D_R2R_OSH_OH2 = 'recomb_to_range_osh_oh2'# custom 
SHAPES3D_R2R_OSZ_OH = 'recomb_to_range_osz_oh'# custom 0.0375 unseen 

# MPI3D SPLITS 
MPI3D_R2R_OSH_YAXIS = 'recomb_to_range_osh_yaxis' # original
MPI3D_R2R_OSH_WH1 = 'recomb_to_range_osh_wh1'# original
MPI3D_R2R_OSH_WH2 = 'recomb_to_range_osh_wh2'# original
MPI3D_R2R_OH_WH = 'recomb_to_range_oh_wh'# original

MPI3D_R2R_OSH_OSZ1 = 'recomb_to_range_osh_osz1' 
MPI3D_R2R_OSH_OSZ2 = 'recomb_to_range_osh_osz2'
MPI3D_R2R_CH_OSH1 = 'recomb_to_range_ch_osh1'
MPI3D_R2R_CH_OSH2 = 'recomb_to_range_ch_osh2'
MPI3D_R2R_CH_YAXIS1 = 'recomb_to_range_ch_yaxis1' # 
MPI3D_R2R_CH_YAXIS2 = 'recomb_to_range_ch_yaxis2' # 0.33 




DSPRITES_DATASET_SPLIT_CHOICES = [
    DSPRITES_R2R_SH_SQ_POS_X,
    DSPRITES_R2R_SH_EL_POS_X,
    DSPRITES_R2R_SH_SQ_SCALE,
    DSPRITES_R2R_SH_SQ_POS_X_CENTERED,
    DSPRITES_R2R_SH_SQ_POS_X_FLANKED,
    DSPRITES_R2R_SH_SQ_POS_X_RSHIFT,
    DSPRITES_R2R_SH_SQ_POS_X_LSHIFT,
    SCHOTT_SPLIT,

]

SHAPES3D_DATASET_SPLIT_CHOICES = [    
    SHAPES3D_R2R_OH_WH, 
    SHAPES3D_R2R_OSH_FH, 
    SHAPES3D_R2R_OSH_OH,
    SHAPES3D_R2R_OSH_OSZ1, 
    SHAPES3D_R2R_OSH_OSZ2,
    SHAPES3D_R2R_OSH_OH1,
    SHAPES3D_R2R_OSH_OH2,
    SHAPES3D_R2R_OSZ_OH,
    SCHOTT_SPLIT
]

MPI3D_DATASET_SPLIT_CHOICES = [
    MPI3D_R2R_OSH_YAXIS,
    MPI3D_R2R_OSH_WH1,
    MPI3D_R2R_OSH_WH2,
    MPI3D_R2R_OH_WH,
    MPI3D_R2R_OSH_OSZ1,
    MPI3D_R2R_OSH_OSZ2,
    MPI3D_R2R_CH_OSH1,
    MPI3D_R2R_CH_OSH2,
    MPI3D_R2R_CH_YAXIS1,
    MPI3D_R2R_CH_YAXIS2,
    SCHOTT_SPLIT,
]

SPLIT_CHOICES = DSPRITES_DATASET_SPLIT_CHOICES + SHAPES3D_DATASET_SPLIT_CHOICES + MPI3D_DATASET_SPLIT_CHOICES + [R2E_RANDOM]

from scripts.splits.dsprites_split import DSpritesSplits

dsprites_cg_splits = {
    R2E_RANDOM: DSpritesSplits.recomb_to_element_random, 

    DSPRITES_R2R_SH_SQ_POS_X: DSpritesSplits.recomb_to_range_sh_sq_pos_x,
    DSPRITES_R2R_SH_EL_POS_X: DSpritesSplits.recomb_to_range_sh_el_pos_x,
    DSPRITES_R2R_SH_SQ_SCALE: DSpritesSplits.recomb_to_range_sh_sq_scale,
    DSPRITES_R2R_SH_SQ_POS_X_CENTERED: DSpritesSplits.recomb_to_range_sh_sq_pos_x_centered,
    DSPRITES_R2R_SH_SQ_POS_X_FLANKED: DSpritesSplits.recomb_to_range_sh_sq_pos_x_flanked,
    DSPRITES_R2R_SH_SQ_POS_X_RSHIFT: DSpritesSplits.recomb_to_range_sh_sq_pos_x_rshift,
    DSPRITES_R2R_SH_SQ_POS_X_LSHIFT: DSpritesSplits.recomb_to_range_sh_sq_pos_x_lshift,
    SCHOTT_SPLIT: DSpritesSplits.schott_split,
}

from scripts.splits.shapes3d_split import Shapes3DSplits

shapes3d_cg_splits = {
    R2E_RANDOM: Shapes3DSplits.recomb_to_element_random, 
    
    SHAPES3D_R2R_OH_WH: Shapes3DSplits.recomb_to_range_oh_wh, # orig
    SHAPES3D_R2R_OSH_FH: Shapes3DSplits.recomb_to_range_osh_fh, # orig
    SHAPES3D_R2R_OSH_OH: Shapes3DSplits.recomb_to_range_osh_oh,  # orig
   
    SHAPES3D_R2R_OSH_OSZ1: Shapes3DSplits.recomb_to_range_osh_osz1,
    SHAPES3D_R2R_OSH_OSZ2: Shapes3DSplits.recomb_to_range_osh_osz2,
    SHAPES3D_R2R_OSH_OH1: Shapes3DSplits.recomb_to_range_osh_oh1, 
    SHAPES3D_R2R_OSH_OH2: Shapes3DSplits.recomb_to_range_osh_oh2,
    SHAPES3D_R2R_OSZ_OH: Shapes3DSplits.recomb_to_range_osz_oh,
    SCHOTT_SPLIT: Shapes3DSplits.schott_split, 
}

from scripts.splits.mpi3d_split import MPI3DSplits

mpi3d_cg_splits = {
    # RANDOM 
    R2E_RANDOM: MPI3DSplits.recomb_to_element_random, 

    MPI3D_R2R_OSH_YAXIS: MPI3DSplits.recomb_to_range_osh_yaxis, 
    MPI3D_R2R_OSH_WH1: MPI3DSplits.recomb_to_range_osh_wh1, 
    MPI3D_R2R_OSH_WH2: MPI3DSplits.recomb_to_range_osh_wh2, 
    MPI3D_R2R_OH_WH: MPI3DSplits.recomb_to_range_oh_wh,

    MPI3D_R2R_OSH_OSZ1: MPI3DSplits.recomb_to_range_osh_osz1,  
    MPI3D_R2R_OSH_OSZ2: MPI3DSplits.recomb_to_range_osh_osz2, 
    MPI3D_R2R_CH_OSH1: MPI3DSplits.recomb_to_range_ch_osh1,
    MPI3D_R2R_CH_OSH2: MPI3DSplits.recomb_to_range_ch_osh2,
    MPI3D_R2R_CH_YAXIS1: MPI3DSplits.recomb_to_range_ch_yaxis1,
    MPI3D_R2R_CH_YAXIS2: MPI3DSplits.recomb_to_range_ch_yaxis2,
    SCHOTT_SPLIT: MPI3DSplits.schott_split,
}


#OSH_OH = 'OSH_OH'
#OSH_OSZ = 'OSH_OSZ'
#OSH_WH = 'OSH_WH'
#OSZ_OH = 'OSZ_OH'
#
#OSH_WH_FH = 'OSH_WH_FH'
#OSH_OH_OSZ = 'OSH_OH_OSZ'
#OSH_FH_OSZ = 'OSH_FH_OSZ'
#OSH_OH_OSZ_WH = 'OSH_OH_OSZ_WH'
#OSH_OSZ_FH = 'OSH_OSZ_FH'
#
#RANDOM = 'RANDOM'
#
#FH_OH = 'FH_OH'
#FH_WH = 'FH_WH'
#FH_WH = 'FH_WH'
#EXT = 'EXT'
#OH_WH = 'OH_WH'
#OSH_FH = 'OSH_FH'

#SHAPES3D_SPLIT_TYPE_TO_PARENT = {
#    # SHAPES 3D MONTERO SPLITS
#    SHAPES3D_R2R_OH_WH: OH_WH, 
#    SHAPES3D_R2R_OSH_FH: OSH_FH, 
#    SHAPES3D_R2R_OSH_OH: OSH_OH, 
#    SHAPES3D_R2R_OSH_OSZ_1: OSH_OSZ,
#    SHAPES3D_R2R_OSH_OSZ_2: OSH_OSZ,
#    SHAPES3D_R2R_OSH_OH_1: OSH_OH, 
#    SHAPES3D_R2R_OSH_OH_2: OSH_OH, 
#    SHAPES3D_R2R_OSZ_OH: OSZ_OH,
#}