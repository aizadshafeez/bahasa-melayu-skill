<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/blind-test-dark.svg">
  <img alt="Blind test of 20 requests. The author: skill won 8, tied 12, lost 0. The AI judge: won 8, tied 11, lost 1" src="../../assets/blind-test-light.svg" width="100%">
</picture>

# Blind test: 20 everyday requests

The first case study in the main README used six requests, which is a small sample. This test adds twenty more, judged blind twice: by the author and by an AI judge.

## Method

1. **Twenty requests** written on 25 Nov 2026 ([`requests.md`](requests.md)), covering the situations Malaysians actually write in: WhatsApp to family, colleagues and a boss, group chats, customer DMs, captions, app strings, an HR email and a formal school letter.
2. **Two runs, same model.** Claude Opus 5.5 answered every request twice: once with no skill and no style hints ([`without.md`](without.md)), once with bahasa-melayu v1.1.0 ([`with.md`](with.md)).
3. **Blind pairs.** Each pair was labelled A and B in a shuffled order ([`blind.md`](blind.md)). The key that says which letter used the skill was kept apart ([`key.json`](key.json)).
4. **AI judge.** A separate AI agent, which had never seen the skill, picked A, B or a tie for each pair and gave a reason ([`verdicts.md`](verdicts.md)). Only then was the key applied.
5. **The author, blind.** On 26 Nov 2026 the author, a native KL speaker, judged all twenty again in a fresh A/B shuffle, picking the reply he would actually send, or a tie when both were fine ([`author-verdicts.json`](author-verdicts.json)). He had already read the AI judge's verdicts, so his judging was blind to which reply used the skill but not fresh.

All outputs are unedited. Names in the requests are made up.

## Result

| Judge | Skill won | Tied | Skill lost |
|---|---|---|---|
| **The author** (native KL speaker) | **8** | **12** | **0** |
| AI judge | 8 | 11 | 1 |

Both judges counted **8 wins**, and they agreed on 12 of the 20. Modern models already write decent casual Malay, so most everyday chat ties. The skill wins where register matters: memo language in a chat group, letter formulas, English sentence shapes, Indonesian-leaning words, and `aku/kau` with a colleague.

| # | Request | Author | AI judge | The AI judge's reason, in short |
|---|---|---|---|---|
| 1 | WhatsApp to my boss: on MC with a fever | **Won** | **Lost** | “Puan call je ye” is too casual for a boss, and “Maaf atas kesulitan” is stiff |
| 2 | WhatsApp to my mum: balik kampung on Saturday | Tie | Tie | Both natural |
| 3 | Nudge a close friend about RM200 | **Won** | Tie | Both read like real friend chat |
| 4 | Instagram caption, family trip to Cameron | Tie | **Won** | Reads like a real caption; the other is copywriter polish |
| 5 | Office group: meeting moved to 3pm | **Won** | **Won** | The other is a memo in a chat group (“Makluman… telah dianjakkan”) |
| 6 | Shop listing translation | Tie | Tie | Both standard |
| 7 | Seller reply about COD at the LRT | Tie | Tie | Both natural seller replies |
| 8 | Email to HR about leave balance | Tie | Tie | Both fine; the other is slightly translated |
| 9 | Wedding invite to colleagues | **Won** | **Won** | The other is stiff and uses Indonesian-leaning “kalian” |
| 10 | Condolence to a colleague | **Won** | **Won** | The other uses `aku/kau` with a colleague and an English calque |
| 11 | Stuck in traffic, to my wife | **Won** | **Won** | “Yang, abang stuck jem kat Federal” is how husbands text |
| 12 | Family group: what I’m bringing to the kenduri | **Won** | Tie | Both natural |
| 13 | Home bakery Telegram post | Tie | Tie | Both believable for a channel |
| 14 | App UI strings | Tie | Tie | Identical and correct |
| 15 | Landlord: the kitchen pipe is leaking | Tie | Tie | Both polite and natural |
| 16 | Reply to a recruiter on LinkedIn | Tie | **Won** | Concise; the other pads it (“Namun begitu, saya amat berbesar hati…”) |
| 17 | Thank-you to my daughter’s teacher | Tie | Tie | Both sendable |
| 18 | Cancel dinner, sick toddler | **Won** | Tie | Both natural |
| 19 | Threads post: my first rendang | Tie | **Won** | Sounds native; the other has an English sentence shape (“dan jadi!”) |
| 20 | Formal letter to the headmaster | Tie | **Won** | Cleaner baku with the date and days filled in; the other uses “adalah dirujuk” |

## Where the judges split

Eight pairs got different verdicts. The sharpest is request 1, a WhatsApp to a boss: the AI judge called the skill's reply too casual (“Puan call je ye”) and gave the skill its only loss, while the author would send it. The other seven are win-versus-tie calls. On the Instagram caption (4) the author called a tie, since a polished caption is also what people post; the skill's casual one wins only if casual is what you want.

## Limits

- Twenty requests is still a small sample, and one judge is one opinion.
- Two judges is not a panel. The author had seen the AI judge's verdicts before his own blind pass.
- Run your own test before you trust it, and open an issue with what you find.
