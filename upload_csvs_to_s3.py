import boto3
import glob
import os

# --- Configuration ---
BUCKET_NAME = 'your-bucket-name'  # Replace with your bucket name
# Use a raw string for Windows paths or forward-slashes. Update your folder.
LOCAL_FOLDER_PATH = r'path\to\your\local\folder'
# S3 destination prefix (OBJECT KEY prefix inside the bucket). Do NOT include the s3://<bucket> prefix.
S3_DESTINATION_FOLDER = 'csv_uploads'

# Initialize S3 client using default configured credentials
s3_client = boto3.client('s3')

# Ensure local folder exists
if not os.path.isdir(LOCAL_FOLDER_PATH):
    print(f"Local folder does not exist: {LOCAL_FOLDER_PATH}")
    csv_files = []
else:
    # Change to that directory to simplify listing
    os.chdir(LOCAL_FOLDER_PATH)
    # Find all files matching the CSV extension in the current directory
    csv_files = glob.glob('*.csv')

print(f"Found {len(csv_files)} CSV files to upload.")

# Iterate through the list of files and upload each one
for filename in csv_files:
    # Define the S3 object key (destination path in S3). Strip any leading/trailing slashes.
    prefix = S3_DESTINATION_FOLDER.strip('/')
    if prefix:
        s3_key = f"{prefix}/{os.path.basename(filename)}"
    else:
        s3_key = os.path.basename(filename)

    # Build local file path in case we didn't chdir
    local_path = os.path.join(LOCAL_FOLDER_PATH, filename) if not os.getcwd().startswith(os.path.abspath(LOCAL_FOLDER_PATH)) else filename

    try:
        print(f"Uploading {local_path} to s3://{BUCKET_NAME}/{s3_key}...")
        s3_client.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f"Successfully uploaded: {filename}")
    except Exception as e:
        print(f"Failed to upload {filename}: {e}")

print("All upload operations finished.")
