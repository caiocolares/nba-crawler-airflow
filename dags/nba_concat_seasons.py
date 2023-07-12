from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from os.path import isfile
import pandas as pd
from datetime import datetime

with DAG(
    "nba_concat_seasons", 
    start_date=datetime(2000, 1, 1),
    schedule=None, # Don’t schedule, use for exclusively “externally triggered” DAGs
    description="Nba concat seasons in base path",
    tags=['NBA', 'Crawler', 'Statistics']
) as dag:
    
    base_path = 'data_lake/nba'

    columns = ['year', 'name', 'playerId', 'playerSlug', 'positionId', 'teamId', 'status', 'gamesPlayed', 
        'avgMinutes', 'avgFouls', 'flagrantFouls', 'technicalFouls', 'ejections', 'doubleDouble', 'tripleDouble', 
        'minutes', 'rebounds', 'fouls', 'avgRebounds', 'avgPoints', 'avgFieldGoalsMade', 'avgFieldGoalsAttempted', 
        'fieldGoalPct', 'avgThreePointFieldGoalsMade', 'avgThreePointFieldGoalsAttempted', 'threePointFieldGoalPct', 
        'avgFreeThrowsMade', 'avgFreeThrowsAttempted', 'freeThrowPct', 'avgAssists', 'avgTurnovers', 'points',
        'fieldGoalsMade', 'fieldGoalsAttempted', 'threePointFieldGoalsMade', 'threePointFieldGoalsAttempted', 
        'freeThrowsMade', 'freeThrowsAttempted', 'assists', 'turnovers', 'avgSteals', 'avgBlocks', 'steals', 'blocks',
        'position', 'birthdate', 'college', 'draftinfo', 'birthplace', 'team', 'htwt', 'experience', 'rankingSalary', 'salary']

    @task()
    def concat_file():
        df = pd.DataFrame(columns=columns)
        for y in range(1999, datetime.now().year):
            filename = '{}/season_{}_{}/infos.csv'.format(base_path, y, y + 1)
            if isfile(filename):
                df_temp = pd.read_csv(filename)
                df = pd.concat([df, df_temp], ignore_index=True)
        df.sort_values(by=['playerId', 'year'], inplace=True)
        df.to_csv(base_path + '/nba_concat_seasons.csv', index=False)

    concat_file()

if __name__ == "__main__":
    dag.test()