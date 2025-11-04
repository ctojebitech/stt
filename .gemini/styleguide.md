# Python Project Code Review Style Guide

This project uses:
- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **Poetry**
- **pytest**

## General Guidelines
- Follow **PEP 8** style guide strictly
- Use **type hints** and annotations
- Maintain modular code structure
- Document functions and classes with docstrings
- Keep code DRY (Don't Repeat Yourself)

## Code Review Process

### Review Criteria
- **Correctness:** Logic errors, edge cases, error handling
- **Security:** Input validation, data sanitization
- **Performance:** Algorithm efficiency, database queries
- **Maintainability:** Code structure, documentation
- **Testing:** Unit test coverage, test cases

### Severity Levels
- 🔴 **Critical:** Security/major bugs (block merge)
- 🟠 **High:** Performance/reliability issues
- 🟡 **Medium:** Code quality improvements
- 🟢 **Low:** Style suggestions

## Best Practices
- Run pylint/flake8 before commits
- Write unit tests for new features
- Keep functions focused and small
- Use environment variables for configs
- Document API endpoints with OpenAPI

## Security
- No hardcoded credentials
- Validate all inputs
- Use proper error handling
- Follow OWASP guidelines
- Secure API endpoints

## Dependencies
- Manage using Poetry
- Keep dependencies updated
- Document version requirements
- Check for security vulnerabilities