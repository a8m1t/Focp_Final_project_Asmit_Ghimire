import sys

def analyze_cat_shelter_log(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        other_cats = 0
        total_time_in_house = 0
        durations = []

        for line in lines:
            if line.strip() == "END":
                break

            data = line.strip().split(',')
            cat_name, entry_time, exit_time = data

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            if cat_name == "OURS":
                cat_visits += 1
                total_time_in_house += exit_time - entry_time
                durations.append(exit_time - entry_time)
            else:
                other_cats += 1

        # Calculate average, longest, and shortest visit durations for our cat
        if cat_visits > 0:
            avg_duration = sum(durations) / len(durations)
            longest_duration = max(durations)
            shortest_duration = min(durations)
        else:
            avg_duration = longest_duration = shortest_duration = 0

        # Format total time in hours and minutes
        total_hours = total_time_in_house // 60
        total_minutes = total_time_in_house % 60

        # Display analysis results
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {other_cats}\n")
        print(f"Total Time in House: {total_hours} Hours, {total_minutes} Minutes\n")
        print(f"Average Visit Length: {int(avg_duration)} Minutes")
        print(f"Longest Visit:        {longest_duration} Minutes")
        print(f"Shortest Visit:       {shortest_duration} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{filename}"!')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        analyze_cat_shelter_log(sys.argv[1])
