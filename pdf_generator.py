#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime
from collections import OrderedDict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import os
import pdfkit
import json
import datetime

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

    def __init__(self, web):
        self.web = web
        self.opt = self.web['opt']
        self.plots = []
        self.data = {}
        plt.rcParams["font.family"] = 'KT font'

    def run(self):

        '''
        1. matplotlib 위치 찾기
        2. mpl-data/fonts/ttf에 ttf 폰트 설치
        3. cache directory 찾아서 fontlist-v330.json 파일 삭제
        4. font family 이름 알아내서 rcParams 설정

        font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
        f = [f.name for f in fm.fontManager.ttflist if 'KT' in f.name]
        '''

        with open('./pdf_data_sample.json', encoding='UTF-8') as json_file:
            self.data = json.load(json_file)

        result = self.data['data']
        self.generate_report(result)

        # with dummy data
        example = {
            "inspection": [
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2020-12-31 14:58:27.089000",
                            "id": "1002",
                            "fan": 1,
                            "port": 4,
                            "cpu": 7,
                            "port2": 2
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-01 14:58:27.089000",
                            "id": "1007",
                            "fan": 2,
                            "port": 5,
                            "cpu": 5,
                            "port2": 2
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-02 14:58:27.089000",
                            "id": "1004",
                            "fan": 2,
                            "port": 0,
                            "cpu": 0,
                            "port2": 2
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-03 14:58:27.089000",
                            "id": "1006",
                            "fan": 5,
                            "port": 6,
                            "cpu": 2,
                            "port2": 1
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-04 14:58:27.089000",
                            "id": "1009",
                            "fan": 4,
                            "port": 3,
                            "cpu": 4,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-05 14:58:27.089000",
                            "id": "1002",
                            "fan": 10,
                            "port": 2,
                            "cpu": 3,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-06 14:58:27.089000",
                            "id": "1007",
                            "fan": 8,
                            "port": 4,
                            "cpu": 0,
                            "port2": 3
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-07 14:58:27.089000",
                            "id": "1004",
                            "fan": 3,
                            "port": 2,
                            "cpu": 3,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-08 14:58:27.089000",
                            "id": "1006",
                            "fan": 7,
                            "port": 4,
                            "cpu": 0,
                            "port2": 3
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-09 14:58:27.089000",
                            "id": "1009",
                            "fan": 1,
                            "port": 2,
                            "cpu": 3,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-10 14:58:27.089000",
                            "id": "1011",
                            "fan": 4,
                            "port": 4,
                            "cpu": 9,
                            "port2": 3
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-11 14:58:27.089000",
                            "id": "1012",
                            "fan": 3,
                            "port": 2,
                            "cpu": 3,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-12 14:58:27.089000",
                            "id": "1013",
                            "fan": 7,
                            "port": 4,
                            "cpu": 0,
                            "port2": 3
                        }

                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-13 14:58:27.089000",
                            "id": "1014",
                            "fan": 1,
                            "port": 2,
                            "cpu": 3,
                            "port2": 1
                        }
                },
                {
                    "category": "building",
                    "buildingID": "b001",
                    "inspection_data":
                        {
                            "date": "2021-01-14 14:58:27.089000",
                            "id": "1015",
                            "fan": 4,
                            "port": 4,
                            "cpu": 9,
                            "port2": 3
                        }

                }
            ]
        }
        '''
        df_list = []
        for i in range(len(example['inspection'])):
            df_list.append(example['inspection'][i]['inspection_data'])
        df = pd.DataFrame(df_list)
        imageList = ['grp_alert', 'total_alert', 'total_hist', 'cpu_trend', 'fan_trend', 'port_trend']
        for f in df_list[0]:
            if 'port' in f:
                self.plots.append(f)
            elif f in ['cpu', 'fan']:
                self.plots.append(f)

        for key in self.plots:
            self.generate_plot(df, key)

        for key in ['grp', 'total']:
            self.horizontal_bar(df, key)

        # self.vertical_bar(df)
        self.generate_trend(df)

        return self.generate_report()
        '''

    def generate_report(self, result):

        # html component
        style = f'''
                <style type="text/css">
            /* KT font */
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 400;
                src: url("../font/KTfontLight.woff") format('woff'),
                    url("../font/KTfontLight.eot"),
                    url("../font/KTfontLight.eot?#iefix") format('embedded-opentype');
            }}
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 500;
                src: url("../font/KTfontMedium.woff") format('woff'),
                    url("../font/KTfontMedium.eot"),
                    url("../font/KTfontMedium.eot?#iefix") format('embedded-opentype');
            }}
            @font-face {{
                font-family: "KT";
                font-style: normal;
                font-weight: 600;
                src: url("../font/KTfontBold.woff") format('woff'),
                    url("../font/KTfontBold.eot"),
                    url("../font/KTfontBold.eot?#iefix") format('embedded-opentype');
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
                background: url("../images/ico_building.png") no-repeat;
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
                background: url("../images/ico_up.png") no-repeat;
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
                background: url("../images/ico_down.png") no-repeat;
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
            .chart_view.c4 .chart_wrap {{
                float: none;
                display: block;
                width: 100%;
            }}
            .chart_view.c4 .chart {{
                height: 190px;
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
            .info_box table + table {{
                margin: 30px 0 0;
            }}
            .list_box + .list_box {{
                margin: 30px 0 0;
            }}
            .notice {{
                margin: 5px 0;
                text-align: left;
            }}
            .notice ul {{
                position: relative;
                display: inline-block;
                clear: both;
                padding: 10px;
                border-radius: 10px 10px 0 0;
                background: #3A404D;
                z-index: 5;
            }}
            .notice ul li {{
                float: left;
                height: 23px;
                display: inline-block;
                font-size: 12pt;
                font-weight: 600;
                vertical-align: middle;
                margin: 0 15px 0 0;
                color: #fff;
            }}
            .notice ul li span {{
                display: inline-block;
                font-size: 8.5pt;
                padding: 3px 10px;
                background: rgba(255, 255, 255, 0.2);
                color: #ddd;
                border-radius: 5px;
                margin: 0 10px 0 0;
                vertical-align: middle;
            }}
            .notice dl {{
                flex-direction: column;
                width: 100%;
                height: 100%;
                padding: 15px;
                border: 1px dashed #3A404D;
                margin: -8px 0 0;
            }}
            .notice dl dt,
            .notice dl dd {{
                text-align: left;
            }}
            .notice dl dt {{
                font-size: 10pt;
                font-weight: 600;
                color: #3A404D;
                margin: 0 0 10px;
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
            .preview {{
                display: inline-block;
                width: 100%;
                height: 170px;
                margin: 0 0 10px;
                clear: both;
            }}
            .preview ul {{
                position: relative;
                display: inline-block;
                width: 25%;
                float: left;
            }}
            .preview ul li {{
                position: relative;
                display: inline-block;
                width: 100%;
                height: 80px;
                border-radius: 5px;
            }}
            .preview ul li.green {{
                background: #e6f7f1;
            }}
            .preview ul li.green h2,
            .preview ul li.green span {{
                color: #29cc8c;
            }}
            .preview ul li.green::after {{
                position: absolute;
                right: 15px;
                top: 15px;
                content: '';
                background: url("../images/ico_info_g.png") no-repeat;
                width: 18px;
                height: 18px;
            }}
            .preview ul li.blue {{
                background: #eff2fc;
            }}
            .preview ul li.blue h2,
            .preview ul li.blue span {{
                color: #3d2eec;
            }}
            .preview ul li.blue::after {{
                position: absolute;
                right: 15px;
                top: 15px;
                content: '';
                background: url("../images/ico_info_b.png") no-repeat;
                width: 18px;
                height: 18px;
            }}
            .preview ul li span {{
                position: absolute;
                width: 100%;
                bottom: 10px;
                text-align: center;
                font-size: 10pt;
            }}
            .preview ul li h2 {{
                text-align: center;
                font-size: 15pt;
                font-weight: 600;
            }}
            .preview ul li + li {{
                margin: 5px 0 0;
            }}
            .preview .condition {{
                width: 74%;
                height: 170px;
                float: right;
                font-weight: 600;
                padding: 10px;
                background: #f9f9f9;
                border-top: 3px double #ddd;
                border-bottom: 3px double #ddd;
            }}
            .preview .condition h3 {{
                margin: 0 0 20px;
                padding: 0;
            }}
            .preview .condition p {{
                font-style: 10pt;
                line-height: 1.2rem;
                text-align: left;
            }}
            .none::before,
            .none::after {{
                display: none;
            }}
            .confirm_ok {{
                background: #f9f9f9;
                color: #3A404D;
                font-size: 11pt;
                font-weight: 600;
                padding: 50px 0!important;
            }}
            .confirm_ok strong {{
                color: #1bc0e1;
            }}
        </style>
        '''

        inspect_name = result['workflowName']
        inspect_date = result['runDate']

        html_main = f'''
                <!DOCTYPE html>
                    <html>
                    <head>
                        <meta charset="utf-8">
                        {style}
                    </head>
                    <body>
                        <div class="content">
                            <header>
                                <h1>자동 점검 리포트</h1>
                                <h2>({inspect_name})</h2>
                                <div class="box">
                                    <p>{inspect_date}</p>
                                </div>
                                <div class="summary">
                                    <div class="box">
                                        <h3 class="blue">자동 점검 결과</h3>
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <colgroup>
                                                <col style="width: 33.33%" />
                                                <col style="width: 33.33%" />
                                                <col style="width: 33.33%" />
                                            </colgroup>
                                            <thead>
                                                <tr>
                                                    <th>Group</th>
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
                                        <h3 class="green">형상 점검 결과</h3>
                                        <table width="100%" cellpadding="0" cellspacing="0">
                                            <colgroup>
                                                <col style="width: 33.33%" />
                                                <col style="width: 33.33%" />
                                                <col style="width: 33.33%" />
                                            </colgroup>
                                            <thead>
                                                <tr>
                                                    <th>Group</th>
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
        '''

        ''' list로 html close
                    </div>
                </body>
            </html>
        '''

        html_list = []
        html_list.append(html_main)

        for i, v in enumerate(result['reportData']):
            grp_name = v['groupName']
            print(grp_name)
            total_device = v['deviceTotalCount'] # 그룹 전체 장비수
            alert_device_cnt = 0
            if not v['abnormalDeviceCount'] == None:
                alert_device_cnt = v['abnormalDeviceCount']['currentAbnormalCount'] - v['abnormalDeviceCount']['beforeAbnormalCount']
                                # 현재 비정상 장비수 - 하루 전 비정상 장비수

            # 그룹별 장비 비정상 현황
            alert_by_grp = pd.DataFrame(v['abnormalDeviceStatus'])
            self.horizontal_bar(alert_by_grp, 'grp', i)
            grp_alert = 'grp_alert'+ str(i)

            # 비정상 항목 현황
            alert_by_item = pd.DataFrame(v['abnormalItemStatus'])
            self.horizontal_bar(alert_by_item, 'total', i)
            total_alert = 'total_alert' + str(i)
            top_items = alert_by_item['name'].values[:3]

            # 비정상 장비 추세
            total_alert_trend = pd.DataFrame(v['abnormalDeviceTrend'])
            if not len(total_alert_trend) == 0:
                self.generate_trend(total_alert_trend, i)
                total_trend = f'''<img src="../img/total_trend{str(i)}.png" alt="total_trend">'''
            else:
                total_trend = '<p>No data to display</p>'

            # 항목별 비정상 추세
            item_alert_trend = pd.DataFrame(v['abnormalItemTrend'])
            first_name = top_items[0]
            second_name = top_items[1]
            third_name = top_items[2]
            if not len(item_alert_trend) == 0:
                for item in top_items:
                    self.generate_item_trend(item_alert_trend, item, i)
                first_trend = f'''<img src="../img/{first_name}_trend{str(i)}.png" alt="{first_name}_trend">'''
                second_trend = f'''<img src="../img/{second_name}_trend{str(i)}.png" alt="{second_name}_trend">'''
                third_trend = f'''<img src="../img/{third_name}_trend{str(i)}.png" alt="{third_name}_trend">'''

            else:
                first_trend = '<p>No data to display</p>'
                second_trend = '<p>No data to display</p>'
                third_trend = '<p>No data to display</p>'

            # todoList
            todo_df = v['toDoList']
            todos = []
            if not len(todo_df) == 0:
                for t in todo_df:
                    todo_grp = t['groupName']
                    todo_device = t['deviceName']
                    todo_item = t['workitemName']
                    todo_detail = t['workscriptGuide']

                    todo_notice = f'''
                            <div class="list_box">
                                <div class="notice">
                                    <ul>
                                        <li><span>그룹명</span>{todo_grp}</li>
                                        <li><span>장비명</span>{todo_device}</li>
                                        <li><span>점검항목</span>{todo_item}</li>
                                    </ul>
                                    <dl>
                                        <dt>조치사항</dt>
                                        <dd>{todo_detail}</dd>
                                    </dl>
                                </div>
                            </div>
                    '''
                    todos.append(todo_notice)

                todo_list = ' '.join(todos)

            section = f'''
                <section>
                        <h1>{grp_name}</h1>
                        <article class="graph">
                            <h2><i>01</i>진단결과</h2>
                            <div class="chart_box">
                                <div class="chart_view c1">
                                    <h3>비정상장비</h3>
                                    <ul>
                                        <li class="up">
                                            <span>{alert_device_cnt}</span>어제
                                        </li>
                                        <li class="total">
                                            <p>
                                                <b>장비수</b>
                                                <span>{total_device}</span>
                                            </p>
                                        </li>
                                    </ul>
                                </div>
                                <div class="chart_view c2">
                                    <h3>그룹별 장비 비정상 현황</h3>
                                    <div class="chart">
                                        <img src="../img/{grp_alert}.png" alt="grp_alert">
                                    </div>
                                </div>
                                <div class="chart_view c3">
                                    <h3>비정상 항목 현황</h3>
                                    <div class="chart">
                                        <img src="../img/{total_alert}.png" alt="total_alert">
                                    </div>
                                </div>
                            </div>
                            <div class="chart_box">
                                <div class="chart_view c4">
                                    <h3>비정상 장비 추세</h3>
                                    <div class="chart_wrap">
                                        <h4 class="none">&nbsp;</h4>
                                        <div class="chart">
                                            {total_trend}
                                        </div>
                                    </div>
                                </div>
                                <div class="chart_view c5">
                                    <h3>항목별 비정상 추세</h3>
                                    <div class="chart_wrap_box">
                                        <div class="chart_wrap">
                                            <h4>{first_name} 상태</h4>
                                            <div class="chart">
                                                {first_trend}
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>{second_name} 상태</h4>
                                            <div class="chart">
                                                {second_trend}
                                            </div>
                                        </div>
                                        <div class="chart_wrap">
                                            <h4>{third_name} 상태</h4>
                                            <div class="chart">
                                                {third_trend}
                                            </div>
                                        </div>
                                    <div>
                                </div>
                            </div>
                        </article>
                        <article>
                            <h2><i>02</i>To-Do List</h2>                  
                            {todo_list}
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
                            <h2><i>04</i>장비별 상세정보</h2>
                            <div class="info_box">
                                <div class="preview">
                                    <ul>
                                        <li class="blue">
                                            <h2>V6848XG</h1>
                                            <span>장비명</span>
                                        </li>
                                        <li class="green">
                                            <h2>CPU 사용량</h2>
                                            <span>점검항목</span>
                                        </li>
                                    </ul>
                                    <div class="condition">
                                        <h3>실행조건</h3> 
                                        <p>MEM_USAGE ＜＝ 10</p>
                                    </div>
                                </div>
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
                                        <li class="blue">
                                            <h2>V6848XG</h1>
                                            <span>장비명</span>
                                        </li>
                                        <li class="green">
                                            <h2>CPU 사용량</h2>
                                            <span>점검항목</span>
                                        </li>
                                    </ul>
                                    <div class="condition">
                                        <h3>실행조건</h3> 
                                        <p>MEM_USAGE ＜＝ 10</p>
                                    </div>
                                </div>
                                <h3>실행결과</h3> 
                                <table width="100%" cellpadding="0" cellspacing="0">
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
                                <table width="100%" cellpadding="0" cellspacing="0">
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
                                            <th>test</th>
                                            <th>test2</th>
                                            <th>test3</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>AR-WF6-2541 AR-WF6-2541 AR-WF6-2541 AR-WF6-2541 AR-WF6-2541</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                        </tr>
                                        <tr>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>AR-WF6-2541</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                            <td>-</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </article>
                    </section>
        '''

            html_list.append(section)

        html_list.append('<div> </body> </html>')
        html = ' '.join(html_list)

        now = datetime.datetime.now()
        now_date = now.strftime('%Y%m%d')
        with open(f'''./etc/{now_date}_일일점검리포트.html''', 'w', encoding='UTF-8') as f:
            f.write(html)

        pdfkit.from_file(f'''./etc/{now_date}_일일점검리포트.html''', f'''./pdf/{now_date}_일일점검리포트.pdf''', configuration=config, options=options)

    # '항목별 비정상 추세'
    def generate_plot(self, df, key):

        fig, ax = plt.subplots(figsize=(2.25, 1.75))
        dates = df['date'].values[-7:]
        ax.plot(dates, df[key].values[-7:], label=u'현재', color="#1bc0e1")
        ax.plot(dates, df[key].values[-14:-7], label=u'1주전', color="#9CCC3D")
        ax.plot(dates, df[key].values[-7:] - 1, label=u'1달전', color="#FF3333")

        # simple date format: M-D
        xaxis = []
        xdate = list(np.array(df['date'].tolist()))
        for i in xdate:
            a = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f')
            xaxis.append(datetime.datetime.strftime(a, '%m-%d'))
        xnp = np.arange(len(dates))

        # y축 범례
        ax.set_ylabel('비정상\n 장비수', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 0.98)  # ylabel loc

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        plt.legend(fontsize=8, loc='upper right')
        plt.xticks(xnp, xaxis[-7:], fontsize=7, rotation=45)
        plt.yticks(fontsize=7)
        plt.savefig(str('./img/' + key + '_trend.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

    # 비정상 장비 추세
    def generate_trend(self, df, index):

        fig, ax = plt.subplots(figsize=(2.25, 1.75))
        x = df['groupDate']
        x_tick = np.arange(len(x))
        x_dates = self.date_formatter(x)
        y_value = df['abnormalCount']
        ax.plot(x_dates, y_value, label=u'최근 일주일', color="#1bc0e1")

        # style
        ax.set_ylabel('비정상\n 장비수', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 0.98)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        plt.legend(fontsize=8, loc='upper right')
        plt.xticks(x_tick, x_dates, fontsize=7, rotation=15)
        plt.yticks(fontsize=7)
        plt.savefig(str('./img/total_trend' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

    # 항목별 비정상 추세
    def generate_item_trend(self, df, key, index):

        fig, ax = plt.subplots(figsize=(2.25, 1.75))
        x = df['groupDate']
        x_tick = np.arange(len(x))
        x_dates = self.date_formatter(x)
        y_values = []
        for i in df['list']:
            for j in i:
                if j['name'] == key:
                    y_values.append(j['abnormalCount'])

        ax.plot(x_dates, y_values, label=u'최근 일주일', color="#1bc0e1")

        # style
        ax.set_ylabel('비정상\n 장비수', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 0.98)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        plt.legend(fontsize=8, loc='upper right')
        plt.xticks(x_tick, x_dates, fontsize=7, rotation=15)
        plt.yticks(fontsize=7)
        plt.savefig(str('./img/' + key + '_trend' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

    # '그룹별 장비 비정상 현황', '비정상 항목 현황'
    def horizontal_bar(self, df, key, index):

        fig, ax = plt.subplots(figsize=(3.2, 1.6))
        y_tick = np.arange(len(df['name']))
        y_label = df['name']
        value = df['abnormalCount']
        ax.barh(y_tick, value, align='center',
                color=['#1bc0e1', '#9CCC3D', '#FF3333', '#FF9933', '#363b47'])

        # 범례
        ax.set_ylabel('항목', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.1, 1)
        ax.set_xlabel('비정상 수', fontsize=8)
        ax.xaxis.set_label_coords(1.1, -0.05)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        plt.xticks(fontsize=7)

        if 0 in value.values:
            plt.xticks(range(0,10,2))

        plt.yticks(y_tick, y_label, fontsize=7) # y축 구성
        plt.savefig(str('./img/' + key + '_alert' + str(index) +'.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)
        plt.show()

    def date_formatter(self, date):

        result = []
        date_list = list(np.array(date.tolist()))
        for i in date_list:
            a = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f')
            result.append(datetime.datetime.strftime(a, '%m-%d %H:%M'))

        return result

if __name__ == "__main__":
    # JSON EXAMPLE
    web = {
        'opt': {
            'building_name': 'Building A',
            'abnormal': 1,
            'ap': 1,
            'inspection_date': '',

        }
    }

    test = PdfGenerator(web)
    test.run()
