import schedule
import time
import pd

def click():
    urlfile = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    df = pd.read_csv(urlfile)

schedule.every(10).seconds.do(click())
schedule.every().day.at('01:00').do(click())
while 1:
    schedule.run_pending()
    time.sleep(1)
