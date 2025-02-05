# >>>>>>>>>> Async/Await TaskGroup Execution <<<<<<<<<< (4)
import time
import asyncio

start = time.time()

async def prepareEggs():
    print(f"Preparing Eggs")
    await asyncio.sleep(3)
    print(f"Eggs Prepared")
    return f"Eggs are ready!!!"

async def makeTea():
    print(f"Preparing Tea")
    await asyncio.sleep(2)
    print(f"Tea Prepared")
    return f"Tea are ready!!!"

async def applyButter():
    print(f"Applying Butter")
    await asyncio.sleep(3)
    raise Exception("Tea 404")
    print(f"Butter Applied")
    return f"Bread Is Ready!!!"


async def main():
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks.append(tg.create_task(prepareEggs()))
            tasks.append(tg.create_task(makeTea()))
            tasks.append(tg.create_task(applyButter()))
    
    except Exception as ex:
        print(ex, type(ex))

    try:
        for task in tasks:
            print(task.result())

    except Exception as ex:
        print(ex, type(ex))

    end = time.time()
    print(end - start)

if __name__ == "__main__":
    asyncio.run(main())
