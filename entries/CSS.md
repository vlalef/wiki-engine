# CSS (Cascading Style Sheets)

CSS is a style sheet language used for describing the presentation of a document written in HTML or XML.

## Overview

CSS is designed to enable the separation of presentation and content, including layout, colors, and fonts. This separation improves content accessibility, provides more flexibility, and reduces complexity in the structural content.

### Key Features

- **Cascading Nature**: Multiple style sheets can be combined
- **Selectors**: Target specific HTML elements
- **Box Model**: Controls layout and spacing
- **Responsive Design**: Adapts to different screen sizes
- **Animations**: Creates dynamic visual effects

## History

- **1994**: CSS proposed by Håkon Wium Lie
- **1996**: CSS1 Specification released
- **1998**: CSS2 Released
- **2011**: CSS3 Modules begin rolling out

## Basic Syntax

    /* Selector and Declaration Block */
    selector {
        property: value;
    }

    /* Example */
    .header {
        background-color: #f0f0f0;
        padding: 20px;
        margin: 10px;
        border-radius: 5px;
    }

## Common Concepts

### Selectors
- **Element**: `div`, `p`, `h1`
- **Class**: `.className`
- **ID**: `#idName`
- **Attribute**: `[type="text"]`

### Box Model
1. Content: The actual content area
2. Padding: Space around the content
3. Border: Line around padding
4. Margin: Space outside border

### Layout Systems
- Flexbox: One-dimensional layout
- Grid: Two-dimensional layout
- Float: Traditional layout
- Positioning: Static, relative, absolute, fixed

## Modern Features

### CSS Variables

    :root {
        --primary-color: #007bff;
    }

    .button {
        background-color: var(--primary-color);
    }

### Media Queries

    @media (max-width: 768px) {
        .header {
            font-size: 16px;
        }
    }

## See Also
- [HTML](/wiki/HTML)
- [JavaScript](/wiki/JavaScript)
- [Frontend](/wiki/Frontend)
