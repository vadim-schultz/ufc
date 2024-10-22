from alex import implementation as alex_impl
from implementation import implementation
from javier import implementation as javier_impl
from lars import implementation as lars_impl
from pratiksha import implementation as pratiksha_impl
from vadim_v1 import implementation as vadim_impl1
from vadim_v2 import implementation as vadim_impl2
from vadim_v3 import implementation as vadim_impl3


song = """
There was an old lady who swallowed a fly.
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


def test_alex_implementation():
    assert alex_impl() == song


def test_implementation():
    assert implementation() == song


def test_javier_implementation():
    assert javier_impl() == song


def test_lars_implementation():
    assert lars_impl() == song


def test_pratiksha_implementation():
    assert pratiksha_impl() == song


def test_vadim_implementation_v1():
    assert vadim_impl1() == song


def test_vadim_implementation_v2():
    assert vadim_impl2() == song


def test_vadim_implementation_v3():
    assert vadim_impl3() == song
