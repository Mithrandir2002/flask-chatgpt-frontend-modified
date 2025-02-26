# ChatGPT Web Application

This is a simple web application that uses the GPT-4o language model with fine-tuned artifacts to generate responses to user input. The application is built using [Python Flask](https://flask.palletsprojects.com/en/2.0.x/) and [OpenAI's GPT-4o API](https://beta.openai.com/docs/api-reference/introduction) with [Fine-tuned Artifacts]

## Installation

To install the application, follow these steps:

1. Clone the repository: `https://github.com/Mithrandir2002/flask-chatgpt-frontend-modified.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up your OpenAI API key: [Instructions here](https://beta.openai.com/docs/quickstart)
4. Start the application: `python3 app.py`

## Example web
![Chatbot Image](chatbot.png)


## Finetune

To finetune the model with local informations, follow these steps:

1. Go to folder `\finetune`
2. Add messages and information to `training_data.jsonl` follow below example structure: `{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the University of Science and Technology of Hanoi (USTH)?"}, {"role": "assistant", "content": "USTH, also called Vietnam-France University, is a public university in Hanoi, Vietnam, founded in 2009 under an agreement between Vietnam and France. The official language used for teaching is English."}]}`
3. Edit OpenAI API key in `s.py`, then load the data to OpenAI cloud server: `python3 s.py`
3. Then we have file ID in terminal. Put it into load.py training_file parameters. Change different parameters then run the finetune: `python3 load.py`
4. Check the process and finetuned artifact id: `python3 process_check.py`
5. Add the finetuned artifact id into `qna.py` in line `model="#your_id"`. Then start the check: `python3 qna.py`
You can also add `#artifact_id` on the chatbot code

## Usage

Once the application is running, you can access it by navigating to `http://localhost:5000` in your web browser. Enter a message in the input field and press "Send" to generate a response.

## Contributing

If you'd like to contribute to the project, feel free to submit a pull request. Please make sure to follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

