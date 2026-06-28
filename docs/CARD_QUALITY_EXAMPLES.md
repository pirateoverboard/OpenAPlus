# Card quality examples

This is a documentation library, not deck content. The examples demonstrate
card construction; they are not approved citations. Verify every production
claim against the sources in [SOURCE_AND_CITATION_RULES.md](SOURCE_AND_CITATION_RULES.md).

## Quality baseline

A production card should test one concept, be answerable in about 15 seconds,
stand alone without hidden context, use paraphrased source-backed wording, and
avoid trivia or vague prompts. Lists are appropriate only when the exam expects
a bounded list. Instructor Notes should explain rather than repeat.

## Basic cards — 20 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | “Explain SO-DIMMs, DIMMs, RAM speed, and installation.” | It combines several retrieval targets. | “Which memory form factor is commonly used in laptops?” “SO-DIMM.” | It tests useful recall but no distinction. | “A laptop upgrade slot is too small for a desktop DIMM. Which form factor should you check for?” “SO-DIMM.” | One comparison applied to a clear constraint. |
| B2 | “Tell me everything about HDDs and SSDs.” | The scope and answer length are undefined. | “Which has no moving parts: an HDD or SSD?” “SSD.” | Clear, but it tests only a simple attribute. | “A mobile system needs storage resistant to mechanical shock. Which is the better fit, HDD or SSD?” “SSD, because it has no moving parts.” | The scenario makes the comparison relevant. |
| B3 | “What protocol is M.2?” | M.2 is a form factor, so the premise is ambiguous. | “Is every M.2 drive NVMe?” “No.” | It catches a trap but does not explain it. | “Why can’t the label M.2 alone prove a drive uses NVMe?” “M.2 describes a form factor; an M.2 device may use different interfaces.” | It corrects one misconception with a bounded answer. |
| B4 | “Explain DHCP, DNS, addressing, and routing.” | Four systems are tested at once. | “What service automatically supplies IP configuration?” “DHCP.” | Accurate direct recall, but minimally applied. | “A new client needs automatic IP configuration. Which service should be available?” “DHCP.” | One service is selected from one requirement. |
| B5 | “What is APIPA and list every related troubleshooting step?” | It mixes definition and an unbounded procedure. | “What does an APIPA address suggest?” “Automatic addressing was used.” | It lacks the relevant DHCP context. | “A client has a 169.254.x.x address instead of its expected lease. Which service path should be investigated first?” “DHCP availability and reachability.” | The symptom supports one first investigation. |
| B6 | “What is DNS and how does the whole internet use it?” | It is too broad for a card. | “What does DNS resolve?” “Names to IP addresses.” | Useful, but purely definitional. | “A client reaches a server by IP address but not by hostname. Which service should be checked?” “DNS.” | The symptom tests application, not recitation. |
| B7 | “Compare every feature of TCP and UDP.” | “Every” makes the answer unlimited. | “Which transport protocol is connection-oriented?” “TCP.” | Atomic but basic recall. | “A service requires delivery tracking and retransmission. Which transport protocol fits that requirement?” “TCP.” | One sourced property drives one choice. |
| B8 | “Give all SSH facts.” | Vague and unbounded. | “What port is associated with SSH?” “TCP 22.” | A valid recall card, but better suited to Cloze. | “Which protocol should replace an insecure remote terminal session when encrypted administration is required?” “SSH.” | The Basic format tests protocol selection rather than a port fact. |
| B9 | “Describe every BIOS setting.” | The card has no defined answer. | “What setting controls the device checked first at startup?” “Boot order.” | Clear recall, but no consequence. | “A technician must start from approved removable media once. Which firmware setting determines which device is tried first?” “Boot order.” | One realistic goal maps to one setting. |
| B10 | “Explain all RAID levels.” | Multiple architectures cannot be recalled atomically. | “Does RAID 0 provide redundancy?” “No.” | Clear and useful, but only recall. | “A two-disk array prioritizes capacity and performance but tolerates no disk failure. Which RAID level matches?” “RAID 0.” | The constraints distinguish the answer. |
| B11 | “What is RAID 1, and compare it with every RAID level?” | It combines definition and broad comparison. | “What data layout does RAID 1 use?” “Mirroring.” | Atomic but context-free. | “Two drives must contain matching copies so one drive can fail without immediate data loss. Which RAID level fits?” “RAID 1.” | The scenario tests the purpose of mirroring. |
| B12 | “A printer fails. What is wrong?” | Too little evidence allows many answers. | “Where can pending print jobs be viewed?” “The print queue.” | Clear but not a decision. | “Other applications work, but one job remains paused and later jobs do not print. What should be checked first?” “The print queue.” | The symptom makes the first check defensible. |
| B13 | “Why is Wi-Fi bad?” | “Bad” is vague and subjective. | “Can nearby networks cause Wi-Fi interference?” “Yes.” | It is answerable but nearly self-evident. | “Signal strength is high, but performance drops when overlapping nearby networks become active. What should be investigated?” “Channel interference.” | Relevant evidence supports one cause. |
| B14 | “Explain all battery chemistry.” | It is broad and likely to invite trivia. | “Do lithium-ion batteries require full discharge to prevent memory effect?” “No.” | Useful correction, but the question is leading. | “A user repeatedly deep-discharges a lithium-ion battery to prevent memory effect. What guidance should be corrected?” “Routine deep discharge is not required for that purpose.” | It applies the misconception without expanding scope. |
| B15 | “List every secure port.” | The category is undefined and requires a long list. | “What port is associated with HTTPS?” “TCP 443.” | Valid recall, but Cloze is more efficient. | “A firewall rule must allow standard encrypted web traffic. Which destination port is expected?” “TCP 443.” | Basic is justified by the configuration scenario. |
| B16 | “List all common ports from memory.” | It creates a brittle, high-load answer list. | “Name five common ports.” | The boundary is clearer, but the selection is arbitrary. | “Which standard port is associated with `[one named protocol]`?” | One protocol produces one fast answer; use separate cards. |
| B17 | “Why does every printer jam?” | It assumes one universal cause. | “What component should be inspected for repeated jams?” | The location is missing, so several answers remain. | “Paper repeatedly stops at the same documented path location. What should be inspected there first?” “The path and feed components at that location.” | The observation narrows the first inspection. |
| B18 | “Will this M.2 drive work?” | “This” has no specifications or context. | “Must an M.2 slot and drive be compatible?” “Yes.” | True but not diagnostic. | “An M.2 device fits mechanically but is not detected. What compatibility detail should be verified?” “The slot and device interface support.” | It separates physical fit from interface compatibility. |
| B19 | “Which is better, HDD or SSD?” | “Better” has no workload criterion. | “Which usually has lower access latency?” “SSD.” | A valid comparison but not tied to a decision. | “Choose between HDD and SSD for a workload where low access latency is the stated priority.” “SSD.” | The criterion makes “better” measurable. |
| B20 | “According to the source: `[sentence copied nearly verbatim]`?” | It risks copyright infringement and tests source phrasing. | “What does `[term]` do?” | Paraphrased, but may still be broad. | “Given `[single sourced condition]`, what function or decision follows?” | Original wording tests the concept rather than textual memory. |

## Cloze cards — 15 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | “SSH {{c1::is}} a protocol.” | It hides a filler word. | “SSH uses port {{c1::22}}.” | Useful, but omits transport detail expected by the chosen source. | “SSH commonly uses {{c1::TCP port 22}}.” | It hides one meaningful, bounded fact. |
| C2 | “{{c1::DHCP}} {{c2::uses}} {{c3::UDP}} ports {{c4::67}} and {{c5::68}}.” | Too many siblings fragment one relationship. | “DHCP uses UDP ports {{c1::67 and 68}}.” | One deletion, but roles remain unstated. | “DHCP commonly uses UDP {{c1::67 for the server}} and {{c2::68 for the client}}.” | Two deletions test distinct, meaningful roles. |
| C3 | “An address {{c1::might}} be APIPA.” | The hidden word has no learning value. | “APIPA uses {{c1::169.254.x.x}} addresses.” | Concise, but notation is informal. | “The IPv4 APIPA range is {{c1::169.254.0.0/16}}.” | Precise recall with one target. |
| C4 | “DNS {{c1::does things}} with names.” | The answer is vague. | “DNS resolves {{c1::hostnames}}.” | It omits the result of resolution. | “DNS resolves hostnames to {{c1::IP addresses}}.” | The context and hidden answer form one fact. |
| C5 | “HTTPS uses {{c1::a secure port}}.” | The deletion is descriptive rather than precise. | “HTTPS uses port {{c1::443}}.” | Good recall but omits transport convention. | “HTTPS commonly uses {{c1::TCP port 443}}.” | The complete expected value is hidden. |
| C6 | “RDP {{c1::is used}} remotely.” | Filler is hidden and the fact is weak. | “RDP uses port {{c1::3389}}.” | Useful but lacks transport context. | “RDP commonly uses {{c1::TCP port 3389}}.” | One compact port association. |
| C7 | “SMB is {{c1::important}}.” | “Important” is subjective trivia. | “SMB uses port {{c1::445}}.” | A valid short fact. | “Direct-hosted SMB commonly uses {{c1::TCP port 445}}.” | Wording is more precise while staying atomic. |
| C8 | “IMAP is {{c1::email}}.” | The deletion is overly broad. | “IMAP uses port {{c1::143}}.” | Useful direct recall. | “Standard IMAP commonly uses {{c1::TCP port 143}}.” | It supplies meaningful context without extra deletions. |
| C9 | “POP3 {{c1::downloads}} {{c2::messages}} {{c3::somehow}}.” | Weak and excessive deletions. | “POP3 uses port {{c1::110}}.” | Atomic but minimal. | “Standard POP3 commonly uses {{c1::TCP port 110}}.” | One precise retrieval target. |
| C10 | “SMTP uses {{c1::25}}, {{c2::587}}, {{c3::465}}, and explain each.” | It mixes several contexts and an essay. | “SMTP commonly uses port {{c1::25}}.” | Clear, but the intended context should be sourced. | “The source associates server-to-server SMTP with {{c1::TCP port 25}}.” | The context prevents an ambiguous port list. |
| C11 | “RAID {{c1::0}} is {{c2::fast}} and {{c3::dangerous}}.” | Subjective wording and three targets weaken recall. | “RAID 0 provides {{c1::no redundancy}}.” | Atomic and accurate. | “RAID 0 uses {{c1::striping}} and provides {{c2::no fault tolerance}}.” | Two related deletions test defined properties. |
| C12 | “RAID 1 {{c1::copies stuff}}.” | Informal wording is imprecise. | “RAID 1 uses {{c1::mirroring}}.” | Good direct recall. | “RAID 1 stores matching data copies through {{c1::mirroring}}.” | The sentence supplies enough meaning to stand alone. |
| C13 | “M.2 always means {{c1::NVMe}}.” | It teaches a false absolute. | “M.2 is a {{c1::form factor}}.” | Correct but isolated. | “M.2 identifies a {{c1::form factor}}, not a single storage protocol.” | It targets the exam trap explicitly. |
| C14 | “SO-DIMM means {{c1::small RAM}}.” | The expansion is inaccurate and colloquial. | “SO-DIMM stands for {{c1::Small Outline Dual In-line Memory Module}}.” | Strong acronym recall. | “Laptop memory commonly uses the {{c1::SO-DIMM}} form factor.” | Better when the learning target is recognition rather than spelling the expansion. |
| C15 | “{{c1::TCP}} is {{c2::connection-oriented}}, while {{c3::UDP}} is {{c4::connectionless}}, {{c5::faster}}, and {{c6::better}}.” | Too many deletions plus unsupported absolutes. | “TCP is {{c1::connection-oriented}}.” | Atomic but tests only one side. | “TCP is {{c1::connection-oriented}}; UDP is {{c2::connectionless}}.” | Two parallel facts create two clear reviews. |

## Image cards — 10 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| I1 | A copied laptop photo with every label visible on both sides. | It is copyrighted and reveals the answer. | An original SO-DIMM drawing with a box around the module on both images. | Original, but the question image still exposes the target. | `question_image` masks the SO-DIMM label; `answer_image` reveals and highlights it without moving the diagram. | One original visual target is revealed cleanly. |
| I2 | One motherboard image asks for every slot and connector. | It is a multi-answer visual inventory. | One DIMM slot is outlined, but the prompt says only “What is this?” | The target is singular but context is weak. | The question image masks one slot label and the prompt asks which component accepts a DIMM; the answer image labels that slot. | Visual recognition and prompt context align. |
| I3 | An M.2 diagram changes orientation between front and back. | Layout changes make comparison harder. | The same diagram boxes the device on both sides. | Stable layout, but no occlusion. | The question image masks the key label; the answer image reveals it in the identical location and dimensions. | Only the answer state changes. |
| I4 | A vendor connector photo is traced without permission. | Tracing does not make copied art original. | An original connector outline is shown with the name removed. | Legally safer, but the target may be visually ambiguous. | An original connector diagram preserves distinguishing features, masks one label, and supplies a specific identification prompt. | It is original, answerable, and atomic. |
| I5 | A USB-C image asks for connector type, speed, power, and protocol. | One picture triggers several independent answers. | It asks only for connector type. | Atomic, but front and back are the same unmasked image. | The question image masks the label; the answer image labels the connector, with protocol capabilities left to separate cards. | One visual skill is isolated. |
| I6 | A full BIOS screenshot is copied and asks “Explain this screen.” | Copyright and scope are both problematic. | An original simplified boot-order screen boxes a row. | The box points to the target but does not hide it. | An original question screen masks the boot-order label; the answer screen reveals it and highlights the same control. | The diagram tests one firmware-screen feature. |
| I7 | A printer diagram asks learners to name the entire paper path. | The answer list is unbounded and visually dense. | One jam location is circled. | The answer is implied by the circle. | The question image masks one path-stage label; the answer image reveals that label while retaining orientation cues. | It supports one troubleshooting location. |
| I8 | A RAID diagram shows all labels and asks for the RAID level. | The labels give away the answer. | Disk blocks are shown without a prompt constraint. | Potentially useful, but ambiguous. | The question image masks the layout name; the answer image reveals the sourced RAID label and highlights the data pattern. | Visual pattern recognition is explicit. |
| I9 | A Wi-Fi floor plan asks for every possible interference source. | It requires many speculative answers. | One region is shaded as “bad Wi-Fi.” | The symptom is visible but the cause is not defined. | An original diagram masks one identified interference source; the answer image reveals it while the prompt states the observed condition. | One spatial cause is tested with context. |
| I10 | A motherboard image uses tiny labels and low contrast. | It is inaccessible and hard to review. | A SATA port is boxed with readable contrast. | Better, but both images show the label. | Matching original images use readable contrast; the question masks the SATA label and the answer reveals it, plus a textual answer. | It remains usable and accessible outside the image. |

## Instructor Notes — 10 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| N1 | “The answer is SO-DIMM.” | It repeats the answer. | “Do not confuse it with DIMM.” | It flags confusion but does not explain it. | `### Exam Trap`: “SO-DIMM is the compact form factor; full-size DIMM is commonly associated with desktops.” | It explains the distinction concisely. |
| N2 | “SSDs are better.” | Unsupported and absolute. | “SSDs have no moving parts.” | Relevant, but it does not connect to the scenario. | `### Why`: “No moving parts makes SSD the stronger choice when mechanical shock is the stated concern.” | It ties a sourced property to the decision. |
| N3 | “Remember M.2.” | It adds no value. | “M.2 can be confusing.” | True but vague. | `### Exam Trap`: “M.2 describes the form factor; verify interface compatibility separately.” | It prevents a specific misconception. |
| N4 | “DHCP gives addresses.” | It repeats a direct answer. | “Check DHCP when addressing fails.” | Useful but broad. | `### Why`: “An unexpected automatic address indicates the expected lease path did not complete; verify DHCP availability and reachability.” | It explains the symptom-to-check reasoning. |
| N5 | “DNS means Domain Name System.” | It merely restates an acronym. | “DNS problems affect names.” | Better, but incomplete. | `### Real Help Desk`: “Successful access by IP but failure by hostname narrows the investigation toward name resolution.” | It adds a diagnostic distinction. |
| N6 | “TCP is reliable; memorize it.” | It is simplistic and instructional rather than explanatory. | “TCP tracks delivery.” | Relevant but terse. | `### Why`: “Choose TCP when the scenario explicitly requires connection state, sequencing, or retransmission.” | It connects properties to selection. |
| N7 | “Port 22 is SSH.” | It repeats the answer. | “Do not confuse SSH and Telnet.” | It identifies a trap but gives no criterion. | `### Exam Trap`: “SSH is the encrypted remote-administration choice; keep its port association separate from Telnet.” | It explains the meaningful contrast. |
| N8 | “RAID 0 is risky.” | “Risky” is vague. | “RAID 0 has no redundancy.” | Correct but likely repeats the card. | `### Tech Wisdom`: “Performance or capacity does not substitute for fault tolerance; match the layout to the stated requirement.” | It adds a transferable decision principle. |
| N9 | “Deep-discharge the battery? No.” | It repeats the response. | “Lithium-ion differs from older chemistry.” | The comparison is unspecific. | `### Exam Trap`: “Do not apply memory-effect maintenance advice from older battery chemistries to lithium-ion.” | It addresses the misconception without extra trivia. |
| N10 | A full paragraph copied from course notes. | Copyright risk and excessive length. | A close paraphrase of the same paragraph. | It may preserve source structure too closely. | `### Source Note`: one original sentence explaining the exact scope or ambiguity the card depends on. | It is concise, original, and reviewable. |

## Troubleshooting and scenario cards — 10 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | “A PC has no network. Fix it.” | Many causes and no evidence. | “A client has APIPA. What failed?” | It overstates one possible cause. | “A client expected a DHCP lease but has 169.254.x.x. What service path should be checked first?” “DHCP.” | Evidence supports a first investigation without claiming certainty. |
| T2 | “The internet is broken; is it DNS?” | Leading and underspecified. | “A hostname fails. Check DNS?” | It lacks a control test. | “The same destination works by IP but not hostname. Which service is the MOST likely issue?” “DNS.” | The control result isolates name resolution. |
| T3 | “Wi-Fi is slow. Change channels.” | It prescribes action without evidence. | “Nearby networks exist. Is there interference?” | Possible, but no observed correlation. | “Throughput drops when overlapping nearby networks become active despite strong signal. What is the MOST likely cause?” “Channel interference.” | The condition makes the cause defensible. |
| T4 | “The printer does not print. Replace it.” | It jumps to an expensive action. | “Check the print queue.” | It may be right but lacks a reason. | “One paused job blocks all later jobs while the printer is online. What is the FIRST thing to check?” “The print queue.” | It uses the least disruptive check supported by evidence. |
| T5 | “The computer will not boot. Change BIOS.” | “Will not boot” and “change” are vague. | “Check boot order.” | It lacks the triggering condition. | “Approved boot media is detected but the internal drive starts first. Which setting should be checked?” “Boot order.” | One observed order maps to one setting. |
| T6 | “An M.2 drive is bad because it is not detected.” | It assumes hardware failure. | “Verify M.2 compatibility.” | Good direction, but no distinction. | “The drive fits the socket but is absent from firmware. What compatibility should be verified before replacement?” “Slot and drive interface support.” | It avoids the physical-fit trap. |
| T7 | “SSH fails. Use port 22.” | A port number is not a complete diagnosis. | “Check whether port 22 is blocked.” | One possibility, but other prerequisites are unstated. | “The SSH service is confirmed running locally, but remote connections time out. What network control should be checked next?” “The path or firewall rule for TCP 22.” | Prior evidence makes the next check specific. |
| T8 | “A RAID warning means replace every disk.” | It is destructive and unsupported. | “Check which disk failed.” | Sensible, but lacks process. | “An array reports degraded status. What should be identified before following the vendor replacement procedure?” “The failed member and current array state.” | It prioritizes verification and vendor procedure. |
| T9 | “Paper jams mean bad rollers.” | It asserts one cause without location evidence. | “Inspect the paper path.” | Correct but broad. | “Jams repeat at the same path location. What should be inspected there first?” “The local path and feed components.” | Repetition and location narrow the inspection. |
| T10 | “A slow HDD should be replaced with an SSD.” | It skips diagnosis and assumes the requirement. | “Would an SSD improve access latency?” | It asks a general possibility. | “Testing confirms storage access latency is the bottleneck and low latency is required. Which storage type is the better fit?” “SSD.” | The diagnosis precedes the recommendation. |

## Exam-trap cards — 10 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | “M.2 equals NVMe. True?” | It presents a false absolute as expected knowledge. | “Is every M.2 drive NVMe?” “No.” | It identifies the trap without the rule. | “Why does an M.2 label not guarantee NVMe?” “M.2 is a form factor; verify the interface.” | The corrective principle is explicit. |
| E2 | “APIPA means the NIC is broken.” | It turns a symptom into an unsupported diagnosis. | “Does APIPA prove hardware failure?” “No.” | Correct but purely negative. | “An expected DHCP client has APIPA. Which service path is implicated before assuming NIC failure?” “DHCP availability or reachability.” | It redirects the learner using evidence. |
| E3 | “DNS assigns IP addresses.” | It confuses two services. | “Does DNS replace DHCP?” “No.” | It rejects the trap without testing roles. | “A client needs automatic addressing rather than name resolution. Which service is required?” “DHCP.” | The requirement distinguishes DHCP from DNS. |
| E4 | “UDP is always faster and TCP is always reliable.” | Absolutes ignore context and overstate behavior. | “Which is connection-oriented?” “TCP.” | Correct but only one side. | “A scenario requires connection state and retransmission. Which transport fits?” “TCP.” | The card selects from sourced requirements. |
| E5 | “SSH and Telnet are the same except port.” | It erases the security distinction. | “Which one is encrypted?” “SSH.” | Useful but context-light. | “Which protocol is the secure remote-administration choice, and what common port is associated with it?” “SSH, TCP 22.” | The trap and association are bounded. |
| E6 | “RAID 0 is a backup because data spans disks.” | It teaches a dangerous misconception. | “Is RAID 0 redundant?” “No.” | Correct but shallow. | “Why does RAID 0 fail a fault-tolerance requirement?” “Striping provides no redundancy.” | It links layout to requirement. |
| E7 | “RAID replaces backups.” | It is false and overly broad. | “Is RAID a backup?” “No.” | Important but leading. | “An array tolerates a disk failure but cannot recover deleted files. What separate control is still required?” “A backup.” | The scenario distinguishes availability from recovery. |
| E8 | “Lithium-ion batteries must be fully discharged for memory effect.” | It imports outdated maintenance advice. | “Should lithium-ion be deep-discharged for memory effect?” “No.” | Correct but leading. | “Which assumption is wrong when a user deep-discharges lithium-ion solely to prevent memory effect?” “That routine is required.” | It exposes the misconception in context. |
| E9 | “SSDs cannot fail because they have no moving parts.” | One advantage is turned into an absolute. | “Can SSDs fail?” “Yes.” | True but trivial. | “Does ‘no moving parts’ justify treating SSD storage as failure-proof?” “No; backups are still required.” | It blocks an inference with an actionable principle. |
| E10 | “SO-DIMM means laptop-only memory.” | “Only” overstates typical usage. | “Is SO-DIMM common in laptops?” “Yes.” | Accurate but does not address the absolute. | “A compact system uses SO-DIMM. Which assumption should be avoided?” “That SO-DIMM is exclusive to laptops.” | It corrects the trap without denying common usage. |

## HighYield classification — 5 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Mark every card in an objective HighYield. | The label no longer distinguishes priority. | Mark a card because the author finds it important. | Importance is subjective and undocumented. | Mark a sourced troubleshooting decision HighYield and record reviewer agreement. | It meets the rubric and has review evidence. |
| H2 | Mark a rare connector detail HighYield because it is difficult. | Obscurity is not yield. | Mark it because it appears in a study guide. | Presence alone does not establish priority. | Mark connector identification HighYield when it is explicitly in scope and rapid recognition is required. | Scope and recall need justify the label. |
| H3 | Mark an unsupported “common exam trick” HighYield. | The classification and claim lack evidence. | Mark a plausible confusion without review. | The idea may help, but evidence is missing. | Mark a documented common exam trap HighYield after a reviewer confirms the distinction. | It is sourced and reviewed. |
| H4 | Mark trivia HighYield to make learners notice it. | Tagging cannot turn trivia into useful content. | Keep the trivia card without HighYield. | Removing the tag does not justify the card. | Delete the trivia card unless it supports an in-scope decision or foundational concept. | Quality control happens before tagging. |
| H5 | Mark a card HighYield because all later cards link to it. | Links alone may reflect author structure. | Note that it seems foundational. | The dependency is not demonstrated. | Record which later objectives depend on the sourced concept and obtain reviewer agreement. | The foundational criterion is auditable. |

## Common anti-patterns — 5 example sets

| # | Bad example | Why it is bad | Okay example | Why it is only okay | Great example | Why it is great |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | “Define DHCP, DNS, APIPA, TCP, and UDP.” | It is a multi-concept front. | Ask for two related definitions. | Two answers can still fail independently. | Create one atomic card per retrieval target, then use a scenario only for a distinct relationship. | Each review has one success criterion. |
| A2 | “Explain networking.” | It is overly broad. | “Explain common network services.” | “Common” and answer depth remain vague. | Ask one sourced service-selection or definition question. | Scope and expected answer are explicit. |
| A3 | “What year was `[minor component revision]` announced?” | It is trivia unless the objective requires it. | Keep it as optional context. | Optional context can still distract. | Omit it, or retain a concise sourced note only when it supports an in-scope decision. | Exam relevance controls inclusion. |
| A4 | “`[Product]` always doubles performance.” | The absolute claim is unsupported. | “`[Product]` may improve performance.” | “May” avoids the absolute but remains unmeasurable. | State the sourced condition and ask which option satisfies that specific requirement. | Evidence and constraints replace marketing language. |
| A5 | Copy a source sentence and blank one word. | It tests wording and risks copyright infringement. | Lightly rearrange the source sentence. | Structure and phrasing may remain derivative. | Write an original prompt from the verified concept, then cite the source in metadata. | It tests understanding with traceable provenance. |

## Contributor Self-Review

Before submitting a card, confirm:

- [ ] It tests one concept and has one clear success criterion.
- [ ] A prepared learner can answer it in about 15 seconds.
- [ ] The prompt stands alone without neighboring cards or source context.
- [ ] Every factual claim, including Instructor Notes, is source-backed.
- [ ] Wording is original and paraphrased rather than copied or lightly edited.
- [ ] The card type matches the skill: recall, application, or visual recognition.
- [ ] Scenario details are necessary and support a unique answer.
- [ ] MOST, BEST, and FIRST are used only when evidence establishes the ranking.
- [ ] The front contains no vague wording, hidden assumptions, or multiple questions.
- [ ] Any required list has an exam-supported boundary and stated item count.
- [ ] No other card tests the same learning target in a different format.
- [ ] The card contains no low-value trivia or out-of-scope completeness filler.
- [ ] HighYield and difficulty follow their documented rubrics.
- [ ] Cloze deletions hide meaningful facts and are not excessive.
- [ ] Image cards use original `question_image` and `answer_image` files for a
      single occlusion-style reveal.
- [ ] Instructor Notes add concise reasoning, contrast, or practical value and
      do not repeat the answer.
- [ ] Stable ID, metadata, custom tags, citations, and objective mapping are valid.
- [ ] A reviewer can explain why the card exists and what distinct skill it tests.
