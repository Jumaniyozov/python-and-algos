# Chapter Numbering Analysis & Fix Plan

## Current State vs CLAUDE.md Plan

### ✅ Chapters 1-25: CORRECT
- 01-08: Python Fundamentals ✓
- 09-15: Standard Library ✓
- 16-22: Advanced Python ✓
- 23: pytest ✓
- 24: Package Management ✓
- 25: Code Quality ✓

### ❌ Chapter 26: MISMATCH
**Current:** 26_complexity (Complexity Analysis)
**Should be:** 26: Other Essential Tools (Rich, Click, Pydantic, Loguru)

### ❌ Chapter 27: MISSING
**Should be:** 27: Complexity Analysis (currently in chapter 26)

### ❌ Chapters 28-45: INCORRECT NUMBERING
**Current directories:**
- 29_linked_lists (should be 28)
- 30_stacks_queues (should be 29)
- 31_hash_tables (should be 30)
- 32_trees (should be 31)
- 33_advanced_trees (should be 32)
- 34_heaps (should be 33)
- 35_graphs (should be 34)
- 36_advanced_graphs (should be 35)
- 37_sorting (should be 36)
- 38_searching (should be 37)
- 39_dynamic_programming (should be 38)
- 40_greedy (should be 39)
- 41_backtracking (should be 40)
- 42_bit_manipulation (should be 41)
- 43_advanced_algorithms (should be 42)
- 44_patterns (should be 43)
- 45_interview_strategy (should be 44)

### Missing Chapter 28 (Arrays & Strings)

## Correct Chapter Order (per CLAUDE.md)

**Part 4: Essential External Libraries & Developer Tools (23-26)**
- 23: pytest ✓
- 24: Package Management ✓
- 25: Code Quality ✓
- 26: Other Essential Tools (NEED TO CREATE)

**Part 5: Algorithms and Data Structures (27-44)**
- 27: Complexity Analysis (MOVE from 26)
- 28: Arrays and Strings (MISSING - CREATE)
- 29: Linked Lists (currently 29 ✓)
- 30: Stacks and Queues (currently 30 ✓)
- 31: Hash Tables (currently 31 ✓)
- 32: Trees (currently 32 ✓)
- 33: Advanced Trees (currently 33 ✓)
- 34: Heaps (currently 34 ✓)
- 35: Graphs (currently 35 ✓)
- 36: Advanced Graphs (currently 36 ✓)
- 37: Sorting (currently 37 ✓)
- 38: Searching (currently 38 ✓)
- 39: Dynamic Programming (currently 39 ✓)
- 40: Greedy (currently 40 ✓)
- 41: Backtracking (currently 41 ✓)
- 42: Bit Manipulation (currently 42 ✓)
- 43: Advanced Algorithms (currently 43 ✓)
- 44: Patterns (currently 44 ✓)
- 45: Interview Strategy (currently 45 ✓) - WAIT, this should be 44!

**Actually, the original plan has 45 chapters (0-44), not 46!**

## Fix Plan

1. **Create Chapter 26: Essential Tools**
   - Rich (terminal formatting)
   - Click/Typer (CLI apps)
   - Pydantic (validation)
   - Loguru (logging)

2. **Rename Chapter 26 → 27**
   - mv 26_complexity → 27_complexity

3. **Create Chapter 28: Arrays and Strings**
   - Two pointers pattern
   - Sliding window
   - String manipulation
   - Common array/string problems

4. **Keep chapters 29-45 as is** (they're already correctly numbered!)

## Bonus Chapters (46-47)
- 46_data_science (moved from 23)
- 47_web_development (moved from 24)

These are extra bonus content beyond the main curriculum.
