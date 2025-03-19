import uvicorn
import logging
from utils import setup_logger

if __name__ == "__main__":
    logger = setup_logger("blob-service", logging.DEBUG)
    logger.info("CoAI Blob Service Start")
    
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True, 
        log_level="debug",
        log_config=log_config
    )
