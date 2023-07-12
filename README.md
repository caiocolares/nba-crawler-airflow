# NBA Data Crawler - Airflow

Airflow project...

## Authors

- [@caiocolares](https://www.github.com/caiocolares)



## Run Locally

Clone the project

```bash
  git clone https://github.com/caiocolares/nba-crawler-airflow.git
```

Go to the project directory

```bash
  cd nba-crawler-airflow
```


Create a python virtualenv 
```
python -m venv .venv

source .venv/bin/activate

```

## Environment Variables

```
export AIRFLOW_HOME=$(pwd)

AIRFLOW_VERSION=2.6.2

PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

```

Install python depedencies 

```

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip install beautifulsoup4
pip install lxml
pip install pandas

```


## Start Project 

```

airflow standalone

```

Get admin password on file `standalone_admin_password.txt`


Access [admin panel](http://localhost:8080)

![Login](https://raw.githubusercontent.com/caiocolares/nba-crawler-airflow/main/images/login.png)

![DAG](https://raw.githubusercontent.com/caiocolares/nba-crawler-airflow/main/images/dag.png)

## Tech Stack


**Server:** Airflow, Python, Pandas

## Acknowledgements

- [Airflow](https://airflow.apache.org/)
- [Pandas](https://pandas.pydata.org/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

