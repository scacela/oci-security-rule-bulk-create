from config import *
import math
from textwrap import dedent

def main(datetime_now, count_batches_added, num_rules_to_add_in_current_batch, count_rules_added_total, num_rules_to_add_total):
	num_batches_to_add_total = predict_total_number_of_batches(num_rules_to_add_total)
	percent_batches_deployed = get_percent(count_batches_added, num_batches_to_add_total)
	percent_rules_added_total = get_percent(count_rules_added_total, num_rules_to_add_total)
	print(
	dedent(f'''
	Number of batches deployed:             {str(count_batches_added)} of {str(num_batches_to_add_total)}\t\t{str(percent_batches_deployed)}%
	Number of rules added in current batch: {str(num_rules_to_add_in_current_batch)}
	Total number of rules added:            {str(count_rules_added_total)} of {str(num_rules_to_add_total)}\t{str(percent_rules_added_total)}%
	Current time:                           {str(datetime_now)}'''
	))
def totals(datetime_now, count_batches_added, count_rules_added_total, num_rules_to_add_total, datetime_now_first):
	num_batches_to_add_total = predict_total_number_of_batches(num_rules_to_add_total)
	percent_batches_deployed = get_percent(count_batches_added, num_batches_to_add_total)
	percent_rules_added_total = get_percent(count_rules_added_total, num_rules_to_add_total)
	datetime_total = calculate_timestamp_difference(datetime_now_first, datetime_now)
	print(
	dedent(f'''
	-----
	Grand Totals:
	Total number of batches deployed:       {str(count_batches_added)} of {str(num_batches_to_add_total)}\t\t{str(percent_batches_deployed)}%
	Total number of rules added:            {str(count_rules_added_total)} of {str(num_rules_to_add_total)}\t{str(percent_rules_added_total)}%
	Total time:                             {str(datetime_total)} seconds
	'''
	))
def predict_total_number_of_batches(num_rules_to_add_total):
	if num_rules_to_add_total % security_rules_limit > 0:
		add_one = 1
	else:
		add_one = 0
	num_batches_to_add_total = math.floor(num_rules_to_add_total / security_rules_limit) + add_one
	return num_batches_to_add_total

def calculate_timestamp_difference(datetime_now_first, datetime_now):
	timestamp_difference = datetime_now - datetime_now_first
	total_seconds = timestamp_difference.total_seconds()
	return round(total_seconds, 2)

def get_percent(numerator, denominator):
	percentage = round((numerator / denominator) * 100, 2)
	return percentage