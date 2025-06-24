import asyncio
import time
#import threading # for compare

def day_from_number(day_num):
    day_names=['sunday','monday','tuesday','wednesday','thursday' , 'friday' ,'saturday' , 'sunday']
    time.sleep(0.25) #simulate slow execution or waiting
    return day_names[day_num]

def slow_upper(s):
    time.sleep(0.25)  #simulate slow execution or waiting
    return s.upper()

def slow_upper_dayof_week(day_num):
    dfn= day_from_number(day_num)
    day_of_week_upper=slow_upper(dfn)
    print(f"day_num={day_num}, day_of_week_upper={day_of_week_upper}")


async def day_from_number_async(day_num):
    day_names=['sunday','monday','tuesday','wednesday','thursday' , 'friday' ,'saturday' , 'sunday']
    await asyncio.sleep(0.25) #simulate slow execution or waiting
    return day_names[day_num]

async def slow_upper_async(s):
    await asyncio.sleep(0.25) #simulate slow execution or waiting
    return  s.upper()

async def slow_upper_dayof_week_async(day_num):
    dfn= await day_from_number_async(day_num)
    day_of_week_upper=await slow_upper_async(dfn)
    print(f"day_num={day_num}, day_of_week_upper={day_of_week_upper}")

def some_days_seq():
    start = time.time()
    day_nums=[1,5,3,4,0,6,2,7,1,5,3,4,0,6,2]
    for d in day_nums :
        slow_upper_dayof_week(d)
    end = time.time()
    print(f'Time: {end-start:.2f} sec')  

'''
def some_days_multiple_threads():
    start = time.time()
    day_nums=[1,5,3,4,0,6,2,7,1,5,3,4,0,6,2]
    mes_threads = [threading.Thread(target= slow_upper_dayof_week, args=[d]) for d in day_nums]
    for t in mes_threads :
        t.start()
    for t in mes_threads :
        t.join()
    end = time.time()
    print(f'Multiple thread Time: {end-start:.2f} sec')  
    '''     

def some_days_async():
    start = time.time()
    day_nums=[1,5,3,4,0,6,2,7,1,5,3,4,0,6,2]
    loop = asyncio.new_event_loop()
    tasks=[]
    for d in day_nums :
        tasks.append(loop.create_task(slow_upper_dayof_week_async(d)))
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(f'Async Time: {end-start:.2f} sec')  

async def some_days_async_gather():
    day_nums=[1,5,3,4,0,6,2,7,1,5,3,4,0,6,2]
    await asyncio.gather(*[slow_upper_dayof_week_async(d) for d in day_nums])

def some_days_async_v2():
    start = time.time()
    asyncio.run(some_days_async_gather())
    end = time.time()
    print(f'Async Time v2: {end-start:.2f} sec')      
          


some_days_seq() # Time: 7.52 sec
#some_days_multiple_threads() #Multiple thread Time: 0.51 sec
some_days_async() # Async Time: 0.52 sec
some_days_async_v2() # Async Time: 0.52 sec



