# Carbon Market
Data Science For All

Carbon-Market analysis project

# Table of contents
1. [Web App URL](#webappurl)
2. [GitHub repository](#github)
3. [Documents and reports URL](#documents)
4. [Notebooks URL](#notebooks)
5. [Datasets URL](#datasets)
6. Project and source code
   1. [Runtime settings](#runtime)
      1. [Environment variables](#variables)
   2. [Software requirements](#requirements)
      1. [Build dependencies](#dependencies)
      2. [Project dependencies](#projectdependencies)
   3. [Clone](#clone)
   4. [Install requirements](#installrequirements)
   5. [Test, coverage and package](#test)
   6. [List tasks](#listtasks)
   7. [Run the dash app](#runapp)
   8. [Create the docker image](#createdockerimg)
   9. [Run using docker](#rundocker)
   10. [Push docker image to Azure repository](#pushimagetoregistry)

## Web App URL <a name="webappurl"></a>
https://carbon-market-analysis.azurewebsites.net/

## GitHub repository <a name="github"></a>
https://github.com/apinzonf/ds4a-carbon-market-project

## Documents and reports URL <a name="documents"></a>
https://github.com/apinzonf/ds4a-carbon-market-project/tree/main/documents

## Notebooks URL <a name="notebooks"></a>
https://github.com/apinzonf/ds4a-carbon-market-project/tree/main/notebooks

## Datasets URL <a name="datasets"></a>
https://github.com/apinzonf/ds4a-carbon-market-project/tree/main/data

## Runtime settings <a name="runtime"></a>

| Property | Value      |
|----------|------------|
| Runtime  | Python 3.7 |

### Environment variables <a name="variables"></a>

| Key     | Value |
|---------|-------|
| VERSION | 1.0.0 |

## Software requirements <a name="requirements"></a>
- python >= 3.7
- pip

### Build dependencies <a name="dependencies"></a>
- doit (Python automation tool https://pydoit.org/)
- docker (optional, to create the docker image) 

### Project dependencies <a name="projectdependencies"></a>
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

## Clone <a name="clone"></a>
Clone from Gitub

```bash
git clone https://github.com/apinzonf/ds4a-carbon-market-project.git
```

## Install requirements <a name="installrequirements"></a>
```bash
cd ds4a-carbon-market-project
pip install -r requirements.txt
``` 

## Test, coverage and package <a name="test"></a>
```bash
cd ds4a-carbon-market-project
doit
```

## List tasks <a name="listtasks"></a>
```bash
doit list
```

## Run the dash app <a name="runapp"></a>
```bash
cd ds4a-carbon-market-project/
python app.py
```

## Create the docker image <a name="createdockerimg"></a>
```bash
cd ds4a-carbon-market-project/
doit create_docker_image 
```

## Run using docker <a name="rundocker"></a>
```bash
docker run --rm -p 8050:8050 ds4a-carbon-market-project 
```

## Push docker image to Azure repository <a name="pushimagetoregistry"></a>
```bash
doit push_docker_image --registry apinzonf.azurecr.io
```
apinzonf.azurecr.io is a private repository only used here as an example
