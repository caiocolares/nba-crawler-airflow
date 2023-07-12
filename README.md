# NBA Data Crawler - Airflow

Airflow project...

## Authors

- [@caiocolares](https://www.github.com/caiocolares)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file



## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```


Create a python virtualenv 
```
python -m venv .venv

source .venv/bin/activate

```

Define environment variables

```
export AIRFLOW_HOME=$(pwd)

AIRFLOW_VERSION=2.6.2

PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

```

Install python depedencies 

```

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip install lxml
pip install bs4
pip install pandas

```


Start airflow standalone 

```

airflow standalone

```

Get admin password on file `standalone_admin_password.txt`


Access [admin panel](http://localhost:8080)



## Tech Stack


**Server:** Airflow, Python, Pandas