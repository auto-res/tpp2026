# Historical conditional-source comments

Frozen source comments are preserved, not rewritten retrospectively. Some conditional helper modules say that a map premise remains open, or that no CheckedParts record is supplied by that module. Those comments describe the helper's interface at generation time, not the status of the later complete development.

The accepted `Tests.CompleteUpperRows6.Result` supplies `Lower.checked` and `Upper.checked` to `Joint.complete`, obtaining `initial6x6 : Problem2`. Its exact source is in `problem2/checked-source/`, and the retained final checker receipt confirms acceptance. These comments do not mean Problem 2 is still open. The top-level completion record is dated 19 October 2026.

Problem 3 is different: its conditional premises really are not all supplied, and no complete initial 8×8 theorem is claimed.
