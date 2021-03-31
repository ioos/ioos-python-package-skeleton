---
name: Bug Report
about: Report that something is not working properly
labels: "Type: Bug"
---

Please try to include:

- Code Sample, a copy-pastable example if possible.
- A ["Short, Self Contained, Correct (Compilable) Example](http://sscce.org/)
  will make it much easier for maintainers to help you.
  This [blog post](http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports) has a nice tutorial on how to achieve this.

```python
# Your code goes here

```

```python-traceback
# Your error goes here

```

- Issue description: Please explain **why** the current behavior is a problem..
- Debug info: Which platform (Linux, Windows, macOS, etc.)
- Please include the output of:
  - `python --version`
  - `python -c 'import ioos_pkg_skeleton; print(ioos_pkg_skeleton.__version__)'