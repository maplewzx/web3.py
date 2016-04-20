from web3.web3.property import Property
import web3.utils.utils as utils

properties = [
    {
        "name": "listening",
        "call": "net_listening",
    },
    {
        "name": "peerCount",
        "call": "net_peerCount",
        "outputFormatter": utils.toDecimal
    }
]

class DB(object):

    def __init__(self, web3):
        self._requestManager = web3._requestManager

        for prop in properties:
            prop = Property(prop)
            prop.attachToObject(self)
            prop.setRequestManager(web3._requestManager)