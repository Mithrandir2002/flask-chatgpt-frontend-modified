from openai import OpenAI

client = OpenAI(
  api_key="your_key_here")

job = client.fine_tuning.jobs.create(
    training_file="file-BapZ1gV4DRowjL97hvrG3X",  # Your file ID
    model="gpt-4o-2024-08-06",
    method={
        "type": "supervised",  # Corrected method type
        "supervised": {
            "hyperparameters": {
                "batch_size": "auto",
                "learning_rate_multiplier": "auto",
                "n_epochs": "auto",
            }
        },
    },
)
