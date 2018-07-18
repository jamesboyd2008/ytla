# This file contains aspects of YTLA data that are valuable for scientific
# research.

# for text to property conversion, for when they are spelled differently
attributes = {
    'sel1X': 'sel1X', # ints, 0-6, antenna specific
    'sel2X': 'sel2X', # ints, 0-6, antenna specific
    'intswX': 'intswX', # str, e.g. CORRECT INTERRUPT, antenna specific
    'hybrid_selX': 'hybrid_selX', # str, e.g. SRR selected, antenna specific
    'intLenX': 'intLenX', # float, e.g. 5.000, antenna specific
    'sel1Y': 'sel1Y', # ints, e.g. ~13-19, antenna specific
    'sel2Y': 'sel2Y', # ints, e.g. ~13-19, antenna specific
    'intswY': 'intswY', # str, e.g. CORRECT INTERRUPT, antenna specific
    'hybrid_selY': 'hybrid_selY', # str, e.g. SRR NOT SELECTED, antenna specific
    'intLenY': 'intLenY', # float, e.g. 5.000, antenna specific
    'Timestamp': 'timestamp', # str, x value always, not antenna specific
    'NTState': 'nt_state', # str, not antenna specific
    'NTSelect': 'nt_select', # str, not antenna specific
    'LOfreq': 'lo_freq', # single boring float, usually, not antenna specific
    'LOpower': 'lo_power', # single boring float, usually, not antenna specific
    'lfI_X': 'lfI_X', # these plot nicely as lines, antenna specific
    'lfQ_X': 'lfQ_X', # these plot nicely as lines, antenna specific
    'lfI_Y': 'lfI_Y', # these plot nicely as lines, antenna specific
    'lfQ_Y': 'lfQ_Y', # these plot nicely as lines, antenna specific
    'IFLO_X': 'iflo_x', # these plot nicely as lines, antenna specific
    'IFLO_Y': 'iflo_y' # these plot nicely as lines, antenna specific
}
