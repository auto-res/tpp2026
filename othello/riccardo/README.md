# TPP-mark 2026: certified Othello results in safe Agda

Riccardo Borsetto · Prepared 15 November 2026.

## Claims

| Challenge | Status |
|---|---|
| Problem 1, 4×4 | Proved: White wins; stronger raw score value +8. Historical safe Agda receipts. |
| Problem 2, 6×6 | Proved: raw value +4 AND a completed play of the SAME optimal forcing pair ending Black 16 / White 20. Final safe Agda acceptance: 19 October 2026. |
| Problem 3, 8×8 | NOT proved. Supplementary conditional wrapper only; dependencies and remaining premises not supplied. |

Start with **writeup.pdf** (current report); The AI-assistance section contains the complete current AI-use disclosure. `formal-source.html` contains verbatim statements and endpoints. Keep the PDF and HTML together; some PDF viewers block local links. The HTML is a documentary companion, not newly generated Agda highlighting or proof-checking evidence.

## Problem 1

`problem1/othello-agda-tpp2026-problem1.tar.gz` is the Problem 1 release: source, certificates, highlighted source and cold checker receipts, byte-identical to the original release except that internal working notes, packaging scripts and the superseded original write-up are omitted (listed in its `SUBMISSION.json`). Its “Problem 2 statement only” wording describes that release; Problem 2 is proved in the present report.

After unpacking that nested release, the documented command is:

```
agda --no-libraries --safe --without-K --cubical-compatible -i src src/Everything.agda
```

Agda 2.9.0; see retained binary identity in `SUBMISSION.json`. No new Agda invocation was performed during submission preparation.

## Problem 2

The endpoint is `Tests.CompleteUpperRows6.Result.initial6x6 : Problem2`; the exact accepted endpoint and typed final wrapper are in `problem2/checked-source/`. Start the evidence chain at `problem2/evidence/completion.json`, then `theorem-report.json`, `checker-receipt.json` and `source-audit.json`. `service-reconciliation.json` records whole-service measurements separately from the checker child.

`core-source.zip` contains 91 Agda source files and the library file. `source-graph.json.zst` selects 4,128 non-builtin modules, but many module bytes live in larger external archives. This lightweight package alone is NOT the complete 6×6 source closure. The separate extended archive `othello-agda-tpp2026-six-complete-sources-20261115-v3.tar.gz` contains ALL 4,128 selected project modules and the exact typed wrapper (4,129 source modules), flattened to one `src/`, plus historical row interfaces and evidence. Size: **426,517,206 bytes**; SHA-256: **bc3dfb965a6bc01aa6caca7d62d3f309fb920dc77fa3f038116607d563cd459d**. It must be shared separately, not nested in this small envelope. Source identities match the accepted audit and the exact declared closure resolves; no cold Agda rebuild or empirically validated portable build is claimed. Builtins require the compiler. Donor pools needed by the historical cached invocation are not shipped, but all selected project source bytes are included. See the extended README before trying its untested candidate build command.

`historical-source-manifest.json` predates the final theorem acceptance and intentionally retains its old pending flags. The 19 October completion record supplies the later acceptance. Never interpret source identity checks as fresh Agda checking.

Historical absolute paths, include order and restoration details remain unchanged for provenance. They do not resolve on a reviewer's machine.

## Incomplete Problem 3 supplement

`problem3-partial/Integration.agda` is an accepted historical CONDITIONAL wrapper. Its proof receipt and closure are supplied as provenance. This is not the latest research checkpoint, not a complete dependency package, and not a solution to the 8×8 problem. No complete 8×8 theorem is claimed.

## Integrity

Run `python3 verify.py .` to verify the payload index. `SUBMISSION.json` indexes payload files, not itself, avoiding a hash cycle. The archive digest is in the adjacent external `.sha256` file. This verifies packaged byte identities and documentary status assertions, NOT proof checking, complete dependency restoration or absence of all secrets. Historical paths are deliberately not dereferenced by this verifier.

The extended archive is distributed separately, identified above by filename, size and SHA-256; its download location is provided in the accompanying email.
