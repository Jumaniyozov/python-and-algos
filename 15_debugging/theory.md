# Debugging and Profiling - Theory

## Core Concepts

### 1. Debugging

**What is Debugging?**:
- Process of finding and fixing bugs
- Understanding what code is actually doing
- Identifying why code behaves unexpectedly

**Types of Bugs**:
- Syntax errors: Code won't run
- Runtime errors: Crashes during execution
- Logic errors: Wrong results
- Performance issues: Too slow

### 2. Debugging Tools

**pdb (Python Debugger)**:
- Interactive debugger
- Step through code line by line
- Inspect variables
- Evaluate expressions
- Built into Python

**print() Debugging**:
- Simplest method
- Print variable values
- Track execution flow
- Good for quick checks

**Logging**:
- Structured debugging output
- Different levels (DEBUG, INFO, WARNING, ERROR)
- Can save to files
- Production-ready

**IDE Debuggers**:
- Visual Studio Code
- PyCharm
- Graphical breakpoints
- Easier than command-line pdb

### 3. pdb Commands

**Basic Commands**:
- `l` (list): Show code around current line
- `n` (next): Execute next line
- `s` (step): Step into function
- `c` (continue): Continue execution
- `b` (break): Set breakpoint
- `p` (print): Print variable
- `pp` (pretty print): Pretty print variable
- `w` (where): Show stack trace
- `u` (up): Go up stack
- `d` (down): Go down stack
- `q` (quit): Quit debugger

### 4. Logging Module

**Log Levels** (increasing severity):
- DEBUG: Detailed diagnostic info
- INFO: General informational messages
- WARNING: Something unexpected but not error
- ERROR: Serious problem
- CRITICAL: Very serious error

**Components**:
- Logger: Entry point for logging
- Handler: Sends logs to destination
- Formatter: Formats log messages
- Filter: Selective logging

**Best Practices**:
- Use appropriate log levels
- Include context (timestamps, module names)
- Log to files in production
- Don't log sensitive data

### 5. Profiling

**What is Profiling?**:
- Measuring where time is spent
- Finding performance bottlenecks
- Understanding resource usage

**Types of Profiling**:
- CPU profiling: Time spent in functions
- Memory profiling: Memory allocation
- Line profiling: Time per line of code

**Tools**:
- cProfile: Built-in CPU profiler
- timeit: Micro-benchmarking
- memory_profiler: Memory usage
- tracemalloc: Memory allocation tracking
- line_profiler: Line-by-line timing

### 6. Performance Optimization

**Optimization Steps**:
1. **Measure first**: Profile before optimizing
2. **Find bottleneck**: Focus on slowest parts
3. **Optimize**: Improve critical sections
4. **Measure again**: Verify improvement
5. **Repeat**: Continue until fast enough

**Common Optimizations**:
- Use appropriate data structures
- Cache expensive computations
- Avoid repeated work
- Use built-in functions (written in C)
- Lazy evaluation
- Batch operations

### 7. Memory Profiling

**Why Profile Memory?**:
- Find memory leaks
- Reduce memory usage
- Understand memory allocation patterns

**tracemalloc**:
- Built-in memory tracker
- Shows where memory is allocated
- Can take snapshots
- Compare snapshots

## Debugging Strategies

### 1. Reproduce the Bug
- Create minimal test case
- Document steps to reproduce
- Make it consistent

### 2. Understand the Error
- Read error messages carefully
- Check stack trace
- Identify error location

### 3. Form Hypothesis
- What do you think is wrong?
- Why might this happen?
- What would cause this behavior?

### 4. Test Hypothesis
- Add print statements
- Use debugger
- Add assertions
- Write tests

### 5. Fix and Verify
- Make smallest change possible
- Test the fix
- Make sure it doesn't break other things
- Add test to prevent regression

## Common Debugging Techniques

### Binary Search
Cut problem space in half repeatedly:
1. Check middle of code
2. If bug before middle, search first half
3. If bug after middle, search second half
4. Repeat until found

### Rubber Duck Debugging
Explain code line by line to someone (or something):
- Forces you to think carefully
- Often spot bugs while explaining
- No actual duck required!

### Differential Debugging
Compare working and broken versions:
- What changed?
- What's different?
- Narrow down to specific change

### Error Messages
Read them carefully:
- Type of error
- Error message
- File and line number
- Stack trace

## Best Practices

1. **Use version control**: Easy to revert changes
2. **Write tests**: Catch bugs early
3. **Use assertions**: Validate assumptions
4. **Keep functions small**: Easier to debug
5. **Log, don't print**: Better than print statements
6. **Use debugger**: More powerful than prints
7. **Profile before optimizing**: Optimize real bottlenecks
8. **Document weird behavior**: Help future you
9. **Take breaks**: Fresh perspective helps
10. **Ask for help**: Another pair of eyes
