# rjq
Recursive jq filter

## Description

`rjq` parses the stdin as JSON recursively and feeds the resulting data as an input to the actual `jq` command.

All command line switches are propagated "as is" to `jq`.
