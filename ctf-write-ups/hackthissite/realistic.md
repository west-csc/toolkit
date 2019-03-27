# Realistic Challenges

## Realistic 1: HTML Form Manipulation

>From: HeavyMetalRyan 
>
>Message: Hey man, I need a big favour from you. Remember that website I showed you once before? [Uncle Arnold's Band Review Page](https://www.hackthissite.org/missions/realistic/1/)?  Well, a long time ago I made a $500 bet with a friend that my band  would be at the top of the list by the end of the year. Well, as you  already know, two of my band members have died in a horrendous car  accident... but this ass hole still insists that the bet is on!
> I know you're good with computers and stuff, so I was wondering, is  there any way for you to hack this website and make my band on the top  of the list? My band is Raging Inferno. Thanks a lot, man!

```html
<form action="v.php" method="get">
	<input type="hidden" name="PHPSESSID" value="abcaeadfc31a5c43b2534bf995c0553f">
	<input type="hidden" name="id" value="3">
	<select name="vote">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
	</select>
	<input type="submit" value="vote!">
</form>
```

You are given an HTML form that has dropdowns for rating each band. 

==**Solution.**== Just edit an option on Raging Inferno's voting dropdown so that it has `value="500"`. Then vote using that option.

## Realistic 2: Hidden Link, SQL Injection

> From: DestroyFascism 
>
> Message: I have been informed that you have quite admirable hacking skills. Well, this racist hate group is using [their website](https://www.hackthissite.org/missions/realistic/2) to organize a mass gathering of ignorant racist bastards. We cannot  allow such bigoted aggression to happen. If you can gain access to their administrator page and post messages to their main page, we would be  eternally grateful.

1. Find the hidden element at the bottom of the webpage: a link to the login form. It is hidden with black text on a black background.

```html
<center>
    <a href="/missions/realistic/2/update.php"><font color="#000000">update</font></a></center>
```

2. Given the login form, I immediately started trying SQL injections.
   1. `" or true--"` Didn't work, incorrect credentials.
   2. `'or true--'` Gave me the same authentication error, but also this error message: `SQL Error: .`
   3. ==**Solution.**== `' or '' = '` Did work, use it in **both the username and password fields**.

## Realistic 3

>From: PeacePoetry 
>
>Message: I run this website where people can read and submit peace-related poetry. I am doing this out of good will towards others, and I don't see why I would be making enemies out of this, but some real ass hole hacked my website posting a bunch of ignorant aggressive propaganda on the front page. And I made that website a while ago, and I no longer have access to it. Do you think you can hack in and change it back? Please? Oh, and bonus points if you message me the name of the bastard who did this!
>My website can be found [here](https://www.hackthissite.org/missions/realistic/3).

1. Notice a comment at the bottom of the page's source.

   ``` html
   <!--
   Note to the webmasterThis website has been hacked, but not totally destroyed. The old website is still up. I simply copied the old index.html file to oldindex.html and remade this one. Sorry about the inconvenience.
   -->
   ```

2. Go to oldindex.html to try your luck there.
3. Click on submit poem, this is our only input.
4. Attempts to attack this form:
   1. :x: buffer overflow: just tells you `Sorry, your poem is too large.`
   2. 