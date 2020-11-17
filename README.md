# metaboolizer
Password generator using SHA-256 hashing algorithm. (Python)

Cross-platform (Windows, MacOS, Android, iOS, GNU/Linux), using Kivy Framework.

The program uniquely generates a password of 18 characters, starting from a master key and the service for which the password 
  is being generated name. This is intended to be used in order to have a different strong password for every account, but without
  having to remember them all. In fact, you'll only have to remember the master key.
  The program will not store the master key, nor the different generated passwords.

For "cutting" the 32-byte output of the iterated SHA-256 to a 16 characters password, a simple mod function will be used.
