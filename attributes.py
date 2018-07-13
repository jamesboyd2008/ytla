"""
This file contains aspects of YTLA data that are valuable for scientific
research.
"""

# for text to property conversion, for when they are spelled differently
attributes = {
    'sel1X': 'sel1X', # ints, 0-6, antenna specific                                   done
    'sel2X': 'sel2X', # ints, 0-6, antenna specific                                   done
    'intswX': 'intswX', # CORRECT INTERRUPT, antenna specific
    'hybrid_selX': 'hybrid_selX', # SRR selected, antenna specific
    'intLenX': 'intLenX', # 5.000, antenna specific                                   done
    'sel1Y': 'sel1Y', # ints, ~13-19, antenna specific                                done
    'sel2Y': 'sel2Y', # ints, ~13-19, antenna specific                                done
    'intswY': 'intswY', # CORRECT INTERRUPT, antenna specific
    'hybrid_selY': 'hybrid_selY', # SRR NOT SELECTED, antenna specific                something
    'intLenY': 'intLenY', # 5.000, antenna specific                                   done
    'Timestamp': 'timestamp', # x value always, not antenna specific                  good enough, for now
    'NTState': 'nt_state', # bool, not antenna specific                               done
    'NTSelect': 'nt_select', # bool, not antenna specific                             done
    'LOfreq': 'lo_freq', # single boring float, usually, not antenna specific         done
    'LOpower': 'lo_power', # single boring float, usually, not antenna specific       done
    'lfI_X': 'lfI_X', # line_chart_per_antenna, these plot nicely as lines, antenna specific    done
    'lfQ_X': 'lfQ_X', # line_chart_per_antenna, these plot nicely as lines, antenna specific    done
    'lfI_Y': 'lfI_Y', # line_chart_per_antenna, these plot nicely as lines, antenna specific    done
    'lfQ_Y': 'lfQ_Y', # line_chart_per_antenna, these plot nicely as lines, antenna specific    done
    'IFLO_X': 'iflo_x', # line_chart_per_antenna, these plot nicely as lines, antenna specific  done
    'IFLO_Y': 'iflo_y' # line_chart_per_antenna, these plot nicely as lines, antenna specific   done
}
