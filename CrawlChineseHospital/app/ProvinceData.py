'''
This module include some data about province mapping dict
'''
class ProvinceInformation:
    province_dict = {
        'hebei': '河北省',
        'shandong': '山东省',
        'liaoning': '辽宁省',
        'heilongjiang': '黑龙江省',
        'jilin': '吉林省',
        'gansu': '甘肃省',
        'qinghai': '青海省',
        'henan': '河南省',
        'jiangsu': '江苏省',
        'hubei': '湖北省',
        'hunan': '湖南省',
        'jiangxi': '江西省',
        'zhejiang': '浙江省',
        'guangdong': '广东省',
        'yunnan': '云南省',
        'fujian': '福建省',
        'taiwan': '台湾省',
        'hainan': '海南省',
        'shanxi': '山西省',
        'sichuan': '四川省',
        'shanxi': '陕西省',
        'guizhou': '贵州省',
        'anhui': '安徽省',
        'chongqin': '重庆市',
        'beijing': '北京市',
        'shanghai': '上海市',
        'tianjin': '天津市',
        'guangxi': '广西',
        'neimenggu': '内蒙古',
        'xizang': '西藏',
        'xinjiang': '新疆',
        'ninxiang': '宁夏',
        'aomen': '澳门',
        'xianggan': '香港特别行政区'
    }

    @classmethod
    def get(self, province_name, default_value = None):
        province_name = province_name.lower()
        return self.province_dict.get(province_name, default_value)
