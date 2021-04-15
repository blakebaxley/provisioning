# E11y Provisioning POC 
This is a basic first swing at a POC for e11y account using skeema for schema creation 
We still need to add a global call (if needed) and a call to the PDDB endpoint on the proxy, but there is prior art for all of that

## Setup

1. Install pyenv and pyenv-virtualenv from Homebrew. *(per the Brew install output, you will need to modify your ```.bash_profile``)*
2. Install python 3.8.0: ```pyenv install 3.8.0```
3. Install MySQL: ```brew install mysql```
4. Configure the user and grants: ```CREATE USER 'skeema'@'localhost' IDENTIFIED BY 'Pardot07'; GRANT ALL ON *.* to 'skeema'@'localhost'; FLUSH PRIVILEGES;```
5. Install Skeema from Homebrew: ```brew install skeema/tap/skeema```
6. Create a virtualenv for e11y: ```pyenv virtualenv 3.8.0 e11y2```
7. Clone this repo: ```git clone git@github.com:blakebaxley/provisioning.git```
8. Configure the virtual environment: ```cd top/level/of/this/project; pyenv local e11y2``` *(this will automatically activate the e11y virtual environment whenever you enter this directory)*
9. Install requirements: ```cd provisioning; pip install -r requirements.txt --ignore-installed```
10. Initialize Skeema: ```cd ../skeema_files; skeema init -u skeema -pPardot07 -h localhost```

## Running the app

In a separate terminal window, cd to the provisioning folder (where this file is)

```python app.py```

## Testing the API
In a separate terminal window, make a post to the endpoint, and check to see if a new schema was created in the database

```curl -i -H "Content-Type: application/json" -X POST -d '{"sName":"54552"}' http://localhost:5000/e11y/api/createSchema```

Then drop all the tables with the deprovisioning call

```curl -i -H "Content-Type: application/json" -X POST -d '{"sName":"54552"}' http://localhost:5000/e11y/api/deleteSchema```

