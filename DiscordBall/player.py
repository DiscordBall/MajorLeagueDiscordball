from DiscordBall.build_types import BattingRanges, PitchingRanges
from Utils import db

TABLE = 'Players'

# Range categories
BASE = 'base'
BUFF = 'buff'
DEBUFF = 'debuff'


class Player:
    player_id = None
    first_name = None
    last_name = None
    team = None
    discord_id = None
    position = None
    batting_base_type = None
    batting_buff_1 = None
    batting_buff_2 = None
    batting_debuff = None
    batting_hand_bonus = None
    pitching_base_type = None
    pitching_buff_1 = None
    pitching_buff_2 = None
    pitching_debuff = None
    pitching_hand_bonus = None
    hand = None
    status = None
    always_keep = False
    hype_gif = None
    holidays = None
    rookie_season = None
    vouch_1 = None
    vouch_2 = None

    def __init__(self, **kwargs):
        """
        # TODO add docstrings back when we are done deciding things
        """
        p = None
        if 'player_id' in kwargs and not p:
            conditions = {
                'player_id': kwargs['player_id']
            }
            p = self.get_player_from_db(conditions)
        if 'discord_id' in kwargs and not p:
            conditions = {
                'discord_id': kwargs['discord_id']
            }
            p = self.get_player_from_db(conditions)
        if 'first_name' in kwargs and 'last_name' in kwargs and not p:
            conditions = {
                'first_name': kwargs['first_name'],
                'last_name': kwargs['last_name']
            }
            p = self.get_player_from_db(conditions)

        if not p and 'player_id' in kwargs and 'discord_id' in kwargs:
            db.insert_data(TABLE, kwargs)
            p = self.get_player_from_db(kwargs)

        if p:
            self.player_id = p[0]
            self.discord_id = p[1]
            self.first_name = p[2]
            self.last_name = p[3]
            self.hand = p[4]
            self.position = p[5]
            self.batting_base_type = p[6]
            self.batting_buff_1 = p[7]
            self.batting_buff_2 = p[8]
            self.batting_debuff = p[9]
            self.batting_hand_bonus = p[10]
            self.pitching_base_type = p[11]
            self.pitching_buff_1 = p[12]
            self.pitching_buff_2 = p[13]
            self.pitching_debuff = p[14]
            self.pitching_hand_bonus = p[15]
            self.team = p[16]
            self.status = p[17]
            self.vouch_1 = p[18]
            self.vouch_2 = p[19]
            self.hype_gif = p[20]
            self.always_keep = p[21]

            if self.batting_base_type:
                self.batting_base_type = BattingRanges(BASE, self.batting_base_type)
            if self.batting_buff_1:
                self.batting_buff_1 = BattingRanges(BUFF, self.batting_buff_1)
            if self.batting_buff_2:
                self.batting_buff_2 = BattingRanges(BUFF, self.batting_buff_2)
            if self.batting_debuff:
                self.batting_debuff = BattingRanges(DEBUFF, self.batting_debuff)
            if self.batting_hand_bonus:
                self.batting_hand_bonus = BattingRanges(BUFF, self.batting_hand_bonus)
            if self.pitching_base_type:
                self.pitching_base_type = PitchingRanges(BASE, self.pitching_base_type)
            if self.pitching_buff_1:
                self.pitching_buff_1 = PitchingRanges(BUFF, self.pitching_buff_1)
            if self.pitching_buff_2:
                self.pitching_buff_2 = PitchingRanges(BUFF, self.pitching_buff_2)
            if self.pitching_debuff:
                self.pitching_debuff = PitchingRanges(DEBUFF, self.pitching_debuff)
            if self.pitching_hand_bonus:
                self.pitching_hand_bonus = PitchingRanges(BUFF, self.pitching_hand_bonus)
        else:
            self.player_id = None

    def update_player(self, **kwargs):
        """
        # TODO add docstrings back when we are done deciding things
        """
        conditions = {
            'player_id': self.player_id
        }
        if 'player_id' in kwargs:
            self.player_id = kwargs['player_id']
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        if 'team' in kwargs:
            self.team = kwargs['team']
        if 'discord_id' in kwargs:
            self.discord_id = kwargs['discord_id']
        if 'position' in kwargs:
            self.position = kwargs['position']
        if 'batting_base_type' in kwargs:
            self.batting_base_type = kwargs['batting_base_type']
        if 'batting_buff_1' in kwargs:
            self.batting_buff_1 = kwargs['batting_buff_1']
        if 'batting_buff_2' in kwargs:
            self.batting_buff_2 = kwargs['batting_buff_2']
        if 'batting_debuff' in kwargs:
            self.batting_debuff = kwargs['batting_debuff']
        if 'batting_hand_bonus' in kwargs:
            self.batting_hand_bonus = kwargs['batting_hand_bonus']
        if 'pitching_base_type' in kwargs:
            self.pitching_base_type = kwargs['pitching_base_type']
        if 'pitching_buff_1' in kwargs:
            self.pitching_buff_1 = kwargs['pitching_buff_1']
        if 'pitching_buff_2' in kwargs:
            self.pitching_buff_2 = kwargs['pitching_buff_2']
        if 'pitching_debuff' in kwargs:
            self.pitching_debuff = kwargs['pitching_debuff']
        if 'pitching_hand_bonus' in kwargs:
            self.pitching_hand_bonus = kwargs['pitching_hand_bonus']
        if 'hand' in kwargs:
            self.hand = kwargs['hand']
        if 'status' in kwargs:
            self.status = kwargs['status']
        if 'always_keep' in kwargs:
            self.always_keep = kwargs['always_keep']
        if 'hype_gif' in kwargs:
            self.hype_gif = kwargs['hype_gif']
        if 'holidays' in kwargs:
            self.holidays = kwargs['holidays']
        if 'rookie_season' in kwargs:
            self.rookie_season = kwargs['rookie_season']
        if 'vouch_1' in kwargs:
            self.vouch_1 = kwargs['vouch_1']
        if 'vouch_2' in kwargs:
            self.vouch_2 = kwargs['vouch_2']

        db.update_table(TABLE, kwargs, conditions)

    @classmethod
    def get_player_from_db(cls, conditions):
        """
        Looks up an existing player in the database from the given criteria
        :param conditions: a python dict of table columns and values to look up a player
        :return: If the player exists, returns a tuple containing all data in a given row of the player table. If no player exists, returns None.
        """
        p = db.select_data(TABLE, '*', conditions)
        if p:
            if len(p) == 1:
                return p[0]
        return None
