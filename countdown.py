import datetime
def countdown():
	dt1 = datetime.datetime.now()
	dt2 = datetime.datetime(2021,7,24)
	dt3 = dt2 - dt1
	days = dt3.days + 2
	
	str_days = "今日はETA-" + str(days) + "。\n令和市が消滅するまであと" + str(days) +"日だよ"
	return str_days