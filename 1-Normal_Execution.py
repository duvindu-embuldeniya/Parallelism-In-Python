#>>>>>>>>>> Normal Execution <<<<<<<<<< (1)
import time

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
    prepareEggs()
    makeTea()
    applyButter()

    end = time.time()
    print(f"Total time was {end-start} seconds")


if __name__ == "__main__":
    main()
