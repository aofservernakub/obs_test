from obs import ObsClient
import configparser
import os


def callback(transferredAmount, totalAmount, totalSeconds):
    # Calculate the average upload rate in KB/s.
    average_upload_rate_kb_per_s = transferredAmount / (totalSeconds * 1024)
    print(average_upload_rate_kb_per_s)
    
    # Calculate the upload progress in percentage.
    upload_progress_percent = (transferredAmount / totalAmount) * 100
    print(upload_progress_percent)

def main() :
    conf = configparser.ConfigParser()
    conf.read('config.ini')

    obs_credentials = dict(conf.items('OBS'))
    print(obs_credentials)

    bucket_name = obs_credentials['bucketname']

    # Create an instance of ObsClient.
    obs_client = ObsClient(
        access_key_id=obs_credentials['ak'],    
        secret_access_key=obs_credentials['sk'],    
        server=obs_credentials['endpoint']
    )
    
    # path = os.getcwd()
    files = os.listdir("test/")
    files_xlsx = [f for f in files if f[-3:] == 'csv' and not f.startswith('~')]


    for i in files_xlsx:    
        print("objectKey", "test_uploadbq/"+i)
        print("file_path","test\\"+i,)
  
        # Upload the file and get the response.
        res_upload = obs_client.putFile(
            bucketName=bucket_name,
            objectKey="test_uploadbq/"+i,
            file_path="test\\"+i,
            progressCallback=callback
        )

        if res_upload.status == 200:
            print("File has been uploaded successfully!")
        else:
            raise Exception("Upload failed")

if __name__ == '__main__':

    main()
