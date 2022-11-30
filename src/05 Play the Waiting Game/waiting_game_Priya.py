import time
import random

def waiting_game():
    target = random.randint(2, 4)  
    print(f'\nYour target time is {target} seconds')

    input('Press Enter to Begin ')
    start = time.perf_counter()

    input(f'\nPress Enter again after {target} seconds')
    end = time.perf_counter() - start

    print(f'\nElapsed time: {end :.3f} seconds')
    if end == target:
        print('(Unbelievable! Perfect timing!)')
    elif end < target:
        print(f'({target - end :.3f} seconds too fast)')
    else:
        print(f'({end - target :.3f} seconds too slow)')


# commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
