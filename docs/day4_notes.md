Debugging:

Issue:
recv(1024) captured input before Enter key.

Reason:
Network sockets read available data immediately.

Fix:
Created receive_input() function to read characters until newline.