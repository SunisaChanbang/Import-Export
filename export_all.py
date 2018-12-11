""" export Calculator """
import csv
from itertools import groupby
def export_all():
    """ 'export_all is function sum product since 2014-2018' 
	num10 = ข้าว
	num16 = ของปรุงแต่งจากเนื้อสัตว์ ปลา
	num20 = ของปรุงแต่งทำจากพืชผัก ผลไม้ ลูกนัต
	num27 = เชื้อเพลิงที่ได้จากแร่
	num29 = เคมีภัณฑ์อินทรีย์
	num39 = พลาสติกและของทำด้วยพลาสติก
	num40 = ยางและของทำด้วยาง
	num73 = ของทำด้วยเหล็กหรือเหล็กกล้า
	num84 = เครื่องจักรและส่วนประกอบ
	num85 = เครื่องอุปกรณ์ไฟฟ้าและส่วนประกอบ
	num87 = ยานยนต์และส่วนประกอบ
	num = อื่นๆ
	thai_baht_export = มูลค่าเงินส่งออก
    """
    years = range(2557, 2561)
    for year in years:
        path = 'export%d.txt' % year
        file = open(path)
        data = csv.reader(file)
        table = [row for row in data]
        table[:4]

    thai_export = groupby(table, lambda x: x[1])
    for key, group in thai_export:
       total_baht = 0
       total_duty = 0
       for item in group:
           total_baht += int(item[2])
           total_duty += int(item[3])
           print(item[1], total_baht, total_duty)
export_all()
