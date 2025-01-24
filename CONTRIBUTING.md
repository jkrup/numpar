# Contributing to numpar

Thank you for your interest in contributing to numpar! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. If not, create a new issue with a clear title and description
3. Include steps to reproduce the bug and expected behavior
4. Add relevant system information and package versions

### Suggesting Enhancements

1. Check existing issues for similar suggestions
2. Create a new issue describing your enhancement
3. Explain why this enhancement would be useful
4. Provide examples of how it would work

### Development Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests as needed
5. Run the test suite:
   ```bash
   python -m unittest discover tests
   ```
6. Ensure code follows project style guidelines
7. Commit your changes (`git commit -m 'Add amazing feature'`)
8. Push to your fork (`git push origin feature/amazing-feature`)
9. Open a Pull Request

### Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/numpar.git
   cd numpar
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e .
   ```

## Pull Request Guidelines

1. Update documentation for any changed functionality
2. Add tests for new features
3. Ensure all tests pass
4. Follow existing code style
5. Keep changes focused and atomic

## Style Guidelines

- Follow PEP 8 for Python code
- Use descriptive variable names
- Add docstrings for functions and classes
- Comment complex logic
- Keep functions focused and concise

## Questions?

Feel free to open an issue for any questions about contributing.

Thank you for helping improve numpar!