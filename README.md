# teleburn-tools
Tools for teleburning.

This is a rough draft at a better package that can be used and include other
mappings. Right now there is only a hack on the data structure in
`teleburn_tools.inscriptionid` to form the data correctly and load it correctly
from a user who is likely only dealing with strings.


## Examples

The emblematic example is simply providing an `ordinalid` and getting an ETH
address in return. This is for the case of inscribing and then teleburning.
```
from teleburn_tools import * 

# we have an ordinalid after inscribing
genesis_ordinalid = "6fb976ab49dcec017f1e201e84395983204ae1a7c2abf7ced0a85d692e442799i0"
inscription_from_ordinalid = from_ordinalid(genesis_ordinalid)
inscription_from_ordinalid.as_eth_address()
>>> 0xe43a06530bdf8a4e067581f48fae3b535559da9e
```


Another convenience is if you have a transaction and index. 
This can be useful for teleburning to other chains in the future.
```
known_txn = "6fb976ab49dcec017f1e201e84395983204ae1a7c2abf7ced0a85d692e442799"
known_index = 0
# we know a txn and we write in the index manually
inscription_from_known_txn_known_index = from_txn_index(txn, 0)
inscription_from_known_txn_known_index.as_eth_address()
>>> 0xe43a06530bdf8a4e067581f48fae3b535559da9e
```
