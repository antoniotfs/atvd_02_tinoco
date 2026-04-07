import csv
import random
from pathlib import Path
from faker import Faker

def main():
    fake = Faker("pt_BR")
    output_path = Path("data/raw/orders_fake_10mb.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    TARGET_SIZE_BYTES = 10 * 1024 * 1024 # 10MB
    headers = ["order_id", "customer_name", "city", "order_ts", "amount", "status"]
    statuses = ["delivered", "processing", "cancelled"]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        row_count = 0
        while output_path.stat().st_size < TARGET_SIZE_BYTES:
            row_count += 1
            writer.writerow([
                row_count, fake.name(), fake.city(),
                fake.date_time_between(start_date="-90d").strftime("%Y-%m-%d %H:%M:%S"),
                round(random.uniform(10, 5000), 2), random.choice(statuses)
            ])
    print(f"Arquivo CSV gravado em {output_path}. Total de registros: {row_count}.")

if __name__ == "__main__":
    main()