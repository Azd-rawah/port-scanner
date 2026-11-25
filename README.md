# port-scanner

A small Python TCP port scanner.

## Usage

    python scanner.py

Enter a host and a port range. Open ports are printed with a name for common ones.
Only scan machines you own or have permission to test.

## Example
    host: 127.0.0.1
    Start port: 1
    End port: 1000
    OPEN: 135 RPC
    OPEN: 445 SMB

## What I learned

How ports and TCP connections work, and how Python's socket module checks them, and how threads speed up slow waiting tasks.

## Limits

Only a few common ports have names. An invalid host name still crashes it.
