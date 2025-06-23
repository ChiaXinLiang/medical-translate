import csv
import os
import random

# Set random seed for reproducibility
random.seed(32)

# Define the base path
base_path = "./datasets/train/gpt4/"

# 300 samples total, 9 categories = 33 samples per category (with 3 extra distributed)
samples_per_category = 44
extra_samples = 4

all_samples = []

for i in range(9):
    category = i + 1
    file_path = os.path.join(base_path, f"med_safety_demonstrations_category_{category}.csv")
    
    # Read the CSV file
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Determine number of samples for this category
    n_samples = samples_per_category + (1 if i < extra_samples else 0)
    
    # Sample from this category
    sampled_rows = random.sample(rows, min(n_samples, len(rows)))
    
    # Add category to each row
    for row in sampled_rows:
        row['category'] = category
        all_samples.append(row)

# Shuffle all samples
random.shuffle(all_samples)

# Save to new CSV file
output_path = "./med_safety_sample_300.csv"

# Get fieldnames from the first sample
fieldnames = ['category'] + [k for k in all_samples[0].keys() if k != 'category']

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_samples)

print(f"Successfully created sample with {len(all_samples)} data points")
print(f"Saved to: {output_path}")

# Print category distribution
category_counts = {}
for sample in all_samples:
    cat = sample['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nCategory distribution:")
for cat in sorted(category_counts.keys()):
    print(f"Category {cat}: {category_counts[cat]} samples")