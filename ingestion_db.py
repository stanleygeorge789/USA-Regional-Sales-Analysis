    import pandas as pd
    import os
    from sqlalchemy import create_engine
    import logging
    import time
    
    logging.basicConfig(
        filename="logs/ingestion_db.log",
        level=logging.DEBUG,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    engine = create_engine ('sqlite:///inventory.db')
    
    def ingest_db (df, table_name, engine):
        '''this func will  ingest DF into DB table'''
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
    def load_raw_data():
        '''this func will load CSVs as DF and ingest to DB'''
        start = time.time()
        for file in os.listdir('.'):
            if file.endswith('.csv'):
                df = pd.read_csv(file)
                logging.info(df.shape)
                ingest_db(df, file[:-4], engine)
        end = time.time()
        total_time = (end - start)/60 
        logging.info ('----------Ingestion Complete----------')
        logging.info (f'\nTotal time taken: {total_time} minutes')
    
    if __name__ == '__main__':
        load_raw_data()