# Working with LLMs

## Day 1 of 25

### Introduction

#### course introduction

#### course resources + Handbook
    #  https://half-money-bd8.notion.site/Course-Handbook-Prompt-Engineering-Bootcamp-Working-With-LLMs-Zero-to-Mastery-6234be19ffcd4e02991fa7c5227d21b3

#### Exercise: meet classmates and instructor
#### ZTM Plugin + Understanding your video Player
#### Set your learning streak goal

    # 25 days to complete this course is set

### Section 1: Introduction to Prompt Engineering

#### What is Prompt Engineering
    
    # A multidisciplinary branch of engineering focused on interacting with AI through the
    # integration of fields including Software Engineering, ML, Cognative Science, Business
    # Philosophy, Psychiatry, and Computer Science
#### Why is Prompt Engineering even a thing?
    
    # when the LLMs get big enough, they become much more useful and develop "intelligence"
    # no one knows exactly how LLMs are able to do what they do
    # Prompt Engineering is part of the quest to figure that out
    # prompt quality exponentially improves output performance

#### Breaking GPT
    
    # using ChatGPT play ground -- you'll learn how to set this up later in the course
    # the only time the LLMs "Think" is when they're typing...
    # if you don't understand how these models work, you'll be at a disadvantage 

## Day 2 of 25 | 2024-08-04

#### Applied Prompt Engineering

    # applying the knowledge of LLMs to real world
    # learn the skill and it will help you in all areads of your life
#### Applied Prompt Engineering with NASA

    # BIDARA: ChatGPT-based chatbot that was instructed to help scientists, engineers
        # understand, learn from, and emulate the strategies used by living things
        # to create sustainable design and tech
    # Prompt does all of these  things
        # 1. Tells ChatGPT it is an expert in biomimetic design and other fields
        # 2. Creates a workflow for the next four steps
        # 3. Creates a step-by-step process for ChatGPT - process to be followed
        # 4. Requires the model to provide evidence in the form of peer-reviewed sources
        # 5. Makes the odel respond with expert-level responses (hints are provided too)

#### Why is Prompt Engineering Important to You?

    # The hottest new programming language is English
    # You need to get good at prompt engineering; don't be bad
    # AI won't take your job but a person using AI will take your job
 
#### Homework: AlphaGo
    
    # watched AlphaGo

#### < > Let's Have Some Fun (+ More Resources)

    # signed up for GPT API and added $20 worth of API calls

## Day 3 of 25 | 2024-08-05

### Section 2: Choose Your LLM
    
    # choose GPT4 

#### What I'm Using - Part 1

    # followed setup guidance

#### Optional Setting Up Your Playground

    # playground setup complete
    # MFA setup complete
    # monethly budget setup complete

#### Multi-Modality and Tools in LLMS

    # testing auto-save
    # auto-save setup complete
    # what's multi-modailty?
        # understands text; generates text back
        # it understand images, too; pass it images
    # watch HAL 9000 tonight
    # keypoint: GPT can accept text, images and gen text, images
    # be careful of hallucinations - where things are just made up
    # third model: python execution
        # chatGPT can execute python code

    # Test: Calculate the Fibonacci sequence up to the 10th number

    # Summary
        1. Accept and generate text
        2. Accept and generate images
        3. Browse the internet
        4. Execute Python code

#### Choose You LLM!

    # choose GPT (obviously

### Section 3: Guided Proejct - Build Your First Game (Snake Game)

#### Project Introduction
    
    # creating a snake game using an LLM
    # create new repo for game?
    # add code right here and run it in replit

#### Building Our Snake Game - Part 1

    # previous messages in a chat infulence all other messages within that same chat
    # feed instructions to GPT before prompting for code generation
    # the key here being you need to "warm" GPT up before prompting by asking for steps (in some cases)
    # you provide it context and it helps make responsed more accurate

#### Building Our Snake Game - Part 2

    # manipulating code to change background color
        # simply ask chat gpt where to update the color within the code base it provided

#### Introduction to LLMs - Part 1

### Section 4: How LLMs Work

#### Introduction to LLMS - Part 1

    # use the right lingo so you know what you're saying
    # AI > Machine Learning > Deep Learning > Natural Language Processing (NLP) > 
    # Large Language Models > Large Language Models (LLM) > Prompt Engineering 
    # NLP is most important here - understand text and spoke words
        # that's in contrast to understading code (kind of because every thing must be 0s 1s)

#### Introduction to LLMs - Part 2

    # popular models: GPT-3(OpenAI), GPT-4(OpenAI), PaLM(Google), Claude(Anthropic), LLaMA(Meto)
    # popular chatbots: ChatGPT(OpenAI), Bing Chat(Microsoft), Bard(Google), Claude(Anthropic), Open Source
    # coding AI: GitHub CoPilot, Amazon Codewhisperer
    # writing AI: Jasper AI, Copy AI

## Day 5 of 25 | 2024-08-07

#### Tokens

    # tokens are the way an LLM understands (words but smaller words)
    # 1 token = 0.75 words (approx.)

    # how words are borken into tokens?

    # there are different tokens for each word and space in an LLM
    # there are different toakens for capitalized and lower case words in an LLM

    # what makes an LLM a Large Language Model: 
        # When you ask GPT a questions, it's breaking down your words into tokens
        # it then uses a lot of fancy math and CS to determine the sequence of tokens
        # that are most statistically probable to follow your tokens based on what it learned
        # it it's training data (That's when it's called a word guessing machine)

#### Word Guessing Machine?

    # change mode to complete (legacy)
    # show probabilities to full spectrum
    # set temp to 0  (controls randomness)
    # type in "I'm excited to learn" 
        # GPT will show you the probability of the next word as a percentage when you click the word
    # Temperature increased to 1
        # I'm excited to learn [guessing starts] all the tings I don't know about web development
        # green is less random (more statistically probable); red means less random (more inprobable)
    # more randomness creates issues and less acceptable answers
    # more randomness = more casual, conversational

####  Thinking Like LLMs - Role a Dice

```Python

    # these sections are about  looking at the edge cases and break things down
    
    # Roll a dice: you get a 4 2x in a row
    # because the probability is 47.42% that the number 4 comes after the words roll a dice is 4
    # the reason 4 is going to be the first output regardless, is that 4 was the most common roll in training data
    # GPT 4 writes py code for the second roll and prints 2 on the second turn

    # prompt: pick a number between 1 and 30
    # output: 27 (based on training data)
    # prompt 2: pick a number between 1 and 30
    # output: 24 w/ code:

```

```Python
    
    # Pick a random number between 1 and 30
    random_number = random.randint(1, 30)
    random_number

```

#### Inside LLMs

```Python

    # GPT 3 is an LL with 175 billion parameters spread across 96 layers, trained on 300 billion tokens!!!
        # Tokens = words (kind of)
    
    # 300 billion tokens = 45 TB of text data (books, articles, websites)
        # took all this info and was trained on it
        # more tokens (mostly) means better model

    # 175 billion parameters 96 Layers
        # parameters:
        # layers:
    
    # input layer: Mary ha a
    # output layer: goes through all other layers then reccomends (based on stats) little
        # little is added to the input layer
    # output layer (again): sees "mary had a little" and adds lamb to the input layer
        # this process repeats until all tokens are added 

    # as the models get bigger the "guessing" will get better

    # Weight: tells the model which signals to enhance and which to negate

    # neural networks are modeled after how your brain works
        # we dont really understand how the brain works but we do understand how the systme works
            # we can point to the individual neurons in your brain and say, "if I trigger this neuron, someting happens"
            # but when you put it together w/ all the other neurons, it becomes too complicated to understand
        # this is part of the magic that happens behind the a CS version of neural networks

    # new modles are released all the time and you'll be able to understand

    # Llama 2: 7 billion parameters spread across 32 layers, trained on 2 trillion tokens
        # the more tokens and parameters you have the smarter the model gets
        # it's a strong correlation
    
    # GPT 4 is significantly higher in all areas



```

#### The Transformer Model

```Python
    # predictive text tool on your phone
        # returns the 1st 2nd 3rd most popular responses
    # predictive but not a GPT

    # Understand the Google Whitepaper "Attention Is All You Need"
        # this paper introcuces the transformer model
    
    # used GPT4o to help break down the "Attention Is All You Need"

        # input: Using the Feynman technique, explain the attached document about Transformers.

        # output: 

"Let’s break down the document on Transformers using the Feynman technique, which involves explaining the concept in simple terms as if teaching it to someone else:

Introduction to Transformers

The Transformer model is a type of neural network designed for tasks that involve processing sequences, such as language translation. Unlike previous models that relied on complex structures like Recurrent Neural Networks (RNNs) or Convolutional Neural Networks (CNNs), Transformers use a simpler approach based entirely on attention mechanisms. This makes them more efficient and faster to train because they can process all parts of a sequence simultaneously, rather than one step at a time ￼ ￼.

How Transformers Work

	1.	Model Architecture: Transformers consist of an encoder and a decoder. The encoder processes the input sequence and converts it into a set of continuous representations. The decoder then takes these representations to generate the output sequence, one element at a time. The encoder and decoder are composed of several layers that mainly use attention mechanisms and feed-forward networks ￼ ￼.
	2.	Attention Mechanism: Attention allows the model to focus on different parts of the input sequence when producing each part of the output sequence. This is similar to how humans pay attention to specific words when understanding a sentence. The Transformer uses a specific type of attention called “self-attention,” which helps relate different positions of a single sequence to compute its representation ￼ ￼.
	3.	Multi-Head Attention: This involves using multiple attention mechanisms in parallel, allowing the model to focus on different parts of the sequence simultaneously. This helps the model understand complex relationships within the data ￼.
	4.	Position-wise Feed-Forward Networks: After attention, the data passes through a simple neural network that processes each position independently, adding a layer of complexity and representation power to the model ￼.
	5.	Positional Encoding: Since Transformers do not process sequences in order, they need a way to understand the position of each element in the sequence. Positional encodings are added to the input embeddings to give the model information about the position of each word ￼.

Results and Applications

Transformers have shown impressive results in tasks like language translation, significantly outperforming previous models in both speed and accuracy. For example, in English-to-German translation tasks, Transformers have set new records for translation quality ￼.

Conclusion

Transformers represent a shift in how sequence processing tasks are approached, moving away from the sequential processing of RNNs to a more parallel and efficient method based solely on attention. This makes them powerful tools for a variety of applications beyond just text, potentially including areas like image and audio processing ￼ ￼.

In summary, Transformers have revolutionized the way we handle sequence data, making it faster and more efficient to train models for complex tasks like language translation. The key innovation is the use of attention mechanisms, which allow the model to focus on different parts of the input simultaneously."



    # Refining the Output:

    # input: 

"I still can't understand what is being mentioned. Refine and simplify the explaination so someone who has no tech experience and no knowledge about neural netowkrs can understand this explaination."


    # output: 

    "Certainly! Let's simplify the explanation of Transformers by using an everyday analogy:

### Imagine a Transformer as a Language Expert

Think of a Transformer model as a language expert trying to translate a sentence from English to French. This expert doesn't just translate word by word. Instead, they look at the entire sentence to understand the meaning and context before translating it.

#### Key Ideas Behind Transformers

1. **Seeing the Big Picture**: 
   - Imagine if you were translating a sentence and could look at all the words at once to get the full meaning. Transformers work like this. They can look at the entire sentence in one go, rather than processing one word at a time.

2. **Paying Attention**: 
   - When the expert is translating, they might focus more on certain words depending on their importance. For example, in the sentence "The cat sat on the mat," they might pay more attention to "cat" and "mat" to understand what's happening. This is called "attention" in Transformers, allowing them to concentrate on different words depending on their importance.

3. **Multiple Perspectives**: 
   - The expert doesn't just look at the sentence in one way. They consider different perspectives to understand subtle meanings and nuances. Transformers use something called "multi-head attention" to look at the sentence from different angles simultaneously.

4. **Understanding Word Order**: 
   - Even though the expert looks at the whole sentence at once, they still need to know the order of the words. Transformers use a special technique to keep track of word positions so they understand the sequence properly.

#### Why Are Transformers Powerful?

- **Efficiency**: Because they look at the whole sentence at once, Transformers can translate much faster than older methods that process word by word.
- **Accuracy**: By paying attention to important words and understanding context, Transformers make more accurate translations.
- **Flexibility**: This approach isn't just for languages; it can be used in many fields where understanding sequences is important, like summarizing articles or analyzing music.

### In Summary

Think of Transformers as super-smart translators who can see the big picture of a sentence, focus on important parts, and consider multiple meanings all at once. This makes them very efficient and accurate at translating and understanding languages, making them useful in various tasks beyond just translation."

    # main take away of the google white paper "Attention is All You Need:" Transformers can pay attention to more context


    # when talknig about attention and paying attention to more context means more words (hence: large language model)


    # long-range attention
        # iMessage can't pay attention to the beginning date mentioned in a text and connect the two
        # LLMs can pay attention for longer and see context from further away
```

## Day 6 of 25 | 2024-08-08
#### GPT Meaning


 ```Python

    # GPT stands for Generative Pre-trained Transformer.
     
```
#### Exercise: Visualize the LLM Architecture

```Python
    
    # Prompt GPT4o to give you the architecture of GPT as an image
    # DALL-E is probided for free by MS Bing

    # prompt 1: create an image displaying the internal achitecture of a Large Language Model

    # response: image of what it thinks a neural network looks like

    # promt 2: Make this image more accurate and educational so that I can teach someone about LLMs with ease. Also, personify 
    # the image so it is more humanistic

    # promt 3: Recreate this image with a linear description of how the LLM works and what steps need to be taken for it to 
    # understand data and context (long-range attention)  

    # prompt 4: Move the drawing to the right side of the image and the description down the left side of the image so it's step 
    # by step
    
    # desired image was harder to generate than expected and no perfect image was created!!! Frustrating!

    ```



### Section X: Section Title


#### Subsection Title

```Python

    #
    #
    #

```





