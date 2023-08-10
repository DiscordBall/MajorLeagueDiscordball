from itertools import combinations, chain
import numpy as np
import time
from Utils import sheets

ranges_sheet_id = "1UrOcPLtSYBUbnrOt20crlr8ceqk4KUC8xavvfvl4lvs"
labels = ['Base Type', 'Buffs', 'Debuffs', 'Hand Bonus', 'HR', '3B', '2B', '1B', 'BB', 'PRO', 'FO', 'K', 'RGO', 'LGO', 'Bunt', 'Steal', 'HR', '3B', '2B', '1B', 'BB', 'PRO', 'FO', 'K', 'RGO', 'LGO', 'Total']
BATTING = True
PITCHING = True


def convert_ranges(ranges):
    result_dict = {}

    for row in ranges[1:]:
        trait = {
            'Name': row[0],
            'Ranges': [int(i) for i in row[2:]]
        }
        result_dict[row[1]] = trait
    return result_dict


def parse_ranges_from_sheet(sheet_id: str, range_type: str):
    output_dict = {}
    page_names = ['Base', 'Buff', 'Debuff', 'Hand Bonus']
    for page in page_names:
        output_dict[page] = convert_ranges(sheets.read_sheet(sheet_id, f'{page} {range_type}'))
    return output_dict


def write_to_sheet(sheet_id, page_name, data):
    while True:
        try:
            sheets.append_sheet(sheet_id, page_name, [str(x) for x in data])
            return
        except:
            print('Ran into error writing to sheet, will wait 5 seconds and try again...')
            time.sleep(5)


def generate_all_ranges(sheet_id: str, ranges_dict: dict, range_type: str):
    output_rows = [labels]  # Column headers

    # Get list of range types
    base_type_list = ranges_dict.get('Base')
    buff_type_list = ranges_dict.get('Buff')
    debuff_type_list = ranges_dict.get('Debuff')
    hand_bonus_type_list = ranges_dict.get('Hand Bonus')

    # Check if any types allow multiple traits and overwrite list
    for row in sheets.read_sheet(ranges_sheet_id, 'Config'):
        if row[0] == range_type:
            if int(row[1]) > 1:  # Base
                base_type_list = list(combinations(ranges_dict.get('Base').keys(), int(row[1])))
            if int(row[2]) > 1:  # Buff
                buff_type_list = list(combinations(ranges_dict.get('Buff').keys(), int(row[2])))
            if int(row[3]) > 1:  # De-buff
                debuff_type_list = list(combinations(ranges_dict.get('Debuff').keys(), int(row[3])))
            if int(row[4]) > 1:  # Hand Bonus
                hand_bonus_type_list = list(combinations(ranges_dict.get('Hand Bonus').keys(), int(row[4])))

    # Build ranges
    for base_types in base_type_list:
        for buffs in buff_type_list:
            for debuffs in debuff_type_list:
                for hand_bonuses in hand_bonus_type_list:
                    final_ranges = []
                    base_type_label = base_types
                    buff_label = buffs
                    debuff_label = debuffs
                    hand_bonus_label = hand_bonuses

                    # Base type
                    if type(base_types) == tuple:
                        base_type_label = ' '.join(base_type_label)
                        for base_type in base_types:
                            final_ranges.append(ranges_dict['Base'][base_type]['Ranges'])
                    else:
                        final_ranges.append(ranges_dict['Base'][base_types]['Ranges'])

                    # Buffs
                    if type(buffs) == tuple:
                        buff_label = ' '.join(buff_label)
                        for buff in buffs:
                            final_ranges.append(ranges_dict['Buff'][buff]['Ranges'])
                    else:
                        final_ranges.append(ranges_dict['Buff'][buffs]['Ranges'])

                    # Debuffs
                    if type(debuffs) == tuple:
                        debuff_label = ' '.join(debuff_label)
                        for debuff in debuffs:
                            final_ranges.append(ranges_dict['Debuff'][debuff]['Ranges'])
                    else:
                        final_ranges.append(ranges_dict['Debuff'][debuffs]['Ranges'])

                    # Hand Bonuses
                    if type(hand_bonuses) == tuple:
                        hand_bonus_label = ' '.join(hand_bonus_label)
                        for hand_bonus in hand_bonuses:
                            if hand_bonus in buffs:
                                break
                            final_ranges.append(ranges_dict['Hand Bonus'][hand_bonus]['Ranges'])
                    else:
                        if hand_bonuses in buffs:
                            break
                        final_ranges.append(ranges_dict['Hand Bonus'][hand_bonuses]['Ranges'])

                    # Flatten all the ranges into one list
                    final_ranges = np.array(final_ranges).sum(axis=0)

                    # Stacked Ranges
                    stacked_ranges = []
                    running_total = 0
                    for i in range(len(final_ranges) - 2):
                        temp = final_ranges[i] + running_total
                        running_total += final_ranges[i]
                        stacked_ranges.append(temp)

                    # Final output
                    row = list(chain([base_type_label, buff_label, debuff_label, hand_bonus_label], final_ranges, stacked_ranges, [running_total]))
                    output_rows.append([str(x) for x in row])

    # Clear the existing sheet if it exists
    sheets.clear_page(sheet_id, f"{range_type} Output")
    sheets.batch_update(sheet_id, f"{range_type} Output", output_rows)


if BATTING:
    batting_ranges = parse_ranges_from_sheet(ranges_sheet_id, 'Batting')
    generate_all_ranges(ranges_sheet_id, batting_ranges, 'Batting')

if PITCHING:
    pitching_ranges = parse_ranges_from_sheet(ranges_sheet_id, 'Pitching')
    generate_all_ranges(ranges_sheet_id, pitching_ranges, 'Pitching')
