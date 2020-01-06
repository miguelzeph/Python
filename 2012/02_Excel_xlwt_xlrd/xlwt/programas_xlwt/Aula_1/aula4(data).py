#!/usr/bin/env python
# -*- coding: windows-1251 -*-
# Copyright (C) 2005 Kiseliov Roman

from xlwt import *
from datetime import datetime

w = Workbook()
sheet = w.add_sheet('aula4')

fmts = ['M/D/YY','D-MMM-YY','D-MMM','MMM-YY','h:mm AM/PM','h:mm:ss AM/PM','h:mm',
			'h:mm:ss','M/D/YY h:mm','mm:ss','[h]:mm:ss','mm:ss.0',]

i = 0
for data in fmts:
	sheet.write(i, 0, data)
	
	style = XFStyle()
	
	style.num_format_str = data
	
	sheet.write(i, 1, datetime.now(), style)
	
	i += 1#i = i+1

w.save('aula4(date).ods')
