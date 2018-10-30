import csv
import sys

def import_data(input_file):
    with open(input_file, encoding = 'UTF-8') as f:
        reader = csv.reader(f, delimiter = ';')
        headers = next(reader)
        data = list(reader)
        assert len(data[0]) == len(headers), 'headers and data not aligned'
        return headers, data


def count_cata(headers, data):
    occupation_count = dict()
    state_count = dict()

    try:
        ind_status = headers.index('CASE_STATUS')
    except:
        ind_status = headers.index('STATUS')

    try:
        ind_socName = headers.index('SOC_NAME')
    except:
        ind_socName = headers.index('LCA_CASE_SOC_NAME')

    try:
        ind_state = headers.index('WORKSITE_STATE')
    except:
        ind_state = headers.index('LCA_CASE_WORKLOC1_STATE')

    total = 0
    for entry in data:
        if entry[ind_status] == 'CERTIFIED':
            occupation = entry[ind_socName].strip('"')
            occupation_count[occupation] = occupation_count.get(occupation, 0) + 1
            state = entry[ind_state]
            state_count[state] = state_count.get(state, 0) + 1
            total += 1
    return total, occupation_count, state_count


def sort_cata(cata_count, total):
    cata_list = [[key, value, '{:.1%}'.format(value/total)] \
    for (key, value) in cata_count.items()]
    cata_list.sort(key = lambda x: (-x[1], x[0]))
    return cata_list


def export_result(sorted_occupation, sorted_state, occupation_outfile, state_outfile):
    with open(occupation_outfile, 'w', encoding = 'UTF-8') as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
        writer.writerows(sorted_occupation[:10])

    with open(state_outfile, 'w', encoding = 'UTF-8') as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
        writer.writerows(sorted_state[:10])


data_folder = '../insight_testsuite/tests/test_1/'
input_file = data_folder + 'input/h1b_input.csv'
occupation_outfile = data_folder + 'output/SOC.txt'
state_outfile = data_folder + 'output/state.txt'

headers, data = import_data(input_file)
total, occupation_count, state_count = count_cata(headers, data)
sorted_occupation = sort_cata(occupation_count, total)
sorted_state = sort_cata(state_count, total)
export_result(sorted_occupation, sorted_state, occupation_outfile, state_outfile)
