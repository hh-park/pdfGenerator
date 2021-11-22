#!/usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
                    .notice dl dt::after {{
                        content: "";
                        position: absolute;
                        right: 0;
                        display: inline-block;
                        width: 1px;
                        height: 50px;
                        background: #ccc;
                    }}
                    .notice dl dd {{
                        width: 75%;
                        color: #3A404D;
                        float: left;
                        min-height: 70px;
                    }}
                    .notice dl dd p {{
                      top: 5px;
                      left: 20px;
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
                        padding: 40px 0;
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
                        padding: 0 0 10px;
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
                        background: url("../images/ico_topology.png") no-repeat;
                        margin: 0 10px 0 0;
                        width: 21px;;
                        height: 21px;
                    }}
                    header .summary .box h1 span,
                    .subtitle p {{
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
                        border: 1px solid #fff;
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
                        padding: 0 0 40px;
                    }}
                    .subtitle h1 {{
                        font-size: 18pt;
                        text-align: center;
                    }}
                    .subtitle h1::before {{
                        display: none;
                    }}
                    section,
                    header {{
                        page-break-inside: avoid;
                        page-break-after: always;
                    }}
                    .info_box {{
                        page-break-before: auto;
                    }}
                    table td {{
                        height: 5mm;
                    }}
                    table tr {{
                        page-break-inside: avoid;
                        page-break-after: auto;
                    }}
                </style>
        '''

        try:

            inspect_name = result['workflowName']
            inspect_date = result['runDate']
            inspect_date_short = datetime.strptime(inspect_date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

            group = []
            switch_cnt = []
            ap_cnt = []
            apc_cnt = []

            statCheck = ''
            sumCheck = ''
            summary_by_grp = pd.DataFrame(
                columns=['groupName', 'deviceType', 'nochangeCount', 'createCount', 'updateCount', 'deleteCount'])
            summary_by_grp.loc[0] = ['그룹명', '장비종류', '추가', '제거', '변경', '변동없음']
            summary_by_eq = pd.DataFrame(
                columns=['rootName', 'deviceName', 'checkState', 'ip', 'title', 'vendor'])
            summary_by_eq.loc[0] = ['그룹명', '장비명', '상태', 'IP', '모델명', '제조사']

            if not len(result['reportData']) == 0:
                for i, v in enumerate(result['reportData']):

                    group.append(v['groupName'])
                    # 형상 점검 결과
                    if 'groupCheckResult' in v and 'deviceCheckResult' in v:
                        if not len(v['groupCheckResult']) == 0:
                            grp_df = pd.DataFrame(v['groupCheckResult'])
                            grpName = [group[i] for num in v['groupCheckResult']]
                            grp_df.insert(0, "groupName", grpName, True)
                            summary_by_grp = summary_by_grp.append(grp_df)

                        if not len(v['deviceCheckResult']) == 0:
                            device_df = pd.DataFrame(v['deviceCheckResult'])
                            summary_by_eq = summary_by_eq.append(device_df)

                        grpCheck_table = summary_by_grp.to_html(index=False, classes='summary_table')
                        eqCheck_table = summary_by_eq.to_html(index=False, classes='eq_table')
                        statCheck = f'''
                            <div class="box">
                                <h1 class="ty2">형상 점검 결과<span>{inspect_date}</span></h1>
                                {grpCheck_table}
                                <h2>장비 현황</h2>
                                {eqCheck_table}
                            </div>
                        '''

                    # 자동 점검 결과
                    if 'autoCheckResult' in v:
                        auto_result = {}
                        auto_result['Group'] = group
                        auto_result_col = ['Group']

                        for j in v['autoCheckResult']:
                            auto_result_col.append(j['deviceType'])
                            if j['deviceType'] == 'Switch':
                                switch_cnt.append('비정상 ' + str(j['abnormalCount']) + '대')
                                auto_result['Switch'] = switch_cnt
                            elif j['deviceType'] == 'AP':
                                ap_cnt.append('비정상 ' + str(j['abnormalCount']) + '대')
                                auto_result['AP'] = ap_cnt
                            else:
                                apc_cnt.append('비정상 ' + str(j['abnormalCount']) + '대')
                                auto_result['APC'] = apc_cnt

                        summary_df = pd.DataFrame(auto_result)
                        summary_autochk = pd.DataFrame(columns=auto_result_col)
                        summary_autochk.loc[0] = auto_result_col
                        summary_autochk = summary_autochk.append(summary_df)

                        summary_table = summary_autochk.to_html(index=False)
                        sumCheck = f'''
                            <div class="box">
                                <h1>자동 점검 결과<span>{inspect_date}</span></h1>
                                {summary_table}
                            </div>
                        '''

            else:
                print('\'reportData\' is empty')
                return {
                    "msg": False,
                    "succ": True
                }

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
                            <h1>자동 점검 리포트</h1>
                            {statCheck}
                            {sumCheck}
                        </div>
                    </header>
            '''

            html_list = []
            html_list.append(html_main)

            for i, v in enumerate(result['reportData']):

                if int(v['deviceTotalCount']) == 0:
                    continue

                if 'autoCheckResult' in v:
                    grp_name = v['groupName']
                    total_device = v['deviceTotalCount']  # 그룹 전체 장비수
                    ab_device_cnt = v['abnormalDeviceCount']
                    alert_device_cnt = 0
                    if not ab_device_cnt == None:
                        alert_device_cnt = ab_device_cnt['currentAbnormalCount'] - ab_device_cnt['beforeAbnormalCount']
                        # 현재 비정상 장비수 - 하루 전 비정상 장비수

                    # 그룹별 장비 비정상 현황
                    grp_alert = ''
                    alert_by_grp = pd.DataFrame(v['abnormalDeviceStatus'])
                    if not len(alert_by_grp) == 0:
                        self.horizontal_bar(alert_by_grp, 'grp', i)
                        grp_alert = f'''<img src="../img/grp_alert{str(i)}.png" alt="grp_alert{str(i)}">'''

                    # 비정상 항목 현황
                    total_alert = ''
                    alert_by_item = pd.DataFrame(v['abnormalItemStatus'])
                    if not len(alert_by_item) == 0:
                        self.horizontal_bar(alert_by_item, 'total', i)
                        total_alert = f'''<img src="../img/total_alert{str(i)}.png" alt="total_alert{str(i)}">'''
                    top_items = alert_by_item['name'].values[:3]

                    # 비정상 장비 추세
                    total_trend = ''
                    total_alert_trend = pd.DataFrame(v['abnormalDeviceTrend'])
                    if not len(total_alert_trend) == 0:
                        self.generate_trend(total_alert_trend, i)
                        total_trend = f'''<img src="../img/total_trend{str(i)}.png" alt="total_trend{str(i)}">'''

                    # 항목별 비정상 추세
                    item_alert_trend = pd.DataFrame(v['abnormalItemTrend'])
                    chart_box_list = []
                    chart_wrap_box = ''
                    if not len(item_alert_trend) == 0:
                        for item in top_items:
                            box = self.generate_item_trend(item_alert_trend, item, i)

                            chart_box = f'''
                                <div class="chart_wrap">
                                    <h4>{item} 상태</h4>
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
                                            <li><span>그룹명</span>{todo_grp}</li>
                                            <li><span>장비명</span>{todo_device}</li>
                                            <li><span>점검항목</span>{todo_item}</li>
                                        </ul>
                                        <dl>
                                            <dt>조치사항</dt>
                                            <dd><p>{todo_detail}</p></dd>
                                        </dl>
                                    </div>
                                </div>
                            '''
                            todos.append(todo_notice)
                        todo_list = ' '.join(todos)

                    # 일주일 내 비정상 발생 건수
                    week_total_table = ''
                    if not len(v['abnormalWeek']) == 0:
                        week = pd.DataFrame(v['abnormalWeek'])
                        week2 = pd.DataFrame(
                            columns=['deviceName', 'workitemName', 'd6AbnormalCount', 'd5AbnormalCount', 'd4AbnormalCount',
                                     'd3AbnormalCount', 'd2AbnormalCount', 'd1AbnormalCount', 'd0AbnormalCount'])
                        week2.loc[0] = ['장비명', '점검항목', 'D-6', 'D-5', 'D-4', 'D-3', 'D-2', 'D-1', inspect_date_short]
                        week2 = week2.append(week)
                        week_total_table = week2.to_html(index=False)

                    # 장비별 상세정보
                    device_details = []
                    device_detail_list = ''
                    if not len(v['runResult']) == 0:
                        for r in v['runResult']:
                            device_name = r['deviceName']
                            work_item_name = r['workitemName']
                            work_condition = r['dataJson']  # todo 임성준 차장
                            work_result = pd.read_json(r['dataJson'])
                            new_work_result = pd.DataFrame(columns=work_result.columns.tolist())
                            new_work_result.loc[0] = work_result.columns.tolist()
                            new_work_result = new_work_result.append(work_result)
                            work_table = new_work_result.to_html(index=False)

                            item_detail = f'''
                                <div class="info_box">
                                    <div class="list_box">
                                          <div class="notice">
                                              <ul>
                                                  <li><span>장비명</span>{device_name}</li>
                                                  <li><span>점검항목</span>{work_item_name}</li>
                                              </ul>
                                              <dl>
                                                  <dt>실행조건</dt>
                                                  <dd><p>work_condition</p></dd>
                                              </dl>
                                          </div>
                                    </div>
                                    <h3>실행결과</h3> 
                                    {work_table}
                                </div>
                            '''
                            device_details.append(item_detail)

                        device_detail_list = ' '.join(device_details)

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
                                        {grp_alert}
                                        </div>
                                    </div>
                                    <div class="chart_view c3">
                                        <h3>비정상 항목 현황</h3>
                                        <div class="chart">
                                        {total_alert}
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
                                <h2><i>03</i>일주일 내 비정상 발생 건수</h2>
                                {week_total_table}
                            </article>
                            <article class="item_detail_table">
                                <h2><i>04</i>장비별 상세정보</h2>
                                {device_detail_list}
                            </article>
                        </section>
                    '''

                    html_list.append(section)

            html_list.append('<div> </body> </html>')
            html = ' '.join(html_list)

            now = datetime.now()
            now_date = now.strftime('%Y%m%d')
            # with open(f'''./etc/{now_date}_일일점검리포트.html''', 'w', encoding='UTF-8') as f:
            with open(f'''./etc/{now_date}_{inspect_name}.html''', 'w', encoding='UTF-8') as f:

                f.write(html)

            # pdfkit.from_file(f'''./etc/{now_date}_일일점검리포트.html''', f'''./pdf/{now_date}_일일점검리포트.pdf''', configuration=config, options=options)
            pdfkit.from_file(f'''./etc/{now_date}_{inspect_name}.html''', f'''./pdf/{now_date}_{inspect_name}.pdf''', configuration=config, options=options)

        except Exception as e:
            print(e)
            return {
                "error": e,
                "msg": False,
                "succ": False
            }

    # 비정상 장비 추세
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

        # style
        ax.set_ylabel('비정상\n 장비수', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 1.05)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        tmp_yval = list(set(y_value))
        if not len(tmp_yval) == 1:
            ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            plt.yticks(fontsize=7)
        else:
            plt.yticks(range(0, tmp_yval[0] + 5), fontsize=7)

        if len(x_dates) < 7:
            plt.xticks(x_tick, x_dates, fontsize=7, rotation=30)
        else:
            plt.xticks(x_tick, x_ticks, fontsize=7, rotation=30)

        plt.savefig(str('./img/total_trend' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)

    # 항목별 비정상 추세
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

        # style
        ax.set_ylabel('비정상\n 장비수', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.15, 1.05)  # ylabel loc
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        tmp_yval = list(set(y_values))
        if not len(tmp_yval) == 1:
            ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
            plt.yticks(fontsize=7)
        else:
            plt.yticks(range(0, tmp_yval[0] + 5), fontsize=7)

        if len(x_dates) < 7:
            plt.xticks(x_tick, x_dates, fontsize=7, rotation=30)
        else:
            plt.xticks(x_tick, x_ticks, fontsize=7, rotation=30)

        chart = str('./img/' + key + '_trend' + str(index) + '.png')
        plt.savefig(chart, dpi=100, bbox_inches='tight', pad_inches=0.01)

        return f'<img src=".{chart}" alt="{key}_trend{str(index)}">'

    # '그룹별 장비 비정상 현황', '비정상 항목 현황'
    def horizontal_bar(self, df, key, index):

        fig, ax = plt.subplots(figsize=(3.2, 1.6))
        y_tick = np.arange(len(df['name']))
        y_label = df['name']
        y_value = df['abnormalCount']
        ax.barh(y_tick, y_value, align='center',
                color=['#1bc0e1', '#9CCC3D', '#FF3333', '#FF9933', '#363b47'])

        # 범례
        if key == 'total':
            ax.set_ylabel('항목', rotation=0, fontsize=8)
        elif key == 'grp':
            ax.set_ylabel('그룹', rotation=0, fontsize=8)
        ax.yaxis.set_label_coords(-0.1, 1)
        ax.set_xlabel('비정상 수', fontsize=8)
        ax.xaxis.set_label_coords(-0.1, 0)

        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

        plt.xticks(fontsize=7)
        plt.yticks(y_tick, y_label, fontsize=7)  # y축 구성
        plt.savefig(str('./img/' + key + '_alert' + str(index) + '.png'), dpi=100, bbox_inches='tight', pad_inches=0.01)

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


if __name__ == "__main__":
    test = PdfGenerator()
    test.run()
