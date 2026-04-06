import asyncio
from temporalio.client import Client
from app.workflows import OrdersWorkflow

async def main():
    client = await Client.connect("localhost:8081")
    result = await client.execute_workflow(
        OrdersWorkflow.run, id="order-job-1", task_queue="orders-queue"
    )
    print(f"Processo finalizado com o seguinte status: {result}")

if __name__ == "__main__":
    asyncio.run(main())