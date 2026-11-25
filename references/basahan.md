# Bahasa Basahan: Everyday Malaysian Malay (KL/Selangor default)

*Bahasa basahan* is everyday colloquial Malay. It is not *bahasa pasar*, which is the pidgin Malay that grew between Malay and non-native speakers.

The Malay Malaysians actually type in WhatsApp, Telegram, IG and Threads, and speak at home, at the mamak and in the office pantry. DBP treats this register as non-standard, so most rules here come from linguistics and native usage. Explanations are in English; examples are in Malay.

## Source key

| Key | Source |
|---|---|
| [MP] | Yusoff, Tan, Chen, Liu & Chen (2026), "Can Large Language Models Handle Discourse Particles? A Case Study of Colloquial Malay" (MalayPrag), arXiv:2605.28782, https://arxiv.org/html/2605.28782. Covers **kan** and **ke** only. Data: Reddit and X. Finding: LLMs average 43% accuracy at choosing ke/kan/none from raw text. |
| [LAH] | Ismail & Sarudin (2023), systematic review of *lah* (102 interpretations), GEMA Online 23(1):261–290; Goddard (1994) "The meaning of lah", *Oceanic Linguistics*; Jaafar (UKM), "-lah" functions: softening, confirming, emphasising, intensifying, expressing. Seen via abstracts only. |
| [KV] | "Klang Valley Malay" utterance-final particle study, *Wacana* vol. 19 iss. 2, scholarhub.ui.ac.id/wacana/vol19/iss2/2 (abstract only). |
| [CS] | Code-switching: "Code-switching in Kuala Lumpur Malay: The 'Rojak' Phenomenon" (U. Hawai'i ScholarSpace); Treffers-Daller, Majid, Yap & Flynn (2022), *Languages* 7(4):299 (frequent function-word switches); Alinda Abdul Rashid, UM thesis (intra-sentential switching dominates). Abstracts only. |
| [ME] | Malaysian English particle studies: Tay et al. (2016); Kuang (2017), *J. Modern Languages* (lah, ah, hah); Mohamad (UPM), Chinese Malaysian youth on Facebook (lah, lor, leh most frequent); Ting, Then & Ong, Kuching shops (la 62%, lor 28%). Abstracts only. |
| [NORM] | Malay social-media text-normalisation work (UM PhD thesis on Malay tweets; UKM rule-based normaliser; manglish-nlp docs listing dgn → dengan, utk → untuk). |
| [NK] | Native KL/Selangor speaker knowledge. **Most of this file.** No published source describes these to this level. |

---

## 0. Five rules that matter most

1. **Particles are seasoning, not grammar.** Real chat has one particle every one to three messages, not one per clause. A short reply often has none ("Ok, nanti aku call."). A message with four particles reads like someone performing Malaysian [NK].
2. **Drop the formal words before adding slang.** Getting rid of `tidak`, `sahaja`, `sudah`, `hendak`, `tersebut` and `bagaimana` does more for naturalness than adding `lah`.
3. **Match the other person.** Copy their pronouns, their level of English and their abbreviation density.
4. **Malay frame, English content words.** In KL code-switching, the grammar and particles stay Malay while nouns and verbs switch [CS; NK].
5. **Don't stack regional markers.** Default is KL/Selangor; use northern or Kelantan forms only when asked.

---

## 1. Discourse particles

Position notation: **F** = sentence-final, **P** = right after the focused word or phrase, **I** = initial.

| Particle | Core meaning and tone | Position | Natural examples | Notes |
|---|---|---|---|---|
| **lah / la** | Softens commands and offers; adds emphasis or certainty; also resignation or exasperation [LAH] | P or F | `Jom la makan dulu.` / `Takpe la, esok je.` / `Memang best la tempat tu.` / `Apa la kau ni.` | In chat, `la` is more common than `lah`. It attaches to the word being stressed: `Esok la kita pergi` (stress on esok). Overused = fake. |
| **kan** | "Right?": presents the point as shared knowledge and asks for light agreement [MP] | F (tag), I, or after the subject | `Dia dah makan, kan?` / `Kan aku dah cakap.` / `Kau cuti esok kan?` | **Final tag is the most common** (`Kau cuti esok kan?` over `Kau kan cuti esok?`). "Like I said / told you so" puts kan **first**: `Kan aku dah cakap`, not `Aku kan dah cakap`. After the subject is also used to give a reason everyone should know: `Dia kan sakit, tu yang tak datang`. (Corrected by native review, 25 Nov 2026.) |
| **ke** | Yes/no question marker for genuine uncertainty; "or" between options; rhetorical challenge [MP] | F or P | `Kau marah ke?` / `Nak teh ke kopi?` / `Ni ke yang kau kata sedap?` | The everyday question marker; replaces baku `-kah`. Sabah/Sarawak/northern spelling: `ka`. |
| **je / aje / jer** | "Just / only"; minimises to soften | P | `Sikit je lagi.` / `Tanya je.` / `Aku ada RM20 je.` | `jer` = chat spelling; `aje` a bit older or southern. Very high frequency, sounds natural almost anywhere casual. |
| **pun / pon** | "Also / even"; narrative "then, so"; concessive | P | `Aku pun tak tahu.` / `Dia pun balik.` / `Mahal pun takpe.` | `pon` = chat spelling. |
| **kot / kut** | Hedge: "probably, I guess" | F | `Dia dah sampai kot.` / `Esok hujan kot.` | Not for facts you're sure of. |
| **eh** | Surprise, sudden recall, mild self-correction; soft tag | I or F | `Eh, kau dah sampai?` / `Eh lupa, esok cuti.` / `Best eh?` | |
| **ek / eik** | Soft "okay? / right?": friendly confirmation | F | `Nanti call ek.` / `Esok pukul 8 ek?` | Warmer than `kan?`; common with customers and spouses. |
| **tu / ni** | Demonstratives after the noun; also sentence-final emphasis on the situation | after N, F | `Meeting tu cancel.` / `Dah lambat dah ni.` / `Ni nak tanya sikit.` | `tu/ni` replace `itu/ini` in all casual text. |
| **dah … dah** | Completion; a repeated final `dah` adds emphasis | P and F | `Aku dah siap dah.` / `Dah makan dah.` | The double `dah` is natural in speech and chat. |
| **ah / a** | Topic marker; insistence; questioning tone | P or F | `Ah, malas aku nak pergi.` / `Aku malas ah nak pergi.` / `Cepat ah!` / `Betul ah?` | Natural placements: sentence-initial `Ah,` or right after the word it stresses (`malas ah`). `Aku ah, malas…` is unnatural (native review, 25 Nov 2026). `a` in chat (`best a`). Can sound blunt. |
| **weh / wei / woi** | Calling attention among friends; also emphasis | I or F | `Weh, jom lepak.` / `Penat la wei.` / `Gila ah wei.` | Peers only. Never to parents, elders, bosses or customers. `woi` = rough. |
| **pulak / pula** | Surprise at the unexpected; "of all things"; pushback | P | `Hujan pulak.` / `Kenapa pulak?` / `Aku pulak yang kena.` | Very native; AI almost never uses it. |
| **gak / jugak** | "Also", "quite", or insistence | F | `Best gak.` / `Aku nak gak!` / `Boleh gak.` | `Boleh gak` = "that works, actually". |
| **tau / tahu** | "You know": warning, teasing, affection | F | `Mahal tau benda ni.` / `Jangan lupa tau.` / `Aku merajuk tau.` | Warm or cheeky; common in family and couple chats. |
| **meh (Malay)** | From `mari`: "come / let me" | I | `Meh sini.` / `Meh aku tolong.` | **Different word** from the Cantonese `meh`. |
| **meh (Manglish)** | Incredulous "really?" (Cantonese origin) [ME] | F | `Ye ke? Tak caya meh.` | Mostly Chinese-Malaysian English; Malay speakers use it jokingly. Rare in Malay text. |
| **lor** | Resigned "that's just how it is" (Chinese origin) [ME] | F | `Takde lor.` / `Kau pergi je lor.` | Urban KL Malays use it playfully; one per conversation at most. |
| **mah / ma** | "Obviously" (Chinese origin) [ME] | F | `Aku dah cakap mah.` | Avoid in Malay unless writing a Chinese-Malaysian voice. |
| **doh / dowh** | Youth emphatic "man!" | F | `Best doh.` / `Penat dowh.` | Gen Z, KL/Selangor. Sounds like a try-hard if an "adult" uses it. |
| **ye / ya** | Soft polite "yes / okay?" | F | `Terima kasih ye.` / `Nanti saya pos esok ye.` | The particle that makes service Malay sound friendly. |
| **kejap / jap** | "A moment" | F or I | `Jap, aku check.` / `Tunggu kejap.` | Replaces `sebentar`. |

### 1.1 Combinations that occur
`je la` (Takpe je la), `la kan`, `kan?` after `je` (Sikit je kan?), `ke tak`, `ke apa` (Kau sakit ke apa?), `la wei`, `pun la`, `tau tak`, `dah la` ("enough / forget it": Dah la, malas aku), `kot la`, `je pun` (Seringgit je pun = "it's only a ringgit"), `pulak dah` (Hujan pulak dah) [NK].

### 1.2 Combinations that sound fake
- `lah` + `kan` + `ke` in one short sentence: ✗ `Betul lah kan ke?`
- Ending every sentence in `lah`: ✗ `Saya okay lah. Esok saya datang lah. Terima kasih lah.`
- `lah` on formal-register words: ✗ `Sudah tentulah, saya akan menghantarnya lah.`
- Particles inside full baku sentences: ✗ `Saya tidak dapat hadir lah.` → ✓ `Saya tak dapat datang la.`

### 1.3 ke vs kan vs none [MP]
| Speaker's stance | Use | Example |
|---|---|---|
| Unsure, genuinely asking | ke | `Kedai tu buka ke hari ni?` |
| Believes it; wants a nod | kan | `Kedai tu buka hari ni, kan?` |
| Surprised or annoyed | ke (often + pulak) | `Tutup ke? Ish.` / `Ni ke harga dia?` |
| Plain statement | none | `Kedai tu buka hari ni.` |

---

## 2. Contractions and short forms

| Full | Spoken & typed | Chat-only spelling | Notes |
|---|---|---|---|
| tidak | tak | x, tk | `x` is chat-only, very common [NORM; NK] |
| sudah | dah | dh | |
| hendak | nak | nk | |
| sahaja | je, aje | jer | |
| dekat (at/to) | dekat, kat | kt, dkt | `Aku dekat rumah.` / `Bagi kat dia.` Adult KL chat often keeps `dekat` in full (§9 data: dekat about 4× more than kat). |
| bagaimana | macam mana, camne | cmne, camna | |
| mengapa / kenapa | kenapa, apsal, asal | npe, knp | `apsal/asal` = blunt, friends only |
| tidak apa | takpe, tak apa | xpe | |
| tiada | takde, tak ada | xde | |
| itu / ini | tu / ni | | |
| sedikit | sikit | | |
| mari kita | jom | | |
| selepas itu | lepas tu, pastu | lps tu | |
| sebab | sebab | sbb, sbab | |
| dengan | dengan, ngan | dgn | [NORM] |
| yang | yang | yg | [NORM] |
| untuk | untuk | utk | [NORM] |
| tetapi | tapi | tp | |
| boleh | boleh | blh | |
| macam | macam, cam | mcm | |
| sekarang | sekarang | skrg | |
| orang | orang | org | |
| kau orang / kami orang / dia orang | korang / kitorang / diorang, dorang | | |
| cerita | cerita, citer | | |
| ambil | ambik | | |
| tengah (in progress) | tengah | tgh | `Aku tengah drive.` |
| kena | kena | | passive or obligation: `kena marah`, `kena bayar dulu` |
| buat apa | buat apa, buat pe | wat pe | |
| terima kasih | terima kasih, thanks | tq, tqvm, ty | |
| reduplication | sama-sama | sama2, hati2 | the `2` is chat-only |

Density guide [NK]:
- Gen Z or close friends: heavy abbreviation (`x`, `dh`, `nk`, `yg`).
- Adults with family: moderate (`tak`, `dah`, `nak`, few letter-drops).
- Colleagues: light (`tak`, `dah`, `nak`, otherwise full words).
- Older relatives often write more fully, sometimes in mixed baku.

---

## 3. Simplified grammar

| Baku | Basahan | What changed |
|---|---|---|
| Dia sedang makan. | Dia tengah makan. | `tengah` for `sedang` |
| Saya sudah siap. | Aku dah siap. | pronoun + `dah` |
| Saya akan menelefon awak nanti. | Nanti aku call. | prefix dropped, English verb, object dropped |
| Adakah awak sudah makan? | Dah makan? / Kau dah makan ke? | `adakah` dropped; `ke` or rising tone |
| Bolehkah awak tolong saya? | Boleh tolong tak? / Tolong jap boleh? | `-kah` → `tak` tag |
| Saya hendak pergi ke kedai. | Nak pergi kedai jap. | subject and `ke` dropped |
| Dia dimarahi oleh bosnya. | Dia kena marah dengan bos dia. | `kena` passive; `-nya` → `dia` |
| Rumahnya besar. | Rumah dia besar. | `dia` replaces possessive `-nya` |
| Saya tidak tahu. | Tak tahu. / Entah. | subject dropped |
| Mengapa awak tidak datang? | Kenapa tak datang? / Apsal tak datang? | |
| Di mana awak? | Kat mana? / Kau kat mana? | |
| Apa yang awak buat? | Buat apa tu? | |

Rules [NK]:
- Drop the subject when context makes it obvious (very common).
- Question forms: rising tone with no marker (`Dah makan?`), `X ke?`, `X tak?` (`Nak ikut tak?`), tag `kan?`.
- meN- is often dropped: `aku tengok`, `dia jual`, `nak beli`. Keep it in set words that are natural even casually (`menyampah`, `menyibuk`).

---

## 4. Pronouns by relationship

| Relationship | Self | Other | Example |
|---|---|---|---|
| Close friends, same-age siblings | aku | kau (spoken), ko (typed) | `Ko kat mana? Aku dah sampai.` |
| Urban KL peers, colleagues, some couples | I | you | `I dah sampai, you kat mana?` |
| Polite peers, new acquaintances, early dating | saya | awak | `Awak dah makan?` |
| Husband → wife | abang / saya / I / name | sayang, yang, awak, you, name | `Yang, abang balik lambat sikit, meeting habis lambat.` |
| Wife → husband | saya / sayang / name / I | abang, bang, b, you | `Bang, nanti singgah beli susu Aisyah ye.` |
| Child → parent | adik / along / kakak (birth-order name) / saya | mak, ibu, mama, abah, ayah, papa | `Mak, adik dah sampai KL.` |
| Parent → child | mak / abah / ayah | name, adik, along, angah | `Ayah dah transfer duit, check ye.` |
| To older stranger or service staff | saya | abang/bang, kakak/akak/kak, pakcik, makcik | `Bang, teh o ais satu.` / `Kak, yang ni berapa?` |
| To younger stranger | saya / abang / akak | adik, dik | `Dik, ada saiz M?` |
| Seller → customer (online shop) | saya, kami, admin | sis, akak, bro, abang, tuan/puan, cik | `Hai sis, stok ada lagi ye 😊` |
| Customer → seller | saya | sis, bro, admin, boss | `Sis, boleh COD tak?` |
| Employee → boss (WhatsApp) | saya | Encik/Puan + name, Datuk, boss (if they invite it) | `Baik Encik Hafiz, saya update petang ni.` |
| Plurals | kitorang (we, excluding), kita (inclusive) | korang, diorang | `Korang nak makan mana?` |

Rules [NK]:
- `aku/kau` to elders, bosses or customers is rude.
- `kamu` to an adult peer sounds teacherly.
- `anda` in any personal message sounds like a bank SMS.

### 4.1 Same message, three recipients
- **Wife:** `Yang, abang on the way. Nak abang beli apa-apa tak?`
- **Customer:** `Hai cik, parcel dah pos pagi tadi ye. Tracking no: JX123… Terima kasih support 😊`
- **Boss:** `Salam Encik Hafiz, saya dah hantar laporan ke e-mel. Kalau ada apa-apa nak ubah, bagitau ye.`
- **Friends group:** `Weh aku otw. 10 minit lagi sampai.`

---

## 5. Code-switching (bahasa rojak)

Research shows intra-sentential switching dominates. Malay–English switching also involves unusually frequent function-word switches such as I/you [CS]. In KL Malay the pattern is: **Malay grammar, particles and affixes; English nouns and verbs** [NK].

| Natural (KL) | Why it works |
|---|---|
| `Meeting tu postpone ke Khamis.` | English noun and verb, Malay frame |
| `Aku dah submit dah.` | Malay aspect + English verb + Malay particle |
| `Dia kena cancel last minute.` | `kena` passive on an English verb |
| `Nanti I forward kat you.` | I/you + English verb + `kat` |
| `So far okay je.` | discourse markers like so, actually, anyway, basically |
| `Boleh confirmkan by today?` | Malay suffix on an English root (`confirmkan`, `di-cancel`, `ter-delete`) |
| `Sorry lambat reply.` | sorry, thanks, noted, ok are near-universal |
| `Tengah on the way.` / `OTW.` | fixed English chunks |
| `Rasa macam overthinking pulak.` | English abstract term inside a Malay clause |

| Forced or unnatural | Fix |
|---|---|
| `Makanan tu very sedap.` | `Sedap gila makanan tu.` (Malay adjectives with Malay intensifiers) |
| `Saya akan proceed dengan permohonan tersebut.` | `Saya proceed la dulu.` / formally: `Saya akan teruskan permohonan ini.` (don't mix formal Malay with English verbs) |
| `Dia sangat excited untuk join kita punya event.` | `Dia excited gila nak join event kita.` |
| Long English sentence + one Malay word | Pick one language per clause |
| Switching where Malaysians never do: `Saya pergi ke the mosque.` | `Aku pergi masjid.` |

Words almost always said in English in KL chat [NK]: meeting, submit, confirm, cancel, postpone, update, check, deadline, slot, booking, settle, follow up, on, otw, sorry, thanks, noted, ok, actually, anyway, so, by the way, last minute, parking, traffic jam (`jam`), weekend, office, boss, client.

Words that stay Malay [NK]: food words (`sedap`, `makan`, `lapar`), family terms, religious terms, emotions in close relationships (`rindu`, `sayang`, `penat`, `geram`, `menyampah`).

---

## 6. Common expressions and fillers

| Word | Meaning | Example |
|---|---|---|
| alamak | "oh no" (mild) | `Alamak, tertinggal wallet.` |
| aduhai | theatrical sigh | `Aduhai, jem teruk hari ni.` |
| adoi / aduh | ouch; "ugh" | `Adoi, sakit kepala.` |
| fuh / fuyoh | impressed | `Fuyoh, kereta baru!` |
| best | great, enjoyable | `Best tak movie tu?` |
| syok | really enjoyable | `Syok gila main hujan.` |
| gempak | spectacular | `Gempak konsert semalam.` |
| padu | solid, excellent | `Padu la presentation kau.` |
| terer / terror | skilled | `Terer betul dia masak.` |
| kantoi | caught out | `Kantoi ponteng.` |
| lepak | hang out | `Jom lepak mamak.` |
| mamak | Indian-Muslim 24h restaurant | `Mamak biasa?` |
| ambik | take (casual spelling) | `Ambik je la.` |
| takpe la | never mind (gracious or resigned) | `Takpe la, next time.` |
| no hal | no problem | `No hal bro.` |
| sat | a moment (northern; widely known) | `Sat, aku tengok.` |
| nanti roger / roger | keep me posted | `Dah sampai nanti roger.` |
| on | I'm in | `Futsal malam ni? On.` |
| gila / giler | intensifier "super" | `Mahal gila.` |
| cun | pretty, nice | `Cun baju ni.` |
| sempoi | chill, simple | `Orang dia sempoi je.` |
| member | friend | `Member aku kerja situ.` |
| poyo | lame show-off | `Poyo la dia ni.` |
| menyampah | annoyed, can't stand it | `Menyampah aku tengok.` |
| geram | annoyed, or "so cute I can't stand it" | `Geramnya tengok baby ni.` |
| usha | check out, eye | `Aku usha je dulu.` |
| otw | on the way | `Otw!` |

Religious expressions are **normal everyday Malay** for Muslim Malays, not formality [NK]:
- `InsyaAllah` (will do, God willing; also a soft "maybe")
- `Alhamdulillah` (relief or good news)
- `MasyaAllah` (admiration)
- `Assalamualaikum` (greeting, also to open a WhatsApp to elders)
- `Aamiin` (reply to a doa)
- `Takziah` (condolence)

Omitting them in a family chat can read as cold. Don't push them onto non-Muslim recipients.

---

## 7. Regional markers (avoid unless asked)

| Region | Markers | Example |
|---|---|---|
| KL/Selangor (default) | aku/ko, I/you, tak, je, la, kot, heavy English | `Ko nak gi mana?` |
| Northern (Kedah, Penang, Perlis) | hang (you), cek (I), sat (moment), pi (pergi), dok (tengah), awat (why), habaq (bagitau) | `Hang pi mana tu?` |
| Perak | kome (you), teman (I) | |
| Kelantan / Terengganu | demo/mu (you), ambo/kawe (I), gapo (apa), final -a → -o (mano, gapo) | `Mu gi mano?` |
| Negeri Sembilan | den (I), ekau (you), -o endings | |
| Sabah | bah (particle), sia (I), kamurang (korang), bilang (cakap) | `Ok bah.` |
| Sarawak | kitak (you), kamek (I), sik (tak) | `Kitak sik datang kah?` |

Everything outside the KL row is (perlu semakan): native-common markers, compressed, and dialects vary within each state. Never mix two regions in one voice.

---

## 8a. Adult chat norms, measured [CORPUS]

[CORPUS] = one native KL/Selangor adult's own WhatsApp messages, 2025–2026, analysed with consent: about 12,300 Malay messages to a spouse, a co-parent, family, an old friend, online buyers and sellers, and a hobby community. Only aggregate patterns are kept here. Every example is rewritten, not quoted. One speaker is one voice, so treat these as a well-measured default for an adult who writes "a bit proper", not as a law.

### 8a.1 Readable shortening (the key rule)
Adults shorten **long, very frequent words** by dropping vowels and keep **short core words in full**. Shortening a word that is already three letters (`nk`, `dh`, `blh`) saves almost nothing and is what makes youth text hard to read.

| Keep in full (shortened form appeared <10% of the time) | Shorten (shortened form usual) |
|---|---|
| tak, dah, nak, boleh, je, kalau, untuk, ni, tu, barang, dekat, sorry, terima kasih | sbb (sebab), tp (tapi), mcm (macam), yg (yang), td (tadi), dpt (dapat), skrg (sekarang), ckp (cakap), tgk (tengok), igt (ingat), mmg (memang); lg / nnti about half the time |

- `x` appears mainly inside fixed compounds: `xde`, `xpe`, `xnk`, `xleh`, `xtau`. On its own, `tak` beats `x` about 9 to 1.
- Never seen: `blh`, `utk`, `klu`, `nk` (as a habit), `brg`. Those belong to heavy youth or seller-group style; use them only when mirroring someone who writes that way.
- Formal words almost never appear in chat: `tidak` ≈ 0, `sudah` < 2%, `hendak` 0, `itu/ini` < 1%, `kerana` ≈ 0.

### 8a.2 Shape of a message
- First letter capitalised (83–99% of messages), **no final full stop** (91–99%). Questions often end with no `?` at all, closing on `ke`, `apa`, `mana`.
- Short bubbles: about 6 words on average to close family, 10 to buyers. Several bubbles in a row, not one paragraph.
- Emoji: rare with family (1–2% of messages), more with buyers (8%) and in public hobby groups (24%). `😂` is by far the most common; with buyers, `😁` and `😊` soften a price talk.

### 8a.3 Particles, real frequency (% of messages containing it)
| Particle | Close family | Buyers / sellers |
|---|---|---|
| dah | 11–15 | 18 |
| je | 12–15 | 16 |
| ke | 7–18 (highest with logistics questions) | 10 |
| pun | 6–7 | 8 |
| kot | 3–5 | 5 |
| la / lah | 3–6 / 1 | 5 / 3 |
| kan | 1–2 | 3 |
| ya (polite closer) | ≈ 1 | 7.5 |

So `la` is in **only about 1 message in 20**. `je`, `dah` and `ke` carry most of the colloquial feel.

### 8a.4 Laughter and warmth
- `haha` dominates (about 75% of laughs), at the start or end of a bubble. `hahahaha` for a big laugh.
- `huhu` = sheepish or rueful ("price went up, huhu"). `hehe` is rare in adult male chat; `wkwk` (Indonesian) and `lol` essentially never.
- Stretched letters for warmth, sparingly, mostly to buyers: `ooo`, `ohhh`, `tqqq`, `baikkk`, `bosss`.

### 8a.5 Openers, closers, address
- To buyers and sellers: open with `Salam` (the most common first word after `ok`/`haha`), address with `boss`, `bang` or `bro`, close with `ya`, `terima kasih` (in full more often than `tq`) or the address word: `Ok boss, saya pos esok ya`.
- In public hobby or seller groups: `saya` + `bang`/`boss`, longer messages (about 12 words), more emoji. Group trade words: `lock` (claim an item for sale: "Ni lock boss"), `PO` (pre-order), `PM`, `COD`, `pos`.
- `aah` = yes (very common reply opener). `Oh` / `Ooo` = "I see".
- With a spouse or co-parent, sentence openers are often English discourse words: `I`, `so`, `then`, `as in`, `if`, `or`, `means`, `like I said`, `basically`. `As in…` is the standard way to clarify ("As in nak jumpa kat sana ke?").
- Pronoun pairs stay fixed per person (§4). A spouse who is I/u in normal chat may switch to `aku/kau` only in a heated moment; never write that switch unless the user is drafting exactly that.

### 8a.6 Rewritten examples in this voice
- To a buyer: `Salam boss, kit tu ada lagi. Harga rm280, pos sekali. Kalau ok saya hold dulu ya 😊`
- Price talk: `Haha tu mmg harga pasaran skrg boss. Bawah 250 susah nak dpt dah`
- To a spouse: `Ok, nanti i ambil budak2 dulu then terus balik. U nak kirim apa-apa?`
- To a sibling: `Aku sampai lambat sikit, jem. Ko order dulu la`
- To a co-parent: `Sabtu ni i ambil pukul 10 ok? Then malam i hantar balik`

---

## 8. Tone ladders

**A. "I can't attend tomorrow's meeting; can we move it to Thursday?"**
1. **Very formal (letter or official email):** `Dengan hormatnya, saya ingin memaklumkan bahawa saya tidak dapat menghadiri mesyuarat esok. Sehubungan dengan itu, saya memohon jasa baik tuan untuk menangguhkan mesyuarat tersebut ke hari Khamis. Sekian, terima kasih.`
2. **Formal-friendly (email to boss):** `Salam Encik Hafiz, saya mohon maaf kerana tidak dapat hadir ke mesyuarat esok. Boleh kita anjakkan ke hari Khamis? Terima kasih.`
3. **Casual-polite (WhatsApp to boss or colleague):** `Salam Encik Hafiz, esok saya tak dapat join meeting. Boleh kita anjak ke Khamis? Maaf ye.`
4. **Close friends:** `Weh esok aku tak dapat join la. Khamis boleh tak?`

**B. "Your order has been shipped."**
1. `Dimaklumkan bahawa pesanan tuan/puan telah dihantar. Nombor penjejakan adalah seperti yang berikut: …`
2. `Pesanan anda telah dihantar hari ini. Nombor penjejakan: JX123456789.`
3. `Hai cik! Parcel dah pos pagi tadi ye. Tracking: JX123456789 😊`
4. (to a friend who bought from you) `Barang ko dah pos dah. Esok lusa sampai la tu.`

**C. "I'll be home late, don't wait for me for dinner."**
1. (not used formally)
2. `Saya akan pulang lewat malam ini. Tidak perlu tunggu saya untuk makan malam.` (sounds like a translated novel, which shows why baku is wrong here)
3. `Saya balik lambat sikit malam ni. Makan dulu ye, tak payah tunggu.`
4. (husband → wife) `Yang, abang balik lambat sikit. Makan dulu tau, tak payah tunggu abang.`
