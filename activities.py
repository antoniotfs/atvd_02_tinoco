import os
import pandas as pd
from temporalio import activity
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

@activity.defn
async def generate_csv_activity() -> str:
    from generate_fake_csv import main
    main()
    return "data/raw/orders_fake_10mb.csv"

@activity.defn
async def load_to_mongo(csv_path: str) -> str:
    uri = os.getenv("MONGODB_URI")
    client = MongoClient(uri)
    db = client[os.getenv("MONGODB_DATABASE", "dataops_lab")]
    col = db[os.getenv("MONGODB_COLLECTION", "orders_raw")]
    
    df = pd.read_csv(csv_path)
    col.delete_many({})
    col.insert_many(df.to_dict("records"))
    return f"Sucesso: {len(df)} registros foram processados e inseridos no banco de dados."