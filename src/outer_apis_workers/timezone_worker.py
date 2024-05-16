# curl -X 'GET' \
#   'https://timeapi.io/api/TimeZone/coordinate?latitude=38.9&longitude=-77.03' \
#   -H 'accept: application/json'
#
#
# https://timeapi.io/api/TimeZone/coordinate?latitude=38.9&longitude=-77.03
#
# {
#   "timeZone": "America/New_York",
#   "currentLocalTime": "2024-05-15T22:16:50.5334703",
#   "currentUtcOffset": {
#     "seconds": -14400,
#     "milliseconds": -14400000,
#     "ticks": -144000000000,
#     "nanoseconds": -14400000000000
#   },
#   "standardUtcOffset": {
#     "seconds": -18000,
#     "milliseconds": -18000000,
#     "ticks": -180000000000,
#     "nanoseconds": -18000000000000
#   },
#   "hasDayLightSaving": true,
#   "isDayLightSavingActive": true,
#   "dstInterval": {
#     "dstName": "EDT",
#     "dstOffsetToUtc": {
#       "seconds": -14400,
#       "milliseconds": -14400000,
#       "ticks": -144000000000,
#       "nanoseconds": -14400000000000
#     },
#     "dstOffsetToStandardTime": {
#       "seconds": 3600,
#       "milliseconds": 3600000,
#       "ticks": 36000000000,
#       "nanoseconds": 3600000000000
#     },
#     "dstStart": "2024-03-10T07:00:00Z",
#     "dstEnd": "2024-11-03T06:00:00Z",
#     "dstDuration": {
#       "days": 237,
#       "nanosecondOfDay": 82800000000000,
#       "hours": 23,
#       "minutes": 0,
#       "seconds": 0,
#       "milliseconds": 0,
#       "subsecondTicks": 0,
#       "subsecondNanoseconds": 0,
#       "bclCompatibleTicks": 205596000000000,
#       "totalDays": 237.95833333333334,
#       "totalHours": 5711,
#       "totalMinutes": 342660,
#       "totalSeconds": 20559600,
#       "totalMilliseconds": 20559600000,
#       "totalTicks": 205596000000000,
#       "totalNanoseconds": 20559600000000000
#     }
#   }
# }
