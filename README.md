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
    
    # GPT 4 is significantly higher in all areas



```
### Section X: Section Title


#### Subsection Title

```Python

    #
    #
    #

```
