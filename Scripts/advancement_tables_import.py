from Utils import sheets, db
import time

TABLE = 'AdvancementTables'
sheet_id = "1--O1xRtCryd68NXY-HYPYl8DgMdfMplW2FtoVaNAa7s"
obc_after_data = "OBC After"
outs_recorded_data = "Outs Recorded"
runs_scored_data = "Runs Scored"
batter_end_data = "Batter End Location"
r1b_end_data = "Runner 1B End Location"
r2b_end_data = "Runner 2B End Location"
r3b_end_data = "Runner 3B End Location"

obc_after_data_2_out = sheets.read_sheet(sheet_id, f'{obc_after_data} 2 Outs')
obc_after_data = sheets.read_sheet(sheet_id, obc_after_data)
outs_recorded_data_2_out = sheets.read_sheet(sheet_id, outs_recorded_data)
outs_recorded_data = outs_recorded_data_2_out
runs_scored_data_2_out = sheets.read_sheet(sheet_id, f'{runs_scored_data} 2 Outs')
runs_scored_data = sheets.read_sheet(sheet_id, runs_scored_data)
batter_end_data_2_out = sheets.read_sheet(sheet_id, batter_end_data)
batter_end_data = batter_end_data_2_out
r1b_end_data_2_out = sheets.read_sheet(sheet_id, f'{r1b_end_data} 2 Outs')
r1b_end_data = sheets.read_sheet(sheet_id, r1b_end_data)
r2b_end_data_2_out = sheets.read_sheet(sheet_id, f'{r2b_end_data} 2 Outs')
r2b_end_data = sheets.read_sheet(sheet_id, r2b_end_data)
r3b_end_data_2_out = sheets.read_sheet(sheet_id, r3b_end_data)
r3b_end_data = r3b_end_data_2_out


def process_row(obc_before, outs_before, result, obc_after, runs_scored, outs_recorded, batter_end, r1b_end, r2b_end, r3b_end):
    conditions = {
        'obc_before': obc_before,
        'outs_before': outs_before,
        'result': result
    }

    row_exists = db.select_data(TABLE, '*', conditions)
    if not row_exists and outs_before == 2:
        conditions = {
            'obc_before': obc_before,
            'outs_before': None,
            'result': result
        }
        row_exists = db.select_data(TABLE, '*', conditions)
        if row_exists:
            db_id, db_obc_before, db_outs_before, db_result, db_obc_after, db_runs_scored, db_outs_recorded, db_br_home, db_br_1b, db_br_2b, db_br_3b, defense = row_exists[0]
            if (obc_after, runs_scored, outs_recorded, batter_end, r1b_end, r2b_end, r3b_end) == (db_obc_after, db_runs_scored, db_outs_recorded, db_br_home, db_br_1b, db_br_2b, db_br_3b):
                return
            else:
                row_exists = False
    if not row_exists:
        advancement_row = {
            'obc_before': obc_before,
            'outs_before': outs_before,
            'result': result,
            'obc_after': obc_after,
            'runs_scored': runs_scored,
            'outs_recorded': outs_recorded,
            'br_home': batter_end,
            'br_1b': r1b_end,
            'br_2b': r2b_end,
            'br_3b': r3b_end,
        }
        db.insert_data(TABLE, advancement_row)
    else:
        advancement_row = {
            'obc_after': obc_after,
            'runs_scored': runs_scored,
            'outs_recorded': outs_recorded,
            'br_home': batter_end,
            'br_1b': r1b_end,
            'br_2b': r2b_end,
            'br_3b': r3b_end,
        }
        db.update_table(TABLE, advancement_row, conditions)
    return


for i in range(len(obc_after_data)):
    if 0 < i < 9:
        obc_before = obc_after_data[i][0]
        for j in range(len(obc_after_data)):
            if 0 < j < 11:
                result = obc_after_data[0][j]
                obc_after = obc_after_data[i][j]
                outs_recorded = outs_recorded_data[i][j]
                runs_scored = runs_scored_data[i][j]
                batter_end = batter_end_data[i][j]
                r1b_end = r1b_end_data[i][j]
                r2b_end = r2b_end_data[i][j]
                r3b_end = r3b_end_data[i][j]

                result_2_out = obc_after_data_2_out[0][j]
                obc_after_2_out = obc_after_data_2_out[i][j]
                outs_recorded_2_out = outs_recorded_data_2_out[i][j]
                runs_scored_2_out = runs_scored_data_2_out[i][j]
                batter_end_2_out = batter_end_data_2_out[i][j]
                r1b_end_2_out = r1b_end_data_2_out[i][j]
                r2b_end_2_out = r2b_end_data_2_out[i][j]
                r3b_end_2_out = r3b_end_data_2_out[i][j]

                if obc_before == '':
                    obc_before = None
                else:
                    obc_before = int(obc_before)
                if obc_after == '':
                    obc_after = None
                else:
                    obc_after = int(obc_after)
                if outs_recorded == '':
                    outs_recorded = None
                else:
                    outs_recorded = int(outs_recorded)
                if runs_scored == '':
                    runs_scored = None
                else:
                    runs_scored = int(runs_scored)
                if batter_end == '':
                    batter_end = None
                if r1b_end == '':
                    r1b_end = None
                if r2b_end == '':
                    r2b_end = None
                if r3b_end == '':
                    r3b_end = None

                if obc_after_2_out == '':
                    obc_after_2_out = None
                else:
                    obc_after_2_out = int(obc_after_2_out)
                if outs_recorded_2_out == '':
                    outs_recorded_2_out = None
                else:
                    outs_recorded_2_out = int(outs_recorded_2_out)
                if runs_scored_2_out == '':
                    runs_scored_2_out = None
                else:
                    runs_scored_2_out = int(runs_scored_2_out)
                if batter_end_2_out == '':
                    batter_end_2_out = None
                if r1b_end_2_out == '':
                    r1b_end_2_out = None
                if r2b_end_2_out == '':
                    r2b_end_2_out = None
                if r3b_end_2_out == '':
                    r3b_end_2_out = None

                process_row(obc_before, None, result, obc_after, runs_scored, outs_recorded, batter_end, r1b_end, r2b_end, r3b_end)
                process_row(obc_before, 2, result_2_out, obc_after_2_out, runs_scored_2_out, outs_recorded_2_out, batter_end_2_out, r1b_end_2_out, r2b_end_2_out, r3b_end_2_out)
