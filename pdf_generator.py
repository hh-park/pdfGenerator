#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from fpdf import FPDF
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import ScalarFormatter

WIDTH = 210
HEIGHT = 297

class PdfGenerator():
    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def run(self):

        # initial setting
        pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
        pdf.add_page()
        pdf.add_font('malgun', '', 'malgun.ttf', uni=True)

        # generate charts
        df = pd.read_csv('annual_sales.csv')
        imageList = ['res/inspection.png','res/inspection2.png', 'res/inspection3.png']
        for i in imageList:
            self.generate_plot(df, i)
        # generate pdf
        self.generate_pdf(pdf)
        pdf.output('unicode.pdf', 'F')

    def generate_pdf(self, pdf):

        # HEADER
        pdf.set_font('malgun', '', 14)
        pdf.cell(self.WIDTH - 130)
        pdf.write(8, u'일일 점검 리포트')
        pdf.ln(10)

        # Date
        d = datetime.now()
        yd = d - timedelta(1)
        insp_date_str = u'점검 날짜:'
        pdf.set_font('malgun', '', 8)
        pdf.write(5, f'{insp_date_str}: {yd} ~ {d}')
        pdf.ln(10)

        # BODY
        self.write_title(pdf, u'1. 형성 점검 결과')
        pdf.image('res/inspection.png', 5, 35, 70, 60)
        pdf.image('res/inspection.png', 70, 35, 70, 60)
        pdf.image('res/inspection.png', 140, 35, 70, 60)
        pdf.ln(65)

        self.write_title(pdf, u'2. 자동 점검 결과')
        pdf.ln(120)


        self.write_title(pdf, u'3. to-do list')
        pdf.ln(30)


        self.write_title(pdf, u'4. 일주일 내 비정상 발생 건수')
        pdf.ln(20)


        self.write_title(pdf, u'5. 비정상 점검 결과 상세 정보')
        pdf.ln(10)

    def write_title(self,pdf, txt):

        pdf.set_text_color(r=0, g=0, b=0)
        pdf.set_font('malgun', '', 12)
        pdf.write(5, txt)

    def generate_plot(self, df, filename):

        # print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Serif' in f.name])
        plt.rcParams["font.family"] = 'Malgun Gothic'

        # Create subplot and bar
        fig, ax = plt.subplots()
        ax.plot(df['Year'].values, df['Total'].values, label=u'이번달', color="#E63946", marker='D')
        plt.legend()

        ax.set_title('CPU 사용률', fontweight="bold", fontsize=30, pad=30) # 제목 띄우려고 pad 값 설정함
        # ax.set_xticklabels(df['Year'].values, rotation=90)
        plt.xticks(df['Year'].values, fontsize=12)
        ax.set_ylabel('비정상 장비수', fontsize=20, rotation=90)

        # Save the plot as a PNG
        plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=1)

        plt.show()

if __name__ == "__main__":

    test = PdfGenerator()
    test.run()