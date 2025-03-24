# Contributing to WomenSafe Hub

Thank you for your interest in contributing to WomenSafe Hub! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

This project adheres to our Code of Conduct. By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Issues

- Check if the issue already exists in our issue tracker
- Include detailed steps to reproduce the issue
- Provide system/environment information
- Use the issue template when available

### Submitting Changes

1. Fork the repository
2. Create a new branch for your feature/fix
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Write or update tests
5. Run the test suite
   ```bash
   pytest
   ```
6. Commit your changes
   ```bash
   git commit -m "Description of your changes"
   ```
7. Push to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
8. Submit a Pull Request

### Pull Request Guidelines

- Include a clear description of the changes
- Reference any related issues
- Ensure all tests pass
- Update documentation if needed
- Follow the coding style guide

## Development Setup

See [Setup Guide](docs/setup.md) for detailed instructions.

## Code Style

- Follow PEP 8 guidelines for Python code
- Use descriptive variable and function names
- Comment complex logic
- Keep functions focused and concise

## Testing

- Write unit tests for new features
- Ensure existing tests pass
- Include integration tests when appropriate
- Test edge cases

## Documentation

- Update API documentation for new endpoints
- Document new features in the README
- Include docstrings for Python functions
- Update setup instructions if needed

## Branch Organization

- `main`: production-ready code
- `develop`: development branch
- `feature/*`: new features
- `fix/*`: bug fixes
- `docs/*`: documentation updates

## Communication

- Join our [Discord/Slack] channel
- Participate in discussions
- Ask questions in the appropriate channels

## Security

- Report security vulnerabilities privately
- Follow secure coding practices
- Avoid committing sensitive information
- Use environment variables for secrets

## Recognition

Contributors will be acknowledged in:
- The README.md file
- Our contributors page
- Release notes

Thank you for contributing to make WomenSafe Hub better!