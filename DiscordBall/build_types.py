import Utils.db_interface as db


class BattingType:
    TABLE = 'BattingTypes'
    category = None
    batting_type = None
    name = None
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
    range_sb2b = None
    range_sb3b = None
    range_sb_home = None

    def __init__(self, category: str, batting_type: str):
        conditions = {
            'category': category,
            'type': batting_type}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.category = data[1]
            self.batting_type = data[2]
            self.name = data[3]
            self.range_hr = data[4]
            self.range_3b = data[5]
            self.range_2b = data[6]
            self.range_1b = data[7]
            self.range_bb = data[8]
            self.range_pro = data[9]
            self.range_fo = data[10]
            self.range_k = data[11]
            self.range_rgo = data[12]
            self.range_lgo = data[13]
            self.range_sb2b = data[14]
            self.range_sb3b = data[15]
            self.range_sb_home = data[16]


class PitchingType:
    TABLE = 'PitchingTypes'
    category = None
    batting_type = None
    name = None
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

    def __init__(self, category: str, pitching_type: str):
        conditions = {
            'category': category,
            'type': pitching_type}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.category = data[1]
            self.batting_type = data[2]
            self.name = data[3]
            self.range_hr = data[4]
            self.range_3b = data[5]
            self.range_2b = data[6]
            self.range_1b = data[7]
            self.range_bb = data[8]
            self.range_pro = data[9]
            self.range_fo = data[10]
            self.range_k = data[11]
            self.range_rgo = data[12]
            self.range_lgo = data[13]


class HandBonus:
    TABLE = 'HandBonus'
    categor = None
    batting_type = None
    name = None
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

    def __init__(self, category: str, hand_bonus: str):
        conditions = {
            'category': category,
            'type': hand_bonus
        }
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.category = data[1]
            self.batting_type = data[2]
            self.name = data[3]
            self.range_hr = data[4]
            self.range_3b = data[5]
            self.range_2b = data[6]
            self.range_1b = data[7]
            self.range_bb = data[8]
            self.range_pro = data[9]
            self.range_fo = data[10]
            self.range_k = data[11]
            self.range_rgo = data[12]
            self.range_lgo = data[13]
