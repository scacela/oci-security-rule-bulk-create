import copy_from_template
import get_progress
import sys
from config import *
import datetime
import os
import pandas as pd

def main():

    data_df = pd.read_csv(cidr_ranges_filepath, header=None)
    data_list_of_lists = data_df.values.tolist()
    cidrs = [i for j in data_list_of_lists for i in j]

    num_rules_to_add_total = len(cidrs)
    num_rules_to_add_total_remaining = len(cidrs)

    count_batches_added = 1
    count_rules_added_total = 0
    processed = []
    firstpass = True
    datetime_first = ""

    while num_rules_to_add_total_remaining >= security_rules_limit: # if num_rules_to_add_total < security_rules_limit, that would indicate the last loop i.e. batch
        for cidr in cidrs[0:security_rules_limit]:
            processed.append(cidrs.pop())
        num_rules_to_add_in_current_batch=len(processed)

        built_script_modulename, built_script_filename = copy_from_template.main(processed, count_batches_added)
        built_script_module = __import__(built_script_modulename)
        built_script_module.main(count_batches_added)
        os.remove(built_script_filename)

        count_rules_added_total+=num_rules_to_add_in_current_batch
        datetime_now = datetime.datetime.now()

        if firstpass:
        	datetime_first = datetime_now
        	firstpass = False

        get_progress.main(datetime_now, count_batches_added, num_rules_to_add_in_current_batch, count_rules_added_total, num_rules_to_add_total)
        processed=[]
        count_batches_added+=1
        num_rules_to_add_total_remaining = len(cidrs)
    # last batch
    copy_from_template.main(cidrs, count_batches_added)
    num_rules_to_add_in_current_batch=num_rules_to_add_total_remaining

    built_script_modulename, built_script_filename = copy_from_template.main(cidrs, count_batches_added)
    built_script_module = __import__(built_script_modulename)
    built_script_module.main(count_batches_added)
    os.remove(built_script_filename)

    count_rules_added_total+=num_rules_to_add_in_current_batch
    datetime_now = datetime.datetime.now()
    get_progress.main(datetime_now, count_batches_added, num_rules_to_add_in_current_batch, count_rules_added_total, num_rules_to_add_total)
    get_progress.totals(datetime_now, count_batches_added, count_rules_added_total, num_rules_to_add_total, datetime_first)
main()