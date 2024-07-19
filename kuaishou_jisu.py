#!/usr/bin/python
# coding=utf-8
import sys
import os
import traceback
import requests
import json

SIGN_LOG = 'logs/kuaishou_sign.log'

work_path = os.path.dirname(os.path.abspath(__file__))
SIGN_LOG_FILE = os.path.join(work_path, SIGN_LOG)

refresh_token = "kpn=NEBULA; kpf=ANDROID_PHONE; userId=2763747982; did=ANDROID_66ed15311dadd22f; c=XIAOMI; language=zh-cn; countryCode=CN; sys=ANDROID_14; deviceName=Xiaomi%2823113RKC6C%29; isp=CTCC; ud=2763747982; did_tag=0; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_3f57e8fb0870bfce; boardPlatform=kalama; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1705064314945; cdid_tag=2; max_memory=256; oc=XIAOMI; sh=2400; deviceBit=0; browseType=3; ddpi=420; socName=Qualcomm+Snapdragon+8550; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=15199; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_9762e02834b49e76; sbh=90; darkMode=false; __NSWJ=; client_key=2ac2a76d; kcv=1571; earphoneMode=1; mod=Xiaomi%2823113RKC6C%29; is_background=0; didv=1713301393000; ll_client_time=1714411484883; thermal=10000; icaver=1; ver=12.5; appver=12.5.20.8014; net=WIFI; egid=DFP16BB0F69775469CC6A8108391C5682C98AA6A8F54CFABB7CC31A656D05A6F; keyconfig_state=1; lkvr=YXaLig6qYZ1yvobBi63NbElRVKVnrXDADDxicFFfMblyaNyK6PZbSA7SKvK5GZL9PASYpw; sid=b17118ee-9582-4e16-b999-2d9b308bdaff; cold_launch_time_ms=1719719968786; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP1H4YY2gXlkO10JNjdhDvSiwGsrkcON-pyS_HZwl75xCJNPBb6OLKFQdALJ7UIAf-uC8KLC-9-0Mvc6-EGZGalJUckXV-JKBceMl9aXM_gBBFMY2rJuW93OANXhLS8cGvieTOtEXUC9PDv7Vbn_VhdShzlGnRef6inkMtkzdxFnDtp0LKgGohUcPIXiETOKTWj7wZ7vozBFAamh3QEcGFGhK5DKy8pMdHv5ArtkvHGsl__xMiIOeXrJczwAeI723kdXuKllS1F3Zkpw0ueEEfMcmKAU2MKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP1H4YY2gXlkO10JNjdhDvSiwGsrkcON-pyS_HZwl75xCJNPBb6OLKFQdALJ7UIAf-uC8KLC-9-0Mvc6-EGZGalJUckXV-JKBceMl9aXM_gBBFMY2rJuW93OANXhLS8cGvieTOtEXUC9PDv7Vbn_VhdShzlGnRef6inkMtkzdxFnDtp0LKgGohUcPIXiETOKTWj7wZ7vozBFAamh3QEcGFGhK5DKy8pMdHv5ArtkvHGsl__xMiIOeXrJczwAeI723kdXuKllS1F3Zkpw0ueEEfMcmKAU2MKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQmSZWDP9vZHy7n8RmGfZmIOOoixACZkebUAomKFApITqH0ois71Yiyw6VniwFoYQM6KyU1kY1uo5GOHNRmjjqupUNw2P97Z4mYINx_vUs0-4cxzV5m6Ji4bXe2hjSpCW3LY0wSj0pzHtzAwYKoch_dosvf5dDsCiUAwrVMCjGdfLhUCSFJKXpUhOHYIbbmnCqbkAqinsET0FLgmRPwhztYaEp0eftNRumGRlTzDnTam4VQFlCIgvGwesDlCybmn4pqhmh3RYlrRXlQ5nMpN2pPtzDFdLyEoBTAB"
a_token = "kpn=NEBULA; kpf=ANDROID_PHONE; userId=2763747982; did=ANDROID_66ed15311dadd22f; c=XIAOMI; language=zh-cn; countryCode=CN; sys=ANDROID_14; deviceName=Xiaomi%2823113RKC6C%29; isp=CTCC; ud=2763747982; did_tag=0; app=0; bottom_navigation=true; android_os=0; oDid=ANDROID_3f57e8fb0870bfce; boardPlatform=kalama; newOc=XIAOMI; androidApiLevel=34; slh=0; country_code=cn; nbh=42; hotfix_ver=; did_gt=1705064314945; cdid_tag=2; max_memory=256; oc=XIAOMI; sh=2400; deviceBit=0; browseType=3; ddpi=420; socName=Qualcomm+Snapdragon+8550; sw=1080; ftt=; apptype=22; abi=arm64; cl=0; userRecoBit=0; device_abi=arm64; totalMemory=15199; grant_browse_type=AUTHORIZED; iuid=; rdid=ANDROID_9762e02834b49e76; sbh=90; darkMode=false; __NSWJ=; client_key=2ac2a76d; kcv=1571; earphoneMode=1; mod=Xiaomi%2823113RKC6C%29; is_background=0; didv=1713301393000; thermal=10000; icaver=1; ver=12.5; kuaishou.api_st=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP1H4YY2gXlkO10JNjdhDvSiwGsrkcON-pyS_HZwl75xCJNPBb6OLKFQdALJ7UIAf-uC8KLC-9-0Mvc6-EGZGalJUckXV-JKBceMl9aXM_gBBFMY2rJuW93OANXhLS8cGvieTOtEXUC9PDv7Vbn_VhdShzlGnRef6inkMtkzdxFnDtp0LKgGohUcPIXiETOKTWj7wZ7vozBFAamh3QEcGFGhK5DKy8pMdHv5ArtkvHGsl__xMiIOeXrJczwAeI723kdXuKllS1F3Zkpw0ueEEfMcmKAU2MKAUwAQ; token=Cg9rdWFpc2hvdS5hcGkuc3QSoAEP1H4YY2gXlkO10JNjdhDvSiwGsrkcON-pyS_HZwl75xCJNPBb6OLKFQdALJ7UIAf-uC8KLC-9-0Mvc6-EGZGalJUckXV-JKBceMl9aXM_gBBFMY2rJuW93OANXhLS8cGvieTOtEXUC9PDv7Vbn_VhdShzlGnRef6inkMtkzdxFnDtp0LKgGohUcPIXiETOKTWj7wZ7vozBFAamh3QEcGFGhK5DKy8pMdHv5ArtkvHGsl__xMiIOeXrJczwAeI723kdXuKllS1F3Zkpw0ueEEfMcmKAU2MKAUwAQ; kuaishou.h5_st=Cg5rdWFpc2hvdS5oNS5zdBKgAQmSZWDP9vZHy7n8RmGfZmIOOoixACZkebUAomKFApITqH0ois71Yiyw6VniwFoYQM6KyU1kY1uo5GOHNRmjjqupUNw2P97Z4mYINx_vUs0-4cxzV5m6Ji4bXe2hjSpCW3LY0wSj0pzHtzAwYKoch_dosvf5dDsCiUAwrVMCjGdfLhUCSFJKXpUhOHYIbbmnCqbkAqinsET0FLgmRPwhztYaEp0eftNRumGRlTzDnTam4VQFlCIgvGwesDlCybmn4pqhmh3RYlrRXlQ5nMpN2pPtzDFdLyEoBTAB; egid=DFP924D539BAA8F59D8920D5A4908356AC8021D4B05C6CB56DE5C9C97D2346FE; ll_client_time=1719788576068; appver=12.5.40.8118; net=WIFI; keyconfig_state=1; lkvr=p1PM2DFFkyxfDTu-pBDHZFCMGQcy-doFReFK3eGafulrUZGuj0MStEsG16Ri1BNYRUJX8A; sid=6ab725f1-96cc-4c2a-87b6-44b8af065deb; cold_launch_time_ms=1720148429975"

if refresh_token is None:
    print("请先在环境变量里添加 快手 token")
    exit(0)


def get_baoxiang(token):
    print('开始领取宝箱 💎💎')
    access_token = ''
    try:
        url = "https://nebula.kuaishou.com/rest/wd/encourage/unionTask/treasureBox/report?__NS_sig3=9585c2f24b478ba159c9bbcacdcc598667511e489bb347d7e36adadadcdcdfdee1c1&sigCatVer=1"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "Content-Length": "2",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://nebula.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.post(url, headers=headers, data=json.dumps({}))
        resp_json = resp.json()
        title_reward_count = resp_json['data']['title']['rewardCount']
        print(f"得到金币：{title_reward_count}")
    except:
        print(f"获取异常:{traceback.format_exc()}")

    return access_token


def get_fanbu(token):
    print("开始领取饭补 🍱")
    try:
        # 获取当前的是否领取过饭补
        url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/dish/detail?__NS_sig4=HUDR_sFnX-HFuAE5VsdPNKlLOPr4ntwVLcugxjxZz8_z61EHYFY07AGiHwMelb_ny_pMHxR_0BjgEKKQba1Uc3eSWmMYZtd0w8l4XDj-3MCjD__Ta_XvZSJ4TCB8KqqVKMgRgdptyHjC4q5WxkzlivWeuJ0H73Q5s2-4u88UkwHrtgNYFpaoTLyzpjhJN-kWm8EpIT1cd-4gSarv9lyc5NYynpqIeL1p8oDC_aNVs06Eqr9eEDO9WQN6bPOljEgPJOUyOx2TUE6Zol22dloUXNTFoJdgLPRKfw_RHi0y41S59Nig74-a-EOa976Kn3PySfizrwKPeBfIvE4O9ZR3FHGMRsQPwfpaekre0Ra5-_cMxO_S1KZimvzg8hzW00xtV2EkEeYPLRaBq8MgnbnxspIGrdAT7goeqm_Gr_PeS3rmTNMpgPIhHOlYIzTyVqRydZeTwh5ckgKW0moc1WndwyJqoqIh222uMxhDr_q2L_eyoTgrL6MkureEraDmbuEH0je0NPMrtCfeKHFlC$HE_4b541fe2abe1d0e080900198005f896a0e010702003764000000108874b29de1e08090019b563eda7b563e3100&sigCatVer=1"
        headers = {
            "Host": "encourage.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://encourage.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://encourage.kuaishou.com/activity/dish?layoutType=4&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDA4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8xNyIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDAwOCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzE3IiwiZXh0UGFyYW1zIjp7fX1dfV0",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }
        resp = requests.get(url, headers=headers)
        resp_json = resp.json()
        #print(resp.text)
        if resp_json['result'] == 1:
            if resp_json['data']['mainButtonInfo']['buttonStatus'] == 'TO_COMPLETE':

                url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/dish/report?__NS_sig4=HUDR_sFnX-HFuAE5VsdPNKlLOPr4ntwVLcugxjxZz8_z61EHYFY07AGiHwMelb_ny_pMHxR_0BjgEKKQba1Uc3eSWmMYZtd0w8l4XDj-3MCjD__Ta_XvZSJ4TCB8KqqVKMgRgdptyHjC4q5WxkzlivWeuJ0H73Q5s2-4u88UkwHrtgNYFpaoTLyzpjhJN-kWm8EpIT1cd-4gSarv9lyc5NYynpqIeL1p8oDC_aNVs06Eqr9eEDO9WQN6bPOljEgPJOUyOx2TUE6Zol22dloUXNTFoJdgLPRKfw_RHi0y41S59Nig74-a-EOa976Kn3PySfizrwKPeBfIvE4O9ZB3FHGMRsAPwfpaekre0Ra5-ycExO_S1JZimvzg8hzW00xtV2EkEeYPLRaBq8MgnbnxspIGrdAT7goeqm_Gr_PeS3rmTNMpgPIhHOlYIzTyVqRydZeTwh5ckgKW0moc1WndwyJqoqIh222uMxhDr_q2L_eyoTgrL6MkureEraDmbuEH0je0NPMrtCfeGHFlC$HE_4b541fe2abe1d0e080900153dec924ff8e0107020037680000001bdd71b4d02fe18090019b563eda7b563e9900&sigCatVer=1"

                # 定义请求头
                headers = {
                    "Host": "encourage.kuaishou.com",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
                    "content-type": "application/json",
                    "Accept": "*/*",
                    "Origin": "https://encourage.kuaishou.com",
                    "X-Requested-With": "com.kuaishou.nebula",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://encourage.kuaishou.com/activity/dish?layoutType=4&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDA4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8xNyIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDAwOCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzE3IiwiZXh0UGFyYW1zIjp7fX1dfV0",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie": token
                }

                # 发送 POST 请求
                resp = requests.post(url, headers=headers, data=json.dumps({}))
                resp_json = resp.json()
                if resp_json['result'] == 1:
                    title = resp_json['data']['title']
                    dsd = resp_json['data']['amount']
                    print(f"{title} 共计: {dsd}")
                else:
                    print(resp_json['error_msg'])
            else:
                buttonText = resp_json['data']['mainButtonInfo']['buttonText']
                print(f'还不到饭补时间         {buttonText}')
        else:
            print(resp_json['error_msg'])

    except:
        print(f"获取异常:{traceback.format_exc()}")


def get_money(token):
    print('🥰开始获取当前的现金  💰️💰️💰️💰️💰️💰️💰️')
    money = ''
    try:
        url = "https://nebula.kuaishou.com/rest/n/nebula/activity/earn/overview/basicInfo"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.get(url, headers=headers)
        
        resp_json = resp.json()
        money = resp_json['data']['allCash']
        print(f"现在的钱总共：{money}")
    except:
        print(f"获取异常:{traceback.format_exc()}")

    return money

def get_walk(token):
    print('开始执行步数换金币 🏃')
    try:

        url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/walking/detail?__NS_sig4=HUDR_sFnX-HFuAE5VsdPNKlLOPr4ntwVLcugxjxZz8_z61EHYFY07AGiHwMelb_ny_pMHxR_0BjgEKKQba1Uc3eSWmMYZtd0w8l4XDj-3MCjD__Ta_XvZSJ4TCB8KqqVKMgRgdptyHjC4q5WxkzlivWeuMEH73Q5s2-4u88UkwHrtgNYFpaoTLyzpjhJN-kWm8EpIT1cd-4gSarv9lyc5NYynpqIeL1p8oDC_aNVs06E48ZDBDPBAVd7Wcf92VBvKKxaMh3mQAe1nhm7Hio9fdjZvaMcUc1SdzvMQzAj21S59Nig74-a-EOa976Kn3PySfizrwKPeBfIvE4O9ZB3FHGMRsAPwfpaekre0Ra5-P8MxO_S1KZimvzg8hzW00xtV2EkPPYyfHfQ455BmZ2JctZayZle8i-X-z6H4p6yd16GOasouctNda1Yaxj6PrwadZeTwh5ckgKW0moc1WndwyJqoqIh222uMxhDr_q2L_eyoTgrL6MkureEraDmbuEH0je0NPMrtCfeKHFlC$HE_4b541fe2aba7096f7b9001c139646fdfa9010702003764000000408e77b2c51b6f7b90019b563eda7b563e2600&sigCatVer=1"
        headers = {
            "Host": "encourage.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.700 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha34 ksNebula/12.5.40.8118 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://encourage.kuaishou.com",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://encourage.kuaishou.com/activity/walk?layoutType=4&source=new_task_center&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDQ4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8yMiIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDA0OCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzIyIiwiZXh0UGFyYW1zIjp7fX1dfV0",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        data = {"reportCount":56060,"authorized":True,"stepDataStatus":1,"updateStepInfo":True}
        # 将 data 转换为 json 字符串，并计算其长度，设置 Content-Length
        data_json = json.dumps(data)
        headers['Content-Length'] = str(len(data_json))

        resp = requests.post(url, headers=headers, json=data)
        resp_json = resp.json()
        if resp_json['result'] == 1:
            walking_info = resp_json['data']['walkingInfo']
            rewarded = True
            for item in walking_info:
                if item['rewarded'] == False:
                    rewarded = False

            if rewarded == False:
                title = resp_json['data']['button']['text']
                print(f"可以领取:  {title}")

                url = "https://encourage.kuaishou.com/rest/wd/encourage/unionTask/reward?taskId=20048&rewardType=1&__NS_sig4=HUDR_sFnX-HFuAE5VsdPNKlLOPr4ntwVLcugxjxZz8_z61EHYFY07AGiHwMelb_ny_pMHxR_0BjgEKKQba1Uc3eSWmMYZtd0w8l4XDj-3MCjD__Ta_XvZSJ4TCB8KqqVKMgRgdptyHjC4q5WxkzlivWeuJkH73Q5s2-4u88UkwHrtgNYFpaoTLyzpjhJN-kWm8EpIT1cd-4gSarv9lyc5NYynpqIeL1p8oDC_aNVs06Eqr9eEDO9WQN6bPOljEgPJOUyOx2TUE6Zol22dloUXNTFoJdgLPRKfw_RHi0y41S59Nig74-a-EOa976Kn3PySfizrwKPeBfIvE4O9ZB3FHGMRsAPwfpaekre0Ra5-UsIxO_S1KJimvzg8hzW00xtV2EkEeYPLRaBq8MgnbnxspIGrdAT7goeqm_Gr_PeS3rmTNMpgPIhHOlYIzTyVqRydZeTwh5ckgKW0moc1WndwyJqoqIh222uMxhDr_q2L_eyoTgrL6MkureEraDmbuEH0je0NPMrtCfeLHFlC$HE_4b541fe2ab31c9eb8090013d3667445542010702003765000000448921b87c59ec8090019b563eda7b563ed400&sigCatVer=1"
                headers = {
                    "Host": "encourage.kuaishou.com",
                    "Connection": "keep-alive",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
                    "content-type": "application/json",
                    "Accept": "*/*",
                    "Origin": "https://encourage.kuaishou.com",
                    "X-Requested-With": "com.kuaishou.nebula",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://encourage.kuaishou.com/activity/dish?layoutType=4&encourageEventTracking=W3siZW5jb3VyYWdlX3Rhc2tfaWQiOjIwMDA4LCJlbmNvdXJhZ2VfcmVzb3VyY2VfaWQiOiJlYXJuUGFnZV90YXNrTGlzdF8xNyIsImV2ZW50VHJhY2tpbmdMb2dJbmZvIjpbeyJldmVudFRyYWNraW5nVGFza0lkIjoyMDAwOCwicmVzb3VyY2VJZCI6ImVhcm5QYWdlX3Rhc2tMaXN0XzE3IiwiZXh0UGFyYW1zIjp7fX1dfV0",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cookie": token
                }
                resp = requests.get(url, headers=headers)
                resp_json = resp.json()
                if resp_json['result'] == 1:
                    desc = resp_json['data']['popup']['desc']
                    title = resp_json['data']['popup']['title']
                    print(f"{title} {desc}")  
                else:
                    print(resp_json['error_msg'])  
            else:
                print(resp_json['data']['button']['text'])
        else:
            print(resp_json['error_msg'])
    except:
        print(f"获取异常:{traceback.format_exc()}")



def get_qiandao(token):
    print('❤开始执行签到')
    try:
        url = "https://nebula.kuaishou.com/rest/wd/encourage/unionTask/signIn/report?__NS_sig3=8b9bdcec5f000f5847d7bcd4d3d29c27aae659dd1c4a59c9883cc4c4c2c2c1c0ffdf&sigCatVer=1"

        # 定义请求头
        headers = {
            "Host": "nebula.kuaishou.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23113RKC6C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.226 KsWebView/1.8.90.675 (rel) Mobile Safari/537.36 Yoda/3.1.7-alpha33-intercept1 ksNebula/12.5.20.8014 OS_PRO_BIT/64 MAX_PHY_MEM/15199 AZPREFIX/az4 ICFO/0 StatusHT/34 TitleHT/43 NetType/WIFI ISLP/0 ISDM/0 ISLB/0 locale/zh-cn DPS/19.822 DPP/99 CT/0 ISLM/0",
            "content-type": "application/json",
            "Accept": "*/*",
            "X-Requested-With": "com.kuaishou.nebula",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://nebula.kuaishou.com/nebula/task/earning?source=timer&layoutType=4&hyId=nebula_earning",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": token
        }

        # 发送 POST 请求
        resp = requests.get(url, headers=headers)
        resp_json = resp.json()
        if resp_json['result'] == 1:
            title = resp_json['data']['reportRewardResult']['awardToast']['title']
            print(f"{title}")
            bsd1 = resp_json['data']['reportRewardResult']['awardToast']['basicSignInAwardResultShow']['bottomText']
            bsd2 = resp_json['data']['reportRewardResult']['awardToast']['basicSignInAwardResultShow']['bottomText']
            print(f"正常：{bsd1}  额外：{bsd2}")
        else:
            print(resp_json['error_msg'])
    except:
        print(f"获取异常:{traceback.format_exc()}")


def main():
    get_baoxiang(refresh_token)
    get_fanbu(refresh_token)
    get_walk(a_token)
    get_qiandao(a_token)
    get_money(refresh_token)
if __name__ == '__main__':
    main()