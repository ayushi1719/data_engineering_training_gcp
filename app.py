from helper import GCPHelper
from sys import argv

def main():

    gcp = GCPHelper("test-bucket-ayushi")

    
    filepath = argv[1]
    gcp.upload_file_cloudstorage(filepath, "gs://test-bucket-ayushi")


if __name__ == "__main__":
    main()