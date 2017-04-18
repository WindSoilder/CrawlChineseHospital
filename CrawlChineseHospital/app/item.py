class HospitalInforItem:
    def __init__(self, provinceID, hType, hGrade, hName):
        self.provinceID = provinceID
        self.hType = hType
        self.hGrade = hGrade
        self.hName = hName

    def __str__(self):
        format_str = "医院类型：{hType}\t医院等级：{hGrade}\t医院名称：{hName}"
        return format_str.format(hType=self.hType,
                                 hGrade=self.hGrade,
                                 hName=self.hName)
