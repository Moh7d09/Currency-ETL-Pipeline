from src.extract import get_data
from src.transform import transform_data
from src.load import save_data
from src.analysis import analyze_rates
from src.alert import check_alerts
from apscheduler.schedulers.blocking import BlockingScheduler


def run_pipeline():
    data = get_data()

    if data:

        records = transform_data(data)
        
        # fetch records DB
        save_data(records)

        #analysis
        result = analyze_rates()
        for currency, data in result.items():
            print(currency, "=>", data)
        
        #alert 
        results = analyze_rates()
        check_alerts(results)
        print("Data saved successfully!")

scheduler = BlockingScheduler()

# كل 60 ثانية
scheduler.add_job(run_pipeline, 'cron', hour=9)

print("Automation started ")

scheduler.start()