# Bug Bounty 1

## Guidance for admins/helpers giving hints
- You just need to overwrite `number` to anything other than `0xcafebabe`
- Encourage them to play with different inputs, experimenting with how it looks in the printed stack visualization (gets displayed every time you run the challenge)
- Where is `number` relative to `name` in memory? (look at stack visualization)
- Encourage them to think about what happens if the input is larger than the `name` array. Where will the extra characters/bytes go?

# Solution
Send more than 40 bytes to overwrite `number` to anything other than `0xcafebabe` (`solution.py` for reference)
