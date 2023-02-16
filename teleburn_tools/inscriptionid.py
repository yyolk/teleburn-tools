from hashlib import sha256

class InscriptionIdValue(bytearray):
    def __init__(self, value):
        super().__init__(value)


class InscriptionId:
    """Represents an InscriptionId like `ord::index::entry`"""
    def __init__(self, txid, index):
        self.txid = txid
        self.index = index

    @classmethod
    def loadb(cls, value: InscriptionIdValue) -> "InscriptionId":
        """Loads a bytearray into an InscriptionId"""
        txid = bytes(value[:32])
        index = int.from_bytes(value[32:], byteorder="big")
        return cls(txid, index)

    def dumpb(self) -> InscriptionIdValue:
        """Dumps an InscriptionId into a bytearray"""
        value = bytearray(36)
        value[:32] = self.txid
        value[32:] = self.index.to_bytes(4, byteorder="big")
        return InscriptionIdValue(value)

    def as_eth_address(self) -> str:
        """Serialize into a usable ETH address"""
        sha = sha256(self.dumpb())
        return f"0x{sha.hexdigest()[:40]}"

def from_txn_index(txn: str, index: int):
    """Construct the InscriptionId correctly, given a txn hex string"""
    return InscriptionId(bytes.fromhex(txn)[::-1], index)

def from_ordinal_id(ordinalid: str):
    """Takes an ``ordinalid`` returns an ``InscriptionId``"""
    txn, index = ordinalid.split("i")
    return from_txn_index(txn, index)

