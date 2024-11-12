# "Sing a song".
 
[Original kata](https://github.com/sleepyfox/code-dojo-39/blob/master/python/song.py)
 
## The “Situation”

Code to produce a popular children’s nursery rhyme was produced by a web agency for the customer last year. The customer
now desires to produce multiple different versions of the song using the same structure but based on different themes,
for example a current popular children’s movie featuring a cast of animals. The customer asks that you make the song
configurable for different lists of animals. The customer cannot guarantee that there will be the same number of animals
in each different version.

No documentation or tests were provided by the previous developer.
 
## Your Task
Refactor the code to allow for the customer’s needs. Remember: refactoring can only be done in the presence of tests
that are passing, and after refactoring the tests still pass!

## Legacy code
```python
song = """There was an old lady who swallowed a fly.
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a spider;
That wriggled and wiggled and tickled inside her.
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a bird;
How absurd to swallow a bird.
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cat;
Fancy that to swallow a cat!
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a dog;
What a hog, to swallow a dog!
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a cow;
I don't know how she swallowed a cow!
She swallowed the cow to catch the dog,
She swallowed the dog to catch the cat,
She swallowed the cat to catch the bird,
She swallowed the bird to catch the spider,
She swallowed the spider to catch the fly;
I don't know why she swallowed a fly - perhaps she'll die!

There was an old lady who swallowed a horse...
...She's dead, of course!"""

print(song)
```
