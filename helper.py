from google.cloud import storage

class GCPHelper:

    def __init__(self, bucketname):
        self.bucketname = bucketname
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucketname)


    def upload_file_cloudstorage(self, filepath, gcs_path):
        print(f"UPLOAD -> {filepath} , {gcs_path}, {self.bucketname}") 
        blob = self.bucket.blob(gcs_path)
        blob.upload_from_filename(filepath)




    # def download_file_cloudstorage(self):
    #     print("DOWNLOAD")