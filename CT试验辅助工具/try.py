from docx import Document

# 读取Word文档
doc = Document('1S1-1S2.docx')  # 替换为你的文件路径




# 遍历文档中的所有表格
for table in doc.tables:
    if '绕组编号' in table.rows[1].cells[2].text:
        cell = table.rows[1].cells[3]
        doc_value_serial= cell.text.split()

    if '额定二次电流' in table.rows[1].cells[0].text:
        cell = table.rows[1].cells[1]
        doc_value_I2e= float(cell.text.split()[0])


    if '电阻' in table.rows[1].cells[0].text:
        cell = table.rows[1].cells[1]
        doc_value_R2= float(cell.text.split()[0])

    if '拐点电压' in table.rows[1].cells[0].text:
        cell = table.rows[1].cells[1]
        doc_value_U2= float(cell.text.split()[0])

    # if '变比' in table.rows[1].cells[0].text:
    #     cell = table.rows[1].cells[1]
    #     parts = cell.text.strip().split(" : ")
    #
    #     # 将"："前的字符串转换为浮点数
    #     number_before_colon = float(parts[0])
    #
    #     # 四舍五入到小数点后
    #     rounded_number = round(number_before_colon/100, 0)*100
    #     doc_value_bianbi=cell.text.strip()




# 如果没有找到值，打印提示信息
