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
    # lang_list = ['Bangla']
    if not out_filename:
        out_filename = 'default.pdf'
    print('lang_list: ', lang_list)
    print('outout_filename: ',out_filename)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    # driver = webdriver.Chrome(chrome_options=options)

    output_text = ""
    driver = webdriver.Chrome(chrome_options=options)
    lang_codes = {'Bangla': 'bn', 'Hindi': 'hi', 'Chinese': 'zh-TW', 'Japanese': 'ja'}
    for lang in lang_list:
        ln_code = lang_codes[lang]
        driver.get(f"https://translate.google.com/?sl=auto&tl={ln_code}&text={text}&op=translate")
        time.sleep(5)

        output = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]').text
        output_text += f"\n\n{lang}\n\n"
        output_text += output
        print('language: ', lang)
        print("Translated Paragraph:=> " + output)


    with open(out_filename, 'w+', encoding='UTF-16') as file:
        file.write(output_text)


    driver.close()




