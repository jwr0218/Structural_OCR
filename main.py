

from io import StringIO
import os 

from flask_cors import CORS
import Utils
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('')
pre_dir = "./"
stt = 'test'
path = 'sample.mp4'
model = Utils.load_model()

# Appending app path to upload folder path within app root folder

imgDeleted,imgCropped,data = Utils.extract_from_video(model,pre_dir+path)
#stt = Utils.STT(path)
stt = "testing / we are testing this system. Is this work?"
Utils.markdown(path,data,stt,imgCropped)
print("path  :" ,path)
file_loc = os.path.join(os.getcwd() ,'test_220830.md')
print("UPLOADS : ",file_loc)
file_loc
#, mimetype = 'text/md',attachment_filename='PLEASE.md',
#as_attachment = True)
# Returning file from appended path
#return send_from_directory(directory=current_app.root_path , filename= path)

