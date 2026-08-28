# Development Workflow

This document describes the development workflow used for okoze.

The workflow is intentionally simple. It is designed for a small,
experimental project rather than a large team.

## Features and Tests

Each feature has an ID such as `1B1`. The ID is used consistently
in branches, commits, tests, and other development records.

Development is driven by tests.

Before implementing a feature, I decide what the feature is and record
it in [`docs/features.md`](https://github.com/kepaxy/okoze-pre/blob/main/docs/features.md).

I then create a branch for the feature and record the start of the
feature with an empty commit:

    git commit --allow-empty -m "🟧 1B1 Canvas positioning"

The tests are then defined and implemented.

A test starts as Red and becomes Green when the required behavior has
been implemented and the test passes.

For example:

    🔴 The Canvas can fill the available window
    🔴 The Canvas can be resized when the window size changes

After implementing the required behavior:

    🟢 The Canvas can fill the available window
    🟢 The Canvas can be resized when the window size changes

The Green tests are committed to Git:

    git commit -m "🟢 The Canvas can fill the available window"

If several tests become Green as part of the same change, the commit message uses one representative test as its subject.

The other tests are recorded in the commit message body.

For example:

    git commit -m "🟢 The Canvas can fill the available window" \
    -m "🟢 The Canvas can be resized when the window size changes"

When there is no suitable representative test, the test information can be recorded in the commit message body instead.

## Refactoring

Refactoring is not treated as a separate feature.

When necessary, I refactor the code while developing a feature.
A substantial refactoring is recorded as a separate commit:

    git commit -m "refactor: ..."

Refactoring should not change the intended behavior of the application.

## Fixing Problems

When a problem is discovered, I first define the required correction
and add tests that describe the desired behavior.

The fix is then implemented until the tests become Green.

Fixes are recorded using the 🔧 marker:

    git commit -m "🔧 fix: ..."

The corresponding tests are recorded as 🟢 test commits.

## Pull Requests

Each feature is developed on its own branch.

When the feature is complete, a pull request is created and the branch
is merged into `main`.

The `main` branch is protected by a GitHub ruleset. Development is done on feature branches and merged through pull requests.

The exact Git merge strategy is not considered part of the development
methodology and may be changed as the project evolves.

## Keeping the Workflow Simple

This workflow is deliberately lightweight.

I do not want to introduce a project-management system simply to keep
track of a small number of features and tests.

The goal is to make the development process visible through ordinary
text files, Git commits, branches, and pull requests.

If the workflow itself becomes complicated, that is a sign that it may
need to be simplified.
