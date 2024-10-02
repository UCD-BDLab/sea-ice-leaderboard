import json
import os
import pandas as pd

# Path to the submission folder and leaderboard file
SUBMISSION_FOLDER = 'submission/'
LEADERBOARD_FILE = 'leaderboard.md'

def load_submissions():
    submissions = []
    
    for filename in os.listdir(SUBMISSION_FOLDER):
        if filename.endswith(".json"):
            with open(os.path.join(SUBMISSION_FOLDER, filename)) as f:
                submission = json.load(f)
                submissions.append(submission)
    
    return submissions

def update_leaderboard(submissions):
    # Convert submissions to a DataFrame
    df = pd.DataFrame(submissions)
    
    # Sort by accuracy (you can adjust sorting based on any metric)
    df = df.sort_values(by='accuracy', ascending=False)
    
    # Create a markdown table
    leaderboard_md = '| Rank | Model Name | Methodology | Model Type | Data Used | Accuracy | F1-Score | Precision | Recall | Inference Time |\n'
    leaderboard_md += '|------|-------------|-------------|------------|-----------|----------|----------|-----------|--------|----------------|\n'
    
    for i, row in df.iterrows():
        leaderboard_md += f'| {i+1} | {row["model_name"]} | {row["methodology"]} | {row["model_type"]} | {row["data_used"]} | {row["accuracy"]:.2f} | {row["f1_score"]:.2f} | {row["precision"]:.2f} | {row["recall"]:.2f} | {row["inference_time"]} |\n'
    
    # Write the markdown file
    with open(LEADERBOARD_FILE, 'w') as f:
        f.write('# Sea Ice Classification Benchmark Leaderboard\n\n')
        f.write(leaderboard_md)

if __name__ == "__main__":
    submissions = load_submissions()
    if submissions:
        update_leaderboard(submissions)
        print("Leaderboard updated successfully!")
    else:
        print("No submissions found.")