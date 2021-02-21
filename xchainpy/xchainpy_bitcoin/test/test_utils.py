import pytest
from xchainpy.xchainpy_bitcoin import utils
from xchainpy.xchainpy_bitcoin.models import common
# from xchainpy.xchainpy_util.asset import Asset
# from xchainpy.xchainpy_client.models import tx_types
# from xchainpy.xchainpy_bitcoin.const import *


class TestBitcoinUtils:

    witness = common.Witness_UTXO(
        10000, '0014123f6562aa047dae2d38537327596cd8e9e21932')

    utxo = common.UTXO(hash='7fc1d2c1e4017a6aea030be1d4f5365d11abfd295f56c13615e49641c55c54b8', index=0, witness_utxo=witness,
                       tx_hex='01000000000101233b5e27c30135274523c69c68558dddd265e63d9f2db1953e59c6ba6dc4912e0100000000ffffffff01dc410f0000000000160014ea0b3a147753eaf29d8aa820b335876daa0d61cb02483045022100c324931915f3215cbc4175e196a78b11333dcb08bc929c417bc98645acd638fc022028bb7bbb5da72f630aeba29a76a763407c3a98a7e8809c78ffab02f2d2a4eb0e012102dbc2fa9261379482e9ed484dc2c8b8a3ca7543391de90159a51e1791c4d2271b00000000')
    utxos = [utxo]
    memo = 'SWAP:THOR.RUNE'
    data = utils.compile_memo(memo)

    def test_get_right_vault_fee(self):
        assert utils.get_fee(self.utxos, 10, self.data) == 1890

    def test_get_normal_fee(self):
        assert utils.get_fee(self.utxos, 10) == 1640

    def test_get_minimum_fee_of_1000(self):
        assert utils.get_fee(self.utxos, 1) == 1000