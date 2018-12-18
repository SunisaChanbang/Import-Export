""" Top 10 of Import """
import pygal
def graph():
    """ creat graph Top 10 of Import """

    line_chart = pygal.Bar(legend_at_bottom=True)
    line_chart.title = 'Import Graph (มีหน่วยเป็น ล้านบาท)'
    line_chart.add('เชื้อเพลิงที่ได้จากแร่', 386557)
    line_chart.add('เครื่องจักรและส่วนประกอบ', 368368)
    line_chart.add('ยานยนต์และส่วนประกอบ', 242451)
    line_chart.add('เครื่องอุปกรณ์ไฟฟ้าและส่วนประกอบ', 225960)
    line_chart.add('เหล็กและเหล็กกล้า', 161573)
    line_chart.add('พลาสติกและของทำด้วยพลาสติก', 107461)
    line_chart.add('ของทำด้วยเหล็กหรือเหล็กกล้า', 89784)
    line_chart.add('ทองแดงละของทำด้วยทองแดง', 73749)
    line_chart.add('เคมีภัณฑ์เบ็ดเตล็ด', 54525)
    line_chart.add('อุปกรณ์ที่ใช้ทางทัศนศาสตร์', 52864)
    line_chart.render_to_file("C:/Users/atomic ARM/Desktop/Aom/graph_one.svg")
graph()
