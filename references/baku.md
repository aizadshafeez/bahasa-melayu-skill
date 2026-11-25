# Bahasa Baku — Standard Malaysian Malay (DBP)

Use for anything official: letters, formal email, reports, CVs, public notices, UI copy, academic text. Default authority is Dewan Bahasa dan Pustaka (DBP). Explanations are in English; examples are in Malay. ✗ = wrong or unnatural, ✓ = correct.

## Source key

| Key | Source |
|---|---|
| [KN:kw] | PRPM Khidmat Nasihat archive (DBP's public Q&A). URL pattern: `https://prpm.dbp.gov.my/Cari1.aspx?keyword=<kw>&d=175768`. Date in brackets = date DBP answered. Fetched 25 Nov 2026. |
| [KD] | Kamus Dewan Edisi Keempat / Kamus Dewan Perdana, as shown on prpm.dbp.gov.my |
| [TD p.N] | Tatabahasa Dewan Edisi Ketiga (Nik Safiah Karim et al.), page number as cited by DBP officers in KN answers. The book itself was not reachable (copy sites returned 403). |
| [USM] | Universiti Sains Malaysia lecture slides "Kesalahan Tatabahasa: Kesalahan Umum Penggunaan" (slidetodoc.com mirror) |
| [LMS] | i18nstack `localize-ms` skill (MIT), github.com/i18n-agent/i18nstack |
| [DBPT] | `dbp-translator-claude` skill by Chuah Kee Man (MIT), github.com/keemanxp/dbp-translator-claude |
| [NK] | Native-speaker knowledge, no source fetched. Treat as strong convention, not a DBP ruling. |
| (perlu semakan) | Unverified or sources conflict. Reason given. |

**Key finding:** DBP is looser than the school-textbook "error lists" on several points. "Sangat cantik sekali" is accepted, and so is "adalah" before an adjective phrase. Where a rule is only style, this file says so. Never call something a DBP error unless a row cites one.

---

## 1. Sentence structure

### 1.1 Subjek + predikat, four basic patterns

Ayat dasar = subjek (FN) + predikat. The predicate is one of four phrase types [TD; KN:adalah 26.09.2021].

| Pattern | Example | Linking word |
|---|---|---|
| FN + FN | Samsuri **ialah** rakan karib saya. | `ialah` (optional) |
| FN + FK | Murid-murid itu **sedang belajar**. | none, ever |
| FN + FA | Perlawanan malam ini (**adalah**) sangat penting. | `adalah` allowed, usually dropped |
| FN + FS | Kehadiran mereka **adalah sebagai** pemerhati. / Ayah **di pejabat**. | `adalah` allowed |

The pemeri rule [KN:adalah 20.09.2021, 26.09.2021; KN:seterusnya 16.05.2017]:
- `ialah` comes before FN. `adalah` comes before FA or FS.
- Neither one comes before a verb phrase.

| ✗ | ✓ |
|---|---|
| Anak lelakinya adalah seorang pemuzik. | Anak lelakinya **ialah** seorang pemuzik. |
| Manfaat seterusnya ialah dapat memupuk semangat kerjasama. | Manfaat seterusnya **dapat memupuk** semangat kerjasama. |
| Tujuan program ini adalah untuk membantu peniaga kecil. | Program ini **bertujuan membantu** peniaga kecil. (style fix, see §9) |
| Saya adalah gembira. | Saya gembira. (DBP's FA rule technically allows `adalah` here, but no native writes this; English calque of "I am happy") [NK] |

### 1.2 Ayat songsang (inverted)

Fronting part or all of the predicate is grammatical [KN:ayat songsang 22.08.2017]:
- Biasa: Murid-murid beratur di luar kelas.
- Songsang: **Di luar kelas** murid-murid beratur. (fronted FS: most natural, used everywhere)
- Songsang: **Beratur** murid-murid di luar kelas. (fronted FK: literary or emphatic)

When it sounds natural: fronted time or place adverbials (`Pada tahun 2025, ...`, `Di Malaysia, ...`), fronted adjectives for exclamation (`Cantiknya baju awak!`, `Mahal betul harga rumah sekarang.`), and the passive with a pronoun agent (§2.2). Fronted verb phrases ("Melipat baju lalu menyimpannya, kakak.") read like exam exercises, so avoid them in normal prose [NK].

### 1.3 Ayat tunggal vs majmuk

| Type | Mechanism | Example |
|---|---|---|
| Tunggal | one subject + one predicate | Kedai itu dibuka pukul 9 pagi. |
| Majmuk gabungan | `dan, atau, tetapi, lalu, sambil, malah, serta` | Dia menelefon saya **lalu** meminta maaf. |
| Majmuk pancangan relatif | `yang` | Pelanggan **yang** membuat tempahan awal akan mendapat diskaun. |
| Majmuk pancangan komplemen | `bahawa`, `untuk` | Syarikat mengumumkan **bahawa** harga akan naik. |
| Majmuk pancangan keterangan | `kerana, apabila, jika, walaupun, supaya, sehingga` | **Walaupun** hujan, majlis tetap berjalan. |

**Pairing rule:** with `walaupun` / `meskipun`, use a comma and drop `tetapi` / `namun` [KN:beliau 11.07.2016; TD p.253]:
- ✗ Walaupun beliau sangat kaya tetapi beliau sangat kedekut.
- ✓ Walaupun beliau sangat kaya, beliau sangat kedekut.

**`Dan` at sentence start:** DBP says `dan` joins clauses and is not used to open a sentence; `dengan` can open one ("Dengan hormatnya…") [KN:justeru 17.04.2009].

---

## 2. Hukum D-M (Diterangkan-Menerangkan)

The head (D) comes first and the modifier (M) follows: `Restoran Hasanah, kereta Proton, guru bahasa` [KN:hukum DM 09.05.2011].

| ✗ (M-D, English order) | ✓ (D-M) |
|---|---|
| cili sos | sos cili [USM] |
| Jaya Klinik | Klinik Jaya [USM] |
| lain-lain hal | hal-hal lain [USM] |
| pengguna-mesra | mesra pengguna [LMS] |
| panjang-jangka | jangka panjang [LMS] |
| Ali Bakeri / KL Kopitiam (signboards) | Bakeri Ali / Kopitiam KL [NK, same rule] |

**Exceptions** [KN:hukum DM 09.05.2011, 24.07.2011]: DBP allows exceptions "akibat kebiasaan penggunaan, terutama pada jawatan", for example `perdana menteri`.
- The same pattern covers titles: `timbalan menteri`, `naib canselor`, `timbalan pengarah` [KN:timbalan 22.12.2009 confirms "Timbalan Menteri Kesihatan"]. The general rule for other titles is (perlu semakan): DBP names only "perdana menteri" explicitly.
- Quantifiers and determiners that precede the noun are not D-M violations: `sesuatu perkara`, `beberapa orang`, `semua pelanggan`, `pelbagai barang`, `setiap hari`. They are kata bilangan or penentu, not modifiers [NK, standard TD teaching].
- Borrowed compounds such as `perdana menteri` and `maha guru` follow their source-language order (secondary source only, perlu semakan).
- Plural of an exception: `perdana-perdana menteri`, `Menteri-menteri Besar` [KN:perdana menteri 03.09.2019].

---

## 3. Ayat aktif / pasif

### 3.1 Passive with di- (third person or unstated agent)
`Kebakaran itu telah berjaya dipadamkan oleh pihak bomba.` [KN:oleh pihak 23.02.2023]. The `oleh + FN` can be dropped: `Dia dipukul.` [TD, cited in UKM research].

### 3.2 Passive with first- or second-person agent: no di-, no oleh
The pronoun sits directly before the bare verb [KN:pasif diri pertama; TD p.491]:

| ✗ | ✓ |
|---|---|
| Surat itu telah ditulis oleh saya. | Surat itu telah **saya tulis**. |
| Bakul itu tidak terangkat oleh saya. | Bakul itu **tidak terangkat oleh saya** is the established ter- form; with a plain verb use **tidak saya angkat**. (perlu semakan: the KN answer was read as "saya tidak terangkat", which conflicts with the aspect-before-pronoun rule below) |
| Borang ini perlu diisi oleh anda. | Borang ini perlu **anda isi**. / Sila isi borang ini. |
| Sayur-sayuran mesti disiram oleh kamu. | Sayur-sayuran mesti **kamu siram**. [KN:pasif 14.02.2011] |

Aspect words come before the pronoun: `telah saya hantar`, `akan kami semak`, `sudah awak baca?`

### 3.3 When passive is natural vs a translation habit
Natural Malay passive: topic-first, especially when the doer is obvious or unimportant.
- `Mesyuarat ditangguhkan ke minggu depan.` (natural)
- `Pesanan anda akan dihantar dalam 3 hari bekerja.` (natural)

A translation habit is a passive chain with `oleh` copied from English. Prefer active when the agent matters [DBPT]:
- ✗ Keputusan itu telah dibuat oleh pihak pengurusan selepas cadangan dikemukakan oleh jawatankuasa.
- ✓ Pihak pengurusan membuat keputusan itu selepas jawatankuasa mengemukakan cadangan.

---

## 4. Imbuhan (affixes)

### 4.1 meN- nasal rules
| Root starts with | Prefix | Note | Example |
|---|---|---|---|
| p, b, f, v | mem- | p drops | pukul → memukul, baca → membaca, fitnah → memfitnah |
| t, d, c, j, z | men- | t drops | tulis → menulis, dapat → mendapat, cari → mencari, jual → menjual |
| k, g, h, vowel | meng- | k drops | kira → mengira, guna → menggunakan, hantar → menghantar, ambil → mengambil |
| s, sy | meny- / meng- | s drops | sapu → menyapu, serta → menyertai; syor → mengesyorkan [DBPT] |
| l, m, n, r, w, y, ng, ny | me- | no change | lihat → melihat, rasa → merasa |
| one syllable | menge- | | cat → mengecat, bom → mengebom, lap → mengelap |

Rule to remember: KTSP drop (luluh) [LMS; TD]. Exceptions and traps [NK unless cited]:
- `punya → mempunyai`, not *memunyai (p does not drop).
- Consonant-cluster loans keep the cluster: `proses → memproses`, `kritik → mengkritik`, `praktik → mempraktikkan`, `struktur → menstrukturkan`.
- Meaning splits: `mengkaji` (study) vs `mengaji` (recite the Quran); `mempengaruhi` is the established DBP form.
- `untuk` + verb takes meN-: ✗ untuk muat naik → ✓ untuk **memuat naik**; ✗ untuk tukar → ✓ untuk **menukar** [LMS].

### 4.2 -kan vs -i
| Suffix | Core meaning | Pairs |
|---|---|---|
| -kan | causative or benefactive: make X, do for someone, move the object | menaikkan harga, mendekatkan kerusi, menghantarkan surat kepada |
| -i | locative or repeated: the object is the place or target | menaiki bas, mendekati pelanggan, menghadiri majlis, memasuki dewan |

| ✗ | ✓ | Source |
|---|---|---|
| bagi menyampai ucaptama | bagi **menyampaikan** ucaptama | [KN:menyampai 06.11.2015] |
| memperkasa bahasa Melayu | **memperkasakan** bahasa Melayu | [KN:memperkasakan 10.04.2016] |
| Pertimbang untuk… / Guna pemboleh ubah | **Pertimbangkan** / **Gunakan** | [LMS] |
| Anda himpunkan pasukan anda | Anda **menghimpunkan** pasukan anda | [KN:anda 03.08.2015] |
| membincangkan tentang isu itu | membincangkan isu itu / berbincang tentang isu itu | transitive verbs take no preposition [NK, TD principle] |

`memberi` vs `memberikan` [KN:memberikan 16.10.2014, 08.08.2016; TD p.191, 202]:
- `memberi` + animate recipient: `Ali memberi adiknya sebuah buku.`
- `memberikan` + the thing given: `Ali memberikan buku itu kepada adiknya.` / `memberikan taklimat kepada peserta`

`meningkatkan` vs `mempertingkatkan`: DBP answers conflict [KN:mempertingkatkan 2010–2011]. The 01.10.2010 answer says `meningkatkan` means raise quality or level, while `mempertingkatkan` means make multi-tiered. **Use `meningkatkan`** (perlu semakan; Kamus Dewan editions differ).

### 4.3 Other affixes
| Affix | Function | Examples |
|---|---|---|
| beR- | intransitive, have, state | berjalan, bersedia, berbincang, berumur, bekerja (ber+kerja), belajar (irregular) |
| memper- (-kan/-i) | make more; causative | memperbaiki, memperkenalkan, memperluas, memperoleh |
| ter- | accidental; able (with negation); superlative | tertidur, tidak terangkat, tertinggi |
| ke-…-an | abstract noun; adversative | kebersihan, keputusan, kehujanan, kesejukan |
| peN-…-an | process noun from a meN- verb | pembangunan, penyediaan, penggunaan |
| per-…-an | result or abstract noun from a beR- verb | perjalanan, persatuan, perbincangan, pertandingan |
| peN- | agent or tool | penulis, pengguna, pemadam |
| -an | result or thing | tulisan, makanan, bulanan |

The superlative cannot stack: ✗ `paling tertinggi`, ✗ `tercantik sekali`, ✗ `paling cantik sekali` [KN:sangat sekali 29.03.2010].

---

## 5. Kata ganti nama and register

| Pronoun | Use | Avoid |
|---|---|---|
| saya | default first person, all formal contexts | |
| kami | we (excluding the listener): company or team voice to customers | not for "you and me" |
| kita | we (including the listener) | not in a company-to-customer voice, where "kita" presumes too much |
| anda | impersonal "you": forms, ads, UI, public notices. DBP accepts "Bolehkah kami membantu anda?" [KN:anda 29.01.2009] | **Robotic in any one-to-one message.** No Malaysian writes "anda" to a colleague, spouse, friend or known customer; use a name, title, tuan/puan, awak or you [NK] |
| awak | polite-casual "you" between peers, couples, colleagues | to elders or superiors |
| kamu | adult to child, teacher to class, religious or exhortative ("Sembahyanglah kamu…") | to adults as an equal: sounds condescending [NK]. [LMS] calls kamu "familiar, friends"; that is Indonesian-flavoured and wrong for KL |
| engkau / kau | intimate or rude; literary | formal text |
| beliau | respected third person (elders, officials, people you honour) [KN:beliau 27.10.2014, 11.05.2015] | children or students |
| dia / ia | dia = he/she; `ia` is also valid for things ("ia" = it) [KN:ia benda] | `ianya`, always (§8) |
| baginda | royalty, prophets | anyone else |
| tuan / puan | formal "you" in letters and email; capitalise only in the salutation, lowercase mid-sentence [KN:tuan/puan] | |
| Encik / Cik / Puan + name | Mr / Ms (unmarried or unknown) / Mrs-Madam | Encik is never used alone mid-sentence as "you"; say "Encik Hafiz" or "tuan" |
| saudara / saudari | neutral formal you (letters to the public, forms) | slightly old-fashioned in 2026 email [NK] |

Titles (Datuk, Dato', Datin, Dr., Prof., Ts.) go in the address block and salutation only. In the body use "tuan/puan" or "Datuk" [KN:tuan/puan].

---

## 6. Kata sendi nama (prepositions)

| Word | Use | ✓ | ✗ → ✓ |
|---|---|---|---|
| di | physical place or direction only; written **separate** | di Sarawak, di kiri jalan | ✗ di zaman Jepun → ✓ pada zaman Jepun [USM] |
| di- (prefix) | passive verb, written **joined** | dimakan, dihantar | ✗ di makan [USM] |
| pada | time; non-physical or abstract "place"; people | pada pukul 7, pada hari Isnin, terletak pada takdir Allah [KN:pada di 18.06.2026], harta digunakan pada jalan yang benar [KN 27.10.2026] | |
| ke | to (place, direction, time) | ke Pulau Pinang, dari semasa ke semasa | ✗ ke tiga → ✓ ketiga; ✗ kearah → ✓ ke arah [USM] |
| kepada | to a person or abstract recipient | hantar kepada pelanggan | ✗ hantar ke Encik Ali |
| dari | from: place, time, direction | Encik Roslan dari Jabatan Alam Sekitar; dari pukul 12; dari segi, dari sudut [KN:dari daripada 24.01.2019] | |
| daripada | from: person or source; material; comparison; part of a whole; change | surat **daripada** JAS; diperbuat daripada kulit; lebih mahal daripada; bangun daripada tidur; ambil wang daripada mesin ATM [KN:dari daripada 20.09.2018, 30.07.2012; KD] | ✗ ibrah dari Perang Badar → ✓ ibrah daripada Perang Badar [KN 23.07.2021] |
| dalam | abstract scope, no physical space | dalam hal ini, dalam dunia hari ini | ✗ di kalangan → ✓ **dalam kalangan** [KN:dalam kalangan 21.01.2012] |
| di dalam | inside a physical space | disimpan di dalam beg [KN:di dalam 27.02.2026] | |
| antara … dengan | between two | antara Ali **dengan** Abu [KN:antara dengan 28.05.2025] | ✗ antara Ali dan Abu |
| untuk / bagi | purpose: interchangeable | asrama untuk/bagi penuntut | allotment: only `untuk`, so ✗ Hadiah itu bagimu → ✓ untukmu [KN:bagi untuk 26.05.2024] |
| melalui | via (link, channel) | maklumat boleh didapati **melalui** pautan ini [KN:tersebut 17.09.2025] | ✗ di pautan |

Rule of thumb: `dari` answers "from where or when?"; `daripada` answers "from whom, from what, or compared to what?" [KN; TD p.265].

---

## 7. Kata hubung and penanda wacana

| Word | Status in modern writing |
|---|---|
| dan, atau, tetapi, kerana, jika, supaya, apabila | neutral, always fine |
| namun / namun begitu | fine, slightly formal |
| walaupun …, (no tetapi) | fine (§1.3) |
| oleh itu / oleh sebab itu | fine; DBP prefers "oleh yang demikian" in formal contexts [KN:justeru 17.04.2009] |
| justeru | **Caution.** DBP (21.11.2013) says `justeru` means *malahan, bahkan* or *kebetulan*, **not "oleh itu"**, while a 2019 answer allows it at sentence start [KN:justeru]. Widely used as "therefore" in media. (perlu semakan: Kamus Dewan Perdana 2020 may record the newer sense.) Safest: use `oleh itu`. |
| walau bagaimanapun | correct but stiff; SPM-essay flavour. Once per document at most |
| di samping itu, selain itu, seterusnya, tambahan pula | correct; in a chain they read as a school essay (see malay-ai-tells.md) |
| sehubungan dengan itu, berhubung dengan perkara di atas | letter-only formulas; fine there, stiff anywhere else |
| bila (as "when", conjunction) | baku: `bila` is a question word, `apabila` is the conjunction [NK, standard teaching] |
| yang mana / di mana (relative) | **Wrong** (§8) |

Comma conventions [LMS, partly NK]: no comma before `dan` / `atau` in a two-item list. Put a comma after a fronted subordinate clause (`Jika hujan, …`). [LMS] also suggests a comma before `yang`; that is wrong (its own example "Fail yang anda pilih" has none) [NK].

---

## 8. Plurals, penjodoh bilangan, kata ganda

### 8.1 No double plural
Reduplication marks the plural only when nothing else does [KN:penggandaan jamak; KN:sebarang; KN:para 13.05.2008]:

| ✗ | ✓ |
|---|---|
| banyak buku-buku | banyak buku |
| semua murid-murid | semua murid |
| para guru-guru / para-para pendidik | para guru / para pendidik |
| sebarang buku-buku | sebarang buku |
| 5 fail-fail | 5 fail [LMS] |
| beberapa pelanggan-pelanggan | beberapa pelanggan |

Allowed: `kami semua`, `mereka semua` (DBP 2020: here `semua` means "all of", not number) [KN:semua 18.05.2020]. A 2012 answer disagrees (perlu semakan; the 2020 ruling is newer).

Redundancy DBP flags: `pelbagai jenis barang` → `pelbagai barang`, since `pelbagai` already means "beberapa jenis" [KN:pelbagai 26.08.2013]. Also `bunyi dentam-dentum yang berulang-ulang` → drop `yang berulang-ulang` [KN:tersebut 30.07.2022].

### 8.2 Penjodoh bilangan
| Classifier | For | Example |
|---|---|---|
| seorang | people | seorang pelanggan |
| seekor | animals | seekor kucing |
| sebuah | large or composite objects: house, car, book, company, system [KN:penjodoh bilangan 09.10.2023] | sebuah syarikat |
| sebiji | round or small objects, fruit, cups | sebiji epal, sebiji cawan |
| sekeping | flat, thin: paper, photo, slice, land | sekeping gambar, sekeping tanah |
| sehelai | sheet or strand: cloth, paper, hair | sehelai baju |
| sebatang | long: pen, tree, road, river | sebatang jalan |
| sepucuk | letters, guns | sepucuk surat |
| sekuntum | flowers | sekuntum bunga mawar |
| seutas | chain, rope | seutas rantai |
| sebentuk | ring | sebentuk cincin |

DBP: not every noun has one, so don't force it [KN:penjodoh bilangan 11.04.2020]. In basahan, `satu` replaces most of them ("beli satu kereta").

### 8.3 Kata ganda
- Penuh: `buku-buku`, `cantik-cantik belaka` [KN:penggandaan jamak]
- Berentak: `sayur-mayur`, `kuih-muih`, `lauk-pauk`, `warna-warni`, `gunung-ganang`
- Separa (literary): `dedaun`, `lelangit`
- `kedua-dua` (both), not `kedua` (second): ✗ Kedua ibu bapa saya → ✓ Kedua-dua ibu bapa saya [USM]
- `mana-mana`: "anywhere" = `di mana-mana sahaja`, not `di mana sahaja` [KN:di mana 20.08.2015]

---

## 9. DBP-flagged errors and calques (high frequency)

| ✗ | ✓ | Status |
|---|---|---|
| **Ianya** penting untuk… | **Ia** penting untuk… | DBP error. "ia" + "-nya" double the pronoun [KN:ianya 20.03.2015, 30.04.2019]. Kamus Dewan Perdana records "ianya" only as observed usage; Tatabahasa Dewan doesn't list it [KN:ianya 26.08.2022] |
| Buku ini penting **di mana** ia menjadi rujukan… | Buku ini penting **kerana** ia menjadi rujukan… | DBP error: `di mana` and `yang mana` as relatives are direct translations of where/which; `di mana` is only a question word. Exception: established peribahasa ("Di mana ada kemahuan…") [KN:di mana 29.08.2013] |
| Rumah **di mana** saya dibesarkan | Rumah **tempat** saya dibesarkan / Rumah yang saya diami sejak kecil | same ruling |
| Pilih **yang mana** sesuai | Pilih yang sesuai | same ruling |
| di kalangan pelajar | dalam kalangan pelajar | DBP error [KN] |
| paling cantik sekali / tercantik sekali | paling cantik / tercantik / cantik sekali | DBP error [KN:sangat sekali] |
| sangat cantik sekali | ✓ accepted by DBP; amat/sangat/sungguh/begitu + sekali are fine [KN:sangat sekali 09.08.2009, 29.03.2010] | **Not an error**, though [USM] marks it wrong. Style: pick one intensifier; double intensifiers read as padding |
| Ali **adalah** seorang guru | Ali **ialah** seorang guru | DBP error (adalah before FN) |
| Perlawanan ini adalah sangat penting | ✓ grammatical (adalah + FA) [KN:adalah] | Not an error; drop `adalah` for natural prose |
| Dia **merupakan** sangat rajin | Dia sangat rajin | `merupakan` is an intransitive verb taking an FN ("Saya merupakan mahasiswa tahun kedua") [KN:merupakan 17.08.2023, 03.02.2023]; before an adjective it is wrong by its function (perlu semakan: no explicit KN row on merupakan + FA) |
| **Ia adalah penting untuk** kita menjaga alam sekitar | Kita perlu menjaga alam sekitar. / Menjaga alam sekitar penting. | DBP accepted "Ia penting untuk…" when correcting ianya [KN 30.04.2019], so it's grammatical. It is still an English dummy-"it" calque: **style rule** [DBPT; NK] |
| Saya **adalah** gembira / Saya **adalah** setuju | Saya gembira. / Saya setuju. | style / calque [NK] |
| Walaupun …, **tetapi** … | Walaupun …, … | DBP error [KN:beliau] |
| antara A **dan** B | antara A **dengan** B | DBP error [KN] |
| membincangkan **tentang** | membincangkan / berbincang tentang | error [NK, TD principle] |
| Seperti yang **sedia kita** maklum | Seperti yang **kita sedia** maklum | DBP [KN:sedia maklum] |
| pelbagai jenis produk | pelbagai produk | DBP redundancy [KN:pelbagai] |
| justeru (= therefore) | oleh itu | DBP 2013 says no; conflicting (§7) |
| Ia membuat sense / Ia masuk akal | Logik. / Munasabah. (masuk akal itself is a native idiom; the "ia" subject is the calque) | style [LMS; NK] |
| mengambil tempat (take place) | berlangsung / diadakan | calque [NK] |
| di penghujung hari (at the end of the day) | akhirnya / pada akhirnya | calque [LMS] |
| Ia adalah **satu** keputusan yang baik | Keputusan itu baik. | `satu` as the English article "a": calque [NK] |

---

## 10. Ejaan (spelling)

### 10.1 Compounds: joined vs separate
- **Joined** (kata majmuk mantap; TD lists examples, the list is not closed [KN:kata majmuk mantap 14.01.2017]): antarabangsa, beritahu, bumiputera, jawatankuasa, kakitangan, kerjasama, olahraga, pesuruhjaya, setiausaha, sukarelawan, suruhanjaya, tandatangan, tanggungjawab, warganegara, matahari, bendahari.
  Derived forms: bekerjasama, menandatangani, bertanggungjawab, memberitahu.
- **Separate:**
  - kereta api (not keretapi; gazetted names excepted) [KN:kereta api 14.09.2012]
  - kemas kini (verb `mengemas kini`; noun `pengemaskinian`) [KN:kemas kini]
  - ubah suai, sama ada, sedia maklum, telah pun [KN]
  - kaji selidik [DBPT], muat naik, muat turun, log masuk, kata laluan [LMS]
  - terima kasih, ambil alih [NK]
- **Pun:** separate when it means "juga" (`dia pun`, `telah pun`); joined in conjunctions (`walaupun`, `meskipun`, `kendatipun`, `sekalipun`) [KN:telah pun].

### 10.2 Loanword spelling (DBP pattern: English -ity → -iti, -ic → -ik, -tion → -si)
| ✗ | ✓ |
|---|---|
| kwaliti, kwantiti | kualiti, kuantiti |
| aktivity, aktivitas | aktiviti |
| pratik, dipratikan | praktik, dipraktikkan [KN:praktik 26.02.2014] |
| analisa (Indonesian-style) | analisis |
| sistim | sistem |
| nasehat | nasihat |
| resiko | risiko |
| obyektif | objektif |
| katagori | kategori |
| e-mail, email | e-mel [LMS] |

Spellings in this table without a cited ruling are [NK] (standard DBP forms, all checkable on prpm.dbp.gov.my).

`praktis` vs `praktik`: Malaysians use `praktis` loosely for "practice"; DBP's noun is `praktik`. Use `praktik` in baku, `praktis` only as the adjective "practical" (perlu semakan: no KN row found on "praktis" as a noun).

### 10.3 Capitalisation
- `perdana menteri` is lowercase as a common noun; capitalise it as a title with a name or country (`Perdana Menteri Malaysia`) [KN:perdana menteri 16.08.2023].
- `Tuan/Puan` is capitalised only in the salutation [KN:tuan/puan].
- `Yang benar,`: only the first letter is capitalised [KN:yang benar 21.12.2016].
- Titles: `Apakah yang Perlu Anda Tahu…`, with function words lowercase [KN:anda huruf besar 07.07.2014].

### 10.4 Malaysian vs Indonesian vocabulary (never mix)
| Malaysian | Indonesian (avoid) | Danger |
|---|---|---|
| perlu, memerlukan | butuh | **butuh = vulgar in Malaysia** [LMS] |
| susah, sukar | sulit | sulit = confidential [LMS] |
| pening | pusing | pusing = turn or spin [LMS] |
| belakang (body) | punggung | punggung = buttocks [LMS] |
| mudah | gampang | **gampang = "bastard", a serious insult in Malaysia** [NK] |
| bancian | sensus | banci = census in MY; in ID it's a slur for effeminate men [NK] |
| percuma (free of charge) | gratis | in ID "percuma" = in vain [NK] |
| senang (easy) / gembira (happy) | senang (happy) | MY senang = easy [NK] |
| boleh | bisa | bisa = venom [LMS] |
| polis | polisi | polisi = policy (insurance) in MY [LMS] |
| kereta | mobil | kereta = car [LMS] |
| pejabat, kakitangan, mesyuarat | kantor, karyawan, rapat | [DBPT; LMS] |
| maklumat, kerajaan, hospital | informasi, pemerintah, rumah sakit | [DBPT] |
| muat naik, muat turun, tetapan, kemas kini, padam, tampal, fail, mesej | unggah, unduh, pengaturan, perbarui, hapus, tempel, berkas, pesan | [LMS] |
| Isnin, Khamis, Jumaat, Ahad; Mac, Jun, Julai, Ogos, Disember | Senin, Kamis, Jumat, Minggu; Maret, Juni, Juli, Agustus, Desember | `Minggu` = week [LMS] |
| Amerika Syarikat, Jepun, Perancis | Amerika Serikat, Jepang, Prancis | [LMS] |
| bagaimana, mengapa, tidak, sahaja | gimana, kenapa (also MY), nggak/ngga, saja/aja | aja/nggak are dead giveaways |
| faham | mengerti | `mengerti` exists in MY but sounds Indonesian or literary [NK] |

Numbers and money: `RM1,250.50` (comma thousands, point decimal); dates `15/01/2026` or `15 Januari 2026` [LMS].

---

## 11. Surat rasmi and formal email

### 11.1 Official letter skeleton (Gaya Dewan / civil-service convention)
```
[Alamat pengirim]
Ruj. Kami : …
Tarikh    : 25 November 2026

[Nama dan alamat penerima]

Tuan/Puan,

PERMOHONAN CUTI TANPA GAJI            ← tajuk: huruf besar, tebal

Dengan hormatnya perkara di atas dirujuk.

2.   Saya ingin memohon …               ← para 2 onward numbered
3.   Bersama-sama ini disertakan …

Sekian, terima kasih.

Yang benar,                            ← general letters
   / Saya yang menjalankan amanah,     ← government letters

(tandatangan)
(NUR AINA BINTI AHMAD)
Jawatan
b.p. Ketua Pengarah                    ← if signing on behalf
```
Sources:
- Opening: "Dengan hormatnya perkara di atas dirujuk." [KN:dengan hormatnya 22.02.2013, 01.03.2010]. Also accepted: "Dengan hormatnya saya merujuk perkara yang tersebut di atas." [KN 11.06.2023], "Dengan segala hormatnya merujuk perkara di atas." [KN:perkara di atas 20.02.2023]. ✗ "Dengan hormatnya perkara di atas **adalah** dirujuk" (pemeri before a verb).
- Closing: "Sekian, terima kasih." with a comma [KN:sekian terima kasih 15.12.2021].
- Sign-off: "Yang benar" is fine for general letters; "Saya yang menjalankan amanah" is the set form for government letters [KN:yang benar 19.06.2024]. Organisations may also use "Saya yang menurut perintah" [KN 26.09.2016]. Signature block with `b.p.` per Gaya Dewan [KN:bagi pihak 06.10.2020].
- Other set phrases: "Untuk makluman tuan" / "Untuk makluman tuan juga" [KN:untuk makluman]; "Berhubung dengan perkara di atas," [KN:berhubung]; "Segala kerjasama pihak tuan saya dahului dengan ucapan terima kasih." [KN:ucapan terima kasih].
- Government letters also carry agency slogans (e.g. "BERKHIDMAT UNTUK NEGARA") above the sign-off (perlu semakan: wording varies by agency and administration).

### 11.2 Modern business email (less stiff, still baku)
Malaysian office email in 2026 is baku vocabulary with a lighter structure. Not the full letter template.

| Stiff (letter-in-an-email) | Modern, natural |
|---|---|
| Dengan hormatnya perkara di atas dirujuk. | Salam Encik Hafiz, / Assalamualaikum Puan Aina, |
| Sukacita dimaklumkan bahawa pihak kami telah menerima e-mel tuan. | Terima kasih atas e-mel tuan. |
| Sehubungan dengan itu, pihak kami ingin memohon jasa baik tuan untuk mengemukakan dokumen tersebut. | Boleh tuan kongsikan dokumen berkenaan sebelum Jumaat? |
| Kerjasama pihak tuan amatlah dihargai dan didahului dengan ucapan terima kasih. | Terima kasih atas bantuan tuan. |
| Sekian, terima kasih. Yang benar, | Terima kasih. / Salam hormat, [Nama] |

Salutation norms [NK]:
- Malay Muslim recipient: "Assalamualaikum" or "Salam".
- Mixed or unknown recipient: "Salam sejahtera" (the formal default) or "Selamat pagi".
- Address forms: "Tuan/Puan" when the name is unknown; "Encik/Puan + first name" once known. Never "Dear Sir" calques ("Tuan yang dihormati" is old-fashioned).
- "Mohon" as a polite verb ("Mohon semakan tuan", "Mohon maklum balas") is idiomatic Malaysian office Malay. Keep it.
