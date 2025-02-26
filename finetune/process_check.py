from openai import OpenAI
client = OpenAI(
  api_key="your_key_here")

#job_info = client.fine_tuning.jobs.retrieve("ftjob-W7MPNPOxJwMitdbLtwhvWLEw")
#print(job_info)

jobs = client.fine_tuning.jobs.list()
for job in jobs.data:
    #job_info = client.fine_tuning.jobs.retrieve(job.id)
    #print(job_info)
    print(f"Job ID: {job.id}, Model: {job.fine_tuned_model}, Status: {job.status}")
