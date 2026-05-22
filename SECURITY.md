# Security Policy
[English](https://github.com/elvezjp/add-line-numbers/blob/main/SECURITY.md) | [日本語](https://github.com/elvezjp/add-line-numbers/blob/main/SECURITY_ja.md)

## Supported Versions

The following versions receive security support. We strongly recommend using the latest version.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.2   | :white_check_mark: |
| < 0.1.2 | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in add-line-numbers, please follow the responsible disclosure process below.

### How to Report

1. **Do not** open a public GitHub Issue for security vulnerabilities
2. Send a detailed report to the maintainers via either of the following channels:
   - Open a private GitHub Security Advisory (recommended)
   - Email (see the contact information in the README)

### What to Include

Please include the following information in your report:

- A description of the vulnerability
- Steps to reproduce the problem
- Potential impact and severity
- Suggested fix or mitigation (if any)
- Contact information (optional)

### Example Report

```
Subject: [SECURITY] Potential vulnerability during file processing

Description:
Under certain conditions, unexpected behavior may occur during file processing.

Steps to reproduce:
1. Place a file of a specific format in the inputs/ directory
2. Run python add_line_numbers.py
3. Observe the output

Impact:
Output files may contain unexpected content.

Suggested fix:
Strengthen input file validation.
```

## Response Timeline

- **Initial response**: within 48 hours
- **Status updates**: within 7 days
- **Resolution**: depends on severity
  - Critical: within 14 days
  - High: within 30 days
  - Medium: within 60 days
  - Low: in the next release cycle

## Security Considerations

### File Processing

add-line-numbers is a tool that processes text files:

- UTF-8 text files (.py, .java, .js, .json, .xml, .md, .txt, and more)
- Copies files from an input directory to an output directory

**Recommendations:**

1. Only process files from trusted sources
2. Make sure the output directory does not contain sensitive files
3. Review the contents of output files before sharing them

### Input Validation

add-line-numbers includes the following security-related behaviors:

- Non-UTF-8 files are automatically skipped
- Binary files are automatically skipped
- A non-existent input directory causes the program to exit with an error

### Output Security

When using generated files, be aware of the following:

- Output files contain the original file contents as-is (only line numbers are added)
- If you process a file containing sensitive information, that information will appear in the output
- Review the output before sharing it

### Dependencies

This project has no external library dependencies:

- Uses only the Python 3.11+ standard library
- No `pip install` required
- The lack of external dependencies reduces supply chain attack risk

### Dependabot Alert Policy

While this project has no external Python library dependencies, Dependabot alerts may still occur against GitHub Actions workflows. The policy is as follows.

**Malware tab**: always fix, regardless of where it appears.

**Vulnerable**: follow the table below.

| Target | Action |
|--------|--------|
| Latest version | **Fix** (update dependency / open PR). When a fix can be made via dependency version updates only, the project version itself is not changed |

## Security Best Practices

When using add-line-numbers, we recommend the following:

1. **Stay up to date**: always use the latest version
2. **Inspect inputs**: examine files before processing them
3. **Sandbox**: run on isolated environments (containers or VMs) when processing untrusted files
4. **Validate outputs**: review generated files before using them
5. **Limit privileges**: run with the minimum permissions required

## Known Security Limitations

1. **File size**: extremely large files may cause memory issues
2. **Encoding**: non-UTF-8 files are not processed

## Security Updates

Security updates are released as follows:

- Minor issues: patch version (e.g., 0.1.1)
- Serious issues: minor version (e.g., 0.2.0)

## Acknowledgments

We thank the security researchers who responsibly disclose vulnerabilities.

## Questions

For security-related questions that are not vulnerabilities, please contact us via:

- Open an Issue with the `security` label
- See the contact information in the README
