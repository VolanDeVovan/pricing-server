import json
from scalecodec.type_registry import load_type_registry_file
from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url='wss://mof2.sora.org/',
    type_registry_preset='default',
    type_registry=load_type_registry_file('./custom_types.json'),
)

block_hash = substrate.get_block_hash(block_id=3077347)

extrinsics = substrate.get_block(block_hash=block_hash)['extrinsics']

print('Extrinsincs:', json.dumps([e.value for e in extrinsics], indent=4))

events = substrate.get_events(block_hash)

print("Events:", json.dumps([e.value for e in events], indent=4))
