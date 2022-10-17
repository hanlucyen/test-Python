from statemachine1 import StateMachine
tinhtu_tichcuc = ["vi_dai", "sieu", "vui", "de", "giai_tri"] 
tinhtu_tieucuc = ["chan", "kho", "xau", "kem"]
def trangthai_baudau(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu == "Python":
        trangthaimoi = "Python_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi,txt)
def trangthai_python(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")
    if tu == "is":
        trangthaimoi = "is_state" 
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi, txt)

def trangthai_is_chuyentrangthai(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")

    if tu == "not":
        trangthaimoi = "not_state"
    elif tu in tinhtu_tichcuc:
        trangthaimoi = "pos_state"
    elif tu in tinhtu_tieucuc:
        trangthaimoi = "neg_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi,txt)

def trangthai_isnot_chuyentrangthai(txt):
    splitted_txt = txt.split(None, 1)
    tu, txt = splitted_txt if len(splitted_txt) > 1 else (txt, "")

    if tu in tinhtu_tichcuc:
        trangthaimoi = "pos_state"
    elif tu in tinhtu_tieucuc:
        trangthaimoi = "neg_state"
    else:
        trangthaimoi = "error_state"
    return (trangthaimoi, txt)
def neg_state(txt):
    print("chao!")
    return("neg_state","")
if __name__=="__main__":
    m=StateMachine()
    m.them_Trangthai("Start",trangthai_baudau)
    m.them_Trangthai("Python_state", trangthai_python)
    m.them_Trangthai("is_state", trangthai_is_chuyentrangthai)
    m.them_Trangthai("not_state", trangthai_isnot_chuyentrangthai)
    m.them_Trangthai("neg_state", None, trangthai_ketthuc = 1)
    m.them_Trangthai("pos_state", None, trangthai_ketthuc = 1)
    m.them_Trangthai("error_state", None, trangthai_ketthuc = 1)
    m.thietlap_TrangthaiBatdau("Start")
    m.thucthi("Python is vi_dai")
    m.thucthi("Python is kho")
    m.thucthi("Python is xau")
    m.thucthi("Python is xao")
