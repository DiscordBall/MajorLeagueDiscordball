import Utils.db_interface as db


class PitchingType:
    TABLE = 'PitchingTypes'
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

    def __init__(self, pitching_type: str):
        conditions = {'type': pitching_type}
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


class PitchingBonus:
    TABLE = 'PitchingBonus'
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

    def __init__(self, pitching_bonus: str):
        conditions = {'type': pitching_bonus}
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
