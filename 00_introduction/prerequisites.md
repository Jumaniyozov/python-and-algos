# Prerequisites

This guide outlines what you need to know before starting different parts of the curriculum.

## Part 1: Python Fundamentals (Chapters 1-8)

### Required
- **Computer literacy**: Comfortable using a computer, file system, and terminal/command prompt
- **Text editor**: Ability to open and edit text files
- **Problem-solving mindset**: Willingness to think logically and debug issues

### Recommended
- **Basic math**: Arithmetic, simple algebra (helpful but not required)

### NOT Required
- No prior programming experience needed
- No computer science background needed

---

## Part 2: Standard Library (Chapters 9-15)

### Required
- **Completion of Part 1** or equivalent knowledge:
  - Comfortable with Python syntax
  - Understand functions and classes
  - Can use lists, dictionaries, and basic data structures
  - Familiar with modules and imports

### Recommended
- **Command line basics**: Navigate directories, run Python scripts
- **Git basics**: Version control fundamentals (helpful for practice projects)

---

## Part 3: Advanced Python (Chapters 16-22)

### Required
- **Solid Python foundations** (Parts 1-2 or equivalent):
  - Confident with OOP concepts
  - Understand decorators
  - Comfortable reading Python documentation
  - Experience writing Python programs (500+ lines)

### Recommended
- **Some programming experience**: Having built a few projects helps understand advanced patterns
- **Debugging skills**: Comfortable using pdb or print debugging
- **Understanding of references**: How Python handles object references and memory

---

## Part 4: External Tools (Chapters 23-26)

### Required
- **Python fundamentals** (Part 1)
- **Command line comfort**: Installing packages, running commands
- **Basic project structure**: Understanding of how to organize Python code

### Recommended
- **Git knowledge**: Helpful for understanding pre-commit hooks
- **Virtual environment experience**: Understanding why isolation is important

---

## Part 5: Algorithms & Data Structures (Chapters 27-45)

### Required
- **Python basics** (at minimum Chapters 1-6):
  - Lists, dictionaries, sets
  - Functions and recursion
  - Classes (basic OOP)
  - Comfortable implementing solutions in Python

### Strongly Recommended
- **Mathematical maturity**:
  - Basic algebra
  - Logarithms (understand what log₂ means)
  - Sequences and summations
  - Logic and proofs (helpful for understanding correctness)

### Helpful But Not Required
- **Data structures course**: Having seen the concepts before helps, but not necessary
- **Discrete mathematics**: Sets, graphs, trees, combinatorics

---

## Software Requirements

### Essential
- **Python 3.14+**: Latest version recommended
  - Download from [python.org](https://python.org)
  - Verify: `python --version` or `python3 --version`

### Recommended
- **Code editor** (choose one):
  - VS Code (recommended for beginners)
  - PyCharm
  - Sublime Text
  - Vim/Neovim (if comfortable)

- **Terminal/Shell**:
  - macOS/Linux: Built-in terminal
  - Windows: PowerShell, Windows Terminal, or Git Bash

### Optional but Useful
- **Git**: Version control (for practice projects)
- **uv**: Package manager (covered in Chapter 24)
- **pytest**: Testing framework (covered in Chapter 23)

---

## Time Commitments

### Minimum
- **1-2 hours per day** for consistent progress
- **5-10 hours per week** minimum

### Recommended
- **2-3 hours per day** for faster progress
- **15-20 hours per week**

### Intensive (Interview Prep)
- **4-6 hours per day**
- **30-40 hours per week**

---

## Learning Style Considerations

### This Curriculum Works Best If You
- Learn by doing (lots of examples and exercises)
- Prefer structured, sequential learning
- Want comprehensive coverage of topics
- Like understanding "why" not just "how"

### May Need Supplementation If You
- Learn best through video content (this is text-based)
- Prefer project-based learning (this is concept-first)
- Want quick "cookbook" solutions (this focuses on understanding)

### Supplementary Resources
- **Official Python docs**: [docs.python.org](https://docs.python.org)
- **PEPs**: Python Enhancement Proposals for deep dives
- **LeetCode/HackerRank**: For additional algorithm practice
- **YouTube**: Visual explanations for complex topics

---

## Skill Self-Assessment

### Beginner (Start with Chapter 1)
- [ ] Never programmed before
- [ ] Tried Python briefly but want structured learning
- [ ] Know another language but new to Python

### Intermediate (Start with Chapter 9 or 16)
- [ ] Comfortable writing Python scripts
- [ ] Understand functions, classes, and basic OOP
- [ ] Can debug simple errors independently
- [ ] Want to learn advanced features or algorithms

### Advanced (Start with Chapter 16 or 27)
- [ ] Professional Python developer
- [ ] Understand decorators, generators, context managers
- [ ] Want to master advanced features or prepare for interviews
- [ ] Looking for deep understanding of Python internals

---

## Environment Setup Checklist

Before starting, ensure you have:

```bash
# 1. Python 3.14+ installed
python --version  # or python3 --version
# Should show: Python 3.14.x or higher

# 2. pip available
pip --version  # or pip3 --version

# 3. Can run Python interactively
python
>>> print("Hello, World!")
>>> exit()

# 4. Can run Python scripts
echo 'print("It works!")' > test.py
python test.py
rm test.py

# 5. (Optional) Virtual environment
python -m venv test_env
source test_env/bin/activate  # or test_env\Scripts\activate on Windows
deactivate
rm -rf test_env
```

All working? You're ready to start!

---

## Common Setup Issues

### "Python not found"
- Install Python from python.org
- Add Python to PATH (option during Windows installation)
- Use `python3` instead of `python` on macOS/Linux

### "Permission denied"
- Don't use `sudo` with pip
- Use virtual environments instead
- Check file permissions: `chmod +x script.py`

### "Module not found"
- Activate virtual environment if using one
- Install package: `pip install package_name`
- Check you're using correct Python: `which python` or `where python`

---

## What If I Get Stuck?

### On Concepts
1. Re-read the theory section
2. Run the examples yourself (don't just read)
3. Modify examples to see what changes
4. Skip to tips.md for common mistakes
5. Move on and return later

### On Exercises
1. Try for at least 15-30 minutes
2. Check tips.md for hints
3. Look at solution approach (not full code)
4. Implement yourself
5. Compare with provided solution

### On Prerequisites
- Missing Python basics? Start with Chapter 1
- Missing math? Learn as you go, focus on patterns
- Missing CS theory? This curriculum teaches it

---

## Ready to Start?

If you can:
- Run Python code
- Install Python packages
- Use a text editor
- Commit 1-2 hours per day

Then you're ready! Proceed to `roadmap.md` to choose your learning path.
