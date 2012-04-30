We have Event objects in our system.

Every event ha a status, this can be:

- 'Assigned'
- 'Sent to staffing agency'
- 'Has responses'
- 'Does not have responses'

We need a linechart showing the number of events in our system every day
within a daterange (day-by-day).

The x axis is the date, the y axis is the number of the events.

There should be 4+1 curves displayed (for each status and +1 for deleted events)
If an event is deleted, then it can be counted only for the "deleted curve",
regardless of its status.

The status field of the Event model represents the current status of the event.
When we render the point of last week for example, we need to calculate the
status of the events for the last week. This can be solved using Activity objects.
There is an Activity object for every event status change, and for every deletion.

These Activity objects are always created in this way:
::

  Activity(
      verb='changed status to %d' % status_number,
      target=event
  ).save()

(status_number will be in [0,1,2,3])

The Activity object for deleting an Event:
::

  Activity(
      user=user,
      verb='deleted an event',
      subject=event
  ).save()

There are no test datas provided for this test.

Tasks:

- Calculate the number of events for every day in the given daterange!
- Show them on a linechart, using grpahael.js (http://g.raphaeljs.com/). There should be 5 curves according to its status:
 
  - 'Assigned' : GREEN
  - 'Sent to staffing agency' : BLUE
  - 'Has responses' : YELLOW
  - 'Does not have responses' : RED
  - 'deleted' : GRAY

  (Please use these color  codes for the curves!)

- Format the x-axis of the chart: there should be dates!
- If start_date is not provided, then use the publish date of the  first event!
- If end_date is not provided, use today!
- Using plain SQL statements are forbidden.

Bonus: make as fast as possible (avoid cycles, use more complicated queries)
