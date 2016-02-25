
import sys, re, json 
from transaction import deserialize


# converts hex to JSON string, returns None on failure
def convert(tx_hex, is_compact=False):

    tx_dict = None
    try:
        tx_dict = deserialize(tx_hex)
    except:
        sys.stderr.write('couldn\'t deserialize invalid hex value: {}'.format(tx_hex))
        return None

    # compact version
    tx_json = None
    if is_compact:
        try:
            tx_json = re.sub('\s+', '', json.dumps(tx_dict, sort_keys=True))
        except:
            sys.stderr.write('couldn\'t parse invalid json: {}\n'.format(tx_hex))
            return None

    # formatted version
    else:
        tx_json = json.dumps(tx_dict, indent=4, separators=(',', ': '))
        
            
    return tx_json
