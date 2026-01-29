# Chapter 17: Generators & Iterators

## Overview
This chapter covers Python's powerful iterator and generator protocols, which enable memory-efficient processing of sequences and streams. Generators are one of Python's most elegant features for handling large datasets and infinite sequences.

## Topics Covered
- Iterator protocol (`__iter__` and `__next__`)
- Generator functions and expressions
- Generator methods (send, throw, close)
- `yield from` and subgenerators
- Async generators
- Memory-efficient processing patterns
- Pipeline architectures

## Learning Objectives
By the end of this chapter, you will be able to:
- Implement custom iterators using the iterator protocol
- Create generator functions for lazy evaluation
- Use generator expressions for memory efficiency
- Control generator execution with send, throw, and close
- Build data processing pipelines with generators
- Understand and use async generators
- Apply generators to solve real-world problems

## Prerequisites
- Strong understanding of Python functions (Chapter 5)
- Familiarity with iteration and loops (Chapter 4)
- Understanding of function closures and scope
- Basic knowledge of exceptions

## Chapter Structure
- **theory.md**: Iterator and generator concepts, protocols, and patterns
- **examples.md**: 15 practical, runnable examples
- **exercises.md**: 15 progressive difficulty exercises
- **solutions.md**: Detailed solutions with multiple approaches
- **tips.md**: Best practices, performance tips, and common pitfalls

## Difficulty Level
Intermediate to Advanced - Generators are a fundamental concept that intermediate developers should master.

## Time Estimate
- Theory: 2-3 hours
- Examples: 2-3 hours
- Exercises: 4-5 hours
- Total: 8-11 hours

## Why This Matters
Generators are essential for:
- Processing large files without loading them into memory
- Creating infinite sequences
- Building data processing pipelines
- Improving performance in data-intensive applications
- Implementing coroutines and cooperative multitasking
- Stream processing and ETL operations

Understanding generators will make you more efficient at handling data and writing memory-conscious code. They're used extensively in data science, web scraping, log processing, and anywhere large datasets are involved.

## Real-World Applications
- **Data Science**: Processing large CSV files row by row
- **Web Scraping**: Yielding scraped items as they're collected
- **Log Analysis**: Streaming log file processing
- **API Clients**: Paginated API response handling
- **ETL Pipelines**: Transform data streams efficiently
