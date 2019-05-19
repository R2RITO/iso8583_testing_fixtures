from ISO8583.ISO8583 import ISO8583

def get_iso_from_params(params, mti):
    """
    Create an ISO8583 object from a
    dict with bit numbers as keys and
    bit values as values, and return the bitmap
    and the network iso
    :param dict params: dict with the bits and values
    :returns tuple iso: first element is bitmap as str,
                        second element is iso stream
    """
    iso = ISO8583()
    iso.setMTI(str(mti))
    for k, v in params.items():
        iso.setBit(int(k), v)

    return (iso.getBitmap(), iso.getNetworkISO())
