import pyautogui as py
import pandas as pd
import time
import numpy as np
import keyboard 
import sys, os



# -============IMAGE PATHS ==========-

#  Fixed Charge Code
gsm_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\GSM Fixed Charge pngs\GSM.png'

#  Template VAS
details_but_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\VAS pngs\Details Butt.png'
buttons_but_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\VAS pngs\Buttons Butt.png'
select_vas_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\VAS pngs\Select VAS.png'

#  Template Charges (Fix and USG)
f3_new_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\Charge pngs\F3 New.png'
bundle_code_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\Charge pngs\Bundle Type.png'
bundle_date_from_png = r'B:\Tariffing\MG Auto Tariff\ScreenShots\Charge pngs\Bundle Date From.png'


# -========== VARIABLES ===========-


vas_prim = 'O2PV001'
vprim_on = 'O2PV001_ON'

vas_rrp_row1 = 'VASO2ABSRRPROWP1'
vas_rrp_row2 = 'VASO2ABSRRPROWP2'
vas_rrp_row3 = 'VASO2ABSRRPROWP3'
vas_rrp_row1a = 'ABSRRPROWP1_ON'
vas_rrp_row2a = 'ABSRRPROWP2_ON'
vas_rrp_row3a = 'VASO2ROWPS3_ON'

vas_ws_row1 = 'VASO2ABSROWP1'
vas_ws_row2 = 'VASO2ABSROWP2'
vas_ws_row3 = 'VASO2ABSROWP3'
vas_ws_row1a = 'VASO2ROWPS1_ON'
vas_ws_row2a = 'VASO2ROWPS2_ON'
vas_ws_row3a = 'VASO2WSROWPS3_ON'

vas_5g = '5G'
vas_5ga = '5G_ON'

vas_mms = 'mm'
vas_mmsa = 'MMS_ON'

vas_gp58 = 'gp_58'
vas_gp58a = 'gp_58_ON'

vas_gp2041 = 'gp_2041'
vas_gp2041a = 'gp_2041_ON'

vas_gp986 = 'gp_986'
vas_gp986a = 'gp_986_ON'

vas_gp985 = 'gp_985'
vas_gp985a = 'gp_985_ON'

vas_gs = 'gs'
vas_gsa = 'gs_ON'


vas = [vas_prim, vas_rrp_row1, vas_rrp_row2, vas_rrp_row3, vas_ws_row1, vas_ws_row2, vas_ws_row3,
           vas_5g, vas_mms, vas_gp58, vas_gp2041, vas_gp986, vas_gp985, vas_gs]

vason = [vprim_on, vas_rrp_row1a, vas_rrp_row2a, vas_rrp_row3a, vas_ws_row1a, vas_ws_row2a, vas_ws_row3a,
             vas_5ga, vas_mmsa, vas_gp58a, vas_gp2041a, vas_gp986a, vas_gp985a, vas_gsa]


# -============ KEY FUNCTIONS -===============



def tab():
    py.keyDown('tab')
    time.sleep(0.02)
    py.keyUp('tab')
#     time.sleep(0.02)
    
def backspace():
    py.press('backspace')
    time.sleep(0.05)
    
def space():
    py.keyDown('space')
    time.sleep(0.02)
    py.keyUp('space')
    time.sleep(0.02)

def down():
    py.press('down')

def A():
    py.keyDown('A')
    time.sleep(0.02)
    py.keyUp('A')
    py.press('tab')
    py.keyDown('M')
    time.sleep(0.02)
    py.keyUp('M')
    py.press('tab')
    
def P():
    py.keyDown('P')
    time.sleep(0.02)
    py.keyUp('P')
    py.press('tab')
    
def f34a4():
    f3()
    py.press('f4')
    time.sleep(0.01)
    py.hotkey('alt', 'f4')
               
def f3():
    py.press('f3')
    time.sleep(0.1)

def cf3():
    py.hotkey('ctrl', 'f3')
    time.sleep(0.5)
    
def f4():
    py.press('f4')
    time.sleep(0.01)
    
def af4():
    py.hotkey('alt', 'f4')
    time.sleep(0.5)
               
def ctab():
    py.hotkey('ctrl', 'tab')
    time.sleep(0.2)

# -======= TEMPLATE FUNCS ========-
def onoo():
    py.keyDown('O')
    time.sleep(0.02)
    py.keyUp('O')
    tab()
    py.keyDown('N')
    time.sleep(0.02)
    py.keyUp('N')
    tab()
               
def O():
    py.keyDown('O')
    time.sleep(0.02)
    py.keyUp('O')
    tab()

    
# -======= VAS FUNCTIONS ========- 
               
def dett_butt():
    time.sleep(0.1)
    py.click(details_but_png)
    time.sleep(0.1)
    py.click(buttons_but_png)
    time.sleep(0.1)

def add_o2Vases():
    py.click(select_vas_png)
    time.sleep(0.03)
    for i, j in zip(vas, vason):
        py.write(i, interval=0.01)
        tab()
        py.write(j, interval=0.01)
        tab()
        cf3()
        py.click(select_vas_png)
        time.sleep(0.03)


def add_CHVases():
    py.click(select_vas_png)
    time.sleep(0.03)
    py.write('DYPV001', interval=0.01)
    tab()
    py.write('DYPV001_ON', interval=0.01)
    tab()
    cf3()



