# escape sequence

### Escape Character
#### If you are studying a language when you are a beginner, you may suffer from backslash. Therefore, backslash is a character that can be used in combination. Also, depending on the escape character, the function is different.
| Escape Character | Explanation |
|:-------:|:-------:|
| \n | line break |
| \t | tab |
| \v | vertical tab |
| \b | backspace |
| \f | form feed (line break, move the cursor to the next line) |
| \r | carriage return (line break, move the cursor forward) |
| \a | ringtone (warning) |
| \\' | single quote |
| \\" | double quotes |
| \ \ | \ |
| \000 | ASCII characters in octal notation (null character) |
| \ ? | literal question mark |
| \ hh | ASCII characters in hexadecimal notation |
| \ hhhh | A Unicode character in hexadecimal notation when this escape sequence<br>is used in a wide-character constant or Unicode string literal. |
<br>
***

##### Not many, but I'll show you a few examples.

```py
print("Hello World!")
Hello World!
```
```py
print("Hello\nWorld!") # \n line break
Hello
World!
```
```py
print("Hello\tWorld!") # \t tab
Hello   World!
```
```py
print("H\bello World!") # \b backspace
ello World!
```
```py
print("\000") # \000 null character

```
```py
print("\\Hello World!\\") # \\ '\'
\Hello World!\
```

#### reference site : https://docs.microsoft.com/ko-kr/cpp/c-language/escape-sequences?view=msvc-160

#### If there are any errors or problems in my writing, please let me know and I will correct or delete it.
