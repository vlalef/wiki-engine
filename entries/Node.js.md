# Node.js

Node.js is an open-source, cross-platform JavaScript runtime environment that executes JavaScript code outside a web browser.

## Overview

Node.js enables developers to use JavaScript for server-side scripting, allowing the development of scalable network applications.

### Key Features

- **Event-Driven**: Non-blocking I/O operations
- **Package Management**: NPM (Node Package Manager)
- **Cross-Platform**: Runs on various operating systems
- **Single-Threaded**: Event loop architecture
- **Extensible**: Large ecosystem of modules

## History

- **2009**: Created by Ryan Dahl
- **2011**: NPM package manager introduced
- **2015**: Node.js Foundation established
- **2018**: Node.js and JS foundations merged

## Basic Usage

    // Hello World server');

    const server = http.createServer((req, res) => {
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Hello World\n');
    });

    server.listen(3000);

## Core Features

### Event Loop
- Single-threaded processing
- Non-blocking I/O
- Event-driven architecture

### Package Management
- NPM registry
- package.json
- Dependencies management
- Scripts automation

### Built-in Modules
- **http/https**: Web server functionality
- **fs**: File system operations
- **path**: Path manipulations
- **crypto**: Cryptographic functions

## Common Uses

### Server Applications
- RESTful APIs
- Web servers
- Real-time services

### Development Tools
- Build systems
- Task runners
- Development servers

### Enterprise Applications
- Microservices
- Backend services
- API gateways

## See Also
- [JavaScript](/wiki/JavaScript)
- [Frontend](/wiki/Frontend)
- [PostgreSQL](/wiki/Postgresql)