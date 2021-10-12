#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import pdfkit

config = pdfkit.configuration(wkhtmltopdf='c:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
options = {
    'page-size': 'A4',
    'margin-top': '10mm',
    'margin-bottom': '10mm',
    'margin-right': '10mm',
    'margin-left': '10mm',
    'encoding': "UTF-8",
    'no-outline': None
}

class PdfGenerator():

    def __init__(self):
        plt.rcParams["font.family"] = 'Malgun Gothic'

    def run(self):

        df = pd.read_csv('annual_sales.csv')
        imageList = ['res/grp_alert.png', 'res/total_alert.png', 'res/total_hist.png', 'res/cpu_trend.png',
                     'res/fan_trend.png', 'res/port_trend.png']

        for i in imageList:
            if 'trend' in i:
                self.generate_plot(df, i)
            elif 'alert' in i:
                self.horizontal_bar(df, i)
            else:
                self.vertical_bar(df, i)

        self.generate_html()

    def generate_html(self):

        html = f'''
        <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style type="text/css">
            /* KT font */
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 400;
                src: url("./font/KTfontLight.woff") format('woff'),
                    url("./font/KTfontLight.eot"),
                    url("./font/KTfontLight.eot?#iefix") format('embedded-opentype');
            }}
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 500;
                src: url("./font/KTfontMedium.woff") format('woff'),
                    url("./font/KTfontMedium.eot"),
                    url("./font/KTfontMedium.eot?#iefix") format('embedded-opentype');
            }}
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 600;
                src: url("./font/KTfontBold.woff") format('woff'),
                    url("./font/KTfontBold.eot"),
                    url("./font/KTfontBold.eot?#iefix") format('embedded-opentype');
            }}
    
            /* common */
            @page {{
                margin: 0;
                width: 210mm;
                height: 297mm;
            }}
            html,
            body {{
                margin: 0;
                padding: 0;
                outline: none;
            }} 
            body {{
                width: 1000px;
                position: relative;
                left: calc(50% - 500px);
            }}
            h1, h2, h3, h4, p, div, section, article, header, span, ul, li, dl, dt, dd {{
                position: relative;
                display: block;
                text-align: center;
                margin: 0;
                padding: 0;
                outline: none;
                box-sizing: border-box;
            }}
            h1, h2, h3, h4, span, li, dt, dd {{
                white-space: pre-line;
                word-break: keep-all;
            }}
            .content {{ 
                font-size: 9pt;
                line-height: 1.5;
                font-family: "KT";
                background: #fff; 
                color: #000;
                width: 100%;
            }}
            header {{
                padding: 40px 0 40px; 
                border-bottom: 3px double #ccc;
                margin: 0 0 40px;
            }}
            h1 {{
                font-size: 18pt;
            }}
            h2 {{
                font-size: 15pt;
            }}
            h3 {{
                font-size: 12pt;
            }}
            header .box {{
                text-align: right;
            }}
            header .box p {{
                display: inline-block;
                padding: 5px 20px;
                background: #3A404D;
                color: #fff;
                border-radius: 20px;
                font-weight: 600;
            }}
            header .summary {{
                width: 100%;
            }}
            header .summary .box {{
                display: inline-block;
                width: 48.9%;
            }}
            header .summary .box + .box {{
                margin: 0 0 0 1%;
            }}
            header .summary h3 {{
                text-align: left;
                z-index: 2;
                margin: 0 0 15px;
                color: #3A404D;
            }}
            header .summary h3:after {{
                content: '';
                position: absolute;
                left: 0;
                bottom: 0;
                width: 95px;
                height: 10px;
                z-index: -1;
                opacity: 0.5;
                background: #EEFF00;
            }}
            table {{
                width: 100%;
                table-layout: fixed;
            }}
            table th,
            table td {{
                padding: 10px 0;
                text-align: center;
            }}
            table th {{
                border-bottom: 2px solid #333;
                border-top: 1px solid #333;
            }}
            table td {{
                background: #f1f1f1;
                border-bottom: 1px solid #fff;
            }}
            table td + td {{
                border-left: 1px solid #fff;
            }}
            section {{
                padding: 0 10px;
            }}
            section h1 {{
                font-size: 15pt;
                color: #3A404D;
                text-align: left;
                margin: 0 0 5px;
            }}
            section h1::before {{
                content: '';
                position: relative;
                display: inline-block;
                top: 7px;
                background: url("./images/ico_building.png") no-repeat;
                margin: 0 10px 0 0;
                width: 25px;;
                height: 25px;
            }}
            section h2 {{
                text-align: left;
                font-size: 12pt;
                color: #3A404D;
            }}
            section h2 i {{
                display: inline-block;
                font-size: 20pt;
                font-weight: 400;
                color: #ccc;
                margin: 0 10px 0 0; 
                letter-spacing: -2px;
            }}
            section h3 {{
                text-align: left;
                font-size: 10.5pt;
                color: #3A404D;
                padding: 0 10px 20px;
            }}
            section h3::before {{
                content: '';
                display: inline-block;
                width: 5px;
                height: 5px;
                border-radius: 10px;
                background: #3A404D;
                margin: -4px 5px 0 0; 
            }}
            section h4::before {{
                content: '[';
                display: inline-block;
                margin: 0 5px 0 0;
            }}
            section h4::after {{
                content: ']';
                display: inline-block;
                margin: 0 0 0 5px;
            }}
            section h4 {{
                text-align: left;
                font-size: 10.5pt;
                color: #3A404D;
                padding: 0 10px 10px;
            }}
            section .condition {{
                font-weight: 600;
                line-height: 1.2rem;
                padding: 10px;
                background: #f1f1f1;
                border-top: 3px double #ccc;
                border-bottom: 3px double #ccc;
                margin: 0 0 20px;
            }}
            article {{
                width: 100%;
                height: 100%;
                margin: 0 0 40px;
            }}
            .graph {{
                height: 550px;
            }}
            .chart_box {{
                clear: both;
            }}
            .chart_view {{
                display: inline-block;
                float: left;
                border: 1px solid #3A404D;
                border-radius: 10px;
                padding: 10px 0 0;
                overflow: hidden;
            }}
            .chart_view ul {{
                height: 125px;
            }}
            .chart_view.c1 ul {{
                top: 0px;
            }}
            .chart_view ul li {{
                float: left;
            }}
            .c1,
            .c2 {{
                margin: 0 1% 10px 0; 
            }}
            .c1,
            .c2,
            .c3 {{
                height: 215px;
            }}
            .c1,
            .c4 {{
                width: 25%;
            }}
            .c2,
            .c3 {{
                width: 36%;
            }}
            .c3 {{
                margin: 0 0 10px 0; 
            }}
            .c4,
            .c5 {{
                height: 280px;
            }}
            .c4 {{
                margin: 0 1% 0 0; 
            }}
            .c5 {{
                width: 73.2%;
            }}
            .chart_box ul,
            .chart_wrap,
            .preview ul {{
                width: 100%;
            }}
            .chart_view ul li {{
                display: inline-block;
                vertical-align: middle;
                width: 32.5%;
                font-size: 10pt;
                font-weight: 600;
                color: #666;
            }}
            .chart_view ul li span {{
                font-size: 20pt;
                font-weight: 600;
            }}
            .chart_view ul li.up,
            .chart_view ul li.down {{
                top: 20px;
            }}
            .chart_view ul li.up span {{
                color: #FF3333;
            }}
            .chart_view ul li.up span::before {{
                content: '';
                position: relative;
                top: 3px;
                display: inline-block;
                width: 13px;
                height: 20px;
                background: url("./images/ico_up.png") no-repeat;
                margin: 0 5px 0 0;
            }} 
            .chart_view ul li.down span {{
                color: #1bc0e1;
            }}
            .chart_view ul li.down span::before {{
                content: '';
                position: relative;
                top: 3px;
                display: inline-block;
                width: 13px;
                height: 20px;
                background: url("./images/ico_down.png") no-repeat;
                margin: 0 5px 0 0;
            }} 
            .chart_view ul li.total {{
                width: 35%;
            }}
            .chart_view ul li.total p {{
                position: relative;
                left: calc(50% - 45px);
                width: 90px;
                height: 90px;
                border-radius: 100px;
                background: #FF3333;
            }}
            .chart_view ul li.total span {{
                position: relative;
                top: -18px;
                color: #fff;
                font-size: 24pt;
            }}
            .chart_view ul li.total b {{
                position: relative;
                bottom: -45px;
                font-size: 8pt;
                color: #fff;
                z-index: 5;
            }}
            .chart_view.c4 ul {{
                height: 55px;
                background: #f7f7f7;
                margin: 0 0 10px;
            }}
            .chart_view.c4 ul li {{
                position: relative;
                top: 5px;
                width: 49%;
                height: 40px;
            }}
            .chart_view.c4 ul li + li {{
                border-left: 1px dashed #999;
            }}
            .chart_view.c4 ul li span {{
                font-size: 15pt;
                position: relative;
                top: -20px;
                display: inline-block;
                width: 100%;
            }}
            .chart_view.c4 ul li span::after {{
                content: '대';
            }}
            .chart_view.c4 ul li p {{
                position: relative;
                top: -24px;
            }}
            .chart_view .chart {{
                height: 155px;
                border-radius: 0 0 10px 10px;
                color: #333;
                overflow: hidden;
            }}
            .chart_view.c4 .chart {{
                
            }}
            .chart_view.c5 .chart {{
                height: 190px;
            }}
            .chart_wrap_box {{
                clear: both;
            }}
            .chart_wrap {{
                display: inline-block;
                float: left;
                width: 33%;
                height: 215px;
                border-radius: 0;
            }}
            .chart_wrap .chart {{
                border-radius: 0;
            }}
            .progress {{
                justify-content: flex-start;
                align-items: center;
                width: calc(100% - 10px);
                height: 4px;
                border-radius: 20px;
                margin: 10px 5px 20px;
                background: #ccc;
            }}
            .progress_bar {{
                justify-content: flex-end;
                align-items: center;
                width: 100%;
                height: 4px;
                border-radius: 20px;
                background: #FF3333;
            }}
            .progress_bar::before {{
                content: '';
                position: relative;
                top: -4px;
                display: inline-block;
                width: 10px;
                height: 10px;
                border-radius: 20px;
                background: #FF3333;
            }}
            .progress span {{
                position: absolute;
                right: 5px;
                bottom: -20px;
                align-self: flex-end;
                color: #3A404D;
                font-weight: 600;
                font-size: 10pt;
            }}
            .progress span::after {{
                display: inline-block;
                align-items: center;
                content: '%';
                font-size: 7pt;
                margin: 0 0 0 1px;
            }}
            .notice {{
                border: 1px dashed #ccc;
                padding: 15px;
                margin: 10px 0 0;
                border-radius: 0 10px 10px 10px;
            }}
            .notice dl {{
                flex-direction: column;
                width: 100%;
                height: 100%;
            }}
            .notice dl dt,
            .notice dl dd {{
                text-align: left;
            }}
            .notice dl dt {{
                font-size: 10pt;
                font-weight: 600;
                color: #3A404D;
            }}
            .notice dl dt::before {{
                content: url("../images/ico_notice.png");
                margin: 0 5px 0 0;
            }}
            .notice dl dd {{
                width: 100%;
                color: #3A404D;
                align-items: center;
                margin: 0 10px;
            }}
            .notice dl dd::before {{
                align-self: flex-start;
                content: '-';
                font-weight: 600;
                color: #3A404D;
                font-size: 12pt;
                margin: 0 5px 0 0;
            }}
            .info_box {{
                flex-direction: column;
                margin: 0 0 40px;
                padding: 0 0 40px;
                border-bottom: 1px dashed #ccc;
            }}
            .info_box:last-child {{
                margin: 0;
                padding: 0;
                border: none;
            }}
            .preview {{
                margin: 0 0 20px;
            }}
            .preview ul li {{
                display: inline-block;
                width: 30%;
                height: 85px;
                border-radius: 10px;
                background: #3A404D;
                color: #fff;
                vertical-align: top;
            }}
            .preview ul li + li {{
                margin: 0 0 0 0.5%;
            }}
            .preview ul li p {{
                display: inline-block;
                margin: 0 0 10px;
                color: #ddd;
            }}
            .preview ul li span {{
                font-size: 15pt;
                font-weight: 600;
            }}
            .preview ul li.date span {{
                font-size: 13pt;
            }}
        </style>
    </head>
    <body>
        <div class="content">
            <header>
                <h1>자동 점검 리포트</h1>
                <h2>(점검명)</h2>
                <div class="box">
                    <p>점검일 : 2021-09-27 09:56:00</p>
                </div>
                <div class="summary">
                    <div class="box">
                        <h3>자동 점검 결과</h3>
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <colgroup>
                                <col style="width: 33.33%" />
                                <col style="width: 33.33%" />
                                <col style="width: 33.33%" />
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Building</th>
                                    <th>Switch</th>
                                    <th>AP</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>빌딩 A</td>
                                    <td>비정상 1대</td>
                                    <td>비정상 1대</td>
                                </tr>
                                <tr>
                                    <td>빌딩 B</td>
                                    <td>비정상 2대</td>
                                    <td>비정상 2대</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="box">
                        <h3>형상 점검 결과</h3>
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <colgroup>
                                <col style="width: 33.33%" />
                                <col style="width: 33.33%" />
                                <col style="width: 33.33%" />
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>Building</th>
                                    <th>Switch</th>
                                    <th>AP</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>빌딩 A</td>
                                    <td>+ 1대</td>
                                    <td>0</td>
                                </tr>
                                <tr>
                                    <td>빌딩 B</td>
                                    <td>+ 1대</td>
                                    <td>0</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </header>
            <section>
                <h1>빌딩 A</h1>
                <article class="graph">
                    <h2><i>01</i>진단결과</h2>
                    <div class="chart_box">
                        <div class="chart_view c1">
                            <h3>비정상장비</h3>
                            <ul>
                                <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                <li class="up">
                                    <span>1</span>어제
                                </li>
                                <!-- 3자리까지 표현 -->
                                <li class="total">
                                    <p>
                                        <b>장비수</b>
                                        <span>153</span>
                                    </p>
                                </li>
                                <li class="down">
                                    <span>5</span>1주전
                                </li>
                            </ul>
                        </div>
                        <div class="chart_view c2">
                            <h3>그룹별 장비 비정상 현황</h3>
                            <div class="chart">
                                <img src="./res/grp_alert.png" alt="grp_alert">
                            </div>
                        </div>
                        <div class="chart_view c3">
                            <h3>비정상 항목 현황</h3>
                            <div class="chart">
                                <img src="./res/total_alert.png" alt="total_alert">
                            </div>
                        </div>
                    </div>
                    <div class="chart_box">
                        <div class="chart_view c4">
                            <h3>비정상 장비 추세</h3>
                            <ul>
                                <li class="average">
                                    <span>2</span>
                                    <p>일주일 간 평균</p>
                                </li>
                                <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                <li class="up">
                                    <span>1</span>
                                    <p>어제 대비</p>
                                </li>
                            </ul>
                            <div class="chart">
                                <img src="./res/total_hist.png" alt="total_hist">
                            </div>
                        </div>
                        <div class="chart_view c5">
                            <h3>항목별 비정상 추세</h3>
                            <div class="chart_wrap_box">
                                <div class="chart_wrap">
                                    <h4>CPU 사용률</h4>
                                    <div class="chart">
                                        <img src="./res/cpu_trend.png" alt="cpu_trend">
                                    </div>
                                </div>
                                <div class="chart_wrap">
                                    <h4>팬상태</h4>
                                    <div class="chart">
                                        <img src="./res/fan_trend.png" alt="port_trend">
                                    </div>
                                </div>
                                <div class="chart_wrap">
                                    <h4>포트 상태</h4>
                                    <div class="chart">
                                        <img src="./res/port_trend.png" alt="port_trend">
                                    </div>
                                </div>
                            <div>
                        </div>
                    </div>
                </article>
                <article>
                    <h2><i>02</i>To-Do List</h2>
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <colgroup>
                            <col style="width: 25%" />
                            <col style="width: 25%" />
                            <col style="width: 25%" />
                            <col style="width: 25%" />
                        </colgroup>
                        <thead>
                            <tr>
                                <th>그룹명</th>
                                <th>장비</th>
                                <th>점검항목</th>
                                <th>비정상률</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1F통신실</td>
                                <td>V6848XG</td>
                                <td>CPU 사용량</td>
                                <td>
                                    <div class="progress">
                                        <div class="progress_bar" style="width:56%;"></div>
                                        <span>56</span>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>1F통신실</td>
                                <td>V6848XG</td>
                                <td>CPU 사용량</td>
                                <td>
                                    <div class="progress">
                                        <div class="progress_bar" style="width:70%;"></div>
                                        <span>70</span>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>1F통신실</td>
                                <td>V6848XG</td>
                                <td>CPU 사용량</td>
                                <!-- 100% 이상의 값은 width="100%" 고정 / span 안에 수치만 변동 -->
                                <td>
                                    <div class="progress">
                                        <div class="progress_bar" style="width:100%;"></div>
                                        <span>108</span>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>1F통신실</td>
                                <td>V6848XG</td>
                                <td>CPU 사용량</td>
                                <td>
                                    <div class="progress">
                                        <div class="progress_bar" style="width:5%;"></div>
                                        <span>5</span>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="notice">
                        <dl>
                            <dt>조치사항</dt>
                            <dd>CPU 사용률 조회 (Show CPU) 후 장비 리부팅</dd>
                            <dd>조치사항 2</dd>
                            <dd>조치사항 3</dd>
                        </dl>
                    </div>
                </article>
                <article>
                    <h2><i>03</i>일주일 내 비정상 발생 건수</h2>
                    <table width="100%" cellpadding="0" cellspacing="0">
                        <colgroup>
                            <col style="width: 20%" />
                            <col style="width: 17%" />
                            <col style="width: 8%" />
                            <col style="width: 8%" />
                            <col style="width: 8%" />
                            <col style="width: 8%" />
                            <col style="width: 8%" />
                            <col style="width: 8%" />
                            <col style="width: 15%" />
                        </colgroup>
                        <thead>
                            <tr>
                                <th>장비명</th>
                                <th>점검항목</th>
                                <th>D-6</th>
                                <th>D-5</th>
                                <th>D-4</th>
                                <th>D-3</th>
                                <th>D-2</th>
                                <th>D-1</th>
                                <th>2021-09-27</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>V6848XG</td>
                                <td>CPU 부하</td>
                                <td>1</td>
                                <td>0</td>
                                <td>0</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>V6848XG</td>
                                <td>포트 점검</td>
                                <td>1</td>
                                <td>0</td>
                                <td>0</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>E5624R</td>
                                <td>전원</td>
                                <td>1</td>
                                <td>0</td>
                                <td>0</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>E5624R</td>
                                <td>포트다운</td>
                                <td>1</td>
                                <td>0</td>
                                <td>0</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>U9500H</td>
                                <td>메모리 점검</td>
                                <td>1</td>
                                <td>0</td>
                                <td>0</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                                <td>3</td>
                            </tr>
                        </tbody>
                    </table>
                </article>
                <article>
                    <h2><i>04</i>상세정보</h2>
                    <div class="info_box">
                        <div class="preview">
                            <ul>
                                <li class="date">
                                    <p>점검일시</p>
                                    <span>2021-09-27 14:43:25</span>
                                </li>
                                <li>
                                    <p>장비</p>
                                    <span>V6848XG</span>
                                </li>
                                <li>
                                    <p>점검항목</p>
                                    <span>CPU 사용량</span>
                                </li>
                            </ul>
                        </div>
                        <h3>실행조건</h3> 
                        <div class="condition">MEM_USAGE ＜＝ 10</div>
                        <h3>실행결과</h3> 
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <colgroup>
                                <col style="width: 10%" />
                                <col style="width: 8%" />
                                <col style="width: 10%" />
                                <col style="width: 15%" />
                                <col style="width: 12%" />
                                <col style="width: 15%" />
                                <col style="width: 10%" />
                                <col style="width: 10%" />
                                <col style="width: 10%" />
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>NAME</th>
                                    <th>STATUS</th>
                                    <th>MODEL</th>
                                    <th>ID</th>
                                    <th>IPADDR</th>
                                    <th>MAC</th>
                                    <th>MEM_USAGE</th>
                                    <th>CPU_USAGE</th>
                                    <th>SSID</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>                         
                            </tbody>
                        </table>
                    </div>
                    <div class="info_box">
                        <div class="preview">
                            <ul>
                                <li class="date">
                                    <p>점검일시</p>
                                    <span>2021-09-27 14:43:25</span>
                                </li>
                                <li>
                                    <p>장비</p>
                                    <span>V6848XG</span>
                                </li>
                                <li>
                                    <p>점검항목</p>
                                    <span>CPU 사용량</span>
                                </li>
                            </ul>
                        </div>
                        <h3>실행조건</h3> 
                        <div class="condition">MEM_USAGE ＜＝ 10</div>
                        <h3>실행결과</h3> 
                        <table width="100%" cellpadding="0" cellspacing="0">
                            <colgroup>
                                <col style="width: 10%" />
                                <col style="width: 8%" />
                                <col style="width: 10%" />
                                <col style="width: 15%" />
                                <col style="width: 12%" />
                                <col style="width: 15%" />
                                <col style="width: 10%" />
                                <col style="width: 10%" />
                                <col style="width: 10%" />
                            </colgroup>
                            <thead>
                                <tr>
                                    <th>NAME</th>
                                    <th>STATUS</th>
                                    <th>MODEL</th>
                                    <th>ID</th>
                                    <th>IPADDR</th>
                                    <th>MAC</th>
                                    <th>MEM_USAGE</th>
                                    <th>CPU_USAGE</th>
                                    <th>SSID</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>                         
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>                         
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>                         
                                <tr>
                                    <td>defGsp_112</td>
                                    <td>RUN</td>
                                    <td>AR-WF6-2541</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>172.30.2.112</td>
                                    <td>1C:EC:72:01;8A:48</td>
                                    <td>26.68</td>
                                    <td>2.18</td>
                                    <td>-</td>
                                </tr>                         
                            </tbody>
                        </table>
                    </div>
                </article>
            </section>     
        </div>
    </body>
    </html>

        
        '''

        html_211006 = f'''
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style type="text/css">
                    /* KT font */
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 400;
                        src: url("./font/KTfontLight.woff") format('woff'),
                            url("./font/KTfontLight.eot"),
                            url("./font/KTfontLight.eot?#iefix") format('embedded-opentype');
                    }}
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 500;
                        src: url("./font/KTfontMedium.woff") format('woff'),
                            url("./font/KTfontMedium.eot"),
                            url("./font/KTfontMedium.eot?#iefix") format('embedded-opentype');
                    }}
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 600;
                        src: url("./font/KTfontBold.woff") format('woff'),
                            url("./font/KTfontBold.eot"),
                            url("./font/KTfontBold.eot?#iefix") format('embedded-opentype');
                    }}

                    /* common */
                    @page {{
                        margin: 0;
                        width: 210mm;
                        height: 297mm;
                    }}
                    html,
                    body {{
                        margin: 0;
                        padding: 0;
                        outline: none;
                    }} 
                    h1, h2, h3, h4, p, div, section, article, header, span, ul, li, dl, dt, dd {{
                        position: relative;
                        display: block;
                        text-align: center;
                        margin: 0;
                        padding: 0;
                        outline: none;
                        box-sizing: border-box;
                    }}
                    h1, h2, h3, h4, span, li, dt, dd {{
                        white-space: pre-line;
                        word-break: keep-all;
                    }}
                    .content {{ 
                        font-size: 9pt;
                        line-height: 1.5;
                        font-family: "KT";
                        background: #fff; 
                        color: #000;
                        width: 100%;
                    }}
                    header {{
                        padding: 40px; 
                        border-bottom: 3px double #ccc;
                        margin: 0 0 40px;
                    }}
                    h1 {{
                        font-size: 18pt;
                    }}
                    h2 {{
                        font-size: 15pt;
                    }}
                    h3 {{
                        font-size: 12pt;
                    }}
                    header .box {{
                        text-align: right;
                    }}
                    header .box p {{
                        display: inline-block;
                        padding: 5px 20px;
                        background: #3A404D;
                        color: #fff;
                        border-radius: 20px;
                        font-weight: 600;
                    }}
                    header .summary {{
                        width: 100%;
                    }}
                    header .summary .box {{
                        display: inline-block;
                        width: 48.9%;
                    }}
                    header .summary .box + .box {{
                        margin: 0 0 0 1%;
                    }}
                    header .summary h3 {{
                        text-align: left;
                        z-index: 2;
                        margin: 0 0 15px;
                        color: #3A404D;
                    }}
                    header .summary h3:after {{
                        content: '';
                        position: absolute;
                        left: 0;
                        bottom: 0;
                        width: 95px;
                        height: 10px;
                        z-index: -1;
                        opacity: 0.5;
                        background: #EEFF00;
                    }}
                    table {{
                        width: 100%;
                        table-layout: fixed;
                    }}
                    table th,
                    table td {{
                        padding: 10px 0;
                        text-align: center;
                    }}
                    table th {{
                        border-bottom: 2px solid #333;
                        border-top: 1px solid #333;
                    }}
                    table td {{
                        background: #f1f1f1;
                        border-bottom: 1px solid #fff;
                    }}
                    table td + td {{
                        border-left: 1px solid #fff;
                    }}
                    section {{
                        padding: 0 40px;
                    }}
                    section h1 {{
                        font-size: 15pt;
                        color: #3A404D;
                        text-align: left;
                        margin: 0 0 5px;
                    }}
                    section h1::before {{
                        content: '';
                        position: relative;
                        display: inline-block;
                        top: 7px;
                        background: url("./images/ico_building.png") no-repeat;
                        margin: 0 10px 0 0;
                        width: 25px;;
                        height: 25px;
                    }}
                    section h2 {{
                        text-align: left;
                        font-size: 12pt;
                        color: #3A404D;
                    }}
                    section h2 i {{
                        display: inline-block;
                        font-size: 20pt;
                        font-weight: 400;
                        color: #ccc;
                        margin: 0 10px 0 0; 
                        letter-spacing: -2px;
                    }}
                    section h3 {{
                        text-align: left;
                        font-size: 10.5pt;
                        color: #3A404D;
                        padding: 0 10px 5px;
                    }}
                    section h3::before {{
                        content: '';
                        display: inline-block;
                        width: 5px;
                        height: 5px;
                        border-radius: 10px;
                        background: #3A404D;
                        margin: -4px 5px 0 0; 
                    }}
                    section h4 {{
                        text-align: left;
                        font-size: 10.5pt;
                        color: #3A404D;
                        padding: 0 10px 5px;
                    }}
                    section .condition {{
                        font-weight: 600;
                        line-height: 1.2rem;
                        padding: 10px;
                        background: #f1f1f1;
                        border-top: 3px double #ccc;
                        border-bottom: 3px double #ccc;
                        margin: 0 0 20px;
                    }}
                    article {{
                        width: 100%;
                        height: 100%;
                        margin: 0 0 40px;
                    }}
                    .graph {{
                        height: 510px;
                    }}
                    .chart_box {{
                        clear: both;
                    }}
                    .chart_view {{
                        display: inline-block;
                        float: left;
                        border: 1px solid #3A404D;
                        border-radius: 10px;
                        padding: 10px 0 0;
                        overflow: hidden;
                    }}
                    .chart_view ul {{
                        height: 125px;
                    }}
                    .chart_view.c1 ul {{
                        top: 15px;
                    }}
                    .chart_view ul li {{
                        float: left;
                    }}
                    .c1,
                    .c2 {{
                        margin: 0 1% 10px 0; 
                    }}
                    .c1,
                    .c2,
                    .c3 {{
                        height: 200px;
                    }}
                    .c1,
                    .c4 {{
                        width: 25%;
                    }}
                    .c2,
                    .c3 {{
                        width: 36%;
                    }}
                    .c3 {{
                        margin: 0 0 10px 0; 
                    }}
                    .c4,
                    .c5 {{
                        height: 260px;
                    }}
                    .c4 {{
                        margin: 0 1% 0 0; 
                    }}
                    .c5 {{
                        width: 73.2%;
                    }}
                    .chart_box ul,
                    .chart_wrap,
                    .preview ul {{
                        width: 100%;
                    }}
                    .chart_view ul li {{
                        display: inline-block;
                        vertical-align: middle;
                        width: 32.5%;
                        font-size: 10pt;
                        font-weight: 600;
                        color: #666;
                    }}
                    .chart_view ul li span {{
                        font-size: 20pt;
                        font-weight: 600;
                    }}
                    .chart_view ul li.up,
                    .chart_view ul li.down {{
                        top: 20px;
                    }}
                    .chart_view ul li.up span {{
                        color: #FF3333;
                    }}
                    .chart_view ul li.up span::before {{
                        content: '';
                        position: relative;
                        top: 3px;
                        display: inline-block;
                        width: 13px;
                        height: 20px;
                        background: url("./images/ico_up.png") no-repeat;
                        margin: 0 5px 0 0;
                    }} 
                    .chart_view ul li.down span {{
                        color: #1bc0e1;
                    }}
                    .chart_view ul li.down span::before {{
                        content: '';
                        position: relative;
                        top: 3px;
                        display: inline-block;
                        width: 13px;
                        height: 20px;
                        background: url("./images/ico_down.png") no-repeat;
                        margin: 0 5px 0 0;
                    }} 
                    .chart_view ul li.total {{
                        width: 35%;
                    }}
                    .chart_view ul li.total p {{
                        position: relative;
                        left: calc(50% - 45px);
                        width: 90px;
                        height: 90px;
                        border-radius: 100px;
                        background: #FF3333;
                    }}
                    .chart_view ul li.total span {{
                        position: relative;
                        top: -18px;
                        color: #fff;
                        font-size: 24pt;
                    }}
                    .chart_view ul li.total b {{
                        position: relative;
                        bottom: -45px;
                        font-size: 8pt;
                        color: #fff;
                        z-index: 5;
                    }}
                    .chart_view.c4 ul {{
                        height: 55px;
                        background: #f7f7f7;
                    }}
                    .chart_view.c4 ul li {{
                        position: relative;
                        top: 5px;
                        width: 49%;
                        height: 40px;
                    }}
                    .chart_view.c4 ul li + li {{
                        border-left: 1px dashed #999;
                    }}
                    .chart_view.c4 ul li span {{
                        font-size: 15pt;
                        position: relative;
                        top: -20px;
                        display: inline-block;
                        width: 100%;
                    }}
                    .chart_view.c4 ul li span::after {{
                        content: '대';
                    }}
                    .chart_view.c4 ul li p {{
                        position: relative;
                        top: -24px;
                    }}
                    .chart_view .chart {{
                        height: 160px;
                        border-radius: 0 0 10px 10px;
                        color: #333;
                        overflow: hidden;
                    }}
                    .chart_view.c4 .chart {{

                    }}
                    .chart_view.c5 .chart {{
                        height: 190px;
                    }}
                    .chart_wrap_box {{
                        clear: both;
                    }}
                    .chart_wrap {{
                        display: inline-block;
                        float: left;
                        width: 33%;
                        height: 215px;
                        border-radius: 0;
                    }}
                    .chart_wrap .chart {{
                        border-radius: 0;
                    }}
                    .progress {{
                        justify-content: flex-start;
                        align-items: center;
                        width: calc(100% - 10px);
                        height: 4px;
                        border-radius: 20px;
                        margin: 10px 5px 20px;
                        background: #ccc;
                    }}
                    .progress_bar {{
                        justify-content: flex-end;
                        align-items: center;
                        width: 100%;
                        height: 4px;
                        border-radius: 20px;
                        background: #FF3333;
                    }}
                    .progress_bar::before {{
                        content: '';
                        position: relative;
                        top: -4px;
                        display: inline-block;
                        width: 10px;
                        height: 10px;
                        border-radius: 20px;
                        background: #FF3333;
                    }}
                    .progress span {{
                        position: absolute;
                        right: 5px;
                        bottom: -20px;
                        align-self: flex-end;
                        color: #3A404D;
                        font-weight: 600;
                        font-size: 10pt;
                    }}
                    .progress span::after {{
                        display: inline-block;
                        align-items: center;
                        content: '%';
                        font-size: 7pt;
                        margin: 0 0 0 1px;
                    }}
                    .notice {{
                        border: 1px dashed #ccc;
                        padding: 15px;
                        margin: 10px 0 0;
                        border-radius: 0 10px 10px 10px;
                    }}
                    .notice dl {{
                        flex-direction: column;
                        width: 100%;
                        height: 100%;
                    }}
                    .notice dl dt,
                    .notice dl dd {{
                        text-align: left;
                    }}
                    .notice dl dt {{
                        font-size: 10pt;
                        font-weight: 600;
                        color: #3A404D;
                    }}
                    .notice dl dt::before {{
                        content: url("../images/ico_notice.png");
                        margin: 0 5px 0 0;
                    }}
                    .notice dl dd {{
                        width: 100%;
                        color: #3A404D;
                        align-items: center;
                        margin: 0 10px;
                    }}
                    .notice dl dd::before {{
                        align-self: flex-start;
                        content: '-';
                        font-weight: 600;
                        color: #3A404D;
                        font-size: 12pt;
                        margin: 0 5px 0 0;
                    }}
                    .info_box {{
                        flex-direction: column;
                        margin: 0 0 40px;
                        padding: 0 0 40px;
                        border-bottom: 1px dashed #ccc;
                    }}
                    .info_box:last-child {{
                        margin: 0;
                        padding: 0;
                        border: none;
                    }}
                    .preview {{
                        margin: 0 0 20px;
                    }}
                    .preview ul li {{
                        display: inline-block;
                        width: 30%;
                        height: 85px;
                        border-radius: 10px;
                        background: #3A404D;
                        color: #fff;
                        vertical-align: top;
                    }}
                    .preview ul li + li {{
                        margin: 0 0 0 0.5%;
                    }}
                    .preview ul li p {{
                        display: inline-block;
                        margin: 0 0 10px;
                        color: #ddd;
                    }}
                    .preview ul li span {{
                        font-size: 15pt;
                        font-weight: 600;
                    }}
                    .preview ul li.date span {{
                        font-size: 13pt;
                    }}
                </style>
            </head>
            <body>
                <div class="content">
                    <header>
                        <h1>자동 점검 리포트</h1>
                        <h2>(점검명)</h2>
                        <div class="box">
                            <p>점검일 : 2021-09-27 09:56:00</p>
                        </div>
                        <div class="summary">
                            <div class="box">
                                <h3>자동 점검 결과</h3>
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>Building</th>
                                            <th>Switch</th>
                                            <th>AP</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>빌딩 A</td>
                                            <td>비정상 1대</td>
                                            <td>비정상 1대</td>
                                        </tr>
                                        <tr>
                                            <td>빌딩 B</td>
                                            <td>비정상 2대</td>
                                            <td>비정상 2대</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="box">
                                <h3>형상 점검 결과</h3>
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>Building</th>
                                            <th>Switch</th>
                                            <th>AP</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>빌딩 A</td>
                                            <td>+ 1대</td>
                                            <td>0</td>
                                        </tr>
                                        <tr>
                                            <td>빌딩 B</td>
                                            <td>+ 1대</td>
                                            <td>0</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </header>
                    <section>
                        <h1>빌딩 A</h1>
                        <article class="graph">
                            <h2><i>01</i>진단결과</h2>
                            <div class="chart_box">
                                <div class="chart_view c1">
                                    <h3>비정상장비</h3>
                                    <ul>
                                        <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                        <li class="up">
                                            <span>1</span>어제
                                        </li>
                                        <!-- 3자리까지 표현 -->
                                        <li class="total">
                                            <p>
                                                <b>장비수</b>
                                                <span>153</span>
                                            </p>
                                        </li>
                                        <li class="down">
                                            <span>5</span>1주전
                                        </li>
                                    </ul>
                                </div>
                                <div class="chart_view c2">
                                    <h3>그룹별 장비 비정상 현황</h3>
                                    <div class="chart">
                                        <img src="./res/grp_alert.png" alt="grp_alert">
                                    </div>
                                </div>
                                <div class="chart_view c3">
                                    <h3>비정상 항목 현황</h3>
                                    <div class="chart">
                                        <img src="./res/total_alert.png" alt="total_alert">
                                    </div>
                                </div>
                            </div>
                            <div class="chart_box">
                                <div class="chart_view c4">
                                    <h3>비정상 장비 추세</h3>
                                    <ul>
                                        <li class="average">
                                            <span>2</span>
                                            <p>일주일 간 평균</p>
                                        </li>
                                        <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                        <li class="up">
                                            <span>1</span>
                                            <p>어제 대비</p>
                                        </li>
                                    </ul>
                                    <div class="chart">
                                        <img src="./res/total_hist.png" alt="total_hist">
                                    </div>
                                </div>
                                <div class="chart_view c5">
                                    <h3>항목별 비정상 추세</h3>
                                    <div class="chart_wrap_box">
                                        <div class="chart_wrap">
                                            <h4>CPU 사용률</h4>
                                            <div class="chart">
                                                <img src="./res/cpu_trend.png" alt="cpu_trend">
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>팬상태</h4>
                                            <div class="chart">
                                                <img src="./res/fan_trend.png" alt="port_trend">
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>포트 상태</h4>
                                            <div class="chart">
                                                <img src="./res/port_trend.png" alt="port_trend">
                                            </div>
                                        </div>
                                    <div>
                                </div>
                            </div>
                        </article>
                        <article>
                            <h2><i>02</i>To-Do List</h2>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <colgroup>
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                </colgroup>
                                <thead>
                                    <tr>
                                        <th>그룹명</th>
                                        <th>장비</th>
                                        <th>점검항목</th>
                                        <th>비정상률</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:56%;"></div>
                                                <span>56</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:70%;"></div>
                                                <span>70</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <!-- 100% 이상의 값은 width="100%" 고정 / span 안에 수치만 변동 -->
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:100%;"></div>
                                                <span>108</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:5%;"></div>
                                                <span>5</span>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <div class="notice">
                                <dl>
                                    <dt>조치사항</dt>
                                    <dd>CPU 사용률 조회 (Show CPU) 후 장비 리부팅</dd>
                                    <dd>조치사항 2</dd>
                                    <dd>조치사항 3</dd>
                                </dl>
                            </div>
                        </article>
                        <article>
                            <h2><i>03</i>일주일 내 비정상 발생 건수</h2>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <colgroup>
                                    <col style="width: 20%" />
                                    <col style="width: 17%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 15%" />
                                </colgroup>
                                <thead>
                                    <tr>
                                        <th>장비명</th>
                                        <th>점검항목</th>
                                        <th>D-6</th>
                                        <th>D-5</th>
                                        <th>D-4</th>
                                        <th>D-3</th>
                                        <th>D-2</th>
                                        <th>D-1</th>
                                        <th>2021-09-27</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>V6848XG</td>
                                        <td>CPU 부하</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>V6848XG</td>
                                        <td>포트 점검</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>E5624R</td>
                                        <td>전원</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>E5624R</td>
                                        <td>포트다운</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>U9500H</td>
                                        <td>메모리 점검</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                </tbody>
                            </table>
                        </article>
                        <article>
                            <h2><i>04</i>상세정보</h2>
                            <div class="info_box">
                                <div class="preview">
                                    <ul>
                                        <li class="date">
                                            <p>점검일시</p>
                                            <span>2021-09-27 14:43:25</span>
                                        </li>
                                        <li>
                                            <p>장비</p>
                                            <span>V6848XG</span>
                                        </li>
                                        <li>
                                            <p>점검항목</p>
                                            <span>CPU 사용량</span>
                                        </li>
                                    </ul>
                                </div>
                                <h3>실행조건</h3> 
                                <div class="condition">MEM_USAGE ＜＝ 10</div>
                                <h3>실행결과</h3> 
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 10%" />
                                        <col style="width: 8%" />
                                        <col style="width: 10%" />
                                        <col style="width: 15%" />
                                        <col style="width: 12%" />
                                        <col style="width: 15%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>NAME</th>
                                            <th>STATUS</th>
                                            <th>MODEL</th>
                                            <th>ID</th>
                                            <th>IPADDR</th>
                                            <th>MAC</th>
                                            <th>MEM_USAGE</th>
                                            <th>CPU_USAGE</th>
                                            <th>SSID</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                    </tbody>
                                </table>
                            </div>
                            <div class="info_box">
                                <div class="preview">
                                    <ul>
                                        <li class="date">
                                            <p>점검일시</p>
                                            <span>2021-09-27 14:43:25</span>
                                        </li>
                                        <li>
                                            <p>장비</p>
                                            <span>V6848XG</span>
                                        </li>
                                        <li>
                                            <p>점검항목</p>
                                            <span>CPU 사용량</span>
                                        </li>
                                    </ul>
                                </div>
                                <h3>실행조건</h3> 
                                <div class="condition">MEM_USAGE ＜＝ 10</div>
                                <h3>실행결과</h3> 
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 10%" />
                                        <col style="width: 8%" />
                                        <col style="width: 10%" />
                                        <col style="width: 15%" />
                                        <col style="width: 12%" />
                                        <col style="width: 15%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>NAME</th>
                                            <th>STATUS</th>
                                            <th>MODEL</th>
                                            <th>ID</th>
                                            <th>IPADDR</th>
                                            <th>MAC</th>
                                            <th>MEM_USAGE</th>
                                            <th>CPU_USAGE</th>
                                            <th>SSID</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                    </tbody>
                                </table>
                            </div>
                        </article>
                    </section>     
                </div>
            </body>
            </html>

        '''

        html_210930 = f'''
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style type="text/css">
                    /* KT font */
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 400;
                        src: url("./font/KTfontLight.woff") format('woff'),
                            url("./font/KTfontLight.eot"),
                            url("./font/KTfontLight.eot?#iefix") format('embedded-opentype');
                    }}
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 500;
                        src: url("./font/KTfontMedium.woff") format('woff'),
                            url("./font/KTfontMedium.eot"),
                            url("./font/KTfontMedium.eot?#iefix") format('embedded-opentype');
                    }}
                    @font-face {{
                        font-family: "KT";
                        font-style: normal;
                        font-weight: 600;
                        src: url("./font/KTfontBold.woff") format('woff'),
                            url("./font/KTfontBold.eot"),
                            url("./font/KTfontBold.eot?#iefix") format('embedded-opentype');
                    }}
            
                    /* common */
                    @page {{
                        margin: 0;
                        width: 210mm;
                        height: 297mm;
                    }}
                    html,
                    body {{
                        margin: 0;
                        padding: 0;
                        outline: none;
                    }} 
                    h1, h2, h3, h4, p, div, section, article, header, span, ul, li, dl, dt, dd {{
                        position: relative;
                        display: block;
                        text-align: center;
                        margin: 0;
                        padding: 0;
                        outline: none;
                        box-sizing: border-box;
                    }}
                    h1, h2, h3, h4, span, li, dt, dd {{
                        white-space: pre-line;
                        word-break: keep-all;
                    }}
                    .content {{ 
                        font-size: 9pt;
                        line-height: 1.5;
                        font-family: "KT";
                        background: #fff; 
                        color: #000;
                        width: 100%;
                    }}
                    header {{
                        padding: 40px 40px 60px; 
                        border-bottom: 3px double #ccc;
                        margin: 0 0 60px;
                    }}
                    h1 {{
                        font-size: 18pt;
                    }}
                    h2 {{
                        font-size: 15pt;
                    }}
                    h3 {{
                        font-size: 12pt;
                    }}
                    header .box {{
                        text-align: right;
                    }}
                    header .box p {{
                        display: inline-block;
                        padding: 5px 20px;
                        background: #3A404D;
                        color: #fff;
                        border-radius: 20px;
                        font-weight: 600;
                    }}
                    header .summary {{
                        width: 100%;
                    }}
                    header .summary .box {{
                        display: inline-block;
                        width: 48.9%;
                    }}
                    header .summary .box + .box {{
                        margin: 0 0 0 1%;
                    }}
                    header .summary h3 {{
                        text-align: left;
                        z-index: 2;
                        margin: 0 0 15px;
                        color: #3A404D;
                    }}
                    header .summary h3:after {{
                        content: '';
                        position: absolute;
                        left: 0;
                        bottom: 0;
                        width: 95px;
                        height: 10px;
                        z-index: -1;
                        opacity: 0.5;
                        background: #EEFF00;
                    }}
                    table {{
                        width: 100%;
                        table-layout: fixed;
                    }}
                    table th,
                    table td {{
                        padding: 10px 0;
                        text-align: center;
                    }}
                    table th {{
                        border-bottom: 2px solid #333;
                        border-top: 1px solid #333;
                    }}
                    table td {{
                        background: #f1f1f1;
                        border-bottom: 1px solid #fff;
                    }}
                    table td + td {{
                        border-left: 1px solid #fff;
                    }}
                    section {{
                        padding: 0 40px;
                    }}
                    section h1 {{
                        font-size: 15pt;
                        color: #3A404D;
                        text-align: left;
                        margin: 0 0 5px;
                    }}
                    section h1::before {{
                        content: '';
                        position: relative;
                        display: inline-block;
                        top: 7px;
                        background: url("./images/ico_building.png") no-repeat;
                        margin: 0 10px 0 0;
                        width: 25px;;
                        height: 25px;
                    }}
                    section h2 {{
                        text-align: left;
                        font-size: 12pt;
                        color: #3A404D;
                    }}
                    section h2 i {{
                        display: inline-block;
                        font-size: 20pt;
                        font-weight: 400;
                        color: #ccc;
                        margin: 0 10px 0 0; 
                        letter-spacing: -2px;
                    }}
                    section h3 {{
                        text-align: left;
                        font-size: 10.5pt;
                        color: #3A404D;
                        padding: 0 10px 5px;
                    }}
                    section h3::before {{
                        content: '';
                        display: inline-block;
                        width: 5px;
                        height: 5px;
                        border-radius: 10px;
                        background: #3A404D;
                        margin: -4px 5px 0 0; 
                    }}
                    section h4 {{
                        text-align: left;
                        font-size: 10.5pt;
                        color: #3A404D;
                        padding: 0 10px 5px;
                    }}
                    section .condition {{
                        font-weight: 600;
                        line-height: 1.2rem;
                        padding: 10px;
                        background: #f1f1f1;
                        border-top: 3px double #ccc;
                        border-bottom: 3px double #ccc;
                        margin: 0 0 20px;
                    }}
                    article {{
                        width: 100%;
                        height: 100%;
                        margin: 0 0 40px;
                    }}
                    .chart_box {{
                        clear: both;
                    }}
                    .chart_view {{
                        display: inline-block;
                        float: left;
                        border: 1px solid #3A404D;
                        border-radius: 10px;
                        padding: 10px 0 0;
                        overflow: hidden;
                    }}
                    .chart_view ul {{
                        height: 125px;
                    }}
                    .chart_view.c1 ul {{
                        top: 15px;
                    }}
                    .chart_view ul li {{
                        float: left;
                    }}
                    .c1,
                    .c2 {{
                        margin: 0 1% 10px 0; 
                    }}
                    .c1,
                    .c2,
                    .c3 {{
                        height: 200px;
                    }}
                    .c1,
                    .c4 {{
                        width: 25%;
                    }}
                    .c2,
                    .c3 {{
                        width: 36%;
                    }}
                    .c3 {{
                        margin: 0 0 10px 0; 
                    }}
                    .c4,
                    .c5 {{
                        height: 260px;
                    }}
                    .c4 {{
                        margin: 0 1% 0 0; 
                    }}
                    .c5 {{
                        width: 73.2%;
                    }}
                    .chart_box ul,
                    .chart_wrap,
                    .preview ul {{
                        width: 100%;
                    }}
                    .chart_view ul li {{
                        display: inline-block;
                        vertical-align: middle;
                        width: 32.5%;
                        font-size: 10pt;
                        font-weight: 600;
                        color: #666;
                    }}
                    .chart_view ul li span {{
                        font-size: 20pt;
                        font-weight: 600;
                    }}
                    .chart_view ul li.up span {{
                        color: #FF3333;
                    }}
                    .chart_view ul li.up span::before {{
                        content: '';
                        position: relative;
                        top: 3px;
                        display: inline-block;
                        width: 13px;
                        height: 20px;
                        background: url("./images/ico_up.png") no-repeat;
                        margin: 0 5px 0 0;
                    }} 
                    .chart_view ul li.down span {{
                        color: #1bc0e1;
                    }}
                    .chart_view ul li.down span::before {{
                        content: '';
                        position: relative;
                        top: 3px;
                        display: inline-block;
                        width: 13px;
                        height: 20px;
                        background: url("./images/ico_down.png") no-repeat;
                        margin: 0 5px 0 0;
                    }} 
                    .chart_view ul li.total {{
                        width: 35%;
                    }}
                    .chart_view ul li.total p {{
                        position: relative;
                        left: calc(50% - 45px);
                        width: 90px;
                        height: 90px;
                        border-radius: 100px;
                        background: #FF3333;
                    }}
                    .chart_view ul li.total span {{
                        position: relative;
                        top: -18px;
                        color: #fff;
                        font-size: 24pt;
                    }}
                    .chart_view ul li.total b {{
                        position: relative;
                        bottom: -45px;
                        font-size: 8pt;
                        color: #fff;
                        z-index: 5;
                    }}
                    .chart_view.c4 ul {{
                        height: 55px;
                        background: #f7f7f7;
                    }}
                    .chart_view.c4 ul li {{
                        position: relative;
                        top: 5px;
                        width: 49%;
                        height: 40px;
                    }}
                    .chart_view.c4 ul li + li {{
                        border-left: 1px dashed #999;
                    }}
                    .chart_view.c4 ul li span {{
                        font-size: 15pt;
                        position: relative;
                        top: -20px;
                        display: inline-block;
                        width: 100%;
                    }}
                    .chart_view.c4 ul li span::after {{
                        content: '대';
                    }}
                    .chart_view.c4 ul li p {{
                        position: relative;
                        top: -24px;
                    }}
                    .chart_view .chart {{
                        height: 160px;
                        border-radius: 0 0 10px 10px;
                        color: #333;
                        overflow: hidden;
                    }}
                    .chart_view.c4 .chart {{
                       
                    }}
                    .chart_view.c5 .chart {{
                        height: 190px;
                    }}
                    .chart_wrap_box {{
                        clear: both;
                    }}
                    .chart_wrap {{
                        display: inline-block;
                        float: left;
                        width: 33%;
                        height: 215px;
                        border-radius: 0;
                    }}
                    .chart_wrap .chart {{
                        border-radius: 0;
                    }}
                    .progress {{
                        justify-content: flex-start;
                        align-items: center;
                        width: calc(100% - 10px);
                        height: 4px;
                        border-radius: 20px;
                        margin: 10px 5px 20px;
                        background: #ccc;
                    }}
                    .progress_bar {{
                        justify-content: flex-end;
                        align-items: center;
                        width: 100%;
                        height: 4px;
                        border-radius: 20px;
                        background: #FF3333;
                    }}
                    .progress_bar::before {{
                        content: '';
                        position: relative;
                        top: -4px;
                        display: inline-block;
                        width: 10px;
                        height: 10px;
                        border-radius: 20px;
                        background: #FF3333;
                    }}
                    .progress span {{
                        position: absolute;
                        right: 5px;
                        bottom: -20px;
                        align-self: flex-end;
                        color: #3A404D;
                        font-weight: 600;
                        font-size: 10pt;
                    }}
                    .progress span::after {{
                        display: inline-block;
                        align-items: center;
                        content: '%';
                        font-size: 7pt;
                        margin: 0 0 0 1px;
                    }}
                    .notice {{
                        border: 1px dashed #ccc;
                        padding: 15px;
                        margin: 10px 0 0;
                        border-radius: 0 10px 10px 10px;
                    }}
                    .notice dl {{
                        flex-direction: column;
                        width: 100%;
                        height: 100%;
                    }}
                    .notice dl dt,
                    .notice dl dd {{
                        text-align: left;
                    }}
                    .notice dl dt {{
                        font-size: 10pt;
                        font-weight: 600;
                        color: #3A404D;
                    }}
                    .notice dl dt::before {{
                        content: url("../images/ico_notice.png");
                        margin: 0 5px 0 0;
                    }}
                    .notice dl dd {{
                        width: 100%;
                        color: #3A404D;
                        align-items: center;
                        margin: 0 10px;
                    }}
                    .notice dl dd::before {{
                        align-self: flex-start;
                        content: '-';
                        font-weight: 600;
                        color: #3A404D;
                        font-size: 12pt;
                        margin: 0 5px 0 0;
                    }}
                    .info_box {{
                        flex-direction: column;
                        margin: 0 0 40px;
                        padding: 0 0 40px;
                        border-bottom: 1px dashed #ccc;
                    }}
                    .info_box:last-child {{
                        margin: 0;
                        padding: 0;
                        border: none;
                    }}
                    .preview {{
                        margin: 0 0 20px;
                    }}
                    .preview ul li {{
                        display: inline-block;
                        width: 30%;
                        height: 85px;
                        border-radius: 10px;
                        background: #3A404D;
                        color: #fff;
                        vertical-align: top;
                    }}
                    .preview ul li + li {{
                        margin: 0 0 0 0.5%;
                    }}
                    .preview ul li p {{
                        display: inline-block;
                        margin: 0 0 10px;
                        color: #ddd;
                    }}
                    .preview ul li span {{
                        font-size: 15pt;
                        font-weight: 600;
                    }}
                    .preview ul li.date span {{
                        font-size: 13pt;
                    }}
                </style>
            </head>
            <body>
                <div class="content">
                    <header>
                        <h1>자동 점검 리포트</h1>
                        <h2>(점검명)</h2>
                        <div class="box">
                            <p>점검일 : 2021-09-27 09:56:00</p>
                        </div>
                        <div class="summary">
                            <div class="box">
                                <h3>자동 점검 결과</h3>
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>Building</th>
                                            <th>Switch</th>
                                            <th>AP</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>빌딩 A</td>
                                            <td>비정상 1대</td>
                                            <td>비정상 1대</td>
                                        </tr>
                                        <tr>
                                            <td>빌딩 B</td>
                                            <td>비정상 2대</td>
                                            <td>비정상 2대</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="box">
                                <h3>형상 점검 결과</h3>
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                        <col style="width: 33.33%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>Building</th>
                                            <th>Switch</th>
                                            <th>AP</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>빌딩 A</td>
                                            <td>+ 1대</td>
                                            <td>0</td>
                                        </tr>
                                        <tr>
                                            <td>빌딩 B</td>
                                            <td>+ 1대</td>
                                            <td>0</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </header>
                    <section>
                        <h1>빌딩 A</h1>
                        <article>
                            <h2><i>01</i>진단결과</h2>
                            <div class="chart_box">
                                <div class="chart_view c1">
                                    <h3>비정상장비</h3>
                                    <ul>
                                        <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                        <li class="up">
                                            <span>1</span>어제
                                        </li>
                                        <!-- 3자리까지 표현 -->
                                        <li class="total">
                                            <p>
                                                <b>장비수</b>
                                                <span>153</span>
                                            </p>
                                        </li>
                                        <li class="down">
                                            <span>5</span>1주전
                                        </li>
                                    </ul>
                                </div>
                                <div class="chart_view c2">
                                    <h3>그룹별 장비 비정상 현황</h3>
                                    <div class="chart">
                                        <img src="./res/grp_alert.png" alt="grp_alert">
                                    </div>
                                </div>
                                <div class="chart_view c3">
                                    <h3>비정상 항목 현황</h3>
                                    <div class="chart">
                                        <img src="./res/total_alert.png" alt="total_alert">
                                    </div>
                                </div>
                            </div>
                            <div class="chart_box">
                                <div class="chart_view c4">
                                    <h3>비정상 장비 추세</h3>
                                    <ul>
                                        <li class="average">
                                            <span>2</span>
                                            <p>일주일 간 평균</p>
                                        </li>
                                        <!-- 증가할 경우 class="up" / 감소할 경우 class="down" 추가 -->
                                        <li class="up">
                                            <span>1</span>
                                            <p>어제 대비</p>
                                        </li>
                                    </ul>
                                    <div class="chart">
                                        <img src="./res/total_hist.png" alt="total_hist">
                                    </div>
                                </div>
                                <div class="chart_view c5">
                                    <h3>항목별 비정상 추세</h3>
                                    <div class="chart_wrap_box">
                                        <div class="chart_wrap">
                                            <h4>CPU 사용률</h4>
                                            <div class="chart">
                                                <img src="./res/cpu_trend.png" alt="cpu_trend">
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>팬상태</h4>
                                            <div class="chart">
                                                <img src="./res/fan_trend.png" alt="port_trend">
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>포트 상태</h4>
                                            <div class="chart">
                                                <img src="./res/port_trend.png" alt="port_trend">
                                            </div>
                                        </div>
                                    <div>
                                </div>
                            </div>
                        </article>
                        <article>
                            <h2><i>02</i>To-Do List</h2>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <colgroup>
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                    <col style="width: 25%" />
                                </colgroup>
                                <thead>
                                    <tr>
                                        <th>그룹명</th>
                                        <th>장비</th>
                                        <th>점검항목</th>
                                        <th>비정상률</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:56%;"></div>
                                                <span>56</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:70%;"></div>
                                                <span>70</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <!-- 100% 이상의 값은 width="100%" 고정 / span 안에 수치만 변동 -->
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:100%;"></div>
                                                <span>108</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>1F통신실</td>
                                        <td>V6848XG</td>
                                        <td>CPU 사용량</td>
                                        <td>
                                            <div class="progress">
                                                <div class="progress_bar" style="width:5%;"></div>
                                                <span>5</span>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <div class="notice">
                                <dl>
                                    <dt>조치사항</dt>
                                    <dd>CPU 사용률 조회 (Show CPU) 후 장비 리부팅</dd>
                                    <dd>조치사항 2</dd>
                                    <dd>조치사항 3</dd>
                                </dl>
                            </div>
                        </article>
                        <article>
                            <h2><i>03</i>일주일 내 비정상 발생 건수</h2>
                            <table width="100%" cellpadding="0" cellspacing="0">
                                <colgroup>
                                    <col style="width: 20%" />
                                    <col style="width: 17%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 8%" />
                                    <col style="width: 15%" />
                                </colgroup>
                                <thead>
                                    <tr>
                                        <th>장비명</th>
                                        <th>점검항목</th>
                                        <th>D-6</th>
                                        <th>D-5</th>
                                        <th>D-4</th>
                                        <th>D-3</th>
                                        <th>D-2</th>
                                        <th>D-1</th>
                                        <th>2021-09-27</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>V6848XG</td>
                                        <td>CPU 부하</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>V6848XG</td>
                                        <td>포트 점검</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>E5624R</td>
                                        <td>전원</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>E5624R</td>
                                        <td>포트다운</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                    <tr>
                                        <td>U9500H</td>
                                        <td>메모리 점검</td>
                                        <td>1</td>
                                        <td>0</td>
                                        <td>0</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                        <td>3</td>
                                    </tr>
                                </tbody>
                            </table>
                        </article>
                        <article>
                            <h2><i>04</i>상세정보</h2>
                            <div class="info_box">
                                <div class="preview">
                                    <ul>
                                        <li class="date">
                                            <p>점검일시</p>
                                            <span>2021-09-27 14:43:25</span>
                                        </li>
                                        <li>
                                            <p>장비</p>
                                            <span>V6848XG</span>
                                        </li>
                                        <li>
                                            <p>점검항목</p>
                                            <span>CPU 사용량</span>
                                        </li>
                                    </ul>
                                </div>
                                <h3>실행조건</h3> 
                                <div class="condition">MEM_USAGE ＜＝ 10</div>
                                <h3>실행결과</h3> 
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 10%" />
                                        <col style="width: 8%" />
                                        <col style="width: 10%" />
                                        <col style="width: 15%" />
                                        <col style="width: 12%" />
                                        <col style="width: 15%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>NAME</th>
                                            <th>STATUS</th>
                                            <th>MODEL</th>
                                            <th>ID</th>
                                            <th>IPADDR</th>
                                            <th>MAC</th>
                                            <th>MEM_USAGE</th>
                                            <th>CPU_USAGE</th>
                                            <th>SSID</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                    </tbody>
                                </table>
                            </div>
                            <div class="info_box">
                                <div class="preview">
                                    <ul>
                                        <li class="date">
                                            <p>점검일시</p>
                                            <span>2021-09-27 14:43:25</span>
                                        </li>
                                        <li>
                                            <p>장비</p>
                                            <span>V6848XG</span>
                                        </li>
                                        <li>
                                            <p>점검항목</p>
                                            <span>CPU 사용량</span>
                                        </li>
                                    </ul>
                                </div>
                                <h3>실행조건</h3> 
                                <div class="condition">MEM_USAGE ＜＝ 10</div>
                                <h3>실행결과</h3> 
                                <table width="100%" cellpadding="0" cellspacing="0">
                                    <colgroup>
                                        <col style="width: 10%" />
                                        <col style="width: 8%" />
                                        <col style="width: 10%" />
                                        <col style="width: 15%" />
                                        <col style="width: 12%" />
                                        <col style="width: 15%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                        <col style="width: 10%" />
                                    </colgroup>
                                    <thead>
                                        <tr>
                                            <th>NAME</th>
                                            <th>STATUS</th>
                                            <th>MODEL</th>
                                            <th>ID</th>
                                            <th>IPADDR</th>
                                            <th>MAC</th>
                                            <th>MEM_USAGE</th>
                                            <th>CPU_USAGE</th>
                                            <th>SSID</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                        <tr>
                                            <td>defGsp_112</td>
                                            <td>RUN</td>
                                            <td>AR-WF6-2541</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>172.30.2.112</td>
                                            <td>1C:EC:72:01;8A:48</td>
                                            <td>26.68</td>
                                            <td>2.18</td>
                                            <td>-</td>
                                        </tr>                         
                                    </tbody>
                                </table>
                            </div>
                        </article>
                    </section>     
                </div>
            </body>
            </html>

        '''

        with open('html.html', 'w', encoding='UTF-8') as f:
            f.write(html)

        pdfkit.from_file('html.html', '점검리포트.pdf', configuration=config, options=options)

    def generate_plot(self, df, filename):

        name = filename[4:7]

        # '항목별 비정상 추세'
        fig, ax = plt.subplots(figsize=(2.25, 2))
        ax.plot(df['date'].values[:7], df[name].values[:7], label=u'이번달', color="#1bc0e1")
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # plt.ylabel('비정상 장비수', fontsize=10, rotation=90)
        plt.legend(fontsize=8, loc='upper right')
        plt.xticks(df['date'].values, fontsize=8)
        plt.yticks(fontsize=8)

        plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0.05)
        plt.show()

    def horizontal_bar(self, df, filename):

        # '그룹별 장비 비정상 현황', '비정상 항목 현황'
        fig, ax = plt.subplots(figsize=(3.2, 1.6))
        obj = df['total_obj'].values[:4]
        y_pos = np.arange(len(obj))  # Todo position?
        performance = df['total_stat'].values[:4]

        ax.barh(y_pos, performance, align='center',
                color=['#1bc0e1', '#9CCC3D', '#FF3333', '#FF9933', '#363b47'])
        ax.set_yticks(y_pos)
        ax.set_yticklabels(obj, fontsize=10)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # plt.xticks(fontsize=10)
        plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

    def vertical_bar(self, df, filename):

        # '비정상 장비 추세'
        x = np.arange(3)
        obj = ['CPU 사용률', '팬상태', '포트상태']
        values = df['grp_stat'].values[:3]
        fig, ax = plt.subplots(figsize=(2, 1.6))

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        plt.bar(x, values, width=0.25, color='#1bc0e1')
        plt.xticks(x, obj, fontsize=8)
        plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

if __name__ == "__main__":
    test = PdfGenerator()
    test.run()