# -*- coding: utf-8 -*-
from tqdm import tqdm
table = '0123456789'
for i1 in tqdm(table):
	for i2 in tqdm(table):
		for i3 in table:
			for i4 in table:
				for i5 in table:
					for i6 in table:
						for i7 in table:
							for i8 in table:
								for i9 in table:
									for i10 in table:
										tmp = i1+i2+i3+i4+i5+i6+i7+i8
										ReR = int(tmp,16)+0x3
										ReL = int((i9 + i10)*4,16)+0x3A5B0D91
										ReR = ReR & 0xffffffff
										ReL = ReL & 0xffffffff
										if ReR^ReL == 0x405004A1:
											ReL = int((i9+i10)*4,16)+0xFA0B0759
											ReR = int(tmp,16)+0x2
											ReL = ReL & 0xffffffff
											ReR = ReR & 0xffffffff
											if ReL^ReR == 0x00000278:
												print tmp+i9+i10
												print 'success'