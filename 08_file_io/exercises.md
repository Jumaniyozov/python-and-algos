# File I/O and Path Handling: Practice Exercises

## Exercise 1: Word Counter
Write a function `count_words(filename)` that:
- Reads a text file
- Returns a dictionary with word counts
- Handles file not found errors gracefully

## Exercise 2: CSV Processor
Create a function that:
- Reads a CSV file with columns: name, score
- Calculates average score
- Writes results to a new CSV with an additional "grade" column

## Exercise 3: JSON Configuration Manager
Create a class `ConfigManager` that:
- Loads config from JSON file
- Provides `get(key, default)` method
- Saves updated config back to file
- Creates default config if file doesn't exist

## Exercise 4: File Backup
Write `backup_file(filename)` that:
- Creates a backup with timestamp (e.g., `file.txt.2024-01-01_12-30-00.bak`)
- Returns the backup filename
- Uses pathlib

## Exercise 5: Directory Tree
Create `print_tree(path, indent=0)` that:
- Prints directory structure recursively
- Shows files and folders with proper indentation
- Example output:
```
data/
  subfolder1/
    file1.txt
    file2.txt
  subfolder2/
    file3.txt
```

## Exercise 6: Log File Analyzer
Write a function that:
- Reads a log file line by line
- Counts ERROR, WARNING, INFO messages
- Returns statistics dictionary
- Handles large files efficiently

## Exercise 7: File Merger
Create `merge_files(file_list, output_file)` that:
- Merges multiple text files into one
- Adds filename headers between sections
- Uses context managers properly

## Exercise 8: Path Utilities
Create a module with functions:
- `get_file_extension(path)` - return extension
- `change_extension(path, new_ext)` - change file extension
- `get_filename_without_ext(path)` - get name without extension
- All should use pathlib

## Exercise 9: Binary File Splitter
Write `split_file(filename, chunk_size)` that:
- Splits binary file into chunks
- Names chunks: `file.part1`, `file.part2`, etc.
- Returns list of chunk filenames

## Exercise 10: CSV to JSON Converter
Create a converter that:
- Reads CSV file
- Converts to JSON format
- Handles nested structures (e.g., "address.city" column becomes `{"address": {"city": "..."}}`)"

## Challenge 1: File Watcher
Implement a class that:
- Monitors a file for changes
- Calls a callback function when file is modified
- Runs in background thread

## Challenge 2: Smart File Differ
Create a function that:
- Compares two files
- Shows line-by-line differences
- Highlights added/removed/changed lines
- Similar to `diff` command output

## Challenge 3: Atomic File Writer
Implement `atomic_write(filename, content)` that:
- Writes to temporary file first
- Only replaces original if write succeeds
- Ensures no data loss on error

See solutions.md for answers!
