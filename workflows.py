from datetime import timedelta
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from activities import generate_csv_activity, load_to_mongo

@workflow.defn
class OrdersWorkflow:
    @workflow.run
    async def run(self) -> str:
        path = await workflow.execute_activity(
            generate_csv_activity, start_to_close_timeout=timedelta(minutes=5)
        )
        result = await workflow.execute_activity(
            load_to_mongo, path, start_to_close_timeout=timedelta(minutes=5)
        )
        return result