# >>>>>>>>>> Futures In Async/Await <<<<<<<<<< (9) | Normally handle by modern libraries...
import asyncio

async def worker(future):
    print(f"Inside worker function")
    await asyncio.sleep(2)
    future.set_result("Promissed fulfilled!")
    await asyncio.sleep(2)
    print(f"Outside worker function")

async def main():
    loop = asyncio.get_event_loop()

    #create a future object
    future = loop.create_future()

    #create our task
    task = asyncio.create_task(worker(future))

    #wait for future to be completed
    result = await future
    print(result)

   #await our co-routine
    await task

if __name__ == "__main__":
     asyncio.run(main())







