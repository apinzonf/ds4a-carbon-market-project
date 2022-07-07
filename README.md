# Carbon Market
Data Science For All

Carbon-Market analysis project

## Runtime settings

| Property | Value      |
|----------|------------|
| Runtime  | Python 3.7 |

### Environment variables

| Key     | Value |
|---------|-------|
| VERSION | 1.0.0 |

## software Requirements
- python >= 3.7
- pip

### Build dependencies
- doit (Python automation tool https://pydoit.org/)
- docker (optional, to create the docker image) 

### Project dependencies
#### Project dependencies
- dash
- plotly
- pandas
- dash_bootstrap_components
- Flask==2.1.2
- pycountry
- waitress
#### Test dependencies
- pytest==7.1.2
#### Build dependencies
- doit==0.34.2
- doit-py>=0.4.0
- mock
#### Coverage
- coverage==6.4.1


### Test and coverage dependencies
- pytest
- mock
- coverage>=4.0

## Clone 
Clone from Gitub

```bash
git clone https://github.com/apinzonf/ds4a-carbon-market-project.git
```

## Install requirements
```bash
cd ds4a-carbon-market-project
pip install -r requirements.txt
``` 

## Test, coverage and package
```bash
cd ds4a-carbon-market-project
doit
```

## List tasks
```bash
doit list
```

## Run the dash app
```bash
cd ds4a-carbon-market-project/
python app.py
```

## Create the docker image
```bash
cd ds4a-carbon-market-project/
doit create_docker_image 
```

## Run using docker 
```bash
docker run --rm -p 8050:8050 ds4a-carbon-market-project 
```

## Push docker image to Azure repository
```bash
doit push_docker_image --registry apinzonf.azurecr.io
```
apinzonf.azurecr.io is a private repository only used here as an example
