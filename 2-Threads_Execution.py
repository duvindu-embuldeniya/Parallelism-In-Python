#>>>>>>>>>> Thread Execution <<<<<<<<<< (2)
import time
from threading import Thread

start = time.time()

def prepareEggs():
    print(f"Preparing Eggs")
    time.sleep(3)
    print(f"Eggs Prepared")

def makeTea():
    print(f"Preparing Tea")
    time.sleep(2)
    print(f"Tea Prepared")

def applyButter():
    print(f"Applying Butter")
    time.sleep(3)
    print(f"Butter Applied")

def main():
    t1 = Thread(target = prepareEggs)
    t2 = Thread(target = makeTea)
    t3 = Thread(target = applyButter)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end = time.time()
        
    print(f"Total time was {end-start} seconds")


if __name__ == "__main__":
    main()
