from Utils import db


class BattingRanges:
    TABLE = 'BattingRanges'
    category = None
    name = None
    abb = None
    range_hr = None
    range_3b = None
    range_2b = None
    range_1b = None
    range_bb = None
    range_pro = None
    range_fo = None
    range_k = None
    range_rgo = None
    range_lgo = None
    bunt_tier = None
    steal_tier = None

    def __init__(self, category: str, abb: str):
        conditions = {
            'category': category,
            'abb': abb}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.category = data[0]
            self.name = data[1]
            self.abb = data[2]
            self.range_hr = data[3]
            self.range_3b = data[4]
            self.range_2b = data[5]
            self.range_1b = data[6]
            self.range_bb = data[7]
            self.range_pro = data[8]
            self.range_fo = data[9]
            self.range_k = data[10]
            self.range_rgo = data[11]
            self.range_lgo = data[12]
            self.bunt_tier = data[13]
            self.steal_tier = data[14]


class PitchingRanges:
    TABLE = 'PitchingRanges'
    category = None
    name = None
    abb = None
    range_hr = None
    range_3b = None
    range_2b = None
    range_1b = None
    range_bb = None
    range_fo = None
    range_k = None
    range_po = None
    range_rgo = None
    range_lgo = None
    bunt_tier = None
    steal_tier = None

    def __init__(self, category: str, abb: str):
        conditions = {
            'category': category,
            'abb': abb}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.category = data[0]
            self.name = data[1]
            self.abb = data[2]
            self.range_hr = data[3]
            self.range_3b = data[4]
            self.range_2b = data[5]
            self.range_1b = data[6]
            self.range_bb = data[7]
            self.range_pro = data[8]
            self.range_fo = data[9]
            self.range_k = data[10]
            self.range_rgo = data[11]
            self.range_lgo = data[12]
            self.bunt_tier = data[13]
            self.steal_tier = data[14]
