import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from app.activities import generate_csv_activity, load_to_mongo
from app.workflows import OrdersWorkflow

async def main():
    client = await Client.connect("localhost:8081")
    worker = Worker(
        client, task_queue="orders-queue",
        workflows=[OrdersWorkflow],
        activities=[generate_csv_activity, load_to_mongo]
    )
    print("Serviço de processamento em segundo plano iniciado. Em escuta...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())