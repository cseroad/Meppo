#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import random
import re
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Seeyon_OA_finereport_login'
AUTHOR="CSeroad"
REMARK='致远OA 帆软报表登录'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/seeyonreport/ReportServer?op=fs_load&cmd=fs_signin&_=1673833136504"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r1 = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if 'FineReport' in r1.text and r1.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['vuln_url'] = vuln_url
            return result
        else:
            pass
    except Exception as e:
        pass

def exp(target):
    pass


if __name__ == '__main__':
    poc("https://127.0.0.1")