from Utils import db


class Park:
    TABLE = "Parks"
    abb = None
    name = None
    range_hr = None
    range_3b = None
    range_2b = None
    range_1b = None
    range_bb = None
    channel_id = None

    def __init__(self, abb: str):
        conditions = {'abb': abb}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.abb = data[1]
            self.name = data[2]
            self.range_hr = data[3]
            self.range_3b = data[4]
            self.range_2b = data[5]
            self.range_1b = data[6]
            self.range_bb = data[7]
            self.channel_id = data[8]

