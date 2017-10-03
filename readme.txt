
For Medlars format
Institute for Operations Research and the Management Sciences (INFORMS)


WINDOWS:
    environment:
        pip freeze > requirements.txt
        
        pip install -r requirements.txt.




    virtuallen :
        virtualenv --python=c:\Python27\python.exe venv
        venv\Scripts\activate
    
    python main.py

MAC OSX: 
    virtualenv -p /usr/bin/python2.7 venv 
    source venv/bin/activate 
    pip install -r requirements.txt.
    python main.py