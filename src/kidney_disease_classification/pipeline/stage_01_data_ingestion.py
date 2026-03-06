from kidney_disease_classification.config.configuration import ConfigurationManager
from kidney_disease_classification.components.data_ingestion import DataIngestion
from kidney_disease_classification import logger
from pathlib import Path

STAGE_NAME='Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager(
        config_filepath=Path("config/config.yaml"),
        params_filepath=Path("params.yaml")
)

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e