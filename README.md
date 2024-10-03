# Sea Ice Classification Benchmark Leaderboard

## Repository Overview

Welcome to the **Sea Ice Classification Leaderboard**, where research meets competition, and the best models rise to the top! 🚀

This repository serves as the **official benchmark** for sea ice type classification models. Here, researchers, students, and industry professionals can submit their models, challenge existing baselines, and **contribute to advancing the state of the art** in sea ice classification.

 **Think you’ve built a better model?** This is the place to prove it! Submit your model, and let’s see where it stands among the best! 


[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](https://github.com/bdlab-ucd/sea-ice-leaderboard)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)

## Leaderboard

| Rank | Model Name     | Methodology       | Model Type  | Data Used         | Accuracy | F1-Score | Precision | Recall | Inference Time |
|------|----------------|-------------------|-------------|-------------------|----------|----------|-----------|--------|----------------|
| 1    | Example_Model  | Supervised        | CNN         | Labeled           | 0.95     | 0.93     | 0.94      | 0.92   | 0.02 sec       |
| 2    | Model_Y        | Semi-Supervised   | Transformer | Both              | 0.92     | 0.90     | 0.91      | 0.89   | 0.03 sec       |
| 3    | Model_Z        | Supervised        | Hybrid      | Labeled           | 0.90     | 0.88     | 0.89      | 0.87   | 0.04 sec       |


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


