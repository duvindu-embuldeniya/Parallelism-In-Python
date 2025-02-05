# >>>>>>>>>> Semaphores In Async/Await <<<<<<<<<< (7)
import asyncio

async def worker(semaphore):
    async with semaphore:
        print(f"Inside worker function")
        await asyncio.sleep(2)
        print(f"Outside worker function")


async def main():

    #semaphore with a maximum of x2 co-routines
    semaphore = asyncio.Semaphore(2)

    #create a list of tasks
    tasks = [worker(semaphore) for _ in range(5)]

    #like batch approach
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
