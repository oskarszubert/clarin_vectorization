import urllib.request as request
import json
import time
import shutil
import os


class ClarinNlprest2:
    def __init__(self, source_path, save_to_dir, url, user, task='wcrft2'):
        self.user = user
        self.task = task
        self.url = url
        self.source_path = source_path
        self.save_to_dir = save_to_dir


    def upload(self, file):
        with open (file, 'rb') as myfile:
            doc=myfile.read()
        return request.urlopen(request.Request(self.url+'/upload/',doc,{'Content-Type': 'binary/octet-stream'})).read();


    def process(self, data):
            doc=json.dumps(data)
            taskid = request.urlopen(request.Request(self.url+'/startTask/',doc.encode(),{'Content-Type': 'application/json'})).read();
            time.sleep(0.2);

            resp = request.urlopen(request.Request(self.url+'/getStatus/'+taskid.decode('utf-8')));
            data=json.load(resp)
            while data['status'] == 'QUEUE' or data['status'] == 'PROCESSING' :
                time.sleep(0.5);
                resp = request.urlopen(request.Request(self.url+'/getStatus/'+taskid.decode('utf-8')));
                data=json.load(resp)
            if data['status']=='ERROR':
                print('Error ' + data['value']);
                return None;
            return data['value']


    def tokenize_zip_file(self, filename):
        file_id = self.upload(  os.path.join( self.source_path, filename) )
        file_id = file_id.decode('utf-8')
        lpmn='filezip('+ file_id +')|'+self.task+'|dir|makezip'
        data={'lpmn':lpmn,'user':self.user}
        data=self.process(data)

        if data:
            data=data[0]['fileID'];
            content = request.urlopen(request.Request(self.url+'/download'+data)).read();
            with open ( os.path.join(self.save_to_dir, filename), 'wb') as outfile:
                outfile.write(content)


    def tokenize_directory(self):
        for dir in os.listdir(self.source_path):
            print(f'Sending {dir} to clarin-pl.')
            self.tokenize_zip_file(filename=dir)
