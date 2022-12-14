# WebEng22_Full-Stack-Comrades

### UniView Website

#### Functionality Requirements Report is at the link below -> 
https://docs.google.com/spreadsheets/d/1GqqP_t0dQVbJOB64EJoC6flGX8PWPmG5JRZP1xR_mP8/edit?usp=sharing

###### Project Environment Setup

- Create a virtual Python environment:\
```pip install virtualenv```

- Navigate towards project root and create the vEnv:\
```virtualenv flask```

- Activate before installing packages (you must always activate your environment before working on your project):\
```source flask/bin/activate```

- For Windows:\
```Set-ExecutionPolicy RemoteSigned```
```flask\Scripts\activate```
```Set-ExecutionPolicy Restricted```

- Install Flask and corresponding useful libraries:\
```pip install Flask```\
```pip install pandas```\
```pip install numpy```

- Install the project dependencies. The command below generates the  *requirements.txt* file:\
```pip freeze > requirements.txt```
___
###### Generated *requirements.txt* file must contain the following packages:
- certifi==2021.10.8
- click==8.0.3
-  Flask==2.0.2
-  itsdangerous==2.0.1
-  Jinja2==3.0.3
-  MarkupSafe==2.0.1
-  numpy==1.21.2
-  pandas==1.3.5
-  python-dateutil==2.8.2
-  pytz==2021.3
-  six==1.16.0
-  Werkzeug==2.0.2

###### Install the packages:
```pip install -r requirements.txt```

#### You are Set!
___

###### How to run:

- Set global variable for the project:\
```export FLASK_APP=WebEng22_Full-Stack-Comrades```
- For Windows:\
```powershell```
```$env:FLASK_APP = "__init__.py"```

- Install more things
```pip install Flask-SQLAlchemy```
```pip install requests```
```pip install flask_login```

- Navigate to the folder **containing** the *WebEng22_Full-Stack-Comrades* project and execute:\
```flask run```
___

## License

MIT
