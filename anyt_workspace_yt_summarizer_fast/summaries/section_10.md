# Section 10: Contrarian Development Philosophy

**Timestamp:** 18:30 - 21:54

## Summary

The conversation shifts to Peter's unconventional technical choices in building OpenClaw. The host notes: "in terms of building open claw. Um you're also kind of taking a little bit of a contrarian view at sometimes like which model you like for coding, which one you like to run your bot on. Um and then also like how you actually like you know code. Um work trees get git work trees have kind of been a popular thing. There's more and more tools embracing them but you're just you're just like you know no work trees just multiple checkouts of the repo and like parallel you know terminal windows" [18:30].

Peter starts with his model choice: "Yeah I feel like the whole world does cloud code and I don't think I could have built the thing with cloud code" [18:54]. He explains his preference: "Like I I love codex because it it looks through way more files be before it decides what to what to change. You don't need to do so much charade to get a good output. If you're skilled a skilled driver I sometimes even say uh you can get reasonably good output with any tool but codex is just is just really brilliant" [19:00].

The tradeoff is speed: "It is incredibly slow. So sometimes I use like 10 at the same side at the same time uh like maybe six on that screen and to there and to there" [19:24]. This creates complexity: "and I don't like this is already a lot of complexity in my head there's a lot of jumping so I try to minimize anything else that is complexity" [19:32].

This leads to his workflow philosophy: "so in my head main is always shippable I just have multiple copies of the same repository that all are on main so I don't have to deal with how do I name that branch" [19:40]. He lists the benefits: "Um there could be like conflicts on naming. I cannot go back. It's there are certain restrictions when you use work trees that I don't need to care about if it's copies" [19:54].

Peter avoids additional tooling complexity: "I don't like to use a UI because that's again just added complexity" [20:02]. The host agrees: "Yeah" [20:09]. Peter emphasizes simplicity: "Like they're simpler and less friction I have. All I care about is like syncing and text" [20:09]. He doesn't need visual complexity: "I don't necessarily need to see so much code. I I mostly see it like flying by. Sometimes there's like gnarly stuff that I want to like take a look" [20:16].

His approach relies on clear thinking upfront: "But in most cases, if you clearly understand the design and think it through and discuss it with your with your agent, it's fine" [20:25].

Peter shares another contrarian choice: "I'm also very happy that I didn't even build an MCP support. So, Open Claw is very successful and there's no MCP support in there" [20:32]. He clarifies with an asterisk: "With a small asterisk, I built a skill that uses makeporter, which is one of my tools that converts MCPS into CLIs. And then you can just use any MCP as a CLI" [20:40].

This allows him to bypass MCP's limitations: "Um, but I totally skip the whole classical MCP crap. So you because you don't then you can actually if you need to you can use MCPS on the fly. You don't have to restart unlike unlike Codex or cloud code where you actually have to restart the whole thing" [20:50]. He sees clear benefits: "I think it's way more egent and also scales way better" [21:05].

Peter criticizes Anthropic's approach: "Now you see entropic they do they built like a tool called search feature like something super custom for MCPS that was like in beta because it's like so gnarly" [21:08]. His solution is simpler: "No, just have CLI bot really is good at Unix. You can have as many as you want and it just works" [21:18].

He's pleased with the validation: "So like I'm very happy that I got very little complaints about the MCP stuff" [21:28]. The host summarizes the philosophy: "It's kind of back to you're just giving it the same tools that humans liked to use" [21:35]. Peter confirms: "And not invented stuff for for bots, per se" [21:40]. The host adds: "Yeah. Humans, no insane human tries to call an MCP manually. Yeah. You just want to use CLIs" [21:43]. Peter concludes: "That's the future" [21:53].

## Key Takeaways

- Peter chose Codex over Claude Code because it examines more files before making changes, despite being slower
- Instead of git worktrees, he uses multiple repository checkouts on main to minimize cognitive complexity
- By converting MCPs to CLIs via makeporter, OpenClaw avoids MCP's limitations while maintaining compatibility with the ecosystem
