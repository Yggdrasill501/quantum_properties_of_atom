import scipy.constants

PLANCK_CONSTANT = scipy.constants.Planck

# First experiment

# Errors
OFFSET_MULTIMETER_1 = 3
OFFSET_MULTIMETER_2 = 2

PHOTON_VOLTAGE = {
    """Dictionary from experiment.
    
    :key wavelength: wavelenght of filter,
    :value voltage: voltage of photon.
    """
    "shade1": {
        578: 360,
        546: 514,
        436: 825,
        405: 715,
        365: 1040
        },
    "shade2": {
        578: 665,
        546: 775,
        436: 1155,
        405: 1280,
        365: 1620
        },
    "shade3": {
        578: 550,
        546: 695,
        436: 1174,
        405: 1310,
        365: 1650
        }
}
