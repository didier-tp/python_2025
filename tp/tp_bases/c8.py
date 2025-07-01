import datetime

date_naissance=datetime.datetime(year=1969,month=7,day=11)
s_date_naissance = date_naissance.strftime("%A %Y-%m-%d")
print("je suis né le " , s_date_naissance)