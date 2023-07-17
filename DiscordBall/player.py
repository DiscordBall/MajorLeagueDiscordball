import Utils.db_interface as db

TABLE = 'Players'


class Player:
    player_id = None
    first_name = None
    last_name = None
    team = None
    discord_id = None
    position = None
    batting_type = None
    pitching_type = None
    pitching_bonus = None
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
        Creates an instance of the player class. To look up an existing player, you should include their player ID, discord token, or first and last name. If a player does not exist in the database and a player ID and discord token is provided, it will create a new row in the Players table with all data that has been passed in.
        :param kwargs:\n
        player_id: a unique numeric identifier for each player
        first_name: player's first name
        last_name: player's last name
        team: team the player is currently on
        discord_id: Discord snowflake that links to the player's account
        position: player's primary defensive position
        batting_type: player's batting type
        pitching_type: player's pitching type
        pitching_bonus: player's pitching bonus
        hand: left or right
        status: 1=active, 2=retired, etc
        always_keep: whether or not the bot should always assume the player is going to keep their pitch on substitutions, defaults to false
        hype_gif: a gif that will be displayed in game discussion when the player triggers a hype ping via run score, triple play, etc
        holidays: list of holidays the player has opted to have paused timers
        rookie_season: the player's innaugural season in the league
        vouch_1: player ID for a player that vouched for them to join the league
        vouch_2: player ID for a player that vouched for them to join the league
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
            self.first_name = p[1]
            self.last_name = p[2]
            self.discord_id = p[3]
            self.hand = p[4]
            self.position = p[5]
            self.batting_type = p[6]
            self.pitching_type = p[7]
            self.pitching_bonus = p[8]
            self.team = p[9]
            self.status = p[10]
            self.vouch_1 = p[11]
            self.vouch_2 = p[12]
            self.hype_gif = p[13]
            self.always_keep = p[14]
        else:
            self.player_id = None

    def update_player(self, **kwargs):
        """
        Note: must include player ID
        :param kwargs:\n
        player_id: a unique numeric identifier for each player
        first_name: player's first name
        last_name: player's last name
        team: team the player is currently on
        discord_id: Discord snowflake that links to the player's account
        position: player's primary defensive position
        batting_type: player's batting type
        pitching_type: player's pitching type
        pitching_bonus: player's pitching bonus
        hand: left or right
        status: 1=active, 2=retired, etc
        always_keep: whether or not the bot should always assume the player is going to keep their pitch on substitutions, defaults to false
        hype_gif: a gif that will be displayed in game discussion when the player triggers a hype ping via run score, triple play, etc
        holidays: list of holidays the player has opted to have paused timers
        rookie_season: the player's innaugural season in the league
        vouch_1: player ID for a player that vouched for them to join the league
        vouch_2: player ID for a player that vouched for them to join the league
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
        if 'batting_type' in kwargs:
            self.batting_type = kwargs['batting_type']
        if 'pitching_type' in kwargs:
            self.pitching_type = kwargs['pitching_type']
        if 'pitching_bonus' in kwargs:
            self.pitching_bonus = kwargs['pitching_bonus']
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
