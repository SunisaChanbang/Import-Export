""" Top 10 of Export """
import pygal
def graph():
    """ creat graph Top 10 of Export """

    line_chart = pygal.Bar(legend_at_bottom=True)
    line_chart.title = 'Export Graph (มีหน่วยเป็น ล้านบาท)'
    line_chart.add('ยานยนต์และส่วนประกอบ', 868901)
    line_chart.add('เครื่องจักรและส่วนประกอบ', 868901)
    line_chart.add('พลาสติกและของทำด้วยพลาสติก', 340409)
    line_chart.add('เครื่องอุปกรณ์ไฟฟ้าและส่วนประกอบ', 340409)
    line_chart.add('ยางและของทำด้วยาง', 147046)
    line_chart.add('ของปรุงแต่งจากเนื้อสัตว์ ปลา', 147046)
    line_chart.add('เชื้อเพลิงที่ได้จากแร่', 80262)
    line_chart.add('เคมีภัณฑ์อินทรีย์', 80262)
    line_chart.add('ของทำด้วยเหล็กหรือเหล็กกล้า', 80262)
    line_chart.add('ข้าว', 80262)
    line_chart.render_to_file("C:/Users/Desktop/Aom/graph_two.svg")
graph()
