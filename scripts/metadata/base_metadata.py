import abc 
import numpy as np 
from typing import Dict, Tuple
import logging 

logging.basicConfig(level=logging.INFO)

class BaseMetadata(abc.ABC): 

    @staticmethod 
    def get_role_filler_info(factors: np.array, s_category_to_fac_idxs: Dict[str, Tuple]) -> Dict[Tuple, int]:
        m = {}  

        for s_category, fac_idxs in s_category_to_fac_idxs.items(): 
            n_fillers = (np.bincount(
                factors[:, np.array([fac_idxs])].ravel()) != 0).sum()
            m[fac_idxs] = n_fillers
            logging.info(f'For semantic category {s_category}, there are {n_fillers} fillers')
        logging.info(f'Total # fillers is {sum(m.values())}')
        return dict(sorted(m.items(), key=lambda x: x[0]))
    
    @staticmethod 
    def get_n_fillers_per_role(role_filler_info: Dict[Tuple, int]) -> np.array: 

        n_fillers_per_fac = np.zeros(shape=len(list(sum(role_filler_info.keys(), ()))))
    
        for fac_idxs, n_fillers in role_filler_info.items(): 
            n_fillers_per_fac[np.array(fac_idxs)] = n_fillers
        
        return np.array(n_fillers_per_fac).astype(np.int64)
    