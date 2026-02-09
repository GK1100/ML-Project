import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.utils import read_params
from src.logger import logging


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("data", "processed", "train.csv")
    test_data_path: str = os.path.join("data", "processed", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            # 1. Read parameters
            params = read_params()

            raw_data_path = params["data"]["raw_data_path"]
            test_size = params["data"]["test_size"]
            random_state = params["data"]["random_state"]

            # 2. Read raw data (DO NOT modify raw data)
            df = pd.read_csv(raw_data_path)
            logging.info("Raw dataset read successfully")

            # 3. Create processed data directory
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # 4. Train-test split
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(
                df,
                test_size=test_size,
                random_state=random_state
            )

            # 5. Save processed data
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False
            )

            logging.info("Data ingestion completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
