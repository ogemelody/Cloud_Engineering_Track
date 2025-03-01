# __Background__

You have a list of domain names from a log file, indicating the number of times the computer accessed those sites. However, the list shows subdomains too, but you want to see only the main sites and the total number of accesses.
For example __6.clients-channel.google.com__ and __apis.google.com__ should be counted together as __google.com__.

## Task - Aggregate The Log File
Complete the function that takes two arguments:
- log_file - a list of domain names, showing the number of access requests to each domain, as you copied it from the logs. It’s not really a file, it’s a string representing the file’s content.
- min_hits (optional) - defines what is the minimum number of accesses in order to appear on the output list. If this is not given, consider it 0.
  
Return a string ready to be printed, showing the sites with the total number of accesses, in a descending order.

## Output requirements
The output should show the sites with the total number of accesses in parentheses.
Sites should have only 2 levels (e.g. ebay.com), except for .co.xx and .com.xx type domains, which should have 3 levels (e.g. amazon.co.jp).
The list should be sorted in descending order of access. If two sites have the same number of accesses, sort them alphabetically.
Entries should be separated by newlines (\n).

