import random

def check_guess(random_num, guess):
    """Compares random number to current guess. Returns a tuple comprising two
    items: loop status (i.e., continue = True/False) and a corresponding
    message and hint (if appropriate).

    Parameters:
        randum_num (int): random number to match
        guess (int): number provided by user

    Returns:
        tuple: (< status >, < message >)
    """

    if guess < random_num:
        return (True, "Guess incorrect. Provide a HIGHER number.")
    elif guess > random_num:
        return (True, "Guess incorrect. Provide a LOWER number.")
    else:
        return (False, "Guess correct.")


def main():
    """Orchestrates program flow.

    Parameters:
        None

    Returns:
        None
    """

    random_num = random.randint(0, 100) # generate random int between 0-100
    count = 0 # track number of guesses

    while True:
        try:
            guess = int(input('Enter a number between 0 and 100: '))
            status, message = check_guess(random_num, guess) # unpack
            count += 1
            if status:
                print(message) # guess again
            else:
                print(f"{message} Random number = {random_num}. Guess count = {count}.")
                break # exit loop
        except ValueError:
            continue


if __name__ == '__main__':
    main()