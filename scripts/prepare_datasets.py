import os
from huggingface_hub import login, HfApi
from datasets import load_dataset

# Directly assign the Hugging Face API token
hf_api_token = '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'

# Create a global instance of HfApi
hf_api = HfApi()

# Authenticate with Hugging Face
try:
    print(f"Attempting to authenticate with token: {'*' * len(hf_api_token) if hf_api_token else 'None'}")
    login(token=hf_api_token, add_to_git_credential=True)
    print("Successfully authenticated with Hugging Face.")
except ValueError as e:
    print(f"Authentication failed: {str(e)}")
    print(f"Token used: {'*' * len(hf_api_token) if hf_api_token else 'None'}")
    exit(1)  # Exit the script if authentication fails

def search_datasets(query, num_results=5):
    """Search for datasets on Hugging Face."""
    datasets = hf_api.list_datasets(search=query, limit=num_results)
    return [dataset.id for dataset in datasets]

def download_dataset(dataset_id):
    """Download a dataset from Hugging Face."""
    try:
        dataset = load_dataset(dataset_id)
        print(f"Successfully downloaded dataset: {dataset_id}")
        return dataset
    except Exception as e:
        print(f"Error downloading dataset {dataset_id}: {str(e)}")
        return None

def prepare_dataset(dataset, dataset_id, save_dir):
    """Prepare the dataset for use with the coding agent and save it to disk."""
    if 'train' in dataset:
        prepared_data = dataset['train']
    else:
        prepared_data = dataset

    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Save the dataset to disk
    save_path = os.path.join(save_dir, f"{dataset_id}.arrow")
    prepared_data.save_to_disk(save_path)

    print(f"Saved prepared dataset to {save_path}")
    return prepared_data

def main():
    save_dir = "/home/ubuntu/coding-agent/datasets"
    coding_datasets = search_datasets("coding programming")

    for dataset_id in coding_datasets:
        dataset = download_dataset(dataset_id)
        if dataset:
            prepared_data = prepare_dataset(dataset, dataset_id, save_dir)
            print(f"Prepared and saved dataset: {dataset_id}")
            # Here you can add code to integrate the prepared data with your coding agent

if __name__ == "__main__":
    main()