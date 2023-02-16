import ctypes

class InscriptionIdValue(ctypes.Structure):
    _fields_ = [('data', ctypes.c_ubyte * 36)]

class InscriptionId:
    """Represents an InscriptionId like `ord::index::entry`"""
    def __init__(self, txid, index):
        self.txid = txid
        self.index = index

    @staticmethod
    def loadb(value: InscriptionIdValue) -> 'InscriptionId':
        txid = bytes(value.data[:32])
        index = int.from_bytes(value.data[32:], byteorder='big')
        return InscriptionId(txid, index)

    def dumpb(self) -> InscriptionIdValue:
        value = InscriptionIdValue()
        value.data[:32] = self.txid
        value.data[32:] = self.index.to_bytes(4, byteorder='big')
        return value


def from_txn_index(txn: str, index: int):
    """Construct the InscriptionId correctly, given a txn hex string"""
    return InscriptionId(bytes.fromhex(txn)[::-1], index)

def from_ordinal_id(ordinalid: str):
    """Takes an ``ordinalid`` returns an ``InscriptionId``"""
    txn, index = ordinalid.split("i")
    return from_txn_index(txn, index)
