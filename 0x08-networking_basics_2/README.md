# Networking Basics #1

In this project, we'll explore fundamental concepts related to networking, IP addresses, and host configurations. The tasks involve writing Bash scripts to perform specific networking operations.

## Concepts

### What is localhost/127.0.0.1?

- **localhost**: It is a hostname that refers to the current device used to access it, typically via loopback interface (127.0.0.1). It is used for testing and network diagnostics.

### What is 0.0.0.0?

- **0.0.0.0**: It is a non-routable meta-address used to designate an invalid or unknown target. In the context of server configuration, it usually means "all available interfaces" or "any address."

### What is /etc/hosts?

- **/etc/hosts**: It is an operating system file that maps hostnames to IP addresses. It is a plain text file used for local name resolution before DNS resolution.

### How to display your machine’s active network interfaces?

- Use the `ifconfig` command to display active network interfaces.

## Tasks

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server to meet the following requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

Example:

```bash
$ ping localhost
# Output: PING localhost (127.0.0.1) ...

$ ping facebook.com
# Output: PING facebook.com (157.240.11.35) ...

$ sudo ./0-change_your_home_IP
# Output: (no output, script execution)

$ ping localhost
# Output: PING localhost (127.0.0.2) ...

$ ping facebook.com
# Output: PING facebook.com (8.8.8.8) ...
