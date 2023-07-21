from Utils import sheets, db

TABLE = 'BaserunnerAdvancement'
sheet_id = "1--O1xRtCryd68NXY-HYPYl8DgMdfMplW2FtoVaNAa7s"
obc_after_data = "OBC After"
outs_recorded_data = "Outs Recorded"
runs_scored_data = "Runs Scored"
batter_end_data = "Batter End Location"
r1b_end_data = "Runner 1B End Location"
r2b_end_data = "Runner 2B End Location"
r3b_end_data = "Runner 3B End Location"

obc_after_data = sheets.read_sheet(sheet_id, obc_after_data)
outs_recorded_data = sheets.read_sheet(sheet_id, outs_recorded_data)
runs_scored_data = sheets.read_sheet(sheet_id, runs_scored_data)
batter_end_data = sheets.read_sheet(sheet_id, batter_end_data)
r1b_end_data = sheets.read_sheet(sheet_id, r1b_end_data)
r2b_end_data = sheets.read_sheet(sheet_id, r2b_end_data)
r3b_end_data = sheets.read_sheet(sheet_id, r3b_end_data)

for i in range(len(obc_after_data)):
    if i > 0:
        obc_before = obc_after_data[i][0]
        for j in range(len(obc_after_data)):
            if j > 0:
                result = obc_after_data[0][j]
                obc_after = obc_after_data[i][j]
                outs_recorded = outs_recorded_data[i][j]
                runs_scored = runs_scored_data[i][j]
                batter_end = batter_end_data[i][j]
                r1b_end = r1b_end_data[i][j]
                r2b_end = r2b_end_data[i][j]
                r3b_end = r3b_end_data[i][j]
                if obc_after == '':
                    obc_after = None
                if outs_recorded == '':
                    outs_recorded = None
                if runs_scored == '':
                    runs_scored = None
                if batter_end == '':
                    batter_end = None
                if r1b_end == '':
                    r1b_end = None
                if r2b_end == '':
                    r2b_end = None
                if r3b_end == '':
                    r3b_end = None

                conditions = {
                    'obc_before': obc_before,
                    'outs_before': None,
                    'result': result,
                }

                row_exists = db.select_data(TABLE, '*', conditions)
                if not row_exists:
                    advancement_row = {
                        'obc_before': obc_before,
                        'outs_before': None,
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
