from openai import OpenAI

client = OpenAI(
  api_key="your_key_here"
)
# Upload training file
file = client.files.create(
    file=open("training_data.jsonl", "rb"),  # Ensure this file exists in the same directory
    purpose="fine-tune"
)

# Print the uploaded file ID
print("Uploaded File ID:", file.id)
