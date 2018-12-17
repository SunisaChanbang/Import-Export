""" Top 10 of Import """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
def graph():
    """ creat graph Top 10 of Import """
    fp = mpl.font_manager.FontProperties(family='JasmineUPC',size=24)
    x = np.arange(0,10)
    y = [386557057065, 368368395622, 242451971944, 225960095934, 161573560379, 107461232731, 89784502211, 73749349545, 54525219632, 52864743212]
    name = ['เชื้อเพลิงที่ได้จากแร่', 'เครื่องจักรและส่วนประกอบ', 'ยานยนต์และส่วนประกอบ', 'เครื่องอุปกรณ์ไฟฟ้าและส่วนประกอบ', 'เหล็กและเหล็กกล้า', 'พลาสติกและของทำด้วยพลาสติก', 'ของทำด้วยเหล็กหรือเหล็กกล้า', 'ทองแดงละของทำด้วยทองแดง', 'เคมีภัณฑ์เบ็ดเตล็ด', 'อุปกรณ์ที่ใช้ทางทัศนศาสตร์']
    ax = plt.gca(xticks=x)
    ax.set_xticklabels(name,rotation=1000,fontproperties=fp)
    plt.bar(x,y,color='g')
    plt.show()
graph()
