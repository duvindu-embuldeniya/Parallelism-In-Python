# >>>>>>>>>> Events In Async/Await <<<<<<<<<< (8)
import asyncio

async def worker(event):
    print(f"Inside worker function")
    await event.wait()
    # await asyncio.sleep(2)
    print(f"Outside worker function")

async def main():
    
    #create an event
    event = asyncio.Event()

    #create our task
    task = asyncio.create_task(worker(event))

    #wait for some time
    await asyncio.sleep(2)

    #say now it's ok to run
    event.set()

    #await our co-routine
    await task
    

if __name__ == "__main__":
    asyncio.run(main())