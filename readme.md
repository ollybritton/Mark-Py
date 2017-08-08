# Mark-Py
Mark-Py is a Markov Bot which is a form of chatbot which takes text and outputs text which is different, but seemingly related. This program takes a text file and returns another text file which is in a similar style, but with new content. I also have a [Javascript version of this](https://github.com/ollybritton/Mark-Js), named `Mark-Js`, which is similar but is designed to generate smaller amounts of text for things like twitter bots.

## Use
To use the program itself, first you need to place the text file in the directory, and then link to it in the `FILE` variable near the top of the script. If you want to set a specific output location, you can also link to that in the `OUTPUT` variable.

There are a couple files you can try yourself, located in the `samples` directory.

+ `rap.txt` contains a vast majority of Eminem's songs, which can be used to generate awesome new songs. Here's a sample of the output from that.
  + "sh\*\* I just saw her cheek
  + and smearin her lipstick, I slipped this in church
  + and smack your face looks the knife
  + My mother's throat
  + \*AHHHHHHHH!\* Guess who's back
  + Back back \*scratch\*"


+ `interstellar.txt` contains the entire script of Christopher Nolan's hit film *Interstellar*, and can be used to generate dramatic quotes, creating instant drama in any situation.
  - Hey, Brand?
  - Yeah?
  - Bring a physical dimension.
  - You have worked out the Endurance.
  - Imperfect contact.
  - Override.
  - Hatch lockout.
  - Is he locked on yet?

There are also some variables that you can tweak with to get a different results:

+ `PARAGRAPHS_PER_FILE`, this sets the amount of paragraphs per file, *surprise, surprise*. If the text file you feed it also has a lot of newlines itself, it might generate more paragraphs then you specify.

+ `SENTENCES_PER_PARAGRAPH`, this is also very obvious but if you have trouble reading capital letters, it sets the amount of sentences in a paragraph.

+ `MAX_WORDS`, this sets the maximum amount of words in a sentence.

+ `CHAIN_LENGTH`, this sets the length of the head of a chain. This will make more sense if you read the "How" section. Basically, it sets the "resolution" of the Markov bot – bots with longer `CHAIN_LENGTH`s will form more complex sentences, but require much more starting text to form coherent sentences and phrases. I would suggest setting it to `2`, as it performs the best. This value has to be higher than `1`.

## How
Markov bots are made by creating Markov "chains" which represent the probability that one specific word follows another. For example, lets say we have the phrase: `"this is a test"` and `"this is also a test"`.

First, we split the text into sections which consist of a "head" and a "tail", and what each phrase starts with (assuming `CHAIN_LENGTH` is equal to two):

    (this, is) -> (a)
    (is, a) -> (test)
    (a, test) -> (this)
    (test, this) -> (is)
    (this, is) -> (also)
    (is, also) -> (a)
    (also, a) -> (test)

    starting = (this, this)

Then, we "add" together and duplicate chains. In our case, we have a repeated `(this, is)`:

    (this, is) -> (a, also)
    (is, a) -> (test)
    (a, test) -> (this)
    (test, this) -> (is)
    (is, also) -> (a)
    (also, a) -> (test)

So now we know that when a sentence starts with `this is`, we need to follow it with either an `also` or `a`.

To generate a new phrase, we simply choose a word from the `starting` words, and then search for "heads" that also begin with that.

    starting_choice = this
    search = (this, is)

Now we have a starting "head", we chose from the available words in the "tail":

    head = (this, is)
    tail = (a, also)

    random_choice = a

Now we repeat the above step, but starting with `a`. This yields:

    current = "this is a "
    head = (a, test)

Now we have `this is a test`. Of course, this is already a phrase as the amount of original text is so small, but now imagine doing the same process for a much larger file, building up an entire dictionary of phrases and things that follow them and you'll be able to generate lots of new phrases.
