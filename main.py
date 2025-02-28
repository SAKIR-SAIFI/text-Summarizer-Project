from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_tranformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = 'Data Tranformation Stage'
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 