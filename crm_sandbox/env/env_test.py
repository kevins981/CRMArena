#!/usr/bin/env python3
"""
Test file for functions.py
Tests the get_non_transferred_case_ids function
"""

import sys
import os
from crm_sandbox.env.connect_sandbox import SalesforceConnector
from pprint import pprint

# Add the current directory to the path so we can import functions
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from functions import *


def task_1050():
    # Which states have the quickest case closure rate over the past 6 months?
    # Today's date: 2024-11-09
    sf_connector = SalesforceConnector(org_type="original")

    end_date = "2024-11-09T00:00:00Z"
    period = "month"
    interval_count = 6

    result = get_start_date(end_date, period, interval_count)
    print(f"Six months before {end_date} is: {result}")
    
    # Get cases from the past 5 months
    start_date = result
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], sf_connector=sf_connector)
    print(f"Cases in the past 6 months: {cases}")
    
    # Add shipping state information to the cases
    cases_with_state = get_shipping_state(cases, sf_connector=sf_connector)
    print(f"Cases with shipping state: {cases_with_state}")

    # Calculate average closure times by region (state)
    region_closure_times = calculate_region_average_closure_times(cases_with_state, sf_connector=sf_connector)
    print(f"Average closure times by state: {region_closure_times}")
    
    # Find the state with the quickest (minimum) closure time
    state_with_quickest_closure = find_id_with_min_value(region_closure_times, sf_connector=sf_connector)
    print(f"State with quickest case closures: {state_with_quickest_closure}")

def task_1041():
    #During the summer of 2021, which states had the quickest case closures? Return only the two-letter abbreviation of the most matching state (eg. CA).
    sf_connector = SalesforceConnector(org_type="original")

    result = get_period("Summer", 2021) 
    print(f"Summer 2021 is: {result}")

    start_date = result['start_date']
    end_date = result['end_date']
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], sf_connector=sf_connector)
    print(f"Cases in the past 5 months: {cases}")
    
    # Add shipping state information to the cases
    cases_with_state = get_shipping_state(cases, sf_connector=sf_connector)
    print(f"Cases with shipping state: {cases_with_state}")

    # Calculate average closure times by region (state)
    region_closure_times = calculate_region_average_closure_times(cases_with_state, sf_connector=sf_connector)
    print(f"Average closure times by state: {region_closure_times}")
    
    # Find the state with the quickest (minimum) closure time
    state_with_quickest_closure = find_id_with_min_value(region_closure_times, sf_connector=sf_connector)
    print(f"State with quickest case closures: {state_with_quickest_closure}")


def task_165():    
    # Is there a specific month in the past 6 quarters where the cases for Hydro Racer Swim Fins significantly surpassed those of other months? The associated product Id is 01tWs000002wT5JIAU.
    sf_connector = SalesforceConnector(org_type="original")

    # Get the order item IDs for the product
    product_id = "01tWs000002wT5JIAU"
    order_item_ids = get_order_item_ids_by_product(product_id, sf_connector=sf_connector)
    print(f"Order item IDs for product {product_id}: {order_item_ids}")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2023-01-05T00:00:00Z"
    period = "quarter"
    interval_count = 6
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Six quarters before {end_date} is: {result}")

    start_date = result
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, order_item_ids=order_item_ids, sf_connector=sf_connector)
    pprint(cases)

def task_130():    
    # Is there a specific month in the past three quarters when the All-Around Yoga Tank cases we received were significantly higher than in other months? The associated product Id is 01tWs000002wQXGIA2. 
    # Today's date: 2022-08-20
    sf_connector = SalesforceConnector(org_type="original")
    product_id = "01tWs000002wQXGIA2"
    order_item_ids = get_order_item_ids_by_product(product_id, sf_connector=sf_connector)
    print(f"Order item IDs for product {product_id}: {order_item_ids}")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2022-08-20T00:00:00Z"
    period = "quarter"
    interval_count = 3
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Three quarters before {end_date} is: {result}")

    start_date = result
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, order_item_ids=order_item_ids, sf_connector=sf_connector)
    pprint(cases)
    

def task_780():    
    # task 780: Identify the agent with the highest number of transfers in the past two months among those handling at least one case.
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2021-09-22T00:00:00Z"
    period = "month"
    interval_count = 2
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Two months before {end_date} is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result
    transferred_cases = get_agent_transferred_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    print(f"Transferred cases between {start_date} and {end_date}: {transferred_cases}")


def task_742():    
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2021-06-20T00:00:00Z"
    period = "quarter"
    interval_count = 3
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Three quarters before {end_date} is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result
    non_transferred_cases = get_non_transferred_case_ids(start_date, end_date, sf_connector=sf_connector)
    print(f"Non-transferred case IDs between {start_date} and {end_date}: {non_transferred_cases}")
    
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], case_ids=non_transferred_cases, sf_connector=sf_connector)
    pprint(cases)
    
    # Call calculate_average_handle_time on the retrieved cases
    average_handle_times = calculate_average_handle_time(cases, sf_connector=sf_connector)
    pprint(f"Average handle times by agent: {average_handle_times}")
    
    # Find the agent with the highest average handle time
    agent_with_max_handle_time = find_id_with_max_value(average_handle_times, sf_connector=sf_connector)
    print(f"Agent with highest average handle time: {agent_with_max_handle_time}")

def task_696():    
    # Over the past 2 weeks, identify the agent with the shortest handle time who has managed more than one case. Today is 2020-04-26
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2020-04-26T00:00:00Z"
    period = "week"
    interval_count = 2
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Two weeks before {end_date} is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result
    non_transferred_cases = get_non_transferred_case_ids(start_date, end_date, sf_connector=sf_connector)
    print(f"Non-transferred case IDs between {start_date} and {end_date}: {non_transferred_cases}")
    
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], case_ids=non_transferred_cases, sf_connector=sf_connector)
    pprint(cases)
    
    # Call calculate_average_handle_time on the retrieved cases
    average_handle_times = calculate_average_handle_time(cases, sf_connector=sf_connector)
    pprint(f"Average handle times by agent: {average_handle_times}")
    
    # Find the agent with the highest average handle time
    agent_with_max_handle_time = find_id_with_max_value(average_handle_times, sf_connector=sf_connector)
    print(f"Agent with highest average handle time: {agent_with_max_handle_time}")

def task_652():   
    # # In the past 3 months, which agent achieved the lowest average handle time while handling more than 2 cases? Return only the Id of the agent. Today's date: 2022-08-22
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26

    end_date = "2022-08-22T00:00:00Z"
    period = "month"
    interval_count = 3
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Two weeks before {end_date} is: {result}")

    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result
    end_date = "2022-08-22T00:00:00Z"

    non_transferred_cases = get_non_transferred_case_ids(start_date, end_date, sf_connector=sf_connector)
    print(f"Non-transferred case IDs between {start_date} and {end_date}: {non_transferred_cases}")

    agent_handled_cases = get_agent_handled_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    pprint(f"Agent handled cases: {agent_handled_cases}")

    qualified_agent_ids = get_qualified_agent_ids_by_case_count(agent_handled_cases, 2, sf_connector=sf_connector)
    pprint(f"Qualified agent IDs: {qualified_agent_ids}")
    
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], agent_ids=qualified_agent_ids, sf_connector=sf_connector)
    pprint(cases)

    average_handle_times = calculate_average_handle_time(cases, sf_connector=sf_connector)
    pprint(f"Average handle times by agent: {average_handle_times}")

    agent_with_min_handle_time = find_id_with_min_value(average_handle_times, sf_connector=sf_connector)
    pprint(f"Agent with shortest average handle time: {agent_with_min_handle_time}")


def task_650():   
    # Find the agent with the shortest handle time who managed more than one case in Winter 2021.  Today's date: 2023-12-21
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26

    result = get_period("Winter", 2021) 
    print(f"Winter 2021 is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result['start_date']
    end_date = result['end_date']

    non_transferred_cases = get_non_transferred_case_ids(start_date, end_date, sf_connector=sf_connector)
    print(f"Non-transferred case IDs between {start_date} and {end_date}: {non_transferred_cases}")

    agent_handled_cases = get_agent_handled_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    pprint(f"Agent handled cases: {agent_handled_cases}")

    qualified_agent_ids = get_qualified_agent_ids_by_case_count(agent_handled_cases, 2, sf_connector=sf_connector)
    pprint(f"Qualified agent IDs: {qualified_agent_ids}")
    
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], agent_ids=qualified_agent_ids, sf_connector=sf_connector)
    pprint(cases)

    average_handle_times = calculate_average_handle_time(cases, sf_connector=sf_connector)
    pprint(f"Average handle times by agent: {average_handle_times}")

    agent_with_min_handle_time = find_id_with_min_value(average_handle_times, sf_connector=sf_connector)
    pprint(f"Agent with shortest average handle time: {agent_with_min_handle_time}")


def task_656():   
    # In the first quarter of 2023, find the agent with the longest handle time who managed cases. 
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26

    result = get_period("Q1", 2023) 
    print(f"First Quarter 2023 is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result['start_date']
    end_date = result['end_date']
    non_transferred_cases = get_non_transferred_case_ids(start_date, end_date, sf_connector=sf_connector)
    print(f"Non-transferred case IDs between {start_date} and {end_date}: {non_transferred_cases}")

    agent_handled_cases = get_agent_handled_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    pprint(f"Agent handled cases: {agent_handled_cases}")

    qualified_agent_ids = get_qualified_agent_ids_by_case_count(agent_handled_cases, 0, sf_connector=sf_connector)
    pprint(f"Qualified agent IDs: {qualified_agent_ids}")
    
    # Call get_cases with start_date, end_date, and the non_transferred case IDs
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], agent_ids=qualified_agent_ids, sf_connector=sf_connector)
    pprint(cases)

    average_handle_times = calculate_average_handle_time(cases, sf_connector=sf_connector)
    pprint(f"Average handle times by agent: {average_handle_times}")

    agent_with_max_handle_time = find_id_with_max_value(average_handle_times, sf_connector=sf_connector)
    pprint(f"Agent with longest average handle time: {agent_with_max_handle_time}")


def task_859():    
    # Find the agent with the highest number of transfer counts who managed multiple cases in Fall 2020.
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26

    result = get_period("Fall", 2020) 
    print(f"Fall 2020 is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result['start_date']
    end_date = result['end_date']

    # Call get_cases with start_date, end_date
    cases = get_cases(start_date=start_date, end_date=end_date, sf_connector=sf_connector)
    pprint(f"cases within period: {cases}")

    agent_handled_cases = get_agent_handled_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    pprint(f"Agent handled cases: {agent_handled_cases}")

    qualified_agent_ids = get_qualified_agent_ids_by_case_count(agent_handled_cases, 2, sf_connector=sf_connector)
    pprint(f"Qualified agent IDs: {qualified_agent_ids}")

    transferred_cases = get_agent_transferred_cases_by_period(start_date, end_date, qualified_agent_ids, sf_connector=sf_connector)
    pprint(f"Transferred cases for qualified agents: {transferred_cases}")

def task_781():    
    # Identify the agent with the highest number of transfers over the last 5 quarters among those who managed cases.
    # Today's date: 2024-07-27
    sf_connector = SalesforceConnector(org_type="original")

    # Get the start date
    # Call get_start_date to find the date two weeks before 2020-04-26
    end_date = "2024-07-27T00:00:00Z"
    period = "quarter"
    interval_count = 5
    
    result = get_start_date(end_date, period, interval_count)
    print(f"Five quarters before {end_date} is: {result}")
    
    # Call get_non_transferred_case_ids with the calculated start date and end date
    start_date = result

    # Call get_cases with start_date, end_date
    cases = get_cases(start_date=start_date, end_date=end_date, statuses=["Closed"], sf_connector=sf_connector)
    pprint(f"cases within period: {cases}")

    agent_handled_cases = get_agent_handled_cases_by_period(start_date, end_date, sf_connector=sf_connector)
    pprint(f"Agent handled cases: {agent_handled_cases}")

    qualified_agent_ids = get_qualified_agent_ids_by_case_count(agent_handled_cases, 1, sf_connector=sf_connector)
    pprint(f"Qualified agent IDs: {qualified_agent_ids}")

    transferred_cases = get_agent_transferred_cases_by_period(start_date, end_date, qualified_agent_ids, sf_connector=sf_connector)
    pprint(f"Transferred cases for qualified agents: {transferred_cases}")


def task_260():
    # What is the most frequent problem with Retro Style Sneakers in Winter 2021? The associated product Id is 01tWs000002wQygIAE.
    # Return only the issue Id of the most reported issue for this product.
    # Today's date: 2023-01-04
    sf_connector = SalesforceConnector(org_type="original")


    product_id = "01tWs000002wQygIAE"
    order_item_ids = get_order_item_ids_by_product(product_id, sf_connector=sf_connector)
    print(f"Order item IDs for product {product_id}: {order_item_ids}")

    result = get_period("Winter", 2021) 
    print(f"Winter 2021 is: {result}")

    issue_counts = get_issue_counts(result['start_date'], result['end_date'], order_item_ids, sf_connector=sf_connector)
    pprint(f"Issue counts: {issue_counts}")

    issue_with_max_count = find_id_with_max_value(issue_counts, sf_connector=sf_connector)
    pprint(f"Issue with max count: {issue_with_max_count}")
    


def task_327():
    # What was the most frequent problem with Air Zoom Pegasus in the fourth quarter of 2020? The associated product Id is 01tWs000002wRLFIA2.
    # Return only the issue Id of the most reported issue for this product.
    # Today's date: 2023-01-04
    sf_connector = SalesforceConnector(org_type="original")

    product_id = "01tWs000002wRLFIA2"
    order_item_ids = get_order_item_ids_by_product(product_id, sf_connector=sf_connector)
    print(f"Order item IDs for product {product_id}: {order_item_ids}")

    result = get_period("Q4", 2020) 
    print(f"Q4 2020 is: {result}")

    issue_counts = get_issue_counts(result['start_date'], result['end_date'], order_item_ids, sf_connector=sf_connector)
    pprint(f"Issue counts: {issue_counts}")

    issue_with_max_count = find_id_with_max_value(issue_counts, sf_connector=sf_connector)
    pprint(f"Issue with max count: {issue_with_max_count}")
    

if __name__ == "__main__":
    # task_742()
    # task_696()
    # task_780()
    # task_781()
    # task_327()
    task_1050()
    # task_130()
    # task_132()
    # task_165()
    # task_652()
