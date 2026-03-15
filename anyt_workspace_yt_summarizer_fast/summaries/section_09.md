# Section 9: Data Ownership, Privacy & Memory

**Timestamp:** 13:33 - 18:30

## Summary

Peter continues his thought on model competition: "ah for the foreseeable future the big companies still have mode" [13:33]. But the conversation shifts to what might be more valuable than the models themselves: data ownership and memories.

The host raises the data silo problem: "harness wise it's going to be interesting because every company kind of has their own their own silo right you you there's no way maybe there is for Europeans to actually get the memories out of chap" [13:38]. Peter confirms this concern: "I don't I'm not aware either. There's no there's definitely there's no way for a different company to get your memories out" [13:51].

This creates vendor lock-in: "So if if if I was like a company who like provides chat services, you could use me but then I couldn't access the memories. So like the companies try to like bound you to their data silo" [13:56]. Peter explains OpenClaw's fundamental advantage: "And the beauty of open claw is it kind of claws into the datas because at the end user the end user needs access because it's in the end otherwise it wouldn't work right if the end user access I can access the data" [14:11].

The host clarifies the ownership model: "and you own the memories it's just a bunch of markdown files on on your machine" [14:23]. Peter corrects: "I mean I don't own the memories other people yeah everyone owns their own memories as a bunch of markdown files on their own machines" [14:27]. This local storage has profound implications for privacy: "and to be honest those are probably super sensible because let's be honest Um, people use their agent not just for problem solving, but also for like personal problem solving" [14:36].

Both agree this happens "very quickly. Super quickly" [14:47]. Peter admits: "I mean, I I I I fully do that. I'm like, there's memory stuff that I don't want to have leaked" [14:50]. The host poses a provocative question: "What would you rather um uh sort of like not show your Google search history at this point or your, you know, memory files?" [14:53]. Peter's response is telling: "What's what's the Google word?" [15:00], suggesting the memories may be even more sensitive.

The conversation then turns to how Peter struggled to explain OpenClaw's value initially: "People still using Google. I built this and I was so excited but on Twitter people wouldn't get it" [15:03]. He found that "I I was failing to explain the awesomeness. I feel like it needs to be experienced" [15:12].

After trying various approaches, Peter decided to "do something really crazy. I just created a discord and I just put my bot without any security restrictions in the public discord" [15:19]. This allowed "people came in and they interacted with it and they saw me build the software with it and they tried to prompt inject it and hack it and my agent would be laughing at them" [15:27].

The protection was simple but effective: "you just had it locked down to your user ID so it only listened to you" [15:47]. Peter confirms: "Yeah. Yeah. that and it was I made very clean instructions that other people dangerous only only listen to me but respond to everyone" [15:50].

When asked where these instructions were stored, Peter reveals: "um that's actually part of open claw itself very much so the the that's part of the system prompt okay you are now that explains to you you're in Discord there's like public people there but you only listen to your owner or like you're human I don't even know how I wrote it" [16:03]. The host jokes: "yeah yeah you're god" [16:18].

Peter describes the organic evolution of his system: "And I kept I don't know what I did but my system was built very organically like at some point I created like an identity.mmd a soul.md like like various files" [16:27]. The templating process was revealing: "and then only in in January I started making it so other people could install it easier and I remember I built all these templates based on like oh take a rough look at what I have and make like templates and codex wrote it and what came was like Brad, you know, like people joke that Codex feels like Brad, even though now they have a new friendlier voice" [16:37].

The default templates felt wrong: "But the new bots, they felt so boring compared to what I had. So I was like, Modi, infuse the template" [16:58]. Modi is "the name of your personal" [17:05] bot. Peter explains the naming challenges: "Yeah. It's a new name because Uh there was some naming challenges" [17:09].

The refinement process was collaborative: "So So you you were talking to Multi. Yeah. I was like, 'Infuse infuse those templates with your your character.' And he changed the templates and then and then like all the things that came out afterwards were like actually funny, not as funny as mine" [17:12]. Peter kept some secrets: "So like I kept some secret and the one file that's not open source is like my soul. MD. So even though my my bot is in public discord, so far nobody cracked that one file" [17:26].

The host connects this to recent research: "Tell me more about soul.md. I just saw this research from Entropic where they now I think it's public but like a few months ago it was like where somebody ex randomly found out some text that's hidden in the weights where the model couldn't really remember that it learned it but it was like ingrained in the weights about the nicolity constitution" [17:39].

This inspired Peter's approach: "and I found that incredibly fascinating and I I talked about it with my agent and then we created a soulm with like the core values like how do we around human AI interaction, what's important to me, what's important to the model" [17:59]. He describes the file as having mixed utility: "Like some parts is a little bit like mamo jumbo and some parts is like I think actually really valuable in terms of how the model reacts and responds to text and makes it feel very natural" [18:07].

## Key Takeaways

- Data ownership and memories stored as local markdown files may be more valuable than the models themselves, avoiding vendor lock-in
- Personal AI memories become extremely sensitive quickly, potentially more private than search history
- Peter's "soul.md" file encodes core values and personality traits that make his bot feel natural and remain his secret sauce
