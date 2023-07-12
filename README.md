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
python3 -m venv .venv

source .venv/bin/activate

```

## Environment Variables

```
export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False

AIRFLOW_VERSION=2.6.2

PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

```

Install python depedencies 

```

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip install beautifulsoup4 lxml pandas

```


## Start Project 

```

airflow standalone

```

Get admin password on file `standalone_admin_password.txt`


Access [admin panel](http://localhost:8080)

![image](https://github.com/caiocolares/nba-crawler-airflow/assets/26276218/e59f89d5-7e73-4c15-869e-fbb4650b854b)

![image](https://github.com/caiocolares/nba-crawler-airflow/assets/26276218/e50628a5-d4f7-4259-9754-1c5b2c5d9593)

### Testing the operator directly
![image](https://github.com/caiocolares/nba-crawler-airflow/assets/26276218/b8bd4a52-6541-4cd1-ada0-e8eac02d8c86)

## Tech Stack


**Server:** Airflow, Python, Pandas

## Acknowledgements

- [Airflow](https://airflow.apache.org/)
- [Pandas](https://pandas.pydata.org/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

