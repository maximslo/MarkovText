# MarkovText
📖 Trained text generator using first order Markov chains.  
🔮 A script built in Python that I plan to scale to a web application in the future.

## What is a Markov chain?
Named after Russian mathematician Andrey Makrov, a Markov chain is model describing a sequence of possible events or "states". For example, if you made a chain model of a baby's behavior, you might include "playing," "eating", "sleeping," and "crying" as states. In addition, a Markov chain tells you the probabilitiy of hopping, or "transitioning," from one state to any other state, like the chance that a baby currently playing will fall asleep in the next five minutes. It's often described as a stochaistic model because it describes the path of **random** events, where the probability of each event depends only on the state attained in the previous event.

#### "Stickiness"
In real life, a baby is more likely to sleep after crying, perhaps because it becomes tired. But if the probability of transitioning from one state to another is equal in our model, the chain will not be realistic. To make our model more like real life, we can change the probability of transitioning to sleeping after crying to be higher than playing. This is adding what I like to call "stickiness." The "crying" state could have a 0.3 probability of staying put, a 0.6 probability of transitioning to the "sleeping" state, and a 0.1 chance of transitioning to the "playing" state.

## What does it look like? 
Theoretically, states can be connected by arrows, with some arrows circling back to themselves (a state can be followed by itself)! But real modelers don't always draw arrow diagrams. Instead they use a "transition matrix" to tally the transition probabilities. Every state possible is included once as a row and again as a column, and each cell in the matrix tells you the probability of transitioning from its row's state to its column's state. In the matrix, the cells do the same job that the arrows do in the diagram.

## How are they useful?
In the hands of metereologists, ecologists, computer scientists, financial engineers and other people who need to model big phenomena, Markov chains can get to be quite large and powerful. For example, the algorithm Google uses to determine the order of search results, called PageRank, is a type of Markov chain.

#### Importing text:

    word_dict = create_dictionary('filename.txt')
  
* Make sure the file you want to model is in the same directory!

#### Generating text:

    generate_text(word_dict, lenth of generated text)
