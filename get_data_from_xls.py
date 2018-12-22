import xlrd
import logging

def get_data_from_xls(path_to_xls):
    	
	logging.info('Geting xls file')
	exel_data_file = xlrd.open_workbook(path_to_xls)
	logging.info('[+] Ok')

	sheet = exel_data_file.sheet_by_index(0)

	row_count = sheet.nrows
	af = r = s = p = q = f = g = d = e = ad = ae = ab = ac = x = y = v = w = l = m = j = k = 0
	logging.info('Parsing')
	if row_count > 0:
		for row in range(0,row_count):
			if 'И/М' in str(sheet.cell_value(row, 1)):
				af += sheet.cell_value(row, 5)
			elif sheet.cell_value(row, 1) == '33korovy.com.ua':
				s = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						r += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'Входящий звонок comua':
				q = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						p += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'vetapteka-litarova.com.ua':
				g = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						f += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'Входящий звонок (ветаптека Литарова)':
				e = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						d += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'krolikam.com.ua':
				ae = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						ad += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'Входящий звонок (ветаптека Кроликам)':
				ac = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						ab += 1
					else:
						break
			elif sheet.cell_value(row, 1) == '33korovy.zakupka.com':
				y = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						x += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'Входящий звонок Zakupk':
				w = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						v += 1
					else:
						break
			elif sheet.cell_value(row, 1) == '33korovy.in.ua' or sheet.cell_value(row, 1) == 'Быстрый заказ с 33korovy.in.ua':
				m += sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						l += 1
					else:
						break
			elif sheet.cell_value(row, 1) == 'Входящий звонок 33 Korovy':
				k = sheet.cell_value(row, 5)
				for i in range(1,40):
					if 'Заказ покупателя ЛИТ' in sheet.cell_value(row + i, 1):
						j += 1
					else:
						break
	logging.info('[+] Successful')

	af = float('{:.2f}'.format(af))

	if s == 0:	s == '0,00'
	if q == 0:	q = '0,00'
	if g == 0:	g = '0,00'
	if e == 0:	e = '0,00'
	if ae == 0:	ae = '0,00'
	if ac == 0:	ac = '0,00'
	if y == 0:	y = '0,00'
	if w == 0:	w = '0,00'
	if m == 0:	m = '0,00'
	if k == 0:	k = '0,00'
	
	

	return {'af':af, 's':s, 'r':r, 'q':q, 'p':p, 'g':g, 'j':j, 'k':k, 'f':f, 'e':e, 'd':d, 'ad':ad, 'ae':ae, 'ac':ac, 'ab':ab, 'y':y, 'x':x, 'w':w, 'v':v, 'm':m, 'l':l}

if __name__ == '__main__':
	print(get_data_from_xls('17.xls'))
