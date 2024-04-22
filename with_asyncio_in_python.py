import time
import asyncio


async def washClothes():
    print("Start washClothes()")
    await asyncio.sleep(4)
    print("End washClothes()")
    return "Clothes are washed!"

async def doDishes():
    print("Start doDishes()")
    await asyncio.sleep(3)
    print("End doDishes()")
    return "Dishes are washed!"

async def main():
    start_time = time.time()

    batch = asyncio.gather(washClothes(), doDishes())
    result_clothesWashed, result_dishesWashed = await batch

    # clothes_task = asyncio.create_task(washClothes())
    # dishes_task = asyncio.create_task(doDishes())
    # result_clothesWashed = await clothes_task
    # result_dishesWashed = await dishes_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of clothes washed: {result_clothesWashed}")
    print(f"Result of dishes washed: {result_dishesWashed}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())