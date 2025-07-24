# Python libgpiod Information
>Version 1.0  
>Date: Fall 2025
---
## Why `python-libgpiod`?

The Raspberry Pi 5 introduces new hardware (the RP1 I/O controller) and a more modern way of working with GPIO that older libraries like `RPi.GPIO` and `GPIO Zero` no longer fully support.

In this course, we will use **`python-libgpiod`** for the following reasons:

- It works reliably with the **Raspberry Pi 5** and the newer **RP1 chip**.  
- It uses the **modern Linux GPIO interface** (character devices under `/dev/gpiochipN`), which is aligned with how Linux manages hardware today.  
- It gives you **more control and visibility** into how GPIO lines work — which is important when learning about **operating systems and peripheral management**.  

We won't be using older libraries like `RPi.GPIO` or `GPIO Zero`, as they either no longer work correctly on the Pi 5 or abstract away too much detail for this course’s focus.



For more Information on APIs: [See `libgpiod core API`](https://libgpiod.readthedocs.io/en/latest/core_api.html)


