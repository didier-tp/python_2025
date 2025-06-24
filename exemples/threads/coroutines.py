import asyncio
import time

async def r42_after_500ms():
    await asyncio.sleep(1)
    return "42"

async def l2():
    print(await r42_after_500ms())  # will print "42".

async def simple_print(msg):
    print(msg)    

asyncio.run(l2())

asyncio.run(simple_print("welcome"))

def my_async_run(coroutine):
    #sort of new REPL (Read-Eval-Print-Loop)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)
    #... plus ... finalisation...

my_async_run (simple_print("welcome"))  

async def upper_after_delay(s,delay=1):
    await asyncio.sleep(delay)
    return s.upper()

async def in_specific_order():
    print(f"in_specific_order() started at {time.strftime('%X')}")
    s1 = await upper_after_delay("ile-de-",2)
    print(f"s1={s1}")
    s2 = await upper_after_delay("france",2)
    s3= s1+s2
    print(f"s2={s2} s3={s3}")
    print(f"in_specific_order() finished at {time.strftime('%X')}")

async def in_same_time():
    print(f"in_same_time() started at {time.strftime('%X')}")
    task1 = asyncio.create_task( upper_after_delay("ile-de-",2))
    task2 = asyncio.create_task(upper_after_delay("france",2))
    s1 = await task1
    print(f"s1={s1}")
    s2 = await task2
    #NB: TaskGroup pour attendre en meme temps fin de task1 et task2 : à partir seulement de  python 3.11
    s3= s1+s2
    print(f"s2={s2} s3={s3}") 
    print(f"in_same_time() finished at {time.strftime('%X')}")  
  

asyncio.run(in_specific_order())
asyncio.run(in_same_time())