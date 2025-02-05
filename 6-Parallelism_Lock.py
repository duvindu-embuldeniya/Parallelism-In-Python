# >>>>>>>>>> Locks In Async/Await <<<<<<<<<< (6)
import time
import asyncio

value = 50
lock = asyncio.Lock()

async def func1():
    async with lock:
        global value
        await asyncio.sleep(2)
        x = 10
        x += value
        return x

async def func2():
    async with lock:
        global value
        value = 55
        return value

async def main():
    t1 = asyncio.create_task(func1())
    t2 = asyncio.create_task(func2())

    result_t1 = await t1
    result_t2 = await t2

    print(result_t1)
    print(result_t2)

if __name__ == "__main__":
    asyncio.run(main())
