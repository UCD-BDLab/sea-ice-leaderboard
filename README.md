# Sea Ice Leaderboard


Welcome to the Sea Ice Leaderboard repository! This repository serves as a benchmark and evaluation platform for sea ice type classification models. It provides a centralized place for researchers and practitioners to contribute their models, evaluate them on standardized datasets, and compare their performance on the leaderboard.

## Goals
- Provide an open-source framework for evaluating sea ice classification models.
- Establish a baseline for both supervised and semi-supervised learning approaches.
- Facilitate reproducibility and transparency in research related to sea ice classification.

## Repository Structure
- **`data/`**: Links and scripts for downloading and preprocessing datasets.
- **`notebooks/`**: Jupyter notebooks demonstrating usage, model training, and evaluation.
- **`models/`**: Pre-trained models and scripts to run inference.
- **`leaderboard/`**: Scripts for evaluating models and calculating leaderboard metrics.

## How to Contribute
1. **Clone the Repository**:
    ```bash
    git clone git@github.com:bdlab-ucd/sea-ice-leaderboard.git
    ```
2. **Add Your Model**:
   - Place your model code and any dependencies in a new folder under `models/`.
   - Make sure to include a `README.md` file explaining your model and its usage.

3. **Run Evaluation**:
   - Use the evaluation scripts in `leaderboard/` to test your model on the provided datasets.

4. **Submit Your Results**:
   - Create a pull request with your model's results and code.
   - Include details like model architecture, training setup, and any relevant parameters.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions, feel free to reach out via issues or email [team@bdlab-ucd.com](mailto:team@bdlab-ucd.com).
