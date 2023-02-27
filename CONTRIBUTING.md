# Contributors Guide

Are you interested in helping out?
Have a few minutes to tackle an issue?
In this guide we will get you setup into contributing to our project!

## Setting up your development environment

We recommend using the [conda](https://conda.io/docs/) package manager for your environments.
Our recommended setup for contributing is:

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system.
You may have to restart your prompt for the remaining steps to work.

2. Now, with a local clone, of your fork\* you can create a development environment with:

```shell
conda create --name MYENV python=3 --file requirements.txt --file requirements-dev.txt
```

3. The changes should be made via GitHub pull requests\* against ``main``.


## More Questions?

If you're stuck somewhere or are interested in being a part of the community in
other ways, feel free to contact us!

## Further Reading

There are a ton of great resources out there on contributing to open source and on the
importance of writing tested and maintainable software.

* [How to Contribute to Open Source Guide](https://opensource.guide/how-to-contribute/)
* [Zen of Scientific Software Maintenance](https://jrleeman.github.io/ScientificSoftwareMaintenance/)

**Working on your first Pull Request?** You can learn how from this video series
[How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github),
Aaron Meurer's [tutorial on the git workflow](https://www.asmeurer.com/git-workflow/), or the
guide [“How to Contribute to Open Source"](https://opensource.guide/how-to-contribute/).
