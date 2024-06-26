import cProfile
import time

def api_call():
    time.sleep(2)
    return None

def process_data():
    for i in range(10**7):
        pass

def sort_data():
    for i in range(10**8):
        pass

    process_data()

def reload_data():
    process_data()
    sort_data()
    time.sleep(2)

def main():
    api_call()
    sort_data()
    reload_data()

if __name__ == '__main__':
    print("Timing program.......")
    #cProfile.run('main()', sort='cumtime')
    cProfile.run('main()', sort='tottime') # shows which function took longer to run

