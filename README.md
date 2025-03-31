# Wiki

A Django-based encyclopedia web application that supports Markdown-formatted entries created as a part of the course CS50 from Harvard.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Create a virtual environment:
```bash
  python -m venv venv
```

2. Activate the virtual environment:
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. For install required packages, with the virtual environment activated, run:
```bash
  pip install django markdown2
```

## Project Structure

```
wiki/
├── encyclopedia/
│   ├── static/
│   │   └── encyclopedia/
│   │       ├── styles.css
│   │       └── ...
│   ├── templates/
│   │   └── encyclopedia/
│   │       ├── layout.html
│   │       ├── index.html
│   │       ├── entry.html
│   │       ├── edit.html
│   │       └── ...
│   └── entries/
│       ├── Python.md
│       ├── Django.md
│       ├── HTML.md
│       └── ...
├── wiki/
└── ..."
```

## Core Features

### Entry Management
- View entries in HTML format (converted from Markdown)
- Create new encyclopedia entries
- Edit existing entries
- Store entries as Markdown files

### Navigation
- List all available entries
- Search entries by title
- View random entries
- Edit entries through web interface

### Interface
- Responsive layout with sidebar
- Bootstrap-styled components
- Search functionality in sidebar
- Clean content display

## Running the Project

1. Start the development server (with the virtual environment activated):
```bash
  python manage.py runserver
```

2. Access the application at `http://127.0.0.1:8000` (or `http://localhost:8000`)

## Template Structure

### Index Page (`index.html`)
- Lists all available encyclopedia entries
- Links to individual entry pages

### Entry Page (`entry.html`)
- Displays formatted entry content
- Provides edit button for each entry

### Edit Page (`edit.html`)
- Form for editing entry content
- Markdown textarea input
- Save functionality

## Styling

The project uses custom CSS for:
- Responsive layout
- Form styling
- Button designs
- Sidebar navigation
- Content formatting

## License

MIT License