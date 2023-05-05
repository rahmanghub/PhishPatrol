# PhishPatrol

PhishPatrol is a command-line tool to detect phishing URLs using an XGBoost classifier. It extracts features from a given URL and predicts whether it is safe or dangerous.

## Linux Installation

1. Clone the repository: wget clone https://github.com/rahmanghub/PhishPatrol.git


2. Install the required packages: pip install -r requirements.txt


3. Run the tool: python PhishPatrol.py


## Windows Installation

1. Download the file

2. Extract it

3. Install the required packages: pip install -r requirements.txt

4. Run the tool: python PhishPatrol.py


## Usage

To use PhishPatrol, simply run the `phishpatrol.py` script and enter a URL when prompted. The tool will extract features from the URL and use an XGBoost classifier to predict whether it is safe or dangerous.

## Developers

Hemateja Pulikanti  - https://www.linkedin.com/in/hemateja-pulikanti-47a19924b

Abdul Rahman M      - https://www.linkedin.com/in/abdul-rahman-m-660158206/

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.

## Warning

This model has an accuracy rate of 94%, which means it is very accurate in identifying phishing URLs. However, it is important to note that no model is 100% accurate, and there may be instances where it falsely identifies a legitimate URL as phishing, or vice versa. Therefore, it is recommended to use this tool in conjunction with other security measures and exercise caution when making decisions based on its predictions.

## License

PhishPatrol is licensed under the GNU General Public License v3.0. See `LICENSE` for more information.
