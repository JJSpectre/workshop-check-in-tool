# Workshop Check-In Tool

A Python tool for checking students in at the door of a campus tech workshop. It matches each arriving student against the RSVP list, admits walk-ins while seats are open, starts a waitlist once the room is full, and prints an attendance report when check-in ends.

Built for ITSC 1212 (Project 3) at UNC Charlotte. The scenario: staff were checking names off a printed list by hand, so names got misspelled, people were counted twice, and nobody knew how many seats were left.

## How to run it

1. Install [Python 3](https://www.python.org/downloads/)
2. Download `workshop_check_in.py`
3. Open a terminal in that folder and run:

```
python workshop_check_in.py
```

Enter the workshop name and room capacity, then type each student's name as they arrive. Type `done` to finish and see the report.

## Example

Workshop "Intro to Python" with a capacity of 4. Arrivals, in order: `  ava smith `, `BEN LEE`, `Dev Patel`, `ava smith` again, a blank entry, `carla diaz`, `Jordan Kim`, then `done`.

```
Admitted as an RSVP.
Admitted as an RSVP.
Admitted as a walk-in.
Already checked in.
Please enter a name.
Admitted as an RSVP.
Added to waitlist.

Workshop: Intro to Python
Room occupancy: 4 of 4
Checked in (3): Ava Smith, Ben Lee, Carla Diaz
Walk-ins (1): Dev Patel
No-shows (6): Axel Rodriguez, Eli Jones, Maya Chen, Noah Brooks, Priya Patel, Sam Rivera
Waitlist (1): Jordan Kim
Attendance Rate: 33.3%
```

Messy input like `  ava smith ` and `BEN LEE` still matches the RSVP list, a repeat arrival isn't counted twice, and once the room hits capacity the next person goes to the waitlist.

## How it works

**Cleaning names.** The RSVP export is one messy line of text with extra spaces, mixed capitalization, blank entries, and duplicates. `clean_name()` strips the spaces and capitalizes each word, and `parse_rsvp_list()` splits the text on commas and keeps only unique, non-blank names, which leaves 8 students.

**Check-in rules**, checked in order (the first match wins):

1. Blank name: ask for a name
2. Already checked in or a walk-in: say so, don't count them again
3. Already on the waitlist: say so, don't add them again
4. Room is full: add to the waitlist
5. On the RSVP list: check in as an RSVP
6. Anything else: check in as a walk-in

Duplicates are checked before capacity, so someone who's already in the room can't also end up on the waitlist.

**Loops.** A `for` loop goes through the RSVP names because that list's length is known ahead of time. A `while` loop runs check-in because there's no way to know how many students will show up before someone types `done`.

**The report.** The checked-in, walk-in, and no-show lists are sorted alphabetically. The waitlist stays in arrival order, since that's the order people get let in. The attendance rate counts only RSVP'd students who checked in, and returns 0.0 if the RSVP list is empty, so it never divides by zero.

## How I built it

- Wrote the check-in rules as comments at the top of the file before writing any code
- Planned the program flow with a flowchart
- Split the work into four functions: `clean_name()`, `parse_rsvp_list()`, `find_no_shows()`, and `attendance_rate()`
- Tested every check-in rule plus edge cases: a room filling exactly to capacity, a student arriving twice, a waitlisted student arriving again, a messy RSVP name, everyone showing up, nobody showing up, and an invalid capacity
