

environment:
    pip freeze > requirements.txt
    
    pip install -r requirements.txt.



virtuallen :
    virtualenv myvenv
    myvenv\Scripts\activate