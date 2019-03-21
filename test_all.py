import os
import pytest
import ex2, ex3

a = '{"e":[[{"e":86,"c":23,"a":{"a":[120,169,"green","red","orange"],"b":"red"},"g":"yellow","b":["yellow"],"d":"red","f":-19}'

p = [
'sayndz zfxlkl attjtww cti sokkmty brx fhh suelqbp',
'xmuf znkhaes pggrlp zia znkhaes znkhaes',
'nti rxr bogebb zdwrin',
'sryookh unrudn zrkz jxhrdo gctlyz',
'bssqn wbmdc rigc zketu ketichh enkixg bmdwc stnsdf jnz mqovwg ixgken',
'flawt cpott xth ucwgg xce jcubx wvl qsysa nlg',
'qovcqn zxcz vojsno nqoqvc hnf gqewlkd uevax vuna fxjkbll vfge',
'qrzf phwuf ligf xgen vkig elptd njdm gvqiu epfzsvk urbltg dqg',
'sfpku viwihi fje umdkwvi ejzhzj qrbl sfpku sad nawnow ksnku',
'nzhj mfudick ueaa jnhz kpy pzk',
'euiin xvl elaoelu wbdd xlv jtm nohtq gfdbgdg gdfggdb edtym',
'xfmkn wyww woe hwysuh gjw dtk utryasc dela eluk vmmun',
'nmag qfwe cwslmgd nlhf hpf',
'ifs sszo iod isf jna',
]





def test_is_validate_one_password():
    """Check if this function return true if password is validate and false if password is unvalidate"""
    assert  (ex2.is_val_one_password(p[0]) and
             not ex2.is_val_one_password(p[1]) and
             ex2.is_val_one_password(p[2]) and
             ex2.is_val_one_password(p[3]) and
             ex2.is_val_one_password(p[4]) and
             ex2.is_val_one_password(p[5]) and
             ex2.is_val_one_password(p[6]) and
             ex2.is_val_one_password(p[7]) and
             not ex2.is_val_one_password(p[8]) and
             ex2.is_val_one_password(p[9]) and
             ex2.is_val_one_password(p[10]) and
             ex2.is_val_one_password(p[11]) and
             ex2.is_val_one_password(p[12])
             )

def test_validator():
    """Check if vialidator working correct in our file"""
    assert ex2.validator('skychallenge_skyphrase_input.txt') == 383



def test_sum():
    """Check if sum working correct in our file"""
    assert ex3.sum('skychallenge_accounting_input.txt') == 111754