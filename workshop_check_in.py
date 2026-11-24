# JJSpectre
# Coursework project, UNC Charlotte (Fall 2026)
#
# Workshop Check-In Tool
# Checks students in at the door of a workshop on campus. Compares
# each arriving student against the RSVP list, keeps track of walk-ins and a
# waitlist when the room fills up, and prints an attendance report at the end.

# Check-In Rules
# Inputs: workshop name (str), room capacity (int), then arriving students'
#         names one at a time (str) until the user types "done"
# Given: rsvp_text (str), the RSVP names exported by the Outreach team,
#        separated by commas
#
# Valid Input:
#   room capacity is 1 or more    -> continue
#   room capacity is less than 1  -> show an error and stop
#
# Cleaning Names (applies to every RSVP name and every name typed in):
#   remove extra spaces at the start and end, then capitalize each word
#   ("  ava smith " -> "Ava Smith"), so the same person always matches
#
# Each Arriving Student (checked in this order, the first match wins):
#   name is blank                          -> ask for a name, nothing changes
#   already checked in or a walk-in        -> say they are already checked in
#   already on the waitlist                -> say they are already on the waitlist
#   room is full                           -> add them to the waitlist
#   name is on the RSVP list               -> add them to the checked-in list
#   anything else                          -> add them to the walk-in list
#
# Attendance Rate:
#   (RSVP'd students who checked in / students on the RSVP list) * 100,
#   rounded to 1 decimal place. If the RSVP list is empty, the rate is 0.0.


# Provided RSVP List
# Exported from the RSVP form. 
# DO NOT CHANGE THIS LINE.
rsvp_text = "ava smith, Ben Lee,  CARLA DIAZ , eli jones, Ava Smith, maya chen,, Noah Brooks , priya patel, axel rodrigueZ, Sam Rivera"

# Add your code here:

# Remove surrounding spaces and standardize capitalization so names match.
def clean_name(name):
    return name.strip().title()


# Convert the comma-separated text into a list of unique, cleaned RSVP names.
def parse_rsvp_list(rsvp_text):
    rsvp_list = []

    for name in rsvp_text.split(","):
        name = clean_name(name)

        # Skip empty entries and names already added to the list.
        if name != "" and name not in rsvp_list:
            rsvp_list.append(name)

    return rsvp_list


# Build a new list of RSVP students who were not admitted.
# The original RSVP and checked-in lists remain unchanged.
def find_no_shows(rsvp_list, checked_in):
    no_shows = []

    for name in rsvp_list:
        if name not in checked_in:
            no_shows.append(name)

    return no_shows


# Calculate the percentage of RSVP students who checked in.
# Walk-ins are excluded because they did not RSVP.
def attendance_rate(num_checked_in, num_rsvps):
    # Avoid division by zero when the RSVP list is empty.
    if num_rsvps == 0:
        return 0.0

    return round((num_checked_in / num_rsvps) * 100, 1)


# Collect the workshop information and convert capacity to an integer.
workshop_name = input("Enter workshop name: ")
capacity = int(input("Enter room capacity: "))

# Only begin check-in when the room capacity is valid.
if capacity < 1:
    print("Error: Room capacity must be 1 or more.")
else:
    rsvp_list = parse_rsvp_list(rsvp_text)

    # Keep RSVP arrivals, walk-ins, and waiting students in separate lists.
    checked_in = []
    walk_ins = []
    waitlist = []

    name = clean_name(input("Enter student name (done to finish): "))

    # Continue accepting students until "done" is entered in any capitalization.
    while name.lower() != "done":
        if name == "":
            print("Please enter a name.")

        # Check duplicates before capacity so admitted students cannot
        # also be placed on the waitlist when the room is full.
        elif name in checked_in or name in walk_ins:
            print("Already checked in.")
        elif name in waitlist:
            print("Already on the waitlist.")

        # Both RSVP arrivals and walk-ins occupy seats.
        elif len(checked_in) + len(walk_ins) >= capacity:
            waitlist.append(name)
            print("Added to waitlist.")

        # With space available, admit the student into the appropriate list.
        elif name in rsvp_list:
            checked_in.append(name)
            print("Admitted as an RSVP.")
        else:
            walk_ins.append(name)
            print("Admitted as a walk-in.")

        # Ask again after every outcome, including blank or repeated names.
        name = clean_name(input("Enter student name (done to finish): "))

    # Calculate the report values after check-in ends.
    # Waitlisted students are excluded from room occupancy.
    no_shows = find_no_shows(rsvp_list, checked_in)
    rate = attendance_rate(len(checked_in), len(rsvp_list))
    occupancy = len(checked_in) + len(walk_ins)

    # Alphabetize the report lists, but preserve waitlist arrival order.
    checked_in.sort()
    walk_ins.sort()
    no_shows.sort()

    print()
    print("Workshop:", workshop_name)
    print("Room occupancy:", occupancy, "of", capacity)

    # Show each list's count and comma-separated names.
    # Display "None" when a list is empty.
    if len(checked_in) == 0:
        print("Checked in (0): None")
    else:
        print("Checked in (" + str(len(checked_in)) + "): "
              + ", ".join(checked_in))

    if len(walk_ins) == 0:
        print("Walk-ins (0): None")
    else:
        print("Walk-ins (" + str(len(walk_ins)) + "): "
              + ", ".join(walk_ins))

    if len(no_shows) == 0:
        print("No-shows (0): None")
    else:
        print("No-shows (" + str(len(no_shows)) + "): "
              + ", ".join(no_shows))

    if len(waitlist) == 0:
        print("Waitlist (0): None")
    else:
        print("Waitlist (" + str(len(waitlist)) + "): "
              + ", ".join(waitlist))

    print("Attendance Rate: " + str(rate) + "%")
