import datetime

date1 = datetime.datetime(2025,5,18) # (year,month,day)18 mai 2025
d=maintenant = datetime.datetime.now()
print("date1=",date1) #2025-05-18 00:00:00
print("maintenant=",maintenant) # 2025-05-21 09:47:53.340047 ou autre

print("au format yyyy-mm-dd %Y-%m-%d : " , d.strftime("%Y-%m-%d"))
print("au format dd/mm/yyyy %d/%m/%Y : " , d.strftime("%d/%m/%Y"))

print("avec jour de la semaine : " , d.strftime("%A %Y-%m-%d"))
print("avec heure %H:%M:%S : " , d.strftime("%Y-%m-%d %H:%M:%S"))