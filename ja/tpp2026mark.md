---
layout: page
title: TPP-mark 2026
permalink: /ja/tpp2026mark/
lang: ja
description: Othello（Reversi）の既知の解決結果を定理証明支援系で形式化する TPP-mark 2026 の課題です。
---

## 課題：Othello の解決結果を定理証明支援系で形式化せよ

<ul class="event-list">
  <li><strong>作問：</strong>谷口雅弥（Masaya Taniguchi）</li>
  <li><strong>締切：</strong>TPP2026前日（2026年11月15日）</li>
  <li><strong>解答提出先：</strong><code>{masaya.taniguchi, sho.sonoda} AT riken.jp</code></li>
</ul>

Othello（Reversi）について、既知の解決結果を任意の定理証明支援系上で定理として形式化せよ。

使用する定理証明支援系は Lean、Isabelle/HOL、Rocq、Agda などから自由に選んでよい。

対象は 4×4、6×6、8×8 とする。

> [!IMPORTANT]
> AIの利用は可とします。AI を使った場合は、AI の使い方を説明してください。

## 問題1：4×4 Othello

4×4 Othello の標準初期局面について、最善手でプレイした場合では後手（白）が勝つことを証明せよ。

関連文献： [3], [4]

## 問題2：6×6 Othello

6×6 Othello の標準初期局面について、最善手でプレイした場合では後手（白）が 20–16 で勝つことを証明せよ。

関連文献： [2], [3], [4]

## 問題3：8×8 Othello

標準 8×8 Othello の初期局面について、最善手でプレイした場合では引き分けになることを証明せよ。

関連文献： [1], [3], [4], [5]

## 参考文献

[1] Hiroki Takizawa.
“Othello is Solved.”
arXiv:2310.19387, 2023.
— 問題3の直接の基礎文献。

[2] Joel F. Feinstein.
“6x6 Othello.”
1993.
— 問題2の直接の基礎文献。

[3] H. Jaap van den Herik, Jos W. H. M. Uiterwijk, and Jack van Rijswijck.
“Games Solved: Now and in the Future.”
Artificial Intelligence 134(1–2), 277–311, 2002.
— 問題1–3に共通する solved game の分類と背景。

[4] Victor Allis.
Searching for Solutions in Games and Artificial Intelligence.
Ph.D. thesis, University of Limburg, Maastricht, 1994.
— 問題1–3に共通するゲーム解決の一般的方法論。

[5] Donald E. Knuth and Ronald W. Moore.
“An Analysis of Alpha-Beta Pruning.”
Artificial Intelligence 6(4), 293–326, 1975.
— 問題3を中心に、大規模探索を形式化する際の基礎文献。

[TPP 2026 日本語案内に戻る]({{ '/ja/' | relative_url }}) / [English version]({{ '/en/tpp2026mark/' | relative_url }})
