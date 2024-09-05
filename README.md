## Plan

**Sorting:** Sort the activities by their start times to check overlapping in a greedy manner.

**Greedy Algorithm:**
Maintain 2 variables for 2 people track when they are next available.

- Assign to a person if the next available is earlier than the activity's start time.
- Repeat check next person available time.
- Exit if no person have next available time is earlier than the activity time

**Output:**
- Valid case: all activities can be assigned
- Impossible case: any activity failed to be assigned