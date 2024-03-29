from .data import extract_data, decimal_default


def data_structure_generator(samples_info):
    information = {}
    for comparison in samples_info.keys():
        data = []
        data_points = []
        data_points_current_run = []
        for sample in samples_info[comparison]['data']:
            info_data = {
                'key': sample,
                'values': samples_info[comparison]['data'][sample]
                }
            if sample == "other":
                data_points += samples_info[comparison]['data'][sample]
            else:
                data_points += samples_info[comparison]['data'][sample]
                data_points_current_run += samples_info[comparison]['data'][sample]
            data.append(info_data)
        information['data_' + comparison] = data
        if len(data_points) > 0:
            information['data_' + comparison + '_min_x'] = min(data_points, key=lambda v: v['x'])['x']
            information['data_' + comparison + '_max_x'] = max(data_points, key=lambda v: v['x'])['x']
            information['data_' + comparison + '_min_y'] = min(data_points, key=lambda v: v['y'])['y']
            information['data_' + comparison + '_max_y'] = max(data_points, key=lambda v: v['y'])['y']
        if len(data_points_current_run) > 0:
            information['data_' + comparison + '_min_x_current_run'] = min(data_points_current_run, key=lambda v: v['x'])['x']
            information['data_' + comparison + '_max_x_current_run'] = max(data_points_current_run, key=lambda v: v['x'])['x']
            information['data_' + comparison + '_min_y_current_run'] = min(data_points_current_run, key=lambda v: v['y'])['y']
            information['data_' + comparison + '_max_y_current_run'] = max(data_points_current_run, key=lambda v: v['y'])['y']
        if comparison == "x_vs_y":
            information['data_' + comparison + '_min_x_current_run'] = -25
            information['data_' + comparison + '_max_y_current_run'] = 400
            from dataprocessor.models import Line
            line = Line.get_line(comparison)
            if line:
                line = Line.get_line(comparison)[0]
                info_data['slope'] = decimal_default(line.slope)
                info_data['intercept'] = decimal_default(line.intercept)
                info_data['color'] = '#C70039'
                information['data_' + comparison + '_slope'] = decimal_default(line.slope)
                information['data_' + comparison + '_intercept'] = decimal_default(line.intercept)
                information['data_' + comparison + '_std_err'] = decimal_default(line.stderr)
                information['data_' + comparison + '_stdev'] = decimal_default(line.stdev)
                information['data_' + comparison + '_p_value'] = decimal_default(line.p_value)
                information['data_' + comparison + '_r_value'] = decimal_default(line.r_value)
                information['data_' + comparison + '_color'] = '#C70039'
                continue
        information['data_' + comparison + '_slope'] = None
        information['data_' + comparison + '_intercept'] = None
        information['data_' + comparison + '_std_err'] = None
        information['data_' + comparison + '_stdev'] = None
        information['data_' + comparison + '_p_value'] = None
        information['data_' + comparison + '_r_value'] = None
        information['data_' + comparison + '_color'] = None

    return information


def chromosome_percentage_reads(data):
    chr_data = {"Chr1": [], "Chr2": [], "Chr3": [], "Chr4": [], "Chr5": [], "Chr6": [], "Chr7": [], "Chr8": [],
                "Chr9": [], "Chr10": [],
                "Chr11": [], "Chr12": [], "Chr13": [], "Chr14": [], "Chr15": [], "Chr16": [], "Chr17": [], "Chr18": [],
                "Chr19": [], "Chr20": [],
                "Chr21": [], "Chr21": [], "Chr22": [], "ChrX": [], "ChrY": []}
    reads = 0
    for sample in data:
        reads = decimal_default(sample['chr1']) + decimal_default(sample['chr2']) + decimal_default(
            sample['chr3']) + decimal_default(sample['chr4']) + decimal_default(sample['chr5']) + \
                decimal_default(sample['chr6']) + decimal_default(sample['chr7']) + decimal_default(
            sample['chr8']) + decimal_default(sample['chr9']) + decimal_default(sample['chr10']) + \
                decimal_default(sample['chr11']) + decimal_default(sample['chr12']) + decimal_default(
            sample['chr13']) + decimal_default(sample['chr14']) + decimal_default(sample['chr15']) + \
                decimal_default(sample['chr16']) + decimal_default(sample['chr17']) + decimal_default(
            sample['chr18']) + decimal_default(sample['chr19']) + decimal_default(sample['chr20']) + \
                decimal_default(sample['chr21']) + decimal_default(sample['chr22']) + decimal_default(
            sample['Chrx']) + decimal_default(sample['chry']) + reads
        chr_data["Chr1"].append({'x': 0, 'y': decimal_default(sample['chr1']), 'label': sample['sample_id']})
        chr_data["Chr2"].append({'x': 1, 'y': decimal_default(sample['chr2']), 'label': sample['sample_id']})
        chr_data["Chr3"].append({'x': 2, 'y': decimal_default(sample['chr3']), 'label': sample['sample_id']})
        chr_data["Chr4"].append({'x': 3, 'y': decimal_default(sample['chr4']), 'label': sample['sample_id']})
        chr_data["Chr5"].append({'x': 4, 'y': decimal_default(sample['chr5']), 'label': sample['sample_id']})
        chr_data["Chr6"].append({'x': 5, 'y': decimal_default(sample['chr6']), 'label': sample['sample_id']})
        chr_data["Chr7"].append({'x': 6, 'y': decimal_default(sample['chr7']), 'label': sample['sample_id']})
        chr_data["Chr8"].append({'x': 7, 'y': decimal_default(sample['chr8']), 'label': sample['sample_id']})
        chr_data["Chr9"].append({'x': 8, 'y': decimal_default(sample['chr9']), 'label': sample['sample_id']})
        chr_data["Chr10"].append({'x': 9, 'y': decimal_default(sample['chr10']), 'label': sample['sample_id']})
        chr_data["Chr11"].append({'x': 10, 'y': decimal_default(sample['chr11']), 'label': sample['sample_id']})
        chr_data["Chr12"].append({'x': 11, 'y': decimal_default(sample['chr12']), 'label': sample['sample_id']})
        chr_data["Chr13"].append({'x': 12, 'y': decimal_default(sample['chr13']), 'label': sample['sample_id']})
        chr_data["Chr14"].append({'x': 13, 'y': decimal_default(sample['chr14']), 'label': sample['sample_id']})
        chr_data["Chr15"].append({'x': 14, 'y': decimal_default(sample['chr15']), 'label': sample['sample_id']})
        chr_data["Chr16"].append({'x': 15, 'y': decimal_default(sample['chr16']), 'label': sample['sample_id']})
        chr_data["Chr17"].append({'x': 16, 'y': decimal_default(sample['chr17']), 'label': sample['sample_id']})
        chr_data["Chr18"].append({'x': 17, 'y': decimal_default(sample['chr18']), 'label': sample['sample_id']})
        chr_data["Chr19"].append({'x': 18, 'y': decimal_default(sample['chr19']), 'label': sample['sample_id']})
        chr_data["Chr20"].append({'x': 19, 'y': decimal_default(sample['chr20']), 'label': sample['sample_id']})
        chr_data["Chr21"].append({'x': 20, 'y': decimal_default(sample['chr21']), 'label': sample['sample_id']})
        chr_data["Chr22"].append({'x': 21, 'y': decimal_default(sample['chr22']), 'label': sample['sample_id']})
        chr_data["ChrX"].append({'x': 22, 'y': decimal_default(sample['Chrx']), 'label': sample['sample_id']})
        chr_data["ChrY"].append({'x': 23, 'y': decimal_default(sample['chry']), 'label': sample['sample_id']})
    for chr in chr_data:
        for i in range(len(chr_data[chr])):
            chr_data[chr][i]['y'] /= reads
    return [{"key": key, "values": values} for key, values in chr_data.items()]


def chromosome_coverage(data, exclude_chry=True):
    if exclude_chry:
        return [{
            'key': sample['sample_id'], 'values': [
                {'x': 0, 'y': decimal_default(sample['chr1_coverage']), 'label': '1'},
                {'x': 1, 'y': decimal_default(sample['chr2_coverage']), 'label': '2'},
                {'x': 2, 'y': decimal_default(sample['chr3_coverage']), 'label': '3'},
                {'x': 3, 'y': decimal_default(sample['chr4_coverage']), 'label': '4'},
                {'x': 4, 'y': decimal_default(sample['chr5_coverage']), 'label': '5'},
                {'x': 5, 'y': decimal_default(sample['chr6_coverage']), 'label': '6'},
                {'x': 6, 'y': decimal_default(sample['chr7_coverage']), 'label': '7'},
                {'x': 8, 'y': decimal_default(sample['chr8_coverage']), 'label': '8'},
                {'x': 8, 'y': decimal_default(sample['chr9_coverage']), 'label': '9'},
                {'x': 9, 'y': decimal_default(sample['chr10_coverage']), 'label': '10'},
                {'x': 10, 'y': decimal_default(sample['chr11_coverage']), 'label': '11'},
                {'x': 11, 'y': decimal_default(sample['chr12_coverage']), 'label': '12'},
                {'x': 12, 'y': decimal_default(sample['chr13_coverage']), 'label': '13'},
                {'x': 13, 'y': decimal_default(sample['chr14_coverage']), 'label': '14'},
                {'x': 14, 'y': decimal_default(sample['chr15_coverage']), 'label': '15'},
                {'x': 15, 'y': decimal_default(sample['chr16_coverage']), 'label': '16'},
                {'x': 16, 'y': decimal_default(sample['chr17_coverage']), 'label': '17'},
                {'x': 17, 'y': decimal_default(sample['chr18_coverage']), 'label': '18'},
                {'x': 18, 'y': decimal_default(sample['chr19_coverage']), 'label': '19'},
                {'x': 19, 'y': decimal_default(sample['chr20_coverage']), 'label': '20'},
                {'x': 20, 'y': decimal_default(sample['chr21_coverage']), 'label': '21'},
                {'x': 21, 'y': decimal_default(sample['chr22_coverage']), 'label': '22'},
                {'x': 22, 'y': decimal_default(sample['chrx_coverage']), 'label': 'X'}]} for sample in data]
    else:
        return [{
            'key': sample['sample_id'], 'values': [
                {'x': 0, 'y': decimal_default(sample['chr1_coverage']), 'label': '1'},
                {'x': 1, 'y': decimal_default(sample['chr2_coverage']), 'label': '2'},
                {'x': 2, 'y': decimal_default(sample['chr3_coverage']), 'label': '3'},
                {'x': 3, 'y': decimal_default(sample['chr4_coverage']), 'label': '4'},
                {'x': 4, 'y': decimal_default(sample['chr5_coverage']), 'label': '5'},
                {'x': 5, 'y': decimal_default(sample['chr6_coverage']), 'label': '6'},
                {'x': 6, 'y': decimal_default(sample['chr7_coverage']), 'label': '7'},
                {'x': 8, 'y': decimal_default(sample['chr8_coverage']), 'label': '8'},
                {'x': 8, 'y': decimal_default(sample['chr9_coverage']), 'label': '9'},
                {'x': 9, 'y': decimal_default(sample['chr10_coverage']), 'label': '10'},
                {'x': 10, 'y': decimal_default(sample['chr11_coverage']), 'label': '11'},
                {'x': 11, 'y': decimal_default(sample['chr12_coverage']), 'label': '12'},
                {'x': 12, 'y': decimal_default(sample['chr13_coverage']), 'label': '13'},
                {'x': 13, 'y': decimal_default(sample['chr14_coverage']), 'label': '14'},
                {'x': 14, 'y': decimal_default(sample['chr15_coverage']), 'label': '15'},
                {'x': 15, 'y': decimal_default(sample['chr16_coverage']), 'label': '16'},
                {'x': 16, 'y': decimal_default(sample['chr17_coverage']), 'label': '17'},
                {'x': 17, 'y': decimal_default(sample['chr18_coverage']), 'label': '18'},
                {'x': 18, 'y': decimal_default(sample['chr19_coverage']), 'label': '19'},
                {'x': 19, 'y': decimal_default(sample['chr20_coverage']), 'label': '20'},
                {'x': 20, 'y': decimal_default(sample['chr21_coverage']), 'label': '21'},
                {'x': 21, 'y': decimal_default(sample['chr22_coverage']), 'label': '22'},
                {'x': 22, 'y': decimal_default(sample['chrx_coverage']), 'label': 'X'},
                {'x': 23, 'y': decimal_default(sample['chry_coverage']), 'label': 'Y'}]} for sample in data]


def median_coverage(data):
    batch_data = {'13': {'data': {}, 'fields': ('flowcell_id__run_date', 'median_13')},
                  '18': {'data': {}, 'fields': ('flowcell_id__run_date', 'median_18')},
                  '21': {'data': {}, 'fields': ('flowcell_id__run_date', 'median_21')},
                  'x': {'data': {}, 'fields': ('flowcell_id__run_date', 'median_x')},
                  'y': {'data': {}, 'fields': ('flowcell_id__run_date', 'median_y')}}
    batch_data = extract_data(data=data, info=batch_data, label=lambda x: "median",
                              x_format=lambda x: x.timestamp() * 1000,
                              extra_info=lambda x: {'label': x['flowcell_id__flowcell_barcode']})
    return [{"key": k, 'values': d['data']['median']} for k, d in batch_data.items()]


def ncd_data(data, pre_legend=None, chr=None, size=1):
    info_to_extract = {'13': {'data': {}, 'fields': ('flowcell_id__run_date', 'ncd_13')},
                       '18': {'data': {}, 'fields': ('flowcell_id__run_date', 'ncd_18')},
                       '21': {'data': {}, 'fields': ('flowcell_id__run_date', 'ncd_21')},
                       'x': {'data': {}, 'fields': ('flowcell_id__run_date', 'ncd_x')},
                       'y': {'data': {}, 'fields': ('flowcell_id__run_date', 'ncd_y')}}
    ncd_batch_data = extract_data(data=data, size=size, info=info_to_extract, label=lambda x: 'ncd',
                                  x_format=lambda x: x.timestamp() * 1000,
                                  extra_info=lambda x: {'flowcell': x['flowcell_id__flowcell_barcode'],
                                                        'type': x['sample_type__name'], 'sample': x['sample_id']})
    if pre_legend is not None:
        return [{"max_y": max(d['data']['ncd'], key=lambda v: v['y'])['y'],
                 "min_y": min(d['data']['ncd'], key=lambda v: v['y'])['y'],
                 "key": pre_legend + " " + k,
                 'values': d['data']['ncd']} for k, d in ncd_batch_data.items() if chr is None or chr == k]
    else:

        return [{"max_y": max(d['data']['ncd'], key=lambda v: v['y'])['y'],
                 "min_y": min(d['data']['ncd'], key=lambda v: v['y'])['y'],
                 "key": k, 'values': d['data']['ncd']} for k, d in ncd_batch_data.items()]


def fetal_fraction(data, label=lambda x: 'hist', size=1):
    samples_info_ff_formatted = {'ff_time': {'data': {}, 'fields': ('flowcell_id__run_date', 'ff_formatted')}}
    samples_info_ff_formatted = extract_data(data=data, info=samples_info_ff_formatted, size=size, label=label,
                                             x_format=lambda x: x.timestamp() * 1000,
                                             replace_NA_with=-0.01)
    return data_structure_generator(samples_info_ff_formatted)
