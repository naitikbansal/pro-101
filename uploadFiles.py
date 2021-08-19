import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        

        for  root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path= os.path.relpath(local_path,file_from)
                dropbox_path= os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token='sl.A210pKOy7ATMsHi6imUULu_06j-810ntkX9obEFMw-U8trSK0Roh17g1MzlnMGCb8LtV0-BWISEmGPZtwdW9_Q_OcJ6At49Ba_lUEh0Y7k4hlDp2wGMezLinEDmGWh11AsaXHog'
    transferData=TransferData(access_token)

    file_from=str(input("Enter the folder path to transfer: "))
    file_to=input("Enter the full path to upload to dropbox: ")


    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
        