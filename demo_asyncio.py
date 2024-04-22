import time
import asyncio
async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(1)
    print("End brewCoffee()")
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(2)
    print("End toastBagel()")
    return "Bagel toasted"

async def main():
    start_time = time.time()
    # result_coffee = brewCoffee()
    # result_bagel = toastBagel()

    # demo batch approach of asyncio
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch

    # demo each task
    coffee_task = asyncio.create_task(brewCoffee())
    bagel_task = asyncio.create_task(toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total execution of time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
