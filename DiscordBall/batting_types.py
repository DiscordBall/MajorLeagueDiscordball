import Utils.db_interface as db


class BattingType:
    TABLE = 'BattingTypes'
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
    range_sb2b = None
    range_sb3b = None
    range_sb_home = None

    def __init__(self, batting_type: str):
        conditions = {'type': batting_type}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.batting_type = data[1]
            self.name = data[2]
            self.range_hr = data[3]
            self.range_3b = data[4]
            self.range_2b = data[5]
            self.range_1b = data[6]
            self.range_bb = data[7]
            self.range_fo = data[8]
            self.range_k = data[9]
            self.range_po = data[10]
            self.range_rgo = data[11]
            self.range_lgo = data[12]
            self.range_sb2b = data[13]
            self.range_sb3b = data[14]
            self.range_sb_home = data[15]