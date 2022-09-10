from rflib import *

d = RfCat(idx=0)

d.setMdmModulation(MOD_ASK_OOK)
d.setFreq(433920000)
d.setMdmSyncMode(0)
d.setMdmDRate(1000)
d.setMaxPower()

# Message sent 7x
# Signal in hex eeeeeeeeeeeabaeeeeeea
# Signal in binary 11101110111011101110111011101110111011101110101010111010111011101110111011101110101 
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xee\xee\xa0')

# Message sent 7 times
# Signal eeeeeeeeeeeabaeeeeab8
# Signal in binary 111011101110111011101110111011101110111011101010101110101110111011101110101010111

d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')
d.RFxmit(b'\xee\xee\xee\xee\xee\xea\xba\xee\xeb\xae\x80')