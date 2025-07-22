from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(F"stage {STAGE_NAME} Initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(F">>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation"
try:
    logger.info(F"stage {STAGE_NAME} Initiated")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(F">>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer"
try:
    logger.info(F"stage {STAGE_NAME} Initiated")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(F">>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(F"stage {STAGE_NAME} Initiated")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(F">>>>>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<<<<\n")

except Exception as e:
    logger.exception(e)
    raise e