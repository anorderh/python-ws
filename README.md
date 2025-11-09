# 💬 Python Real-Time Chat Server & Client using WebSockets

## Overview

The goal here was to get a better understanding of RTC via WebSockets and understand how messages can be bidirectionally sent from client & server.

## Features

-   Server
    -   Python script capable of exposing a WebSocket connection
    -   Able to accept connections from multiple clients
    -   Able to assign UUIDs and relay messages between clients
-   Client
    -   Python script joining WebSocket connection and sending chat messages
    -   Utilizes multithreading and `asyncio` to concurrently read incoming messages and prompt user for text input

## Technologies

-   Python for scripting
    -   `asyncio` for concurrency
    -   `prompt_toolkit` for user input
-   `websockets` for RTC

## Takeaways

-   This project helped expose me to bi-directional server & client communication. It also exposed me to Python execution management, relating to its built-in GIL, how the event loop determines which co-routines to run next, and how multithreading can be utilizied here to satisfy concurrency requirements.
