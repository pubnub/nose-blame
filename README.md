# Nose Blame Plugin

Nose plugin to allow for assigning owners to entire test suites and/or individual test cases.

Outputs json blame report to stdout or specified file.

## Installation

```
pip install nose-blame
```

## Usage

```
--with-blame                      | enable blame plugin
--blame-file <path/to/file.json>  | path to json file for blame report, prints to stdout if not set
```
`NOSE_WITH_BLAME` and `NOSE_BLAME_FILE` environment variables may be used in lieu of cli flags.
