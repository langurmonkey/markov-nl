Markov chain for NL
===================

`markov-nl.py` is a very minimalistic order-1 Markov model for natural language generation. It takes a file with a text and generates n sentences using a Markov chain. Just for fun.

Usage
-----

The following generates 20 sentences using `file.txt`.

```bash
$  markov-nl.py file.txt 20
```
For example, using the open domain book "20000 leagues under the sea" by Jules Verne:

```bash
$  markov-nl.py 2000-leagues-under-sea.txt 100
```

For more help, use:

```bash
$  markov-nl.py --help
```
