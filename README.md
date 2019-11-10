Markov chain for NL
===================

`markov-nl.py` is a very minimalistic order-1 Markov model for natural language generation. It takes a file with a text and generates n sentences using a Markov chain. Just for fun.
Original source is [here](https://www.reddit.com/r/linux/comments/du0m7h/really_fast_markov_chains_in_20_lines_of_sh_grep/f70uull?utm_source=share&utm_medium=web2x).

Usage
-----

The following generates 20 sentences using `file.txt`.

```bash
$  markov-nl.py file.txt 20
```
For example, using the open domain book "20000 leagues under the sea" by Jules Verne:

```bash
$  markov-nl.py 2000-leagues-under-sea.txt

Contempt for the ocean it must have to a thousand miles an enthusiastic colourist. 
Nemo. Whiskers like the ships bottom of the quays and not see how to keep ones self
Professor that before Vanikoro. Disheartened. Returning to finish please. Prompt his
movements and I saw floating under water is introduced which is there are real.
Advantageously as a submerged But the air by this book which were profoundly dark
spots. Landscape Captain you maintain yourselves in the day before. Ensued. Date.
```

For more help, use:

```bash
$  markov-nl.py --help
```
