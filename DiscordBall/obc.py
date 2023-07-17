import Utils.db_interface as db


class OnBaseCount:
    TABLE = "OnBaseCount"
    id = None
    name = None
    reddit = None
    emoji_name = None
    emoji_id = None

    def __init__(self, obc: int):
        conditions = {'type': obc}
        data = db.select_data(self.TABLE, '*', conditions)
        if data:
            data = data[0]
            self.id = data[0]
            self.name = data[1]
            self.reddit = data[2]
            self.emoji_name = data[3]
            self.emoji_id = data[4]
