# README

![](docs/res/logo.png)

AIKA is an AI-based app that can be used to replace or support the earlier stages of the integration course for migrants. 

## Motivation

The average waiting time for an integration course in 2023 was more than 5 months (according to the Federal Audit Office). This is a period of time in which refugees and other groups of migrants have to wait for an offer of a place on a course. There is also a lack of staff and inaccessible offers in the area of law & political education, which in turn makes life in Germany more difficult for many people and makes the work of social workers inefficient.

## Implementierung

The user interacts with AIKA mainly via a chat in which he communicates with a bot whose responses are generated with the help of LLMs running on the server. 
![](docs/res/interface_ex.png)


AIKA's curriculum consists of three parts: Language, Law and Everyday Life. 

### Sprache

The curriculum corresponds to language level A2.1 and aims to improve writing, listening and reading skills. Speaking will also be included at a later stage. 

AIKA's Intelligent Tutoring System helps the user to master the curriculum by adapting the learning process to the user's needs by evaluating the user's current progress and generating suitable tasks. 

### Recht und Alltag

This part facilitates the user's integration process with regard to everyday activities and bureaucracy in Germany. The user can ask AIKA's ChatBot questions, e.g. about waste separation or filling out an application, and read the answers generated by fine-tuned LLMs in the chat. 
