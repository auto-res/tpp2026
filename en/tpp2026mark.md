---
layout: page
title: TPP-mark 2026
permalink: /en/tpp2026mark/
lang: en
description: The TPP-mark 2026 challenge is to formalize known solved results for Othello (Reversi) in a proof assistant.
---

## Challenge: Formalize the solved results for Othello in a proof assistant

<ul class="event-list">
  <li><strong>Problem author:</strong> Masaya Taniguchi</li>
  <li><strong>Deadline:</strong> The day before TPP 2026 (November 15, 2026)</li>
  <li><strong>Submit solutions to:</strong> <code>{masaya.taniguchi, sho.sonoda} AT riken.jp</code></li>
</ul>

Formalize the known solved results for Othello (Reversi) as theorems in any proof assistant.

You may use any proof assistant, such as Lean, Isabelle/HOL, Rocq, or Agda.

The target board sizes are 4×4, 6×6, and 8×8.

> [!IMPORTANT]
> The use of AI is permitted. If you use AI, please explain how you used it.

## Problem 1: 4×4 Othello

Prove that, from the standard initial position in 4×4 Othello, the second player (White) wins under optimal play.

Related references: [3], [4]

## Problem 2: 6×6 Othello

Prove that, from the standard initial position in 6×6 Othello, the second player (White) wins 20–16 under optimal play.

Related references: [2], [3], [4]

## Problem 3: 8×8 Othello

Prove that, from the standard initial position in 8×8 Othello, the game ends in a draw under optimal play.

Related references: [1], [3], [4], [5]

## References

[1] Hiroki Takizawa.
“Othello is Solved.”
arXiv:2310.19387, 2023.
— The primary reference for Problem 3.

[2] Joel F. Feinstein.
“6x6 Othello.”
1993.
— The primary reference for Problem 2.

[3] H. Jaap van den Herik, Jos W. H. M. Uiterwijk, and Jack van Rijswijck.
“Games Solved: Now and in the Future.”
Artificial Intelligence 134(1–2), 277–311, 2002.
— A classification of solved games and background common to Problems 1–3.

[4] Victor Allis.
Searching for Solutions in Games and Artificial Intelligence.
Ph.D. thesis, University of Limburg, Maastricht, 1994.
— General methodology for solving games, relevant to Problems 1–3.

[5] Donald E. Knuth and Ronald W. Moore.
“An Analysis of Alpha-Beta Pruning.”
Artificial Intelligence 6(4), 293–326, 1975.
— A foundational reference for formalizing large-scale search, particularly for Problem 3.

[Back to the TPP 2026 English page]({{ '/en/' | relative_url }}) / [日本語版]({{ '/ja/tpp2026mark/' | relative_url }})
