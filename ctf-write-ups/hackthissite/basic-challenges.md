# Basic Challenges

## Basic 1: HTML Comment

> This level is what we call "The Idiot Test", if you can't complete it, don't give up on learning all you can, but, don't go begging to someone else for the answer, thats one way to get you hated/made fun of. Enter the password and you can continue. 

Very simple. Look at the webpage's html source. Find the line that reads:

```html
<!--the first few levels are extremely easy: password is 46fca7bd-->
```

This comment gives you the answer. :key: `46fca7bd`

## Basic 2: Logical Input

>Network Security Sam set up a password protection script. He made it load the real password from an unencrypted text file and compare it to the password the user enters. However, he neglected to upload the password file...

Just leave the input box blank. If the password will be checked by seeing if it is equivalent to a nonexistant file, just input a nonexistant password. :key: ` `

## Basic 3: Hidden Input (points to file)

>This time Network Security Sam remembered to upload the password file, but there were deeper problems than that.

Again, use inspect element to view the code surrounding the password field. Immediately something should stand out to you. (There is a hidden input box.)

```html
<center>
	<b>Password:</b><br>
	<form action="/missions/basic/3/index.php" method="post">
		<input type="hidden" name="file" value="password.php">
		<input type="password" name="password"><br><br>
		<input type="submit" value="submit">
	</form>
</center>
```

The hidden `file` field refers to an external document in the same directory as the page we are viewing, called `password.php`. Navigate to that file, https://www.hackthissite.org/missions/basic/3/password.php. This gives you the key, :key: `8e64abac`.

## Basic 4: Hidden Input (email)

>This time Sam hardcoded the password into the script. However, the password is long and complex, and Sam is often forgetful. So he wrote a script that would email his password to him automatically in case he forgot. Here is the script:

Same as the last level, there is a hidden field in the html form.

```html
<center>
    <form action="/missions/basic/4/level4.php" method="post">
    	<input type="hidden" name="to" value="sam@hackthissite.org">
        <input type="submit" value="Send password to Sam">
    </form>
</center>
```

Remove the `type="hidden"` attribute from the `to` input, and that will allow you to view and edit the input box it corresponds to.

```html
<input type="" name="to" value="sam@hackthissite.org">
```

Then enter your email (that you used to sign up for the site) in the box and click "Send email to Sam". You will recieve the password email.

```
To: <your email>
Subject: Your password reminder
From: sam@hackthissite.org
Message-Id: <20181204011932.AB790C1315@www.hackthissite.org>
Date: Mon, 3 Dec 2018 20:19:32 -0500 (EST)

Sam,
Here is the password: '4cbd1380'.
```

:key:`4cbd1380`

## Basic 5: Hidden Input (email)

>Sam has gotten wise to all the people who wrote their own forms to get the password. Rather than actually learn the password, he decided to make his email program a little more secure.

Use the same exploit detailed for **basic 4**. The email you recieve just has a different code.

```
To: <your email>
Subject: Your password reminder
From: sam@hackthissite.org
Message-Id: <20181204012242.68260C135B@www.hackthissite.org>
Date: Mon, 3 Dec 2018 20:22:42 -0500 (EST)

Sam,
Here is the password: '4a5af6b5'.
```

:key:`4a5af6b5`

## Basic 6: Rotating Caesar Cipher

>Network Security Sam has encrypted his password. The encryption system is publically available and can be accessed with this form. Please enter a string to have it encrypted. <input>
>
>You have recovered his encrypted password. It is: `f6h<j5;k`. Decrypt the password and enter it below to advance to the next level.

The provided form will take any plaintext input and give you what the ciphertext is. Also, you know the ciphertext of Sam's password. Thus you must reverse-engineer the system.

Play with the form a minute to find that it encodes input with a rotating caesar cipher: `aaaaaaa` becomes `abcedfg`. 

Use python's interactive console to quickly reverse the process.

```bash
Michaels-MBP:~ Michael$ python3
Python 3.6.5 (default, Mar 30 2018, 06:42:10) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ciphertext = "f6h<j5;k"
>>> chars = ciphertext.split()
>>> print(chars)
['f6h<j5;k']
>>> chars = [ciphertext[i] for i in range(len(ciphertext))]
>>> print(chars)
['f', '6', 'h', '<', 'j', '5', ';', 'k']
>>> ords = [ord(i) for i in chars]
>>> print(ords)
[102, 54, 104, 60, 106, 53, 59, 107]
>>> ords2 = [ords[i]-(i+1) for i in range(len(ords))]
>>> print(ords2)
[101, 52, 101, 56, 101, 47, 52, 99]
>>> ords2 = [ords[i]-i for i in range(len(ords))]
>>> print(ords2)
[102, 53, 102, 57, 102, 48, 53, 100]
>>> chars2 = [chr(i) for i in ords]
>>> print(chars2)
['f', '6', 'h', '<', 'j', '5', ';', 'k']
>>> chars2 = [chr(i) for i in ords2]
>>> print(chars2)
['f', '5', 'f', '9', 'f', '0', '5', 'd']
>>> print("".join(chars2))
f5f9f05d
```

 :key: `f5f9f05d`

## Basic 7: UNIX 'cal' Command and Injection

>This time Network Security sam has saved the unencrypted level7 password  in an obscurely named file saved in this very directory.
>
>In other unrelated news, Sam has set up a script that returns the output from the UNIX cal command. Here is the script: <input> Enter the year you wish to view and hit 'view'.

1. Given the page will execute UNIX `cal` command with your given input and provide the output, you want to engineer an input that prints the contents of the current file directory.
2. Enter `2018 && ls` to execute the cal command **and** list the directory contents.
3. Find you need to go to https://www.hackthissite.org/missions/basic/7/k1kh31b1n55h.php based on the directory listing, there you find that the key is 🔑 `08842670`.

## Basic 8: PHP Injection: Server Side Includes

>Sam remains confident that an obscured password file is still the best  idea, but he screwed up with the calendar program. Sam has saved the  unencrypted password file in  /var/www/hackthissite.org/html/missions/basic/8/
>
>However, Sam's young daughter Stephanie has just learned to program in PHP. She's  talented for her age, but she knows nothing about security. She recently  learned about saving files, and she wrote a script to demonstrate her  ability.

I don't know PHP so I had to look this one up. The answer lies in using the injection 

``` php
<!--#exec cmd="ls ../"-->
```

The wrapper executes the code in quotes in a unix terminal on the system. In this case, you print a directory listing of the parent directory, containing the PHP file you hijack. In the listing you find an additional file previously unknown. (https://www.hackthissite.org/missions/basic/8/au12ha39vc.php) Visit this in your browser to find the key. :key: `634a9eb8`

## Basic 9: PHP Injection: Server Side Includes

> Network Security Sam is going down with the ship - he's determined to  keep obscuring the password file, no matter how many times people manage to recover it. This time the file is saved in /var/www/hackthissite.org/html/missions/basic/9/.
>
> In the last level, however, in my attempt to limit people to using server side includes to display the directory listing to level 8 only, I have mistakenly screwed up somewhere. there is a way to get the obscured  level 9 password. See if you can figure out how...
>
> This level seems a lot trickier then it actually is, and it helps to have an  understanding of how the script validates the user's input. The script  finds the first occurance of '<--', and looks to see what follows directly after it.

Same concept as the last one, I just switched out the `ls ../` which would output the contents of the parent directory for:

```php
<!--#exec cmd="ls /var/www/hackthissite.org/html/missions/basic/9/"-->
```

which will dump the directory listing for the next challenge. Again, visit the new file revealed (https://www.hackthissite.org/missions/basic/9/p91e283zc3.php) to find the key. :key: `eb366256`

## Basic 10: Cookie Editing

>Please enter a password to gain access to level 10

Check your cookies, and find the one named  `level10_authorized`. It has an initial value of `no`, change this to `yes`. After you have done this, type anything you want in the password box, and hit submit. :key: (**set your cookie to `yes`**)
