""" Import Calculator """
import csv
from itertools import groupby
def import_all():
    """ 'import_all is function sum product since 2014-2018'
    num23 = วัตถุดิบใช้ผลิตอาหารสัตว์
    num27 = เชื้อเพลิงที่ได้จากแร่
    num31 = ปุ๋ย
    num38 = เคมีภัณฑ์เบ็ดเตล็ด
    num39 = พลาสติกและของทำด้วยพลาสติก
    num84 = เครื่องจักรและส่วนประกอบ
    num85 = เครื่องอุปกรณ์ไฟฟ้าและส่วนประกอบ
    num87 = ยานยนต์และส่วนประกอบ
    num72 = เหล็กและเหล็กกล้า
    num73 = ของทำด้วยเหล็กหรือเหล็กกล้า
    num74 = ทองแดงละของทำด้วยทองแดง
    num76 = อลูมิเนียมและของทำด้วยอลูมิเนียม
    num90 = อุปกรณ์ที่ใช้ทางทัศนศาสตร์
    num = อื่นๆ
    thai_export = มูลค่าส่งเข้าของไทย
    total_baht = รวมมูลค่าเงินส่งเข้า
    total_duty = รวมอากรขาเข้า
    tal_weight = รวมน้ำหนัก
    """
 years = range(2557, 2561)
    for year in years:
        path = 'export%d.txt' % year
        file = open(path)
        data = csv.reader(file)
        table = [row for row in data]
        table[:4]

    thai_baht_import = groupby(table, lambda x: x[1])
    for key, group in thai_baht_import:
       total_baht = 0
       total_duty = 0
       total_weight = 0
       for item in group:
           total_baht += int(item[2])
           total_duty += int(item[3])
           total_weight += int(item[4])
           print(item[1], total_baht, total_duty, total_weight)
import_all()
