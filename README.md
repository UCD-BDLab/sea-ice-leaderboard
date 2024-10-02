# Sea Ice Classification Benchmark Leaderboard

## Repository Overview

This repository serves as the official **benchmarking leaderboard** for sea ice type classification models. It allows researchers and practitioners to submit their models, compare their performance against established baselines, and contribute to advancing the state of the art in sea ice classification. The leaderboard tracks key metrics, including accuracy, F1-score, precision, and recall for both supervised and semi-supervised learning methods.

### Goals

- **Create a centralized leaderboard** for sea ice type classification models.
- **Encourage contributions** and comparisons of different models.
- **Provide baseline models** and easy access to pre-trained checkpoints.
- **Serve as a resource** for researchers working on sea ice classification.

## How to Participate

1. **Clone this Repository**:
   
   ```bash
   git clone https://github.com/your-username/sea-ice-benchmark-leaderboard.git
   cd sea-ice-benchmark-leaderboard


2. **Submit Your Model**:

   - Create a JSON file in the `submission/` folder with the following format:
   
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
   - Ensure that your JSON file is named uniquely (e.g., `model_your_name.json`) and placed in the `submission/` folder.
   - Follow the [submission guidelines](submission/submission_guidelines.md) to ensure correct formatting.

3. **Create a Pull Request**:

   - Once you have added your file, submit a pull request with the following title format:

     ```
     [Submission] Model_Name
     ```

   - The submission will be reviewed, and if the format is correct, the leaderboard will be updated.

4. **Review the Leaderboard**:

   - Once your submission is accepted, check the `leaderboard/leaderboard.md` file to see your model’s ranking.


