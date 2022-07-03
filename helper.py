from selenium import webdriver
from selenium.webdriver.common.by import By

from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

from fpdf import FPDF

import time

def translateDataAndMakePDF(json_data, out_filename):
    text = json_data['text']
    lang_list = json_data['languages']
    if not out_filename:
        out_filename = 'default.pdf'
    print('lang_list: ', lang_list)
    print('outout_filename: ',out_filename)

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")

    # driver = webdriver.Chrome(chrome_options=options)
    # driver.implicitly_wait(10)

    output_text = ""
    # driver = webdriver.Chrome()
    # lang_codes = {'Bangla': 'bn', 'Hindi': 'hi', 'Chinese': 'zh-TW', 'Japanese': 'ja'}
    # for lang in lang_list:
    #     ln_code = lang_codes[lang]
    #     driver.get(f"https://translate.google.com/?sl=auto&tl={ln_code}&text={text}&op=translate")
    #     time.sleep(5)

    #     output = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]').text
    #     output_text += f"\n\n{lang}\n\n"
    #     output_text += output
    #     print('language: ', lang)
    #     print("Translated Paragraph:=> " + output)


    writer = PdfFileWriter() 
    reader = PdfFileReader(open('output.txt', 'rb')) 
    writer.addPage(reader.getPage(0))
    # writer.addPage(reader.getPage(1))
    # writer.addPage(reader.getPage(2))

    writer.setPageMode('/FullScreen')

    output = open('NewGrades.pdf','wb') 
    writer.write(output) 
    output.close()


    # with open('output.txt', 'w+', encoding='utf-8') as file:
    #     file.write(output_text)


    # pdf = FPDF(orientation='P', unit='mm', format='A4')
    # pdf.add_page()
    # pdf.set_font("Arial", size=20)
    # pdf.cell(200, 10, txt=output_text, ln=1, align="L")
    # pdf.output(out_filename)


    # canvas = Canvas(out_filename)
    # canvas.drawString(72, 72, output_text)
    # canvas.save()


    # driver.close()

    translateDataAndMakePDF('so' 'on')



