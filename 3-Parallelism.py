# >>>>>>>>>> Async/Await Batch & single_task Execution <<<<<<<<<< (3)
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
    print(f"Butter Applied")
    return f"Bread Is Ready!!!"

async def main():

    # >>>>> batch approach <<<<< (3.1)
    batch = asyncio.gather(prepareEggs(), makeTea(), applyButter())
    eggResult, teaResult, butterResult = await batch

    print(eggResult)
    print(teaResult)
    print(teaResult)

    # >>>>> single task approach <<<<< (3.2)
    eggTask = asyncio.create_task(prepareEggs())
    teaTask = asyncio.create_task(makeTea())
    butterTask = asyncio.create_task(prepareEggs())

    eggResult = await eggTask
    teaResult = await teaTask
    butterResult = await butterTask

    print(eggResult)
    print(teaResult)
    print(butterResult)

    end = time.time()
        
    print(f"Total time was {end-start} seconds")


if __name__ == "__main__":
    asyncio.run(main())
