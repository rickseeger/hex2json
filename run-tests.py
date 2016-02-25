#!/usr/bin/python2.7

import unittest
from common import convert
 
class TestDeserialize(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_deserialize_on_valid_tx(self):

        # test convert real bitcoin tx https://blockchain.info/tx-index/b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da?format=hex
        tx_hex = '010000000101820e2169131a77976cf204ce28685e49a6d2278861c33b6241ba3ae3e0a49f020000008b48304502210098a2851420e4daba656fd79cb60cb565bd7218b6b117fda9a512ffbf17f8f178022005c61f31fef3ce3f906eb672e05b65f506045a65a80431b5eaf28e0999266993014104f0f86fa57c424deb160d0fc7693f13fce5ed6542c29483c51953e4fa87ebf247487ed79b1ddcf3de66b182217fcaf3fcef3fcb44737eb93b1fcb8927ebecea26ffffffff02805cd705000000001976a91429d6a3540acfa0a950bef2bfdc75cd51c24390fd88ac80841e00000000001976a91417b5038a413f5c5ee288caa64cfab35a0c01914e88ac00000000'
       
        correct_result = '{"ins":[{"outpoint":{"hash":"9fa4e0e33aba41623bc3618827d2a6495e6828ce04f26c97771a1369210e8201","index":2},"script":"48304502210098a2851420e4daba656fd79cb60cb565bd7218b6b117fda9a512ffbf17f8f178022005c61f31fef3ce3f906eb672e05b65f506045a65a80431b5eaf28e0999266993014104f0f86fa57c424deb160d0fc7693f13fce5ed6542c29483c51953e4fa87ebf247487ed79b1ddcf3de66b182217fcaf3fcef3fcb44737eb93b1fcb8927ebecea26","sequence":4294967295}],"locktime":0,"outs":[{"script":"76a91429d6a3540acfa0a950bef2bfdc75cd51c24390fd88ac","value":98000000},{"script":"76a91417b5038a413f5c5ee288caa64cfab35a0c01914e88ac","value":2000000}],"version":1}'

        tx_json = convert(tx_hex, is_compact=True)
        self.assertEqual(tx_json, correct_result)
 

if __name__ == '__main__':
    unittest.main()

