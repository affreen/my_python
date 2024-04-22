import time
import asyncio

def washClothes():
    print("Start washClothes()")
    time.sleep(2)
    print("End washClothes()")
    return "Clothes are washed!"

def doDishes():
    print("Start doDishes()")
    time.sleep(3)
    print("End doDishes()")
    return "Dishes are washed!"

def main():
    start_time = time.time()
    result_clothesWashed = washClothes()
    result_dishesWashed = doDishes()
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of clothes washed: {result_clothesWashed}")
    print(f"Result of dishes washed: {result_dishesWashed}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()