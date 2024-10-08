import time

default_time = 60


def training_session(rounds):
    time_per_round = default_time

    def adjust_time(new_time):
        nonlocal time_per_round
        time_per_round = new_time
        print(f"\nRound time changed to {time_per_round} minutes.")

    for round in range(1, rounds + 1):
        print(f"\n––– Round {round} –––")
        print(f"Round time: {time_per_round} minutes")

        for second in range(2, 0, -1):
            time.sleep(1)

        print("\nThe round is complete!")

        if round < rounds:
            change = input("\nWant to change the time for the next round? (y/n): ").lower()
            if change == 'y':
                try:
                    new_time = int(input("Enter new time in minutes: "))
                    adjust_time(new_time)
                except ValueError:
                    print("Invalid value entered. Time remains unchanged.")

    print("\nTraining is complete!")


num_rounds = int(input("Enter the number of training rounds: "))
training_session(num_rounds)
