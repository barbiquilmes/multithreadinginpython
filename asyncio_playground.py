import asyncio

# https://www.youtube.com/watch?v=t5Bo1Je9EmE&t=585s

# # Like this is like a normal sequential function. It waits until foo finishes executing
# async def main():
#     print("Doing in main ...")
#     await foo("Doing other thing")
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")


# # Like this it waits until main is finish to execute foo, and then ends with no waiting sleep in foo
# async def main():
#     print("Doing in main ...")
#     task = asyncio.create_task(foo("Doing other thing"))
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")
#     print(2**2123)


# # Like this it starts executing main, then waits until task is finish and then continues with main
# async def main():
#     print("Doing in main ...")
#     task = asyncio.create_task(foo("Doing other thing"))
#     await task
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")
#     print("Continue doing in main ...")
#     print(2**2123)


# And here is interesting, cause because main has to await something and a task was built.
# That task will be executed as soon as main is finished or as soon as main is 'paused'
async def main():
    print("Doing in main ...")
    task = asyncio.create_task(foo("Doing other thing"))
    # If this was 0.01, then it would print doing something else, but wouldn't wait the second in foo
    # And finished foo will never be printed
    await asyncio.sleep(0.01)
    print("Continue doing in main ...")
    print("Continue doing in main ...")
    print("Continue doing in main ...")
    print(2**2123)
    print("finished main")
    # if I add this now it will give again the access to foo to continue executing
    # await task

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("finished foo")


asyncio.run(main())