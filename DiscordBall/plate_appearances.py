import DiscordBall
from Utils import db


class GameState:
    inning = None
    outs = None
    obc = None
    runner_1b = None
    runner_2b = None
    runner_3b = None
    pitcher_runner_1b = None
    pitcher_runner_2b = None
    pitcher_runner_3b = None

    def __init__(self):
        # TODO
        return None


class Matchup:
    batting_type: DiscordBall.BattingRanges = None
    pitching_type: DiscordBall.PitchingRanges = None
    pitching_bonus: DiscordBall.PitchingBonus = None
    hand_bonus_applies: bool = False
    park: DiscordBall.Park = None
    infield_in = False
    ranges = None  # list of tuples for min and max?
    ranges_no_modifier = None
    ranges_neutral_park = None
    ranges_all_neutral = None

    def __init__(self):
        # TODO
        return None


class Timer:
    start_time = None
    pitch_submitted = None
    swing_submitted = None
    global_timer_pause_start = None
    global_timer_pause_stop = None
    ab_timer_pause_start = None
    ab_timer_pause_stop = None
    elapsed_timer_pause = None

    def __init__(self):
        # TODO
        return None


class PlateAppearance:
    id = None
    league = None
    season = None
    session = None
    play_number = None
    pitcher: DiscordBall.player = None
    batter: DiscordBall.player = None
    state_before: GameState = None
    state_after: GameState = None
    timers: Timer = None
    matchup: Matchup = None
    pitch_src = None
    swing_src = None
    pitch = None
    swing = None
    diff = None
    result = None
    ip_outs = None
    rbi = None
    runs_scored = None
    play_src = None  # message ID for play in main
    play_archive = None  # reddit commend id for play in game thread

    def __init__(self):
        # TODO
        return None
