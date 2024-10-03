import zipfile
import pathlib 


def make_archive(filepaths, dest_dir):
    dest_path=pathlib.Path(dest_dir, 'compressed.zip')
    with  zipfile.ZipFile(dest_path,'w')  as archive:
          # use 'w' mode to create a new zipped file and use mode 'r' to extract a zipped file
        
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
             
if __name__=='__main__':
    make_archive(filepaths=[""],dest_dir='dest') # add your own filepath here
    
