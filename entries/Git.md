# Git (Version Control System)

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Overview

Created by Linus Torvalds for Linux kernel development, Git has become the most widely used modern version control system in the world.

### Key Features

- **Distributed System**: Full repository on every clone
- **Branching**: Lightweight branch operations
- **Data Integrity**: SHA-1 hash verification
- **Staging Area**: Intermediate commit preparation

## History

- **2005**: Created by Linus Torvalds
- **2007**: Git 1.5.0 released
- **2008**: GitHub launches
- **2018**: Microsoft acquires GitHub

## Basic Commands

    # Initialize repository
    git init

    # Add files to staging
    git add <filename>
    git add .

    # Commit changes
    git commit -m "commit message"

    # Check status
    git status

    # View commit history
    git log

## Common Operations

### Branching

    # Create branch
    git branch feature-branch

    # Switch branch
    git checkout feature-branch

    # Create and switch (combined)
    git checkout -b new-feature

### Remote Operations

    # Add remote
    git remote add origin <url>

    # Push changes
    git push origin main

    # Pull changes
    git pull origin main

## Core Concepts

### The Three States
1. **Modified**: Changes in working directory
2. **Staged**: Marked for next commit
3. **Committed**: Safely stored in database

### Branching Strategy
- **main**: Production-ready code
- **develop**: Integration branch
- **feature**: New features
- **hotfix**: Production bug fixes

## Best Practices

### Commit Messages
- Use present tense
- Be descriptive
- Keep it concise

### Branching
- One feature per branch
- Regular merges
- Clean up old branches

### Collaboration
- Pull before push
- Review changes
- Use meaningful names

## See Also
- [Python](/wiki/Python)
- [Frontend](/wiki/Frontend)
- [PostgreSQL](/wiki/PostgreSQL)
