# -*- coding: utf-8 -*-

'''
모든 기능을 open api 로 제공하는 것에 따른 장단점.
    장점:
        1. 구조가 명확해 진다. 내가 개발할 내용을 먼저 api로 정리함으로 처음부터 설계가 이루어진다.
    단점:
        1. db conn, ssh conn과 같은 자원은 제약이 있는 리소스인데 너무 기능들을 api로 분리하면,
            개발 api 내부에서 db/ssh 에 대한 과다한 session/conn/disconn 이 소비될 수 있다.
            이를 해결하려면, 다수의 db/ssh 세션이 필요한 경우 먼저 object를 요청하고 이를 하부 api에
            제공하여 이를 활용한다. 이를 위해서 object를 pickle 정보로 제공하도록 한다.
'''

api_command_handler = {}

api_command_handler['/pdf'] = {
    'request_main' :  ('service.pdf_generator', 'PdfGenerator')
}