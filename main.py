def solve():
    # Read number of test cases
    T = int(input())

    for case_num in range(1, T + 1):
        # Read number of activities
        N = int(input())

        activities = []
        for i in range(N):
            # Read (Start time, End time) of the i-th activity
            Si, Ei = map(int, input().split())
            activities.append((Si, Ei, i))

        # Sort activities by their start time
        activities.sort()

        # End times for Loraine (C) and Charles (J)
        loraine_end = 0
        charles_end = 0
        result = [''] * N  # Result for each activity

        possible = True
        for start, end, index in activities:
            #  The activity can be assigned to a person if their end time is earlier than the activity’s start time
            if start >= loraine_end:
                # Assign to Loraine (C)
                result[index] = 'C'
                loraine_end = end
            elif start >= charles_end:
                # Assign to Charles (J)
                result[index] = 'J'
                charles_end = end
            else:
                # Neither can take the task, it's impossible
                possible = False
                break

        # Output the result for this case
        if possible:
            print(f"Case #{case_num}: {''.join(result)}")
        else:
            print(f"Case #{case_num}: IMPOSSIBLE")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()
