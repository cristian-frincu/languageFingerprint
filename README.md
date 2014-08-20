languageFingerprint
===================

A program that is able to identify the language an input text is written in. Fully written in python.

The identifucation is done by scanning open source books, a fingerprint is created for
that language and then that can be comapared with the input text.

The response is given as a percentage of certainty beside each language that it tried to match. Currently English and French language
has been tested and is supported. There is no reason why any alpha numeric language won't be supported.

The program is created in such a away that it can be used for more than just human languages, but even programming languages could be 
identified given they are far apart enough.

The program does not scan for a specific whole words, but instead it is looking for short sequences of characters, those are more likely
to repeat. This would be the equivalent to looking at individual sylabels rather than whole words. 

If the body of input text is not long enough it might not be able to pick up any sort of pattern to identify a language over another so false negatives
are a lot more likely to occur than false positives.
