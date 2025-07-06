from datasets import load_dataset, Dataset, DatasetDict
import random
import os

# Original CRMArena data
crmarena_queries = load_dataset("Salesforce/CRMArena", "CRMArena")
crmarena_schema = load_dataset("Salesforce/CRMArena", "schema")

print("Original dataset structure:")
print(crmarena_queries)
print("\nSchema dataset:")
print(crmarena_schema)

# Define the specific tasks we want to filter for
target_tasks = [
    'monthly_trend_analysis',
    'top_issue_identification', 
    'handle_time',
    'transfer_count',
    'best_region_identification'
]

# Filter the dataset for our target tasks
filtered_data = crmarena_queries['test'].filter(lambda example: example['task'] in target_tasks)

print(f"\nFiltered dataset size: {len(filtered_data)}")
print(f"Original dataset size: {len(crmarena_queries['test'])}")

# Group by task
task_groups = {}
for task in target_tasks:
    task_data = filtered_data.filter(lambda example: example['task'] == task)
    task_groups[task] = task_data
    print(f"\nTask '{task}': {len(task_data)} examples")

# Create a DatasetDict with separate datasets for each task
task_datasets = DatasetDict({
    task: dataset for task, dataset in task_groups.items()
})

print(f"\nCreated {len(task_datasets)} task-specific datasets:")
for task_name, dataset in task_datasets.items():
    print(f"  - {task_name}: {len(dataset)} examples")

# Generate random indices and create smaller datasets
print("\n" + "="*80)
print("CREATING RANDOM 10-ROW DATASETS:")
print("="*80)

# Set random seed for reproducibility
random.seed(42)

# Collect all random rows from all tasks
all_random_rows = []

# Generate random indices and collect rows
for task_name, dataset in task_datasets.items():
    if len(dataset) > 0:
        # Generate 10 random indices between 0 and 129
        random_indices = random.sample(range(len(dataset)), 10)
        print(f"\n{task_name}: Random indices: {random_indices}")
        
        # Select the random rows
        random_rows = [dataset[i] for i in random_indices]
        all_random_rows.extend(random_rows)
        
        print(f"Added {len(random_rows)} rows from {task_name}")
    else:
        print(f"\n{task_name}: No data available")

# Create one combined dataset with all 50 rows
combined_dataset = Dataset.from_list(all_random_rows)
print(f"\nCreated combined dataset with {len(combined_dataset)} total rows")

# Shuffle the combined dataset
combined_dataset = combined_dataset.shuffle(seed=42)
print(f"Shuffled the combined dataset to randomize task order")

# Save the combined dataset locally
combined_dataset.save_to_disk("sub_taskset_50qs")
print(f"Saved combined dataset to: sub_taskset_50qs/")

print(f"\nYou can load the combined dataset later using:")
print("dataset = load_from_disk('sub_taskset_50qs')")
