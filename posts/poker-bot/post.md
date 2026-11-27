# Johnny's Poker Bot: LinkedIn post

Images: `poker-1.jpg` to `poker-5.jpg`, uploaded in order as one multi-image post. All are real screens: the admin, table map and big screen from a live 100-bot demo tournament run locally, and the player phone screens from the app's built-in sample mode.

## Post text

```
10,000 players. 1,251 tables. A full poker tournament played to the final hand in 80 seconds, with zero integrity alerts.

That was a simulation, but the engine underneath is the real one. It's Johnny's Poker Bot, a tournament system where the dealer and the tournament director are both software.

Players scan one QR code, type their name, and their phone becomes their seat at the table. Johnny deals, runs the blinds and the clock, splits side pots, breaks and balances tables, and runs the final table without a human dealer. Staff watch from an admin control room, and a big screen shows the event to the room.

There's no AI in the game logic, on purpose. Every deck comes from a server seed committed before registration opens, shuffled with HMAC-SHA256 and Fisher–Yates, so any player can verify a hand in their own browser once the seed is revealed.

The bug I'm proudest of finding came from bots that go all-in constantly. Whole tables busted in one hand and the last few players ended up stranded alone at separate tables. It's fixed, and a property test now replays 150 of those fields on every run.

In a 1,000-player load test across 125 tables, a player's action came back confirmed in 6 ms at the median and 76 ms at p99.

Would you trust a dealer you could audit over one you could see?

#BuildInPublic #SystemDesign #Poker #WebSockets
```

## First comment (post it yourself right after publishing)

```
Code: github.com/jnanottamgy/Poker-Bot
```

## Alt text (one per image)

1. Two phones: a player's live table with fold, call and raise buttons, and the join screen for a 2,000-player tournament.
2. The big-screen display (level clock, blinds, players left, prize pool) above the admin overview of a running 100-bot tournament.
3. The admin view of one live table on green felt, above the live map of every table in the tournament.
4. Two phones: the welcome screen with table and seat, and the "You made it: the final table" screen.
5. Admin standings with the prize ladder, above the fairness audit showing the committed server seed and hand verification.

## Sources for the numbers

- 10,000 players, 1,251 tables, 80 s, zero integrity alerts; the all-in liveness bug and the 150-field property test: `docs/TESTING.md`.
- 1,000-player load test, 125 tables, action round trip 6 ms p50 / 76 ms p99: `docs/TESTING.md`, Measured results (development container, 4 vCPU).

## Notes

- Best window: Tue/Wed/Thu, 7:30 to 9:00 AM IST.
- The phone screens show the app's sample tournament ("Spring Showdown 2026"), not a real event.
