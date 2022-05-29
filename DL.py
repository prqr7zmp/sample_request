# -*- coding: utf-8 -*-
import requests
import os
from datetime import datetime

# ★ポイント1
# ex) set DOWNLOAD_SAVE_DIR=C:/Temp/flaskDownloadSaveDir
DOWNLOAD_SAVE_DIR = "C:/takahashi/git/sample_request"

# main
if __name__ == "__main__":

    # ★ポイント2
    url = "http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/original/2020/01/01/Z__C_RJTD_20200101030000_MSM_GPV_Rjp_Lsurf_FH34-39_grib2.bin"
    response = requests.get(url)

    # ★ポイント3
    #contentType = response.headers['Content-Type']
    #contentDisposition = response.headers['Content-Disposition']
    #ATTRIBUTE = 'filename='
    #fileName = contentDisposition[contentDisposition.find(ATTRIBUTE) + len(ATTRIBUTE):]

    # ★ポイント4
    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_")
    saveFilePath = os.path.join(DOWNLOAD_SAVE_DIR, saveFileName)
    with open(saveFilePath, 'wb') as saveFile:
        saveFile.write(response.content)