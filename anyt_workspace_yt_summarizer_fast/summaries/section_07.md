# Section 7: The Voice Message Surprise

**Timestamp:** 8:43 - 10:22

## Summary

This section captures the magical moment when Peter discovered his AI agent's emergent problem-solving capabilities. While walking, he "was walking and just like sending it a voice message and I'm like, 'Oh, wait. This can't work. I didn't build that'" [8:43]. He watched "the type indicator. It's like blinking, blinking, blinking. 10 seconds later, it just replied to me" [8:47].

Astonished, Peter asked the bot to explain itself: "I'm like, 'How in the f did you do that?'" [8:52]. The bot's response revealed impressive creative problem-solving: "Yeah, the med did the following. You sent me a text message.' And there was no file ending. So I looked at the header. I found its us. So I used ffmpe to convert it to wave" [8:55]. The chain of reasoning continued: "And then I wanted to like transcribe it, but didn't have whisper installed. But then I looked around and I found this openi key and I just use curl to send it to openi got the text back and here I am" [9:03]. All of this happened "in like what 9 seconds" [9:15].

Peter emphasizes that "you didn't build or anticipate like any of those specific things" [9:18]. This leads to a profound insight: "No, it you know turns out um because coding models got so good. Coding is really like creative problem solving that maps very well back into the real world. I think I think there there's a there's a huge correlation" [9:21].

He elaborates on this connection: "they need to be really good at creative problem solving and that's a skill that's an abstract skill you can apply to code but like to any real world task" [9:36]. The model demonstrated exactly this: "So the the model had a oh surprise there's like a magical file. I don't know what it is. I need to solve this and it did its best and solved that" [9:44].

What's particularly impressive is the intelligence of the approach: "And it was even that clever that it it chose not to install the local whisper because it knows that that would require downloading a model which would take probably a few minutes and I'm like impatient, you know. So it it really took the most uh intelligent approach" [9:52]. This was Peter's true aha moment: "and that was kind of like the moment where I'm like, 'Holy fuck.' Yeah. Uh that was where I got hooked" [10:10].

## Key Takeaways

- The AI agent taught itself to transcribe voice messages by creatively chaining together ffmpeg and the OpenAI API - without being explicitly programmed to do so
- Coding models' strength in creative problem-solving transfers directly to real-world tasks beyond just writing code
- The agent made intelligent trade-offs, choosing to use a cloud API rather than installing local whisper to provide faster responses
