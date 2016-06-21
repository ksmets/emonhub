import unittest

from interfacers.Cargo import new_cargo
from interfacers.influx_format import convert_cargo_to_influx_line_format


class InfluxFormatTestCase(unittest.TestCase):

    def test_influx_format(self):
        cargo = new_cargo(rawdata='0,0,0,0,0,0,0,0,0,0,1', nodename='emonpi', names=['power1','power2','power1pluspower2','vrms','t1','t2','t3','t4','t5','t6', 'pulsecount'], realdata=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], nodeid=5, timestamp=1466254323.244743168, scales=[1, 1, 1, 0.01, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1], enabled=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        payload = convert_cargo_to_influx_line_format(cargo)
        self.assertEquals(payload, u'power1,nodeid=5,nodename=emonpi value=0i 1466254323244743168\npower2,nodeid=5,nodename=emonpi value=0i 1466254323244743168\npower1pluspower2,nodeid=5,nodename=emonpi value=0i 1466254323244743168\nvrms,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt1,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt2,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt3,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt4,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt5,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt6,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\npulsecount,nodeid=5,nodename=emonpi value=1i 1466254323244743168\nrssi,nodeid=5,nodename=emonpi value=0i 1466254323244743168\n')

    def test_influx_format_all_enabled(self):
        cargo = new_cargo(rawdata='0,0,0,0,0,0,0,0,0,0,1', nodename='emonpi', names=['power1','power2','power1pluspower2','vrms','t1','t2','t3','t4','t5','t6', 'pulsecount'], realdata=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], nodeid=5, timestamp=1466254323.244743168, scales=[1, 1, 1, 0.01, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1])
        payload = convert_cargo_to_influx_line_format(cargo)
        self.assertEquals(payload, u'power1,nodeid=5,nodename=emonpi value=0i 1466254323244743168\npower2,nodeid=5,nodename=emonpi value=0i 1466254323244743168\npower1pluspower2,nodeid=5,nodename=emonpi value=0i 1466254323244743168\nvrms,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt1,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt2,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt3,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt4,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt5,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt6,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\npulsecount,nodeid=5,nodename=emonpi value=1i 1466254323244743168\nrssi,nodeid=5,nodename=emonpi value=0i 1466254323244743168\n')

    def test_influx_format_some_enabled(self):
        cargo = new_cargo(rawdata='0,0,0,0,0,0,0,0,0,0,1', nodename='emonpi', names=['power1','power2','power1pluspower2','vrms','t1','t2','t3','t4','t5','t6', 'pulsecount'], realdata=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], nodeid=5, timestamp=1466254323.244743168, scales=[1, 1, 1, 0.01, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1], enabled=[1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0])
        payload = convert_cargo_to_influx_line_format(cargo)
        self.assertEquals(payload, u'power1,nodeid=5,nodename=emonpi value=0i 1466254323244743168\nvrms,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nt1,nodeid=5,nodename=emonpi value=0.0 1466254323244743168\nrssi,nodeid=5,nodename=emonpi value=0i 1466254323244743168\n')

if __name__ == '__main__':
    unittest.main()
