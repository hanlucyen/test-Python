class StateMachine:
        tap_xuly={}
        trangthaiBatdau= None
        trangthaiKetthuc=[]
        def __init__(self):
                self.tap_xuly={}
                self.trangthaiBatdau= None
                self.trangthaiKetthuc=[]
        def them_Trangthai(self,trangthai,xuly,trangthai_ketthuc=0):   
                trangthai=trangthai.upper()
                self.tap_xuly[trangthai] = xuly
                if trangthai_ketthuc:
                        self.trangthaiKetthuc.append(trangthai)
        def thietlap_TrangthaiBatdau(self,trangthai):
                self.trangthaiBatdau=trangthai.upper()
        def thucthi(self,dauvao):
                try:
                        xuly=self.tap_xuly[self.trangthaiBatdau]
                except:
                        raise InitializationError("phai gfi .thietlap_TrangthaiBatdau() truoc khi goi .thucthi() ")
                if not self.trangthaiKetthuc:
                        raise InitializationError("it nhat 1 trang thai phai la trang thai ket thuc")
                while True:
                        (TrangThaiMoi,dauvao)=xuly(dauvao)
                        if TrangThaiMoi.upper() in self.trangthaiKetThuc:
                                print("den dich!",TrangThaiMoi)
                                break
                        else:
                                xuly=self.tap_xuly[TrangThaiMoi.upper()]
