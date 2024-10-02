
# Sea Ice Classification Benchmark Submission Guidelines

To submit your model for evaluation and ranking on the leaderboard, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sea-ice-benchmark-leaderboard.git
cd sea-ice-benchmark-leaderboard
```

### 2. Add Your Results

Create a JSON file in the `submission/` folder. Use the following format to add your model results:

```json
{
  "model_name": "Your_Model_Name",
  "methodology": "Supervised / Semi-Supervised",
  "model_type": "Type_of_Model (e.g., CNN, Transformer, etc.)",
  "data_used": "Labeled / Unlabeled / Both",
  "accuracy": 0.XX,
  "f1_score": 0.XX,
  "precision": 0.XX,
  "recall": 0.XX,
  "inference_time": "XX sec"
}
```

### 3. Submit a Pull Request

Once you've added your file, submit a pull request with the following title:

```
[Submission] Your_Model_Name
```

The submission will be reviewed, and if the format is correct, the leaderboard will be updated.