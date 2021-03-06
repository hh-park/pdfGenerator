#!/usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdfkit
import json
from datetime import datetime

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
        self.plots = []
        self.data = {}
        plt.rcParams["font.family"] = 'KT font'

    def generate_report(self, result):

        # html component
        style1 = f'''
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
                margin: 40px 0; 
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
                width: 21px;;
                height: 21px;
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
                padding: 0 10px 10px;
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
                height: 300px;
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
                content: '???';
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
                height: 215px;
            }}
            .chart_view.c5 .chart {{
                height: 215px;
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
                border-bottom:  2px dotted #ccc;
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
                display: inline-block;	
                width: 100%;
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
            .week_data_table table th:nth-child(1) {{	
                width: 20%;	
            }}	
            .week_data_table table th:nth-child(2) {{	
                width: 17%;	
            }}	
            .preview {{
                display: inline-block;
                width: 100%;
                min-height: 170px;
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
                min-height: 170px;
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
            header .summary h1 {{
                margin: 80px 0;
                font-size: 22pt;
                text-align: center;
            }}
            header .summary h1::before {{
                display: none;
            }}
            header .summary .box {{
                margin:  0 0 50px;
            }}
            header .summary .box + .box {{
                border-top: 2px dotted #ccc;
                padding-top: 40px;
            }}
            header .summary .box h1 {{
                text-align: left;
                font-size: 13.5pt;
                margin: 0 0 10px;
                color: #3A404D;
                clear: both;
            }}
            header .summary .box h1::before {{
                content: '';
                position: relative;
                display: inline-block;
                top: 6px;
                background: url("../images/ico_report.png") no-repeat;
                margin: 0 10px 0 0;
                width: 21px;;
                height: 21px;
            }}
            header .summary .box h1.ty2::before {{
                content: '';
                position: relative;
                display: inline-block;
                top: 6px;
                background: url("../images/ico_report2.png") no-repeat;
                margin: 0 10px 0 0;
                width: 21px;;
                height: 21px;
            }}
            header .summary .box h1 span {{
                display: inline-block;
                padding: 3px 15px;
                background: #3A404D;
                color: #fff;
                border-radius: 20px;
                font-weight: 600;
                font-size: 9pt;
                float: right;
                margin: 3px 0 0;
            }}
            header .summary .box h2 {{
                font-size: 11.5pt;
                text-align: left;
                margin: 20px 0 10px;
            }}
            header .summary .box h2::before {{
                content: "";
                display: inline-block;
                width: 4px;
                height: 4px;
                background: #3A404D;
                border-radius: 4px;
                margin: 0 5px 0 0;
            }}
            header .summary .box table.dataframe summary_table th:nth-child(1) {{
                width: 20%;
            }}
            header .summary .box table.dataframe summary_table th:nth-child(2) {{
                width: 20%;
            }}
            header .summary .box table.dataframe summary_table tr:nth-child(even) td:nth-child(3),
            header .summary .box table.dataframe summary_table tr:nth-child(odd) td:nth-child(2) {{
                color: #FF3333;
                font-weight: 600;
            }}
            header .summary .box table.dataframe summary_table tr:nth-child(even) td:nth-child(4),
            header .summary .box table.dataframe summary_table tr:nth-child(odd) td:nth-child(3) {{
                color: #1bc0e1;
                font-weight: 600;
            }}
            header .summary .box table.eq_table th:nth-child(1) {{
                width: 15%;
            }}
            header .summary .box table.eq_table td:nth-child(1) {{
                font-weight: 600;
            }}
            header .summary .box table.eq_table td span::before {{
                content: "";
                display: inline-block;
            }}
            header .summary .box table.eq_table td span.add::before {{
                content: "+";
                display: inline-block;
                margin: 0 5px 0 0;
                color: #999;
            }}
            header .summary .box table.eq_table td span.del::before {{
                content: "-";
                display: inline-block;
                margin: 0 5px 0 0;
                color: #999;
            }}
            header .summary .box table.eq_table td span.modify::before {{
                content: "???";
                display: inline-block;
                margin: 0 5px 0 0;
                color: #999;
            }}
            table {{
                width: 100%;
                table-layout: fixed;
                border: none;
                border-spacing: 0;
                border-collapse: collapse;
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
                border-left: 1px solid #fff;
            }}
            table thead {{	
                display: none;	
            }}	
            table tr:nth-child(1) td {{	
                border: none;	
                border-bottom: 2px solid #333;	
                border-top: 1px solid #333;	
                background: #ffffff;	
                text-align: center;	
                font-weight: 600;	
            }}
            .subtitle {{
                margin: 50px 0;
            }}
            .subtitle h1 {{
                font-size: 16pt;
                text-align: center;
            }}
            .subtitle h1::before {{
                content: "[";
                margin: 0 5px 0 0;
                color: #999;
                background: none;
                width: auto;
                height: auto;
                top: 0;
            }}
            .subtitle h1::after {{
                content: "]";
                margin: 0 0 0 5px;
                color: #999;
            }}
            @media print {{
                section,
                header {{
                    page-break-before: always;
                }}
                .info_box {{
                    border: none;
                    padding: 0;
                    page-break-before: auto;
                }}
                header .summary .box {{
                    border: none;
                    padding: 0;
                }}
                table td {{
                    height: 5mm;
                }}
                table tr {{
                    page-break-inside: avoid;
                    page-break-after: auto;
                }}
                .preview {{
                    min-height: 45mm;
                }}
                .preview .condition {{
                    border-top: 1px solid #ddd;
                    border-bottom: 1px solid #ddd;
                }}
            }}
        </style>
        '''

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
                margin: 40px 0; 
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
                width: 21px;;
                height: 21px;
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
                padding: 0 10px 10px;
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
                height: 570px;
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
                height: 300px;
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
                content: '???';
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
                height: 215px;
            }}
            .chart_view.c5 .chart {{
                height: 215px;
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
            }}
            .info_box:last-child {{
                margin: 0;
                padding: 0;
                border: none;
            }}
            .info_box table + table {{
                margin: 30px 0 0;
            }}
            .notice {{
                text-align: left;
                display: inline-block;	
                width: 100%;
            }}
            .notice ul {{
                position: relative;
                display: inline-block;
                clear: both;
                padding: 10px 40px;
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
                color: #fff;
            }}
            .notice ul li + li {{
              margin: 0 0 0 100px;
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
                display: inline-block;
                width: 100%;
                height: 100%;
                padding: 15px;
                border: 1px solid #3A404D;
                margin: -8px 0 0;
                clear: both;
            }}
            .notice dl dt,
            .notice dl dd {{
              display: inline-block;
                text-align: left;
            }}
            .notice dl dt {{
                top: 10px;
                width: 20%;
                font-size: 10pt;
                font-weight: 600;
                color: #3A404D;
                float: left;
            }}
            .notice dl dd {{
                width: 75%;
                color: #3A404D;
                float: left;
                min-height: 70px;
            }}
            .notice dl dd p {{
              top: -10px;
              display: inline-block;
              font-size: 9pt;
              line-height: 1.5rem;
              margin-block-start: 0;
              margin-block-end: 0;
              text-align: left;
              color: #3A404D;
            }}
            .notice dl dd p::before {{
                content: '-';
                font-weight: 600;
                color: #3A404D;
                font-size: 12pt;
                margin: 0 5px 0 0;
            }}
            .preview {{
                display: inline-block;
                width: 100%;
                min-height: 170px;
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
                min-height: 170px;
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
            header .summary h1 {{
                margin: 80px 0;
                font-size: 22pt;
                text-align: center;
            }}
            header .summary h1::before {{
                display: none;
            }}
            header .summary .box {{
                margin:  0 0 50px;
            }}
            header .summary .box + .box {{
                border-top: 1px dashed #999;
                padding-top: 40px;
            }}
            header .summary .box h1 {{
                text-align: left;
                font-size: 13.5pt;
                margin: 0 0 10px;
                color: #3A404D;
                clear: both;
            }}
            header .summary .box h1::before {{
                content: '';
                position: relative;
                display: inline-block;
                top: 6px;
                background: url("../images/ico_report.png") no-repeat;
                margin: 0 10px 0 0;
                width: 21px;;
                height: 21px;
            }}
            header .summary .box h1.ty2::before {{
                content: '';
                position: relative;
                display: inline-block;
                top: 6px;
                background: url("../images/ico_report2.png") no-repeat;
                margin: 0 10px 0 0;
                width: 21px;;
                height: 21px;
            }}
            header .summary .box h1 span {{
                display: inline-block;
                padding: 3px 15px;
                background: #3A404D;
                color: #fff;
                border-radius: 20px;
                font-weight: 600;
                font-size: 9pt;
                float: right;
                margin: 3px 0 0;
            }}
            header .summary .box h2 {{
                font-size: 11.5pt;
                text-align: left;
                margin: 20px 0 10px;
            }}
            header .summary .box h2::before {{
                content: "";
                display: inline-block;
                width: 4px;
                height: 4px;
                background: #3A404D;
                border-radius: 4px;
                margin: 0 5px 0 0;
            }}
            .summary_table td:nth-child(1) {{
                width: 20%;
            }}
            .summary_table td:nth-child(2) {{
                width: 20%;
            }}
            .eq_table td:nth-child(1) {{
                width: 20%;
            }}
            .eq_table td:nth-child(2) {{
                width: 20%;
            }}
            .week_data_table td:nth-child(1) {{	
                width: 20%;	
            }}	
            .week_data_table td:nth-child(2) {{	
                width: 17%;	
            }}	
            table {{
                width: 100%;
                table-layout: fixed;
                border: none;
                border-color: #fff;
                border-spacing: 0;
                border-collapse: collapse;
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
                border-left: 1px solid #fff;
            }}
            table thead {{	
                display: none;	
            }}	
            table tr:nth-child(1) td {{	
                border: none;	
                border-bottom: 2px solid #333;	
                border-top: 1px solid #333;	
                background: #ffffff;	
                text-align: center;	
                font-weight: 600;	
            }}
            .subtitle {{
                padding: 70px 0;
            }}
            .subtitle h1 {{
                font-size: 16pt;
                text-align: center;
            }}
            .subtitle h1::before {{
                content: "[";
                margin: 0 5px 0 0;
                color: #999;
                background: none;
                width: auto;
                height: auto;
                top: 0;
            }}
            .subtitle h1::after {{
                content: "]";
                margin: 0 0 0 5px;
                color: #999;
            }}
            @media print {{
                section,
                header {{
                    page-break-inside: avoid;
                    page-break-after: auto;
                }}
                .info_box {{
                    page-break-before: auto;
                }}
                header .summary .box {{
                    border: none;
                    padding: 0;
                }}
                table td {{
                    height: 5mm;
                }}
                table tr {{
                    page-break-inside: avoid;
                    page-break-after: auto;
                }}
            }}
        </style>

        '''

        inspect_date = result['runDate']
        inspect_date_short = datetime.strptime(inspect_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        group = []
        type_cnt1 = []
        type_cnt2 = []
        summary_by_grp = pd.DataFrame(
            columns=['groupName', 'deviceType', 'nochangeCount', 'createCount', 'updateCount', 'deleteCount'])
        summary_by_grp.loc[0] = ['?????????', '????????????', '??????', '??????', '??????', '????????????']
        summary_by_eq = pd.DataFrame(
            columns=['rootName', 'deviceName', 'checkState', 'ip', 'standardCheck', 'deviceName'])
        summary_by_eq.loc[0] = ['?????????', '?????????', '??????', 'IP', '?????????', '?????????']
        summary_autochk = pd.DataFrame(columns=['Group', 'Switch', 'AP'])
        summary_autochk.loc[0] = ['Group', 'Switch', 'AP']

        for i, v in enumerate(result['reportData']):

            group.append(v['groupName'])
            # ?????? ?????? ??????
            if not len(v['groupCheckResult']) == 0:
                grp_df = pd.DataFrame(v['groupCheckResult'])
                grpName = [group[i], group[i]]
                grp_df.insert(0, "groupName", grpName, True)
                summary_by_grp = summary_by_grp.append(grp_df)

            if not len(v['deviceCheckResult']) == 0:
                device_df = pd.DataFrame(v['deviceCheckResult'])
                summary_by_eq = summary_by_eq.append(device_df)

            # ?????? ?????? ??????
            for j in v['autoCheckResult']:
                if j['deviceType'] == 'Switch':
                    type_cnt1.append('????????? ' + str(j['abnormalCount']) + '???')
                else:
                    type_cnt2.append('????????? ' + str(j['abnormalCount']) + '???')

        summary_df = pd.DataFrame({'Group': group, 'Switch': type_cnt1, 'AP': type_cnt2})
        summary_autochk = summary_autochk.append(summary_df)

        summary_table = summary_autochk.to_html(index=False)
        grpCheck_table = summary_by_grp.to_html(index=False, classes='summary_table')
        eqCheck_table = summary_by_eq.to_html(index=False, classes='eq_table')

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
        <div class="summary">
            <h1>?????? ?????? ?????????</h1>
            <div class="box">
                <h1 class="ty2">?????? ?????? ??????<span>{inspect_date}</span></h1>
                {grpCheck_table}
                <h2>?????? ??????</h2>
                {eqCheck_table}
            </div>
            <div class="box">
                <h1>?????? ?????? ??????<span>{inspect_date}</span></h1>
                {summary_table}
            </div>
        </div>
    </header>
    '''

        html_list = []
        html_list.append(html_main)

        for i, v in enumerate(result['reportData']):
            root_name = v['deviceCheckResult'][0]['rootName']
            grp_name = v['groupName']
            total_device = v['deviceTotalCount']  # ?????? ?????? ?????????
            ab_device_cnt = v['abnormalDeviceCount']
            alert_device_cnt = 0
            if not ab_device_cnt == None:
                alert_device_cnt = ab_device_cnt['currentAbnormalCount'] - ab_device_cnt['beforeAbnormalCount']
                # ?????? ????????? ????????? - ?????? ??? ????????? ?????????

            # ????????? ?????? ????????? ??????
            grp_alert = ''
            alert_by_grp = pd.DataFrame(v['abnormalDeviceStatus'])
            if not len(alert_by_grp) == 0:
                self.horizontal_bar(alert_by_grp, 'grp', i)
                # grp_alert = 'grp_alert' + str(i)
                grp_alert =  f'''<img src="../img/grp_alert{str(i)}.png" alt="grp_alert">'''

            # ????????? ?????? ??????
            total_alert = ''
            alert_by_item = pd.DataFrame(v['abnormalItemStatus'])
            if not len(alert_by_item) == 0:
                self.horizontal_bar(alert_by_item, 'total', i)
                # total_alert = 'total_alert' + str(i)
                total_alert = f'''<img src="../img/total_alert{str(i)}.png" alt="total_alert">'''
            top_items = alert_by_item['name'].values[:3]

            # ????????? ?????? ??????
            total_alert_trend = pd.DataFrame(v['abnormalDeviceTrend'])
            if not len(total_alert_trend) == 0:
                self.generate_trend(total_alert_trend, i)
                total_trend = f'''<img src="../img/total_trend{str(i)}.png" alt="total_trend">'''
            else:
                total_trend = '<p>No data to display</p>'

            # ????????? ????????? ??????
            item_alert_trend = pd.DataFrame(v['abnormalItemTrend'])
            chart_box_list = []
            chart_wrap_box = ''
            if not len(item_alert_trend) == 0:
                for item in top_items:
                    box = self.generate_item_trend(item_alert_trend, item, i)

                    chart_box = f'''
                        <div class="chart_wrap">
                            <h4>{item} ??????</h4>
                            <div class="chart">
                                {box}
                            </div>
                        </div>  
                    '''
                    chart_box_list.append(chart_box)
                chart_wrap_box = ' '.join(chart_box_list)

            # todoList
            todos = []
            todo_list = ''
            if not len(v['toDoList']) == 0:
                for t in v['toDoList']:
                    todo_grp = t['groupName']
                    todo_device = t['deviceName']
                    todo_item = t['workitemName']
                    todo_detail = t['workscriptGuide']

                    todo_notice = f'''
                        <div class="list_box">
                            <div class="notice">
                                <ul>
                                    <li><span>?????????</span>{todo_grp}</li>
                                    <li><span>?????????</span>{todo_device}</li>
                                    <li><span>????????????</span>{todo_item}</li>
                                </ul>
                                <dl>
                                    <dt>????????????</dt>
                                    <dd>{todo_detail}</dd>
                                </dl>
                            </div>
                        </div>
                    '''
                    todos.append(todo_notice)
                todo_list = ' '.join(todos)

            # ????????? ??? ????????? ?????? ??????
            week_total_table = ''
            if not len(v['abnormalWeek']) == 0:
                week = pd.DataFrame(v['abnormalWeek'])
                week2 = pd.DataFrame(
                    columns=['deviceName', 'workitemName', 'd6AbnormalCount', 'd5AbnormalCount', 'd4AbnormalCount',
                             'd3AbnormalCount', 'd2AbnormalCount', 'd1AbnormalCount', 'd0AbnormalCount'])
                week2.loc[0] = ['?????????', '????????????', 'D-6', 'D-5', 'D-4', 'D-3', 'D-2', 'D-1', inspect_date_short]
                week2 = week2.append(week)
                week_total_table = week2.to_html(index=False)

            # ????????? ????????????
            device_details = []
            device_detail_list = ''
            if not len(v['runResult']) == 0:
                for r in v['runResult']:
                    device_name = r['deviceName']
                    work_item_name = r['workitemName']
                    work_condition = r['dataJson']  # todo ????????? ??????
                    work_result = pd.read_json(r['dataJson'])
                    new_work_result = pd.DataFrame(columns=work_result.columns.tolist())
                    new_work_result.loc[0] = work_result.columns.tolist()
                    new_work_result = new_work_result.append(work_result)
                    work_table = new_work_result.to_html(index=False)

                    item_detail = f'''
                        <div class="info_box">
                            <div class="preview">
                                <ul>
                                    <li class="blue">
                                        <h2>{device_name}</h1>
                                        <span>?????????</span>
                                    </li>
                                    <li class="green">
                                        <h2>{work_item_name}</h2>
                                        <span>????????????</span>
                                    </li>
                                </ul>
                                <div class="condition">
                                    <h3>????????????</h3> 
                                    <p>work_condition</p>
                                </div>
                            </div>
                            <h3>????????????</h3> 
                            {work_table}
                        </div>
                    '''
                    device_details.append(item_detail)

                device_detail_list = ' '.join(device_details)

            section = f'''
                <section>
                    <div class="subtitle">
                        <h1>{root_name}</h1>
                    </div>
                    <h1>{grp_name}</h1>
                    <article class="graph">
                        <h2><i>01</i>????????????</h2>
                        <div class="chart_box">
                            <div class="chart_view c1">
                                <h3>???????????????</h3>
                                <ul>
                                    <li class="up">
                                        <span>{alert_device_cnt}</span>??????
                                    </li>
                                    <li class="total">
                                        <p>
                                            <b>?????????</b>
                                            <span>{total_device}</span>
                                        </p>
                                    </li>
                                </ul>
                            </div>
                            <div class="chart_view c2">
                                <h3>????????? ?????? ????????? ??????</h3>
                                <div class="chart">
                                    <img src="../img/{grp_alert}.png" alt="grp_alert">
                                </div>
                            </div>
                            <div class="chart_view c3">
                                <h3>????????? ?????? ??????</h3>
                                <div class="chart">
                                    <img src="../img/{total_alert}.png" alt="total_alert">
                                </div>
                            </div>
                        </div>
                        <div class="chart_box">
                            <div class="chart_view c4">
                                <h3>????????? ?????? ??????</h3>
                                <div class="chart_wrap">
                                    <h4 class="none">&nbsp;</h4>
                                    <div class="chart">
                                        {total_trend}
                                    </div>
                                </div>
                            </div>
                            <div class="chart_view c5">
                                <h3>????????? ????????? ??????</h3>
                                <div class="chart_wrap_box">
                                    {chart_wrap_box}
                                <div>
                            </div>
                        </div>
                    </article>
                    <article>
                        <h2><i>02</i>To-Do List</h2>                  
                        {todo_list}
                    </article>
                    <article class="week_data_table">
                        <h2><i>03</i>????????? ??? ????????? ?????? ??????</h2>
                        {week_total_table}
                    </article>
                    <article class="item_detail_table">
                        <h2><i>04</i>????????? ????????????</h2>
                        {device_detail_list}
                    </article>
                </section>
        '''

            html_list.append(section)

        html_list.append('<div> </body> </html>')
        html = ' '.join(html_list)

        now = datetime.now()
        now_date = now.strftime('%Y%m%d')
        with open(f'''./etc/{now_date}_?????????????????????.html''', 'w', encoding='UTF-8') as f:
            f.write(html)

        pdfkit.from_file(f'''./etc/{now_date}_?????????????????????.html''', f'''./pdf/{now_date}_?????????????????????.pdf''',
                         configuration=config, options=options)

    # ????????? ?????? ??????
    def generate_trend(self, df, index):

        fig, ax = plt.subplots(figsize=(2.25, 1.75))
        x_tick = np.arange(len(df['groupDate']))
        x_dates = self.date_formatter(df['groupDate'])
        x_ticks = []
        for i, v in enumerate(x_dates):
            if i % 2 == 1:
                x_ticks.append('')
            else:
                x_ticks.append(v)
        y_value = df['abnormalCount']
        ax.plot(x_dates, y_value, color="#1bc0e1")
        # ax.plot(x_dates, y_value, label=u'?????? ?????????', color="#1bc0e1")

        # style
        ax.set_ylabel('?????????\n ?????????', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 1.05)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # plt.legend(fontsize=8, loc='upper right')
        if len(x_dates) < 7:
            plt.xticks(x_tick, x_dates, fontsize=7, rotation=30)
            plt.yticks(range(0, 10, 2), fontsize=7)
        else:
            plt.xticks(x_tick, x_ticks, fontsize=7, rotation=30)
            plt.yticks(fontsize=7)
        plt.savefig(str('./img/total_trend' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)

    # ????????? ????????? ??????
    def generate_item_trend(self, df, key, index):

        fig, ax = plt.subplots(figsize=(2.25, 1.75))
        x = df['groupDate']
        x_tick = np.arange(len(x))
        x_dates = self.date_formatter(x)
        x_ticks = []
        for i, v in enumerate(x_dates):
            if i % 2 == 1:
                x_ticks.append('')
            else:
                x_ticks.append(v)
        y_values = []
        for i in df['list']:
            for j in i:
                if j['name'] == key:
                    y_values.append(j['abnormalCount'])

        if not len(x_tick) == len(y_values):
            return 'No Chart'
        ax.plot(x_dates, y_values, color="#1bc0e1")
        # ax.plot(x_dates, y_values, label=u'?????? ?????????', color="#1bc0e1")

        # style
        ax.set_ylabel('?????????\n ?????????', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 1.05)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # plt.legend(fontsize=8, loc='upper right')
        # ?????? ???(ticks), ?????? ?????????(ticklabels)
        if len(x_dates) < 7:
            plt.xticks(x_tick, x_dates, fontsize=7, rotation=30)
            plt.yticks(range(0, 8, 2), fontsize=7)
        else:
            plt.xticks(x_tick, x_ticks, fontsize=7, rotation=30)
            plt.yticks(fontsize=7)
        chart = str('./img/' + key + '_trend' + str(index) + '.png')
        plt.savefig(chart, dpi=100, bbox_inches='tight', pad_inches=0.01)

        return f'<img src=".{chart}" alt="{key}_trend">'

    # '????????? ?????? ????????? ??????', '????????? ?????? ??????'
    def horizontal_bar(self, df, key, index):

        fig, ax = plt.subplots(figsize=(3.2, 1.6))
        y_tick = np.arange(len(df['name']))
        y_label = df['name']
        y_value = df['abnormalCount']
        ax.barh(y_tick, y_value, align='center',
                color=['#1bc0e1', '#9CCC3D', '#FF3333', '#FF9933', '#363b47'])

        # ??????
        if key == 'total':
            ax.set_ylabel('??????', rotation=0, fontsize=8)
        elif key == 'grp':
            ax.set_ylabel('??????', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.1, 1)
        ax.set_xlabel('????????? ???', fontsize=8)
        ax.xaxis.set_label_coords(-0.1, 0)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        plt.xticks(fontsize=7)

        if 0 in y_value.values:
            plt.xticks(range(0, 10, 2))

        plt.yticks(y_tick, y_label, fontsize=7)  # y??? ??????
        plt.savefig(str('./img/' + key + '_alert' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)
        # plt.show()

    def date_formatter(self, date):

        result = []
        date_list = list(np.array(date.tolist()))
        date_list.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
        for i in date_list:
            a = datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
            result.append(datetime.strftime(a, '%m-%d %H:%M'))

        return result

    def run(self):

        '''
        1. matplotlib ?????? ??????
        2. mpl-data/fonts/ttf??? ttf ?????? ??????
        3. cache directory ????????? fontlist-v330.json ?????? ??????
        4. font family ?????? ???????????? rcParams ??????

        font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
        f = [f.name for f in fm.fontManager.ttflist if 'KT' in f.name]
        '''

        with open('./data_json_1.json', encoding='UTF-8') as json_file:
            self.data = json.load(json_file)

        result = self.data['data']
        self.generate_report(result)


if __name__ == "__main__":
    test = PdfGenerator()
    test.run()
