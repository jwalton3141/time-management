## About

This repo contains code to assist in time-management related tasks carried-out
as part of my role at [Jumping Rivers Ltd](https://www.jumpingrivers.com/about/).

[`time-planner/report.Rmd`](timesheet/report.Rmd) uses events from my Google
Calendar to summarise my upcoming and scheduled client and project work. This
report is deployed to https://jr-jack.jmpr.io/planner/ (viewable only by
Jumping Rivers employees) and is update hourly.

[`time-sheet/report.Rmd`](time-sheet/report.Rmd) uses daily "clocked on" and
"clocked off" events from my Google Calendar to assess my working patterns.
This report is deployed to https://jr-jack.jmpr.io/timesheet/ and is updated
hourly.

## Input data

The data summarised in the generated reports come from events added to my
Google Calendar. An example of what this input looks like is given below
(client names have been sanitised).

![Input data](/examples/input-data.png?raw=true "Events from Google Calendar provide
the source of information for the generated reports.")

## Planner report

This report summarises the upcoming time I have allotted to projects on a
week-by-week basis.

![Planner report](/examples/timeplanner-report.png?raw=true "This report uses
my calendar to summarise the time I've allotted to projects.")

## Timesheet report

This report summarises my working patterns over various time-periods.

![Timesheet report](/examples/timesheet-report.png?raw=true "This report uses
my calendar to inspect my working patterns.")


## Tests

Tests can be run via

```
poetry run test
```