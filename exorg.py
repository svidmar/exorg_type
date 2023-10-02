# This script can be used to determine organisation type based on an organisations name from a CSV file. Can be used to classify unclassified external organisations from Pure, which can then be written back into Pure. 


import csv
import openai

# Replace with your OpenAI API key
api_key = 'my_openai_apikey'

# Specify the model (ChatGPT)
model = 'gpt-3.5-turbo'

# Function to determine the organization type using ChatGPT
def get_organization_type(organization_name):
    try:
        # Initialize the OpenAI API client
        openai.api_key = api_key

        # Construct the conversation with a user message
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Classify the type of organization for '{organization_name}'. The type should be one of the following: 'Academic', 'Funding provider', 'Corporate', 'Municipal', 'Medical', 'NGO', 'Government', 'Region', 'Educational institution'. If none of these are applicable, choose 'Other'."},
        ]

        # Make the API call
        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation,
            max_tokens=50  # Adjust this value as needed

        )

        # Extract and return the assistant's reply, removing leading/trailing whitespace
        assistant_reply = response.choices[0].message["content"].strip()

        # Check if the assistant's reply is one of the allowed types, otherwise set it to "Other"
        allowed_types = ['Academic', 'Funding provider', 'Corporate', 'Municipal', 'Medical', 'NGO', 'Government', 'Region', 'Educational institution']
        return assistant_reply if assistant_reply in allowed_types else 'Other'
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 'Unknown'

# Input and output file paths
input_csv_file = 'input.csv'  # Replace with your input CSV file
output_csv_file = 'output.csv'  # Replace with your output CSV file

# Open input CSV file for reading and output CSV file for writing
with open(input_csv_file, 'r', newline='') as input_file, open(output_csv_file, 'w', newline='') as output_file:
    csv_reader = csv.DictReader(input_file)
    fieldnames = csv_reader.fieldnames + ['type']  # Add 'type' as a new field
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in csv_reader:
        organization_name = row['Name']
        organization_type = get_organization_type(organization_name)
        row['type'] = organization_type
        csv_writer.writerow(row)

print(f"Processing complete. Output saved to {output_csv_file}")
